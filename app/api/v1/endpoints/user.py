from fastapi import APIRouter
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import register_user, list_users

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(user_in: UserCreate):
    return register_user(user_in)

@router.get("/", response_model=list[UserOut])
def get_users():
    return list_users()
