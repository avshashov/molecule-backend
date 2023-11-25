from datetime import date

from pydantic import BaseModel


class PressBase(BaseModel):
    title: str
    description: str
    created_at: date
    preview_photo: int
    external_link: str


class Press(PressBase):
    id: int
    is_posted: bool


class PressCreate(PressBase):
    is_posted: bool | None = None


class PressUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    created_at: date | None = None
    id_posted: bool | None = None
    preview_photo: int | None = None
    external_link: str | None = None
