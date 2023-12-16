from pydantic import BaseModel


class MediaType(BaseModel):
    id: int
    name: str


class MediaTypes(BaseModel):
    types: list[MediaType]


class MediaBase(BaseModel):
    name: str
    description: str


class MediaCreate(MediaBase):
    type_id: int
    link: str


class Media(MediaBase):
    id: int
    media_type: MediaType


class MediaMany(BaseModel):
    media: list[Media]


class MediaUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
