#!/usr/bin/env python3
"""Post-generation fixes for the Python SDK.

Applied after openapi-python-client generation to fix import paths.
The generated code references `types`, `errors`, and `client` modules that
conflict with our hand-written modules, so we rewrite imports to use
the `_generated_*` prefixed copies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def ensure_future_annotations(filepath: Path) -> bool:
    """Inject ``from __future__ import annotations`` if missing.

    This is required for Python 3.9 compatibility when the generated code
    uses PEP 585 (``dict[str, Any]``) or PEP 604 (``X | Y``) syntax.

    Returns True if the file was modified.
    """
    content = filepath.read_text()
    if "from __future__ import annotations" in content:
        return False

    # Insert after any leading docstring/comments/blank lines, but before
    # the first real import or code.  The simplest correct approach: put it
    # right at the top.  If the file starts with a docstring we need to
    # place it after the docstring so Python still sees it as a module
    # docstring.
    lines = content.splitlines(keepends=True)
    insert_idx = 0

    # Skip a leading module docstring (triple-quoted string on line 0/1).
    if lines and (lines[0].startswith('"""') or lines[0].startswith("'''")):
        quote = lines[0][:3]
        if lines[0].count(quote) >= 2:
            # Single-line docstring
            insert_idx = 1
        else:
            # Multi-line docstring – find the closing triple-quote
            for i, line in enumerate(lines[1:], start=1):
                if quote in line:
                    insert_idx = i + 1
                    break

    # Skip blank lines after the docstring so the import is grouped nicely.
    while insert_idx < len(lines) and lines[insert_idx].strip() == "":
        insert_idx += 1

    lines.insert(insert_idx, "from __future__ import annotations\n\n")
    filepath.write_text("".join(lines))
    return True


def rewrite_imports_in_file(filepath: Path) -> bool:
    """Rewrite generated imports to use _generated_* prefixed modules.

    Handles:
    - from ..types import ... -> from .._generated_types import ...
    - from ...types import ... -> from ..._generated_types import ...
    - from ...client import ... -> from ..._generated_client import ...
    - from ...errors import ... -> from ..._generated_errors import ...
    - from .. import errors -> from .. import _generated_errors as errors
    - from ... import errors -> from ... import _generated_errors as errors

    Returns True if the file was modified.
    """
    content = filepath.read_text()
    original = content

    # Rewrite types imports (models use ..types, api uses ...types)
    content = re.sub(
        r"from (\.{2,})types import",
        r"from \1_generated_types import",
        content,
    )

    # Rewrite client imports (api modules use ...client)
    content = re.sub(
        r"from (\.{2,})client import",
        r"from \1_generated_client import",
        content,
    )

    # Rewrite errors imports - direct form
    content = re.sub(
        r"from (\.{2,})errors import",
        r"from \1_generated_errors import",
        content,
    )

    # Rewrite errors imports - module import form
    content = re.sub(
        r"from (\.{2,}) import errors\b",
        r"from \1 import _generated_errors as errors",
        content,
    )

    if content != original:
        filepath.write_text(content)
        return True
    return False


def rewrite_all_imports(package_dir: Path) -> int:
    """Rewrite imports in all generated Python files under api/ and models/.

    Also injects ``from __future__ import annotations`` for Python 3.9
    compatibility.
    """
    count = 0
    for subdir in ["api", "models"]:
        target = package_dir / subdir
        if not target.exists():
            continue
        for py_file in target.rglob("*.py"):
            modified = rewrite_imports_in_file(py_file)
            modified |= ensure_future_annotations(py_file)
            if modified:
                count += 1
    return count


def fix_type_aliases_compat(filepath: Path) -> bool:
    """Fix type alias assignments in _generated_types.py for Python 3.9.

    Type aliases like ``FileContent = IO[bytes] | bytes | str`` are runtime
    expressions, not annotations, so ``from __future__ import annotations``
    does not defer their evaluation.  We rewrite them to use ``Union``/``Optional``.

    Returns True if the file was modified.
    """
    if not filepath.exists():
        return False
    content = filepath.read_text()
    original = content

    # Add Optional, Union to the typing imports if not already present
    if "from typing import" in content:
        needs: list[str] = []
        if "Optional" not in content:
            needs.append("Optional")
        if "Union" not in content:
            needs.append("Union")
        if needs:
            content = content.replace(
                "from typing import",
                "from typing import " + ", ".join(needs) + ",",
            )

    # Fix FileContent type alias (single line)
    content = content.replace(
        "FileContent = IO[bytes] | bytes | str",
        "FileContent = Union[IO[bytes], bytes, str]",
    )

    # Fix FileTypes multi-line type alias:
    # Convert (tuple[...] | tuple[...] | ...) to Union[tuple[...], tuple[...], ...]
    # and str | None to Optional[str].
    # Use \n\) as the closing delimiter because the body contains comments
    # with ) characters that confuse a simple non-greedy match.
    ft_match = re.search(r"(FileTypes\s*=\s*)\((.*?)\n\)", content, re.DOTALL)
    if ft_match and " | " in ft_match.group(2):
        body = ft_match.group(2)
        # str | None → Optional[str]
        body = body.replace("str | None", "Optional[str]")
        # Remove leading | (union separator between tuple entries)
        body = re.sub(r"\n(\s*)\|\s+", r"\n\1", body)
        # Add commas after each top-level tuple closing bracket
        body = re.sub(r"(\])([ \t]*\n)", r"\1,\2", body)
        content = content[: ft_match.start()] + ft_match.group(1) + "Union[" + body + "\n]" + content[ft_match.end() :]

    if content != original:
        filepath.write_text(content)
        return True
    return False


def fix_nullable_from_dict(models_dir: Path) -> int:
    """Add ``or _var is None`` guard to all ``isinstance(_var, Unset)`` checks in model ``from_dict()`` methods.

    The generated code only checks ``isinstance(_var, Unset)`` but when the API
    returns JSON ``null`` the variable is ``None``, not ``Unset``.  This causes
    downstream ``from_dict(None)`` or ``fromisoformat(None)`` crashes.

    The regex only matches ``_var`` temporaries (underscore-prefixed) which are
    used in ``from_dict()``, so ``self.var`` patterns in ``to_dict()`` are not
    affected.

    Idempotent: already-patched lines end with ``is None:`` so the pattern
    (which requires the line to end with ``Unset):``  ) won't re-match.

    Returns the number of files modified.
    """
    if not models_dir.exists():
        return 0
    count = 0
    for py_file in models_dir.rglob("*.py"):
        content = py_file.read_text()
        original = content
        content = re.sub(
            r"if isinstance\((_\w+), Unset\):",
            lambda m: f"if isinstance({m.group(1)}, Unset) or {m.group(1)} is None:",
            content,
        )
        if content != original:
            py_file.write_text(content)
            count += 1
    return count


def fix_datetime_parsing(models_dir: Path) -> int:
    """Fix datetime parsing in generated model ``from_dict()`` methods.

    Two categories of fixes applied to every model file:

    1. **parse_datetime** – replaces ``datetime.datetime.fromisoformat(...)``
       with ``parse_datetime(...)`` which handles the ``Z`` UTC suffix and
       irregular fractional-second digit counts (4, 5, 7–9 digits) that
       Python <3.11 rejects.
    2. **Import injection** – adds ``from .._datetime_compat import parse_datetime``
       after ``import datetime`` when replacements were made.

    Null-safety for ``Unset`` checks is handled separately by
    ``fix_nullable_from_dict()``.

    All transformations are idempotent (safe to re-run).

    Returns the number of files modified.
    """
    if not models_dir.exists():
        return 0
    count = 0
    for py_file in models_dir.rglob("*.py"):
        content = py_file.read_text()
        original = content

        # Replace fromisoformat with parse_datetime – required fields (d.pop())
        content = re.sub(
            r"datetime\.datetime\.fromisoformat\(d\.pop\(([^)]+)\)\)",
            r"parse_datetime(d.pop(\1))",
            content,
        )

        # Replace fromisoformat with parse_datetime – optional fields (temp var)
        content = re.sub(
            r"datetime\.datetime\.fromisoformat\((_\w+)\)",
            r"parse_datetime(\1)",
            content,
        )

        # Also catch any previously-patched .replace("Z", "+00:00") calls
        content = re.sub(
            r"datetime\.datetime\.fromisoformat\((.+?)\.replace\(\"Z\",\s*\"\+00:00\"\)\)",
            r"parse_datetime(\1)",
            content,
        )

        # Inject import if we made parse_datetime replacements
        if content != original and "parse_datetime(" in content:
            import_line = "from .._datetime_compat import parse_datetime"
            if import_line not in content:
                content = content.replace(
                    "import datetime",
                    "import datetime\n\n" + import_line,
                    1,
                )

        if content != original:
            py_file.write_text(content)
            count += 1
    return count


def fix_null_list_responses(api_dir: Path) -> int:
    """Fix generated API endpoints that iterate over response.json() without null checks.

    Two failure modes when the API returns an empty list:

    1. ``response.json()`` returns ``None`` (JSON ``null``) and the subsequent
       ``for ... in _response_NNN:`` raises ``TypeError``.
    2. The response body is completely empty so ``response.json()`` throws
       ``json.decoder.JSONDecodeError`` before we even get a chance to check.

    We rewrite the assignment to ``response.json() if response.content else None``
    and then add the ``if ... is None: ... = []`` fallback.

    Returns the number of files modified.
    """
    if not api_dir.exists():
        return 0
    count = 0
    pattern = re.compile(
        r"^( +)(_response_\d+) = response\.json\(\)\n"
        r"( +)for (\w+) in \2:",
        re.MULTILINE,
    )
    for py_file in api_dir.rglob("*.py"):
        content = py_file.read_text()
        original = content
        content = pattern.sub(
            r"\1\2 = response.json() if response.content else None\n"
            r"\1if \2 is None:\n"
            r"\1    \2 = []\n"
            r"\3for \4 in \2:",
            content,
        )
        if content != original:
            py_file.write_text(content)
            count += 1
    return count


def fix_null_object_responses(api_dir: Path) -> int:
    """Fix generated API endpoints that call ``response.json()`` for single-object responses.

    When the API returns an empty body, ``response.json()`` raises
    ``json.decoder.JSONDecodeError``.  We add a ``if response.content`` guard.

    Two patterns are handled:

    - **Pattern A** – ``response_NNN = Model.from_dict(response.json())``
    - **Pattern B** – ``response_NNN = response.json()`` (standalone, not followed
      by a ``for`` loop — those are already handled by ``fix_null_list_responses``).

    Must run AFTER ``fix_null_list_responses()`` so that list patterns are already
    rewritten and won't match Pattern B (rewritten lines end with ``else None``).

    Returns the number of files modified.
    """
    if not api_dir.exists():
        return 0
    count = 0
    for py_file in api_dir.rglob("*.py"):
        content = py_file.read_text()
        original = content

        # Pattern A: response_NNN = Model.from_dict(response.json())
        content = re.sub(
            r"^(\s+)(response_\d+) = (\w[\w.]*?)\.from_dict\(response\.json\(\)\)$",
            r"\1\2 = \3.from_dict(response.json()) if response.content else None",
            content,
            flags=re.MULTILINE,
        )

        # Pattern B: response_NNN = response.json()  (standalone)
        content = re.sub(
            r"^(\s+)(_?response_\d+) = response\.json\(\)$",
            r"\1\2 = response.json() if response.content else None",
            content,
            flags=re.MULTILINE,
        )

        if content != original:
            py_file.write_text(content)
            count += 1
    return count


def fix_string_to_dict_in_models(models_dir: Path) -> int:
    """Fix additional-properties-only models where the API may return a JSON string.

    These "dict-wrapper" models have ``from_dict`` methods whose first statement
    is ``d = dict(src_dict)``.  When the API returns a JSON string instead of an
    object (e.g. ``"raw": "{...}"``), ``dict(some_string)`` raises ValueError.
    We insert an ``isinstance(src_dict, str)`` guard that JSON-decodes the string.
    Blank strings are treated as empty objects because some API fields return
    ``""`` when the raw payload exists but is empty.

    Returns the number of files modified.
    """
    if not models_dir.exists():
        return 0
    count = 0
    pattern = re.compile(
        r"(    def from_dict\(cls: type\[T\], src_dict: Mapping\[str, Any\]\) -> T:\n)"
        r"( +)d = dict\(src_dict\)",
    )
    replacement = (
        r"\1"
        r"\2if isinstance(src_dict, str):\n"
        r"\2    if not src_dict.strip():\n"
        r"\2        src_dict = {}\n"
        r"\2    else:\n"
        r"\2        import json\n"
        r"\n"
        r"\2        src_dict = json.loads(src_dict)\n"
        r"\2d = dict(src_dict)"
    )
    for py_file in models_dir.rglob("*.py"):
        content = py_file.read_text()
        original = content
        content = pattern.sub(replacement, content)
        if content != original:
            py_file.write_text(content)
            count += 1
    return count


def fix_optional_bools(models_dir: Path) -> int:
    """Fix boolean fields that should be optional.

    Generated attrs models use `Union[Unset, bool]` so this is less
    of an issue than with pydantic, but we keep the hook for safety.
    """
    # With attrs-based generation, optional bools are typically handled
    # via Union[Unset, bool] already. This is a no-op for now but kept
    # as a hook for future fixes.
    return 0


def main() -> None:
    sdk_root = Path(__file__).parent.parent
    package_dir = sdk_root / "src" / "groundcover"
    models_dir = package_dir / "models"
    api_dir = package_dir / "api"

    if not models_dir.exists() and not api_dir.exists():
        print(f"Neither models/ nor api/ found under {package_dir}")
        print("Run code generation first.")
        sys.exit(1)

    print("Applying post-generation fixes...")

    # Rewrite imports to use _generated_* prefixed modules
    # (also injects `from __future__ import annotations` for api/ and models/)
    import_fixes = rewrite_all_imports(package_dir)
    print(f"  Rewrote imports in {import_fixes} files")

    # Inject `from __future__ import annotations` in _generated_*.py files
    # for Python 3.9 compatibility with PEP 585/604 syntax.
    future_fixes = 0
    for name in ["_generated_client.py", "_generated_types.py", "_generated_errors.py"]:
        gen_file = package_dir / name
        if gen_file.exists() and ensure_future_annotations(gen_file):
            future_fixes += 1
    if future_fixes:
        print(f"  Injected future annotations in {future_fixes} _generated_* files")

    # Fix type alias assignments in _generated_types.py for Python 3.9
    types_file = package_dir / "_generated_types.py"
    type_alias_fixed = fix_type_aliases_compat(types_file)
    if type_alias_fixed:
        print("  Fixed type alias assignments in _generated_types.py")

    # Add null-safety guards to all isinstance(_var, Unset) checks in model from_dict()
    nullable_fixes = fix_nullable_from_dict(models_dir)
    if nullable_fixes:
        print(f"  Fixed nullable from_dict in {nullable_fixes} model files")

    # Fix datetime parsing in generated model from_dict() methods
    datetime_fixes = fix_datetime_parsing(models_dir)
    if datetime_fixes:
        print(f"  Fixed datetime parsing in {datetime_fixes} model files")

    # Fix null list responses in generated API endpoints
    null_list_fixes = fix_null_list_responses(api_dir)
    if null_list_fixes:
        print(f"  Fixed null list responses in {null_list_fixes} API files")

    # Fix null object responses in generated API endpoints
    null_obj_fixes = fix_null_object_responses(api_dir)
    if null_obj_fixes:
        print(f"  Fixed null object responses in {null_obj_fixes} API files")

    # Fix string-to-dict in additional-properties-only models
    string_dict_fixes = fix_string_to_dict_in_models(models_dir)
    if string_dict_fixes:
        print(f"  Fixed string-to-dict in {string_dict_fixes} model files")

    # Optional bool fixes (no-op for attrs, kept as hook)
    bool_fixes = fix_optional_bools(models_dir)
    if bool_fixes:
        print(f"  Fixed Optional[bool] fields: {bool_fixes} files")

    total = (
        import_fixes
        + future_fixes
        + int(type_alias_fixed)
        + nullable_fixes
        + datetime_fixes
        + null_list_fixes
        + null_obj_fixes
        + string_dict_fixes
        + bool_fixes
    )
    print(f"Total files modified: {total}")


if __name__ == "__main__":
    main()
