# app/core/security.py
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from jose import jwt

# ==========================
# Password hashing settings
# ==========================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hashed version.
    """
    return pwd_context.verify(plain_password, hashed_password)

# ==========================
# JWT token settings
# ==========================
SECRET_KEY = "your-secret-key"  # change this to a secure random key in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generate a JWT access token with optional expiration time.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """
    Decode a JWT token and return the payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
