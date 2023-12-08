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
    bot_post_setting_id: int


class NewsCreate(NewsBase):
    is_posted: bool | None = None
    bot_post_setting_id: int


class NewsUpdate(BaseModel):
    description: str | None = None
    text: str | None = None
    created_at: date | None = None
    is_posted: bool | None = None
    preview_photo_id: int | None = None
    bot_post_setting_id: int | None = None
