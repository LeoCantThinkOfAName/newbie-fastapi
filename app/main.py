from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Track(BaseModel):
    title: str
    artist: str
    album: str | None = None
    year: int
    label: str | None = None


tracks: list[Track] = []


@app.get("/")
async def root():
    return {"Hello": "World!"}


@app.get("/tracks")
async def get_tracks():
    return tracks


@app.post("/tracks")
async def create_track(track: Track):
    tracks.append(track)
    return track
