# {{project-name}}

{{project-description}}

## Installation

```bash
# Clone the repository
git clone {{repository-url}}
cd {{project-name}}

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
# Or with dev dependencies:
pip install -e ".[dev]"
```

## Development Setup

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Set up pre-commit hooks
pre-commit install

# Run tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html
```

## Usage

```python
from {{project-name}} import main

main.run()
```

## Project Structure

```
{{project-name}}/
├── src/
│   └── {{project-name}}/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
├── .gitignore
└── README.md
```

## Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

## License

MIT License - see LICENSE file for details