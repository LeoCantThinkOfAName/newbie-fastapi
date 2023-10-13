from fastapi import APIRouter
from fastapi.security import APIKeyCookie
from fastapi.requests import Request
from dependencies import MY_SESSION_ID

router = APIRouter()

security = APIKeyCookie(name=MY_SESSION_ID)


@router.post("")
async def logout(
    request: Request,
):
    request.session.clear()
    return {"success": True}
