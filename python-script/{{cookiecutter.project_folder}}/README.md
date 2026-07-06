# {{ cookiecutter.project_name }}

Built using [cc-py](https://github.com/erujs/cc-py) `python-script` template.

## Dependencies

Ensure you have the following installed before getting started:

- **Python {{ cookiecutter.python_version }}+** - required to develop and run the project
- **pytest** – for running tests

## Setup

### Step 1: Clone the generated project
```bash
git clone https://github.com/{{ cookiecutter.author }}/{{ cookiecutter.project_folder }}.git
cd {{ cookiecutter.project_folder }}
```

### Step 2: Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 3: Install the project
```bash
pip install -e ".[dev]"
```

## Usage

```bash
# Run directly
python -m {{ cookiecutter.project_slug }}.main

# Or if installed
{{ cookiecutter.project_slug }}
```

## Project Structure

```bash
{{ cookiecutter.project_folder }}/
├── {{ cookiecutter.project_slug }}/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Test

```bash
pytest
```

✨ Happy coding!
If you find this project useful, a ⭐ on the repo is always appreciated!