from fastapi import FastAPI
from app.api.v1 import endpoints

app = FastAPI(title="{{ cookiecutter.project_name }}")

# Register endpoints
app.include_router(endpoints.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
