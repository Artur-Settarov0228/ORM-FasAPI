from typing import List

from fastapi.routing import APIRouter
# from fastapi.exceptions import HTTPException

from app.database import LocalSession
from app.models.user import User
from app.schemas.users import UserResponse


router = APIRouter(
    prefix="/users",
    tags=["User Endpoints"]
)


@router.get("", response_model=List[UserResponse])
def get_all_products():
    db = LocalSession()

    return db.query(User).all()
