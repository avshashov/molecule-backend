from pydantic import BaseModel


class ElectronsBase(BaseModel):
    name: str
    description: str
    photo_id: int


class Electrons(ElectronsBase):
    id: int


class ElectronsCreate(Electrons):
    pass


class ElectronsUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    photo_id: int | None = None
