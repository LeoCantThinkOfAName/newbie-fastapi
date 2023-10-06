from fastapi import FastAPI
from routers import tracks

app = FastAPI()

fallback = {404: {"description": "Not Found"}}
app.include_router(tracks.router, prefix="/tracks", tags=["Tracks"], responses=fallback)


@app.get("/")
async def root():
    return {"Hello": "World!"}
