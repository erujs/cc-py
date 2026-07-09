"""{{ cookiecutter.project_name }} entry point."""
from fastapi import FastAPI
from app.routers import example
from app.core.cors_middleware import PerPrefixCORSMiddleware


app = FastAPI(title="{{ cookiecutter.project_name }}", version="1.0.0")


app.add_middleware(PerPrefixCORSMiddleware)


app.include_router(example.router)


@app.get("/")
def root():
    return {
        "name": "{{ cookiecutter.project_name }}",
        "version": "1.0.0",
        "status": "online",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok"}