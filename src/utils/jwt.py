from jwt import PyJWKClient
import jwt

from src.utils.config import Config

class JWTHelper:
    def __init__(self, config: Config):
        self.config = config
        self.jwks_client = PyJWKClient(config.jwks_url)


    def verify_access_token(self, token: str) -> dict:
        signing_key = self.jwks_client.get_signing_key_from_jwt(token)

        return jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=self.config.aud,
            issuer=self.config.issuer,
        )