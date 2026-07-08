"""
NOTE: This is a placeholder data layer that reads from local JSON files
under /data. It's meant for prototyping/local dev only.

In a real service, this is where you'd set up your actual database
connection/client instead (e.g. SQLAlchemy engine + session, an async
driver like asyncpg/motor, or an ORM's connection pool) and expose
equivalent read/write functions that your routers call — the goal is
that routers/schemas don't need to change when you swap this out for
a real DB later, only this file does.
"""
import json
from pathlib import Path
from fastapi import HTTPException

DATA_DIR = Path(__file__).parent.parent.parent / "data"


def data_exists(filename: str) -> bool:
    return (DATA_DIR / filename).exists()


def load_json(filename: str) -> dict | list:
    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Requested data is not available",
        )

    try:
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Unexpected error occurred",
        ) from exc