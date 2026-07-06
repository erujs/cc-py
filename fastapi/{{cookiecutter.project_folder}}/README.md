# {{ cookiecutter.project_name }}

Built using [cc-py](https://github.com/erujs/cc-py) `fastapi` template.

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
fastapi dev app/main.py
```

API will be available at:
- Base: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`

## Project Structure

```bash
{{ cookiecutter.project_folder }}/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── cors.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── example.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── example.py
│   └── repositories/
│       ├── __init__.py
│       └── json_store.py
├── data/
│   └── example.json
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## CORS

`app/core/cors.py` restricts each route by origin per prefix in `CORS_RULES`.
Add an entry for every new router prefix you create:

```python
CORS_RULES: dict[str, list[str]] = {
    "/api/example": ["http://localhost:5173", "http://localhost:3000"],
    "/api/your_new_route": ["http://localhost:5173"],
}
```

## Test

```bash
pytest
```

✨ Happy coding!
If you find this project useful, a ⭐ on the repo is always appreciated!