"""Tests for post_generate.py import rewriting."""

from __future__ import annotations

import sys
from pathlib import Path

# Add scripts dir to path so we can import post_generate
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from post_generate import (
    ensure_future_annotations,
    fix_datetime_parsing,
    fix_null_object_responses,
    fix_nullable_from_dict,
    fix_string_to_dict_in_models,
    rewrite_imports_in_file,
)


class TestRewriteImports:
    def test_rewrites_model_types_import(self, tmp_path: Path) -> None:
        """Models use `from ..types import ...` which should become `from .._generated_types import ...`."""
        f = tmp_path / "model.py"
        f.write_text("from ..types import Unset, UNSET\n")
        assert rewrite_imports_in_file(f) is True
        assert f.read_text() == "from .._generated_types import Unset, UNSET\n"

    def test_rewrites_api_types_import(self, tmp_path: Path) -> None:
        """API modules use `from ...types import ...` which should become `from ..._generated_types import ...`."""
        f = tmp_path / "api_mod.py"
        f.write_text("from ...types import UNSET, Unset\n")
        assert rewrite_imports_in_file(f) is True
        assert f.read_text() == "from ..._generated_types import UNSET, Unset\n"

    def test_rewrites_client_import(self, tmp_path: Path) -> None:
        """API modules use `from ...client import ...` which should become `from ..._generated_client import ...`."""
        f = tmp_path / "api_mod.py"
        f.write_text("from ...client import AuthenticatedClient, Client\n")
        assert rewrite_imports_in_file(f) is True
        assert f.read_text() == "from ..._generated_client import AuthenticatedClient, Client\n"

    def test_rewrites_errors_direct_import(self, tmp_path: Path) -> None:
        """Direct errors import: `from ...errors import ApiResponseError`."""
        f = tmp_path / "api_mod.py"
        f.write_text("from ...errors import ApiResponseError\n")
        assert rewrite_imports_in_file(f) is True
        assert f.read_text() == "from ..._generated_errors import ApiResponseError\n"

    def test_rewrites_errors_module_import(self, tmp_path: Path) -> None:
        """Module-level errors import: `from ... import errors` -> `from ... import _generated_errors as errors`."""
        f = tmp_path / "api_mod.py"
        f.write_text("from ... import errors\n")
        assert rewrite_imports_in_file(f) is True
        assert f.read_text() == "from ... import _generated_errors as errors\n"

    def test_no_rewrite_for_unrelated_imports(self, tmp_path: Path) -> None:
        """Imports that don't match any pattern should be left untouched."""
        f = tmp_path / "model.py"
        original = "from ..models import SomeModel\nimport os\n"
        f.write_text(original)
        assert rewrite_imports_in_file(f) is False
        assert f.read_text() == original


class TestEnsureFutureAnnotations:
    def test_injects_at_top_of_plain_file(self, tmp_path: Path) -> None:
        """Files with no docstring get the import at the very top."""
        f = tmp_path / "mod.py"
        f.write_text("from http import HTTPStatus\nfrom typing import Any\n")
        assert ensure_future_annotations(f) is True
        text = f.read_text()
        assert text.startswith("from __future__ import annotations\n")
        assert "from http import HTTPStatus" in text

    def test_injects_after_single_line_docstring(self, tmp_path: Path) -> None:
        """Files starting with a single-line docstring."""
        f = tmp_path / "mod.py"
        f.write_text('"""Module doc."""\nimport os\n')
        assert ensure_future_annotations(f) is True
        lines = f.read_text().splitlines()
        assert lines[0] == '"""Module doc."""'
        assert lines[1] == "from __future__ import annotations"

    def test_injects_after_multi_line_docstring(self, tmp_path: Path) -> None:
        """Files starting with a multi-line docstring."""
        f = tmp_path / "mod.py"
        f.write_text('"""Module\ndoc.\n"""\nimport os\n')
        assert ensure_future_annotations(f) is True
        text = f.read_text()
        assert '"""\nfrom __future__ import annotations' in text

    def test_noop_when_already_present(self, tmp_path: Path) -> None:
        """Files that already have the import should not be modified."""
        f = tmp_path / "mod.py"
        original = "from __future__ import annotations\nimport os\n"
        f.write_text(original)
        assert ensure_future_annotations(f) is False
        assert f.read_text() == original

    def test_idempotent(self, tmp_path: Path) -> None:
        """Calling twice should only inject once."""
        f = tmp_path / "mod.py"
        f.write_text("import os\n")
        ensure_future_annotations(f)
        first_result = f.read_text()
        assert ensure_future_annotations(f) is False
        assert f.read_text() == first_result


class TestFixDatetimeParsing:
    """Tests for fix_datetime_parsing fromisoformat replacement."""

    DATETIME_FIELD = (
        "import datetime\n"
        "        _tmp = d.pop('created_at')\n"
        "        if isinstance(_tmp, Unset) or _tmp is None:\n"
        "            created_at = UNSET\n"
        "        else:\n"
        "            created_at = datetime.datetime.fromisoformat(_tmp)\n"
    )

    NON_DATETIME_FIELD = (
        "        _tmp2 = d.pop('status')\n"
        "        if isinstance(_tmp2, Unset) or _tmp2 is None:\n"
        "            status = UNSET\n"
        "        else:\n"
        "            status = StatusEnum.from_dict(_tmp2)\n"
    )

    def _make_model(self, tmp_path: Path, content: str) -> Path:
        models = tmp_path / "models"
        models.mkdir()
        f = models / "my_model.py"
        f.write_text(content)
        return models

    def test_replaces_fromisoformat_with_parse_datetime(self, tmp_path: Path) -> None:
        """fromisoformat should be replaced with parse_datetime."""
        models = self._make_model(tmp_path, self.DATETIME_FIELD)
        assert fix_datetime_parsing(models) == 1
        result = (models / "my_model.py").read_text()
        assert "parse_datetime(_tmp)" in result
        assert "fromisoformat" not in result

    def test_no_changes_for_non_datetime_file(self, tmp_path: Path) -> None:
        """Files without fromisoformat should not be modified."""
        models = self._make_model(tmp_path, self.NON_DATETIME_FIELD)
        assert fix_datetime_parsing(models) == 0

    def test_mixed_fields(self, tmp_path: Path) -> None:
        """Datetime field gets parse_datetime, non-datetime is untouched."""
        models = self._make_model(tmp_path, self.DATETIME_FIELD + self.NON_DATETIME_FIELD)
        assert fix_datetime_parsing(models) == 1
        result = (models / "my_model.py").read_text()
        assert "parse_datetime(_tmp)" in result
        assert "StatusEnum.from_dict(_tmp2)" in result

    def test_idempotent(self, tmp_path: Path) -> None:
        """Running twice produces the same result."""
        models = self._make_model(tmp_path, self.DATETIME_FIELD)
        fix_datetime_parsing(models)
        first_result = (models / "my_model.py").read_text()
        assert fix_datetime_parsing(models) == 0
        assert (models / "my_model.py").read_text() == first_result


class TestFixNullableFromDict:
    """Tests for fix_nullable_from_dict universal null-safety."""

    NESTED_FIELD = (
        "        _tmp = d.pop('config')\n"
        "        if isinstance(_tmp, Unset):\n"
        "            config = UNSET\n"
        "        else:\n"
        "            config = Config.from_dict(_tmp)\n"
    )

    TO_DICT_FIELD = "        if isinstance(self.config, Unset):\n            pass\n"

    def _make_model(self, tmp_path: Path, content: str) -> Path:
        models = tmp_path / "models"
        models.mkdir()
        f = models / "my_model.py"
        f.write_text(content)
        return models

    def test_adds_none_check(self, tmp_path: Path) -> None:
        """Nested object fields should get an `or _var is None` guard."""
        models = self._make_model(tmp_path, self.NESTED_FIELD)
        assert fix_nullable_from_dict(models) == 1
        result = (models / "my_model.py").read_text()
        assert "if isinstance(_tmp, Unset) or _tmp is None:" in result

    def test_idempotent(self, tmp_path: Path) -> None:
        """Second run returns 0 (no changes)."""
        models = self._make_model(tmp_path, self.NESTED_FIELD)
        assert fix_nullable_from_dict(models) == 1
        assert fix_nullable_from_dict(models) == 0

    def test_already_patched_noop(self, tmp_path: Path) -> None:
        """Lines already containing `or _var is None` are not modified."""
        patched = self.NESTED_FIELD.replace(
            "if isinstance(_tmp, Unset):",
            "if isinstance(_tmp, Unset) or _tmp is None:",
        )
        models = self._make_model(tmp_path, patched)
        assert fix_nullable_from_dict(models) == 0

    def test_does_not_touch_to_dict(self, tmp_path: Path) -> None:
        """self.xxx patterns in to_dict() must not be touched."""
        models = self._make_model(tmp_path, self.TO_DICT_FIELD)
        assert fix_nullable_from_dict(models) == 0
        result = (models / "my_model.py").read_text()
        assert "if isinstance(self.config, Unset):" in result

    def test_multiple_fields(self, tmp_path: Path) -> None:
        """All _var fields in one file are patched."""
        second_field = (
            "        _tmp2 = d.pop('metadata')\n"
            "        if isinstance(_tmp2, Unset):\n"
            "            metadata = UNSET\n"
            "        else:\n"
            "            metadata = Metadata.from_dict(_tmp2)\n"
        )
        models = self._make_model(tmp_path, self.NESTED_FIELD + second_field)
        assert fix_nullable_from_dict(models) == 1
        result = (models / "my_model.py").read_text()
        assert "if isinstance(_tmp, Unset) or _tmp is None:" in result
        assert "if isinstance(_tmp2, Unset) or _tmp2 is None:" in result


class TestFixNullObjectResponses:
    """Tests for fix_null_object_responses API empty-body safety."""

    FROM_DICT_PATTERN = "        response_200 = MyModel.from_dict(response.json())\n        return response_200\n"

    RAW_JSON_PATTERN = "        response_200 = response.json()\n        return response_200\n"

    ALREADY_PROTECTED = "        response_200 = MyModel.from_dict(response.json()) if response.content else None\n"

    def _make_api(self, tmp_path: Path, content: str) -> Path:
        api = tmp_path / "api"
        api.mkdir()
        f = api / "my_endpoint.py"
        f.write_text(content)
        return api

    def test_wraps_from_dict_response_json(self, tmp_path: Path) -> None:
        """Pattern A: Model.from_dict(response.json()) gets content guard."""
        api = self._make_api(tmp_path, self.FROM_DICT_PATTERN)
        assert fix_null_object_responses(api) == 1
        result = (api / "my_endpoint.py").read_text()
        assert "MyModel.from_dict(response.json()) if response.content else None" in result

    def test_wraps_raw_response_json(self, tmp_path: Path) -> None:
        """Pattern B: response.json() standalone gets content guard."""
        api = self._make_api(tmp_path, self.RAW_JSON_PATTERN)
        assert fix_null_object_responses(api) == 1
        result = (api / "my_endpoint.py").read_text()
        assert "response_200 = response.json() if response.content else None" in result

    def test_idempotent(self, tmp_path: Path) -> None:
        """Second run returns 0."""
        api = self._make_api(tmp_path, self.FROM_DICT_PATTERN)
        assert fix_null_object_responses(api) == 1
        assert fix_null_object_responses(api) == 0

    def test_does_not_touch_already_protected(self, tmp_path: Path) -> None:
        """Lines with `response.content` already present are not modified."""
        api = self._make_api(tmp_path, self.ALREADY_PROTECTED)
        assert fix_null_object_responses(api) == 0


class TestFixStringToDictInModels:
    """Tests for string-to-dict additional-properties model safety."""

    MODEL = (
        "from collections.abc import Mapping\n"
        "from typing import Any, TypeVar\n"
        "T = TypeVar('T')\n\n"
        "class Raw:\n"
        "    @classmethod\n"
        "    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:\n"
        "        d = dict(src_dict)\n"
        "        return cls()\n"
    )

    def test_blank_strings_become_empty_dicts(self, tmp_path: Path) -> None:
        models = tmp_path / "models"
        models.mkdir()
        f = models / "raw.py"
        f.write_text(self.MODEL)

        assert fix_string_to_dict_in_models(models) == 1
        result = f.read_text()
        assert "if not src_dict.strip():" in result
        assert "src_dict = {}" in result
        assert "src_dict = json.loads(src_dict)" in result

    def test_idempotent(self, tmp_path: Path) -> None:
        models = tmp_path / "models"
        models.mkdir()
        f = models / "raw.py"
        f.write_text(self.MODEL)

        assert fix_string_to_dict_in_models(models) == 1
        assert fix_string_to_dict_in_models(models) == 0
