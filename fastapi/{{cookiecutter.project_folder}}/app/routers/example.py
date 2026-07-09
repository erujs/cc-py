from fastapi import APIRouter, Request, HTTPException
from app.schemas.example import Example
from app.repositories.json_store import load_json, data_exists


router = APIRouter(prefix="/api/example", tags=["example"], redirect_slashes=False)


@router.get("", response_model=list[Example])
def get_examples(request: Request):
    if not data_exists("example.json"):
        raise HTTPException(status_code=404, detail="Requested data is not available")

    try:
        return load_json("example.json")
    except Exception as error:
        print(error)  # swap for real logging later
        raise HTTPException(status_code=500, detail="Unexpected error occurred")