# cc-py

A minimal, flexible Python project template using [Cookiecutter](https://github.com/cookiecutter/cookiecutter).  
Now supports both **CLI tools** and **FastAPI** apps!

---

## 🚀 Features

- Choose between:
  - 🖥 CLI application template
  - ⚡ FastAPI application template
- 📦 Standard Python layout with `pyproject.toml`
- 🧪 Built-in test structure for both types
- 🛠 CLI entry point (`python -m your_package` or `your_project`)
- 📜 Auto-generated `README.md`, `.gitignore`, and `LICENSE`
- 🔧 Fully customizable via Cookiecutter prompts

---

## 📦 Usage

First, install Cookiecutter (if you haven’t already):

```bash
pip install cookiecutter
```

Then create a new project using this template:

```bash
cookiecutter gh:erujs/cc-py
```

You’ll be prompted to enter:

- project_type: cli or fastapi
- project_name: Name of your project
- project_slug: Folder and CLI name
- package_name: Python package name
- username: Your GitHub/author name
- email: Contact email
- project_description: One-liner description
- license (e.g. MIT)

## Generated Project Structure

### 🖥 CLI Example:

```bash
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

### ⚡ FastAPI Example:

```bash
your_project/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/endpoints.py
│   ├── core/config.py
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
```

## Example

### For CLI project:

```bash
cookiecutter gh:erujs/cc-py
# Select: cli
cd your_project
pip install -e .
your_project  # or: python -m your_package
```

### For FastAPI project:

```bash
cookiecutter gh:erujs/cc-py
# Select: fastapi
cd your_project
pip install -e .
uvicorn app.main:app --reload
```

## License
MIT — feel free to use, modify, and share.