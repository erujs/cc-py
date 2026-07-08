from dataclasses import dataclass
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse


ALLOWED_HEADERS = "Content-Type, Authorization"


@dataclass(frozen=True)
class Rule:
    origins: list[str]
    methods: list[str]


# Map each route prefix to the list of origins and methods allowed to call it.
#
# Local dev origins included by default:
#   - http://localhost:5173  (Vite dev server)
#   - http://localhost:3000  (Next.js dev server)
CORS_RULES: dict[str, Rule] = {
    "/api/example": Rule(
        origins=["http://localhost:3000", "http://localhost:5173"]
        methods=["GET", "POST", "PUT", "DELETE"],
    ),
}


def _match_rule(path: str) -> Rule | None:
    return next((r for p, r in CORS_RULES.items() if path.startswith(p)), None)


def _cors_headers(rule: Rule, origin: str, requested_method: str = "") -> dict:
    """Shared header set for both preflight and real responses."""
    headers = {
        "Access-Control-Allow-Methods": ", ".join(rule.methods + ["OPTIONS"]),
        "Access-Control-Allow-Headers": ALLOWED_HEADERS,
        "Vary": "Origin",
    }

    method_ok = not requested_method or requested_method in rule.methods

    if origin in rule.origins and method_ok:
        headers["Access-Control-Allow-Origin"] = origin

    return headers


class PerPrefixCORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        rule = _match_rule(request.url.path)
        if rule is None:
            return await call_next(request)

        origin = request.headers.get("origin", "")

        if request.method == "OPTIONS":
            requested = request.headers.get("access-control-request-method", "")
            return Response(status_code=200, headers=_cors_headers(rule, origin, requested))

        if origin and origin not in rule.origins:
            return JSONResponse(
                {"detail": "Origin not allowed"},
                status_code=403,
                headers={"Vary": "Origin"},
            )

        if request.method not in rule.methods:
            return JSONResponse(
                {"detail": "Method not allowed for this route"},
                status_code=405,
                headers={"Vary": "Origin"},
            )

        response = await call_next(request)
        response.headers.update(_cors_headers(rule, origin))

        return response