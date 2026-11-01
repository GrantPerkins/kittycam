from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from src.utils.jwt import JWTHelper
from src.utils.config import Config
from src.utils.logger import get_logger


class CloudflareAccessMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, exempt_paths=None):
        super().__init__(app)
        self.exempt_paths = set(exempt_paths or [])
        self.ALLOWED_EMAILS = {
            "gcperk20@gmail.com",
            "krrutkie@gmail.com",
        }
        self.config = Config()
        self.jwt_helper = JWTHelper(self.config)
        self.logger = get_logger()


    async def dispatch(self, request: Request, call_next):

        if request.url.path in self.exempt_paths:
            return await call_next(request)

        token = request.headers.get("CF-Access-Jwt-Assertion")

        if token is None:
            self.logger.error("missing Cloudflare access token")
            return JSONResponse(
                {"detail": "Missing Cloudflare Access token"},
                status_code=401,
            )

        try:
            claims = self.jwt_helper.verify_access_token(token)
        except Exception:
            self.logger.error("invalid token")
            return JSONResponse(
                {"detail": "Invalid token"},
                status_code=401,
            )

        if claims["email"] not in self.ALLOWED_EMAILS:
            self.logger.error(f"email {claims["email"]} not in allowlist")
            return JSONResponse(
                {"detail": f"email not in allowlist"},
                status_code=401,
            )

        self.logger.info(f"claims: {claims}")
        request.state.user = claims
        return await call_next(request)