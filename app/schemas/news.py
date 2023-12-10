from datetime import date

from pydantic import BaseModel


class NewsBase(BaseModel):
    description: str
    text: str
    created_at: date
    preview_photo_id: int


class News(NewsBase):
    id: int
    is_posted: bool
    is_posted_in_bot: bool


class NewsCreate(NewsBase):
    is_posted: bool = True
    is_posted_in_bot: bool = False


class NewsUpdate(BaseModel):
    description: str | None = None
    text: str | None = None
    created_at: date | None = None
    is_posted: bool = True
    preview_photo_id: int | None = None
    is_posted_in_bot: bool = False
