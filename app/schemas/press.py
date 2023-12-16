from datetime import date

from pydantic import BaseModel

from app.schemas import Media


class PressBase(BaseModel):
    title: str
    description: str
    created_at: date
    external_link: str


class Press(PressBase):
    id: int
    is_posted: bool
    preview_photo: Media


class PressMany(BaseModel):
    press: list[Press]


class PressCreate(PressBase):
    is_posted: bool = True
    preview_photo_id: int


class PressUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    created_at: date | None = None
    is_posted: bool = True
    preview_photo_id: int | None = None
    external_link: str | None = None
