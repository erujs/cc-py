from fastapi import APIRouter, Depends, Request
from app.schemas.example import Example
from app.repositories.json_store import load_json
from app.core.cors import check_origin

router = APIRouter(prefix="/api/example", tags=["example"])

def _cors_guard(request: Request) -> None:
    check_origin(request, "/api/example")

@router.get("/", response_model=list[Example])
def get_examples(request: Request, _: None = Depends(_cors_guard)):
    return load_json("example.json")