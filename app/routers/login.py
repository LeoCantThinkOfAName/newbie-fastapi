import secrets
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Form
from fastapi.requests import Request
from dependencies import user

router = APIRouter()


@router.post("")
async def login(
    request: Request,
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    is_correct_user = secrets.compare_digest(username, user["username"])
    is_correct_password = secrets.compare_digest(password, user["password"])

    if not is_correct_user or not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    request.session.update({"username": username})
    return {"success": True}
