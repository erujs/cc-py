# cc-py

Python Project Template ~ A scaffolding tool for quickly creating Python project structures.  

## Dependencies

Ensure you have the following dependencies installed (if you haven’t already):

- **Python 3.8+** - required to develop and run the project
- **pipx** (recommended) – for installing and running the generated CLI apps in isolated environments
- **Cookiecutter** – used to generate new projects from this template

## Installation

You can install using `pipx` (recommended) or clone the repo directly:

### Option 1: Install with pipx
```bash
pipx install git+https://github.com/erujs/cc-py.git
```

### Option 2: Clone the repo
```bash
pip install -e .
```

## Usage

```bash
cookiecutter gh:erujs/cc-py
# Generate a new Python project using this scaffolding tool.
# You’ll be prompted to provide:
#
# - project_slug (python-project): Name of the project folder and CLI entry point
# - package_name (package): Name of the Python package/module
# - username (yourusername): Your GitHub username or author name
# - project_description (description): A short one-line project description
# - license (MIT): License type for the project
```

```bash
# After project generation
cd <project-slug>

# Install the project in editable mode
pip install -e .

# Run the CLI (replace <project-slug> with your chosen name)
<project-slug>
```

### Generated CLI Project Structure:

```bash
python-project/
├── package/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_basic.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## License
MIT — do whatever you want with it.

✨ Happy coding!
If you find this project useful, a ⭐ on the repo is always appreciated!