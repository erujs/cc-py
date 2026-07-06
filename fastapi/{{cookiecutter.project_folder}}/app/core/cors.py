from fastapi import Request, HTTPException

# Map each route prefix to the list of origins allowed to call it.
#
# Local dev origins included by default:
#   - http://localhost:5173  (Vite dev server)
#   - http://localhost:3000  (Next.js dev server)
CORS_RULES: dict[str, list[str]] = {
    "/api/example": ["http://localhost:5173", "http://localhost:3000"],
}

def check_origin(request: Request, route_prefix: str) -> None:
    allowed = CORS_RULES.get(route_prefix, [])
    origin = request.headers.get("origin", "")

    if origin and origin not in allowed:
        raise HTTPException(status_code=403, detail="Origin not allowed")