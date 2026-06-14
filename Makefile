.PHONY: generate lint test test-unit test-e2e format install clean

install:
	uv sync --extra dev

generate:
	cd .. && ./scripts/swagger/generate.sh --python-only

lint:
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/
	uv run mypy src/groundcover/

format:
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

test: test-unit

test-unit:
	uv run pytest tests/unit/ -v --cov=groundcover

test-e2e:
	uv run pytest tests/e2e/ -v

clean:
	rm -rf dist/ build/ *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
