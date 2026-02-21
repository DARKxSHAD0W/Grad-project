from passlib.context import CryptContext

# This uses the Bcrypt algorithm as requested by your teacher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Security:
    @staticmethod
    def hash_password(password: str) -> str:
        """Transforms plain text into an encrypted string."""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Checks if the entered password matches the encrypted one."""
        return pwd_context.verify(plain_password, hashed_password)

security = Security()