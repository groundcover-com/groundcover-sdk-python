"""Root test configuration.

Holds only what has to run on the pytest controller before xdist spawns workers.
"""

from __future__ import annotations

import os

import pytest

from tests.e2e import _names


def pytest_configure(config: pytest.Config) -> None:
    """Pin one run id for the whole run, xdist workers included.

    This lives in the *root* tests conftest on purpose. In ``tests/e2e/conftest.py``
    it only ran on the controller when ``tests/e2e/`` was named on the command line
    (as ``make test-e2e`` and the CI workflow both do). Under a bare ``pytest``,
    args resolve from ``testpaths``, so the e2e conftest loads later during
    collection -- which under xdist happens inside each worker, after spawn. Every
    worker would then mint its own id and the run would silently lose the single
    identity that makes "did this run leave anything behind?" answerable.

    Assigned rather than setdefault: an existing-but-empty ``GC_E2E_RUN_ID`` would
    survive setdefault and leave each worker generating its own id.
    """
    os.environ["GC_E2E_RUN_ID"] = _names.run_id()
