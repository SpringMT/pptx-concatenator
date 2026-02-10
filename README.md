# pptx-concatenator

A Python library for concatenating PowerPoint presentations using [pptx-slide-copier](https://github.com/SpringMT/pptx-slide-copier).

## Features

- Concatenate multiple PPTX files by appending slides
- Preserve formatting, images, and layouts
- Support for both file paths and Presentation objects
- Simple and intuitive API
- Command-line interface for easy usage

## Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

### Requirements

- Python 3.8+
- python-pptx >= 0.6.21
- pptx-slide-copier >= 0.0.5

## Usage

### Command Line Interface

After installation, you can use the `pptx-concat` command to concatenate PPTX files directly from the command line:

```bash
# Concatenate two presentations
pptx-concat source.pptx target.pptx -o output.pptx

# Concatenate multiple presentations
pptx-concat source.pptx file1.pptx file2.pptx file3.pptx -o output.pptx

# Show help
pptx-concat --help
```

### Python API

#### Basic Usage

Concatenate two PPTX files:

```python
from pptx_concatenator import concat_pptx

# Simple function to concatenate two PPTX files
concat_pptx("source.pptx", "target.pptx", "output.pptx")
```

### Using the PptxConcatenator Class

```python
from pptx_concatenator import PptxConcatenator

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
from pptx_concatenator import PptxConcatenator

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

### Running Tests

```bash
# Run tests
make test

# Run tests with coverage
make test-cov
```

### Linting and Formatting

```bash
# Run linter
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
- `make lint` - Run ruff linter
- `make format` - Format code with ruff
- `make format-check` - Check formatting without making changes
- `make clean` - Clean build artifacts and cache files

## CI/CD

This project uses GitHub Actions for continuous integration:

- **Lint**: Checks code quality with ruff
- **Test**: Runs tests on Python 3.8-3.12

## License

MIT
