from fastapi import FastAPI
<<<<<<< Updated upstream
from routers import tracks
=======
from routers import tracks, users, login, logout
from starlette.middleware.sessions import SessionMiddleware
from dependencies import MY_SESSION_ID
>>>>>>> Stashed changes

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    same_site="strict",
    session_cookie=MY_SESSION_ID,
    secret_key="mysecret",
)


fallback = {404: {"description": "Not Found"}}
app.include_router(tracks.router, prefix="/tracks", tags=["Tracks"], responses=fallback)
<<<<<<< Updated upstream
=======
app.include_router(users.router, prefix="/users", tags=["Users"], responses=fallback)
app.include_router(login.router, prefix="/login", tags=["Login"], responses=fallback)
app.include_router(logout.router, prefix="/logout", tags=["Logout"], responses=fallback)
>>>>>>> Stashed changes


@app.get("/")
async def root():
    return {"Hello": "World!"}
