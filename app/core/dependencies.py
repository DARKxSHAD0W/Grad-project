from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings

# This version shows the Username/Password boxes in Swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


def get_current_admin(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the token received from Swagger
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")

        # We ensure the role is lowercase to avoid "Admin" vs "admin" mismatch
        role: str = str(payload.get("scope", "")).lower().strip()

        # Validation Logic
        if username is None:
            raise credentials_exception

        if role != "admin":
            # If the user is logged in but is NOT an admin, they get 403 Forbidden
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Admin privileges required. Current role: {role}"
            )

        return username

    except JWTError:
        raise credentials_exception