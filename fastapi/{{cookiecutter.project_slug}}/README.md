# {{ cookiecutter.project_name }}

Built using [cc-py](https://github.com/erujs/cc-py) `fastapi` template.

## Dependencies

Ensure you have the following installed before getting started:

- **Python {{ cookiecutter.python_version }}+** - required to develop and run the project
- **pytest** – for running tests

## Setup

### Step 1: Clone the generated project
```bash
git clone https://github.com/your-username/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
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
uvicorn app.main:app --reload
```

API will be available at:
- Base: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`

## Project Structure

```bash
{{ cookiecutter.project_slug }}/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   └── cors.py
│   ├── routers/
│   │   └── example.py
│   ├── schemas/
│   │   └── example.py
│   └── repositories/
│       └── json_store.py
├── data/
│   └── example.json
├── tests/
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

## License
MIT — do whatever you want with it.

✨ Happy coding!
If you find this project useful, a ⭐ on the repo is always appreciated!