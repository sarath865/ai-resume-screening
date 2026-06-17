from fastapi import APIRouter
from app.schemas.user import UserRegister, UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user: UserRegister):

    return {
        "message": "User Registered Successfully",
        "email": user.email
    }

@router.post("/login")
def login(user: UserLogin):

    return {
        "message": "Login Working",
        "email": user.email
    }