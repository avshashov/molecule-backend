from pydantic import BaseModel


class MediaBase(BaseModel):
    name: str
    type_id: int
    description: str


class MediaCreate(MediaBase):
    link: str


class Media(MediaCreate):
    id: int
