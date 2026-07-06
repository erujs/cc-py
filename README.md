# cc-py

A collection of Python project scaffolding templates. Generate a new project instantly using [Cookiecutter](https://cookiecutter.readthedocs.io/).

## Dependencies

Ensure you have the following installed before getting started:

- **Python 3.10+**
- **Cookiecutter**

```bash
pip install cookiecutter
```

## Templates

### python-script
A plain Python 3 script/package with a basic CLI entry point and tests.

```bash
cookiecutter gh:erujs/cc-py --directory python-script
```

### fastapi
A layered FastAPI service with routers, schemas, repositories, and per-route CORS enforcement.

```bash
cookiecutter gh:erujs/cc-py --directory fastapi
```

## After Generation

```bash
cd <project-slug>
python -m venv .venv
source .venv/bin/activate
pip install -e .          # python-script
pip install -e ".[dev]"   # fastapi
```

✨ Happy coding!
If you find this project useful, a ⭐ on the repo is always appreciated!