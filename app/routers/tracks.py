from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


class Track(BaseModel):
    id: int
    title: str
    artist: str
    album: str | None = None
    year: int
    label: str | None = None


router = APIRouter()

tracks: list[Track] = [
    {
        "id": 1,
        "title": "Here comes the sun",
        "artist": "Beatles",
        "album": "Abby Road",
        "year": 1969,
        "label": "Apple Records",
    },
    {
        "id": 2,
        "title": "Song 2",
        "artist": "Blur",
        "album": "Blur",
        "year": 1997,
        "label": "Parlophone",
    },
    {
        "id": 3,
        "title": "High & Dry",
        "artist": "Radiohead",
        "album": "The Bends",
        "year": 1995,
        "label": "EMI",
    },
    {
        "id": 4,
        "title": "The Rain Song",
        "artist": "Le Zeppelin",
        "album": "Houses of The Holy",
        "year": 1973,
        "label": "Atlantic Records",
    },
]


@router.get("")
async def get_tracks(skip: int = 0, limit: int = 1, q: str | None = None):
    matched: [Track] = []

    if q:
        for track in tracks:
            if track["artist"].lower() == q.lower():
                matched.append(track)

    else:
        return tracks[skip : skip + limit]
    return matched[skip : skip + limit]


@router.get("/{track_id}")
async def get_track_by_id(track_id: int):
    for track in tracks:
        if track["id"] == track_id:
            return track
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track not found")


@router.post("")
async def create_track(track: Track):
    tracks.append(track)
    return track
