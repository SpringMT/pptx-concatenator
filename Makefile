.PHONY: install test lint format clean

install:
	pip install -e .
	pip install -r requirements-dev.txt

test:
	pytest

test-cov:
	pytest --cov=pptx_concat --cov-report=html --cov-report=term

lint:
	flake8 pptx_concat.py test_pptx_concat.py
	mypy pptx_concat.py

format:
	black pptx_concat.py test_pptx_concat.py
	isort pptx_concat.py test_pptx_concat.py

format-check:
	black --check pptx_concat.py test_pptx_concat.py
	isort --check pptx_concat.py test_pptx_concat.py

clean:
	rm -rf build dist *.egg-info
	rm -rf __pycache__ .pytest_cache .mypy_cache
	rm -rf htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
