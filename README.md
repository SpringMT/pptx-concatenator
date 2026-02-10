# pptx-concatenator

A Python library for concatenating PowerPoint presentations using [pptx-slide-copier](https://github.com/SpringMT/pptx-slide-copier).

## Features

- Concatenate multiple PPTX files by appending slides
- Preserve formatting, images, and layouts
- Support for both file paths and Presentation objects
- Simple and intuitive API

## Installation

```bash
pip install -e .
```

### Requirements

- Python 3.6+
- python-pptx >= 0.6.21
- pptx-slide-copier >= 0.0.5

## Usage

### Basic Usage

Concatenate two PPTX files:

```python
from pptx_concat import concat_pptx

# Simple function to concatenate two PPTX files
concat_pptx("source.pptx", "target.pptx", "output.pptx")
```

### Using the PptxConcatenator Class

```python
from pptx_concat import PptxConcatenator

# Concatenate two presentations
result = PptxConcatenator.concat("source.pptx", "target.pptx", "output.pptx")

# Concatenate multiple presentations
result = PptxConcatenator.concat_multiple(
    "source.pptx",
    ["target1.pptx", "target2.pptx", "target3.pptx"],
    "output.pptx"
)
```

### Working with Presentation Objects

```python
from pptx import Presentation
from pptx_concat import PptxConcatenator

# Load presentations
src_prs = Presentation("source.pptx")
target_prs = Presentation("target.pptx")

# Concatenate
result = PptxConcatenator.concat(src_prs, target_prs)

# Save manually
result.save("output.pptx")
```

## Development

### Setup Development Environment

```bash
make install
```

Or manually:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running Tests

```bash
# Run tests
make test

# Run tests with coverage
make test-cov
```

### Linting and Formatting

```bash
# Run linters
make lint

# Format code
make format

# Check formatting without changes
make format-check
```

### Available Make Commands

- `make install` - Install package and development dependencies
- `make test` - Run tests
- `make test-cov` - Run tests with coverage report
- `make lint` - Run flake8 and mypy
- `make format` - Format code with black and isort
- `make format-check` - Check formatting without making changes
- `make clean` - Clean build artifacts and cache files

## CI/CD

This project uses GitHub Actions for continuous integration:

- **CI**: Runs tests on multiple OS (Ubuntu, macOS, Windows) and Python versions (3.8-3.12)
- **Lint**: Checks code quality with flake8, black, isort, and mypy

## License

MIT
