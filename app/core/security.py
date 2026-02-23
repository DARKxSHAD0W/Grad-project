import os
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

# Set up the encryption context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class SecurityHandler:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password after truncating to 72 chars for bcrypt stability."""
        return pwd_context.hash(password[:72])

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verifies a plain-text password against the stored hash."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict):
        """Generates a JWT access token for a logged-in user."""
        to_encode = data.copy()
        # Calculate expiration time
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        # Sign the token with your SECRET_KEY
        encoded_jwt = jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        return encoded_jwt


# Create the instance for easy import
security = SecurityHandler()