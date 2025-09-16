# app/core/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# ----------------------------------------------------------------------
# DATABASE URL
# ----------------------------------------------------------------------
# Construct the database URL in the format:
# postgresql://<username>:<password>@<host>:<port>/<database_name>
DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

# ----------------------------------------------------------------------
# SQLAlchemy Engine
# ----------------------------------------------------------------------
# The engine manages connections to the database
# echo=True will log all SQL queries (useful for development)
engine = create_engine(DATABASE_URL, echo=settings.DEBUG)

# ----------------------------------------------------------------------
# Session Local
# ----------------------------------------------------------------------
# sessionmaker creates a configured "Session" class
# Each request should use its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ----------------------------------------------------------------------
# Base Model
# ----------------------------------------------------------------------
# All database models should inherit from this base class
Base = declarative_base()

# ----------------------------------------------------------------------
# Dependency for FastAPI routes
# ----------------------------------------------------------------------
# Example usage in routes:
# from fastapi import Depends
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
def get_db():
    """
    Provide a transactional scope around a series of operations.
    Yields a SQLAlchemy Session instance and ensures proper closure.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
