# app/crud/user.py

from sqlalchemy.orm import Session
from app.models.user import User  # your SQLAlchemy User model
from app.schemas.user import UserCreate, UserOut

# -----------------------------
# CRUD operations for User model
# -----------------------------

def create_user(db: Session, user_in: UserCreate) -> UserOut:
    """
    Create a new user in the database.

    Args:
        db (Session): SQLAlchemy DB session.
        user_in (UserCreate): Pydantic schema with user data.

    Returns:
        UserOut: Pydantic schema of the created user.
    """
    # Create a User instance from Pydantic data
    db_user = User(name=user_in.name, email=user_in.email)

    # Add to session and commit
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresh to get auto-generated fields like ID

    # Return as UserOut schema
    return UserOut(id=db_user.id, name=db_user.name, email=db_user.email)


def get_users(db: Session) -> list[UserOut]:
    """
    Retrieve all users from the database.

    Args:
        db (Session): SQLAlchemy DB session.

    Returns:
        list[UserOut]: List of users as Pydantic schemas.
    """
    db_users = db.query(User).all()
    return [UserOut(id=u.id, name=u.name, email=u.email) for u in db_users]


def get_user_by_id(db: Session, user_id: int) -> UserOut | None:
    """
    Retrieve a single user by ID.

    Args:
        db (Session): SQLAlchemy DB session.
        user_id (int): User ID to search for.

    Returns:
        UserOut | None: User if found, otherwise None.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        return UserOut(id=db_user.id, name=db_user.name, email=db_user.email)
    return None
