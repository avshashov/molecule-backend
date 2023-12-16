from pydantic import BaseModel

from app.schemas.media import Media


class ElectronsBase(BaseModel):
    name: str
    description: str


class ElectronsCreate(ElectronsBase):
    photo_id: int


class Electron(ElectronsBase):
    id: int
    preview_photo: Media


class Electrons(BaseModel):
    participants: list[Electron]


class ElectronsUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    photo_id: int | None = None
