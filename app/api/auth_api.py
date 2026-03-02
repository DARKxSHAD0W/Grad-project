from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import security
from app.db.models import Employee

router = APIRouter(prefix="/api/auth", tags=["0. Authentication"])

# Added include_in_schema=False to hide it from the Swagger list
@router.post("/login", include_in_schema=False)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    OAuth2 compatible token login.
    Hiding this from the schema list, but the Authorize button will still call it.
    """
    user = db.query(Employee).filter(Employee.username == form_data.username).first()

    if not user or not security.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = security.create_access_token(
        data={
            "sub": user.username,
            "scope": user.role
        }
    )

    return {"access_token": access_token, "token_type": "bearer"}