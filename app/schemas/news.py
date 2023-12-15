from datetime import date

from pydantic import BaseModel

from app.schemas.media import Media


class NewsBase(BaseModel):
    description: str
    text: str
    created_at: date


class News(NewsBase):
    id: int
    is_posted: bool
    is_posted_in_bot: bool
    preview_photo: Media


class NewsMany(BaseModel):
    news: list[News]


class NewsCreate(NewsBase):
    is_posted: bool = True
    is_posted_in_bot: bool = False
    preview_photo_id: int


class NewsUpdate(BaseModel):
    description: str | None = None
    text: str | None = None
    created_at: date | None = None
    is_posted: bool = True
    preview_photo_id: int | None = None
    is_posted_in_bot: bool = False
