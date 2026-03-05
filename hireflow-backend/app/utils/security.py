from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

# ================= PASSWORD =================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")[:72]
    return pwd_context.hash(password_bytes)

def verify_password(password: str, hashed: str) -> bool:
    password_bytes = password.encode("utf-8")[:72]
    return pwd_context.verify(password_bytes, hashed)

# ================= JWT =================

SECRET_KEY = "super_secret_key_change_this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None