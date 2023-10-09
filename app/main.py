from fastapi import FastAPI
from routers import tracks, users

app = FastAPI()

fallback = {404: {"description": "Not Found"}}
app.include_router(tracks.router, prefix="/tracks", tags=["Tracks"], responses=fallback)
app.include_router(users.router, prefix="/users", tags=["Users"], responses=fallback)


@app.get("/")
async def root():
    return {"Hello": "World!"}
