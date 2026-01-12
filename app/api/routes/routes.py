from fastapi import Depends
from app.api.deps import get_current_user
from app.models.user import User


@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }
