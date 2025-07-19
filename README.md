# cc-py

A minimal, flexible Python project template using [Cookiecutter](https://github.com/cookiecutter/cookiecutter).  
Great for CLI tools, libraries, or general-purpose Python apps.

---

## 🚀 Features

- 📦 Standard project layout
- 🖥 CLI entry point (`your_project` or `python -m your_project`)
- 🧪 Pytest-compatible `tests/` folder
- 📄 Uses `pyproject.toml` with modern `setuptools`
- 📜 Auto-generated `README.md`, `.gitignore`, and `LICENSE`
- 🔧 Fully customizable via Cookiecutter prompts

---

## 📦 Usage

First, install Cookiecutter (if you haven’t already):

```
pip install cookiecutter
```

Then create a new project using this template:

```
cookiecutter gh:erujs/cc-py
```

You’ll be prompted to enter:

- project_slug (project folder name and CLI name)
- package_name (Python importable package)
- username
- project_description
- license (e.g. MIT)

## Generated Project Structure

```
your_project/
├── your_package/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_basic.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Example

```
cookiecutter gh:erujs/cookiecutter-python-template
```

Sample prompt answers:

- project_slug: project-py
- package_name: project
- username: erujs
- email: jerus@example.com
- project_description: A Python project
- license: MIT

Then:

```
cd nudl-py
pip install -e .
project-py
```

## License
MIT — feel free to use, modify, and share.