# app/services/user_service.py
from app.schemas.user import UserCreate, UserOut

# Sample data
sample_users: list[UserOut] = [
    UserOut(id=1, name="Alice Johnson", email="alice@example.com"),
    UserOut(id=2, name="Bob Smith", email="bob@example.com"),
    UserOut(id=3, name="Charlie Brown", email="charlie@example.com"),
]

# In-memory storage for newly created users
users_db: list[UserOut] = sample_users.copy()
next_id = len(users_db) + 1

def register_user(user_in: UserCreate) -> UserOut:
    global next_id
    user = UserOut(id=next_id, name=user_in.name, email=user_in.email)
    users_db.append(user)
    next_id += 1
    return user

def list_users() -> list[UserOut]:
    return users_db
