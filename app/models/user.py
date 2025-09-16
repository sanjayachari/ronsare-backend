# app/models/user.py

from sqlalchemy import Column, Integer, String
from app.core.db import Base  # SQLAlchemy Base from your db.py

# -----------------------------
# User ORM model
# -----------------------------
class User(Base):
    """
    SQLAlchemy User model representing the 'users' table.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
