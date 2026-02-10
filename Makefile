.PHONY: install test test-cov lint format clean

install:
	pip install -e ".[dev]"

test:
	pytest

test-cov:
	pytest --cov=pptx_concatenator --cov-report=html --cov-report=term

lint:
	ruff check pptx_concatenator tests

format:
	ruff format pptx_concatenator tests

format-check:
	ruff format --check pptx_concatenator tests

clean:
	rm -rf build dist *.egg-info
	rm -rf __pycache__ .pytest_cache .ruff_cache
	rm -rf htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
