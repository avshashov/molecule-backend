from pydantic import BaseModel


class MediaBase(BaseModel):
    name: str
    type_id: int
    description: str


class Media(MediaBase):
    id: int
    link: str


class MediaCreate(MediaBase):
    file: bytes
