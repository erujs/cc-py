# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_description }}  
This project was scaffolded using [cc-py](https://github.com/erujs/cc-py), a Cookiecutter template for building Python CLI applications.

## Dependencies

Ensure you have the following dependencies installed (if you haven’t already):

- **Python 3.8+** - required to develop and run the project
- **pipx** (recommended) – for installing and running the generated CLI apps in isolated environments

## Installation

You can install using `pipx` (recommended) or clone the repo directly:

### Option 1: Install with pipx
```bash
pipx install git+https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}.git
```

### Option 2: Clone the repo
```bash
git clone https://github.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e .
```

## Usage

```bash
{{ cookiecutter.project_slug }} # Run the main CLI to start the program
```

## 🧾 License
MIT — do whatever you want with it.