from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyCookie
from dependencies import MY_SESSION_ID
from fastapi.requests import Request

router = APIRouter()

security = APIKeyCookie(name=MY_SESSION_ID)


@router.get("/me", dependencies=[Depends(security)])
async def get_current_user(
    request: Request,
):
    if not request.session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return request.session
