#!/usr/bin/env python3
"""Validate that the OpenAPI 3.0 spec has the same routes as the sdk_routes.yaml allowlist.

Usage:
    python validate_oas3_routes.py /tmp/openapi3.yaml scripts/swagger/sdk_routes.yaml
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


def load_oas3_paths(oas3_path: str) -> set[str]:
    """Extract all paths from an OpenAPI 3.0 spec."""
    with open(oas3_path) as f:
        spec = yaml.safe_load(f)
    return set(spec.get("paths", {}).keys())


def load_sdk_routes(routes_path: str) -> set[str]:
    """Extract all routes from the sdk_routes.yaml allowlist."""
    with open(routes_path) as f:
        config = yaml.safe_load(f)
    return set(config.get("routes", []))


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <openapi3.yaml> <sdk_routes.yaml>")
        sys.exit(1)

    oas3_path = sys.argv[1]
    routes_path = sys.argv[2]

    oas3_paths = load_oas3_paths(oas3_path)
    sdk_routes = load_sdk_routes(routes_path)

    missing_from_oas3 = sdk_routes - oas3_paths
    extra_in_oas3 = oas3_paths - sdk_routes

    if missing_from_oas3:
        print(f"ERROR: {len(missing_from_oas3)} routes in sdk_routes.yaml but missing from OAS3:")
        for route in sorted(missing_from_oas3):
            print(f"  - {route}")

    if extra_in_oas3:
        print(f"WARNING: {len(extra_in_oas3)} routes in OAS3 but not in sdk_routes.yaml:")
        for route in sorted(extra_in_oas3):
            print(f"  + {route}")

    if missing_from_oas3:
        print(f"\nFAILED: {len(missing_from_oas3)} routes missing from OAS3 conversion")
        sys.exit(1)

    print(f"OK: All {len(sdk_routes)} routes from sdk_routes.yaml found in OAS3 spec")
    print(f"OAS3 has {len(oas3_paths)} total paths ({len(extra_in_oas3)} extra)")


if __name__ == "__main__":
    main()
