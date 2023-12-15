from pydantic import BaseModel


class ElectronsBase(BaseModel):
    name: str
    description: str
    photo_id: int


class ElectronsCreate(ElectronsBase):
    pass


class Electrons(ElectronsCreate):
    id: int


class ElectronsUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    photo_id: int | None = None
