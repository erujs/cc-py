# 🧱 Cookiecutter Python Template

A minimal, flexible Python project template using [Cookiecutter](https://github.com/cookiecutter/cookiecutter).  
Great for CLI tools, libraries, or general-purpose Python apps.

---

## 🚀 Features

- 📦 Standard project layout
- 🖥 CLI entry point (`your_project` or `python -m your_project`)
- 🧪 Pytest-compatible `tests/` folder
- 📜 `setup.py` with setuptools
- 📋 `requirements.txt`
- 📄 Auto-generated `README.md` and `.gitignore`
- 🔧 Fully customizable via Cookiecutter prompts

---

## 📦 Usage

First, install Cookiecutter (if you haven’t already):

```
pip install cookiecutter
```

Then create a new project using this template:

```
cookiecutter gh:erujs/cookiecutter-python-template
```

You’ll be prompted to enter:

- Project name
- Slug (import-safe name)
- Author info
- Description
- Python version

## Generated Project Structure

```
your_project/
├── your_project/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── README.md
├── setup.py
└── requirements.txt
```

## Example

```
cookiecutter gh:erujs/cookiecutter-python-template
```

Sample prompt answers:

- project_name: Nudl
- project_slug: nudl
- author_name: Jerus
- email: jerus@example.com
- description: A Python media downloader
- python_version: 3.10

Then:

```
cd nudl
pip install .
nudl  # or python -m nudl
```

## License
MIT — feel free to use, modify, and share.