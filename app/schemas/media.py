from pydantic import BaseModel


class MediaBase(BaseModel):
    name: str
    type_id: int
    link: str
    description: str


class Media(MediaBase):
    id: int


class MediaCreate(MediaBase):
    pass
