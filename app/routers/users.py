import secrets
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from operator import attrgetter

router = APIRouter()

security = HTTPBasic()

user = {"username": "john", "password": "password"}


@router.get("/me")
async def get_current_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    username, password = attrgetter("username", "password")(credentials)
    is_correct_user = secrets.compare_digest(username, user["username"])
    is_correct_password = secrets.compare_digest(password, user["password"])

    if not is_correct_user or not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return {"username": username}
