# app/schemas/user.py

from pydantic import BaseModel, EmailStr

# -----------------------------
# Schema for creating a user
# -----------------------------
class UserCreate(BaseModel):
    """
    Input schema for creating a new user.
    """
    name: str
    email: EmailStr  # Validates proper email format
    password: str    # Plain password input (will be hashed in service layer)


# -----------------------------
# Schema for outputting user data
# -----------------------------
class UserOut(BaseModel):
    """
    Output schema for user data returned by the API.
    """
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allows Pydantic to read data from SQLAlchemy models
