from fastapi import APIRouter, Depends, Request, HTTPException
from app.schemas.example import Example
from app.repositories.json_store import load_json, data_exists
from app.core.cors import check_origin

router = APIRouter(prefix="/api/example", tags=["example"])


def _cors_guard(request: Request) -> None:
    check_origin(request, "/api/example")


@router.get("/", response_model=list[Example])
def get_examples(request: Request, _: None = Depends(_cors_guard)):
    if not data_exists("example.json"):
        raise HTTPException(status_code=404, detail="Requested data is not available")

    try:
        return load_json("example.json")
    except Exception as error:
        print(error)  # swap for real logging later
        raise HTTPException(status_code=500, detail="Unexpected error occurred")