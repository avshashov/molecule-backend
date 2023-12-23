from pydantic import BaseModel, Field

from app.schemas.media import MediaPreviewPhoto


class ElectronsBase(BaseModel):
    name: str = Field(
        title='Participant\'s full name',
        description='Full name of the participant in the electrons section',
        examples=['Test user'],
    )
    description: str = Field(
        title='Participant\'s description',
        description='Description of the participant in the electrons section in markdown format',
        examples=['The man who created the magnificent [picture](url_to_picture)'],
    )


class ElectronsCreate(ElectronsBase):
    photo_id: int = Field(
        title='Photo ID', description='Photo ID of the participant on the section page', examples=[1], gt=0
    )


class Electron(ElectronsBase):
    id: int = Field(title='Participant ID', description='Participant ID', examples=[1], gt=0)
    preview_photo: MediaPreviewPhoto


class Electrons(BaseModel):
    participants: list[Electron] = Field(
        title='Participants list', description='List of all members of the electrons section'
    )


class ElectronsUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        title='New participant\'s full name',
        description='New full name of the participant in the electrons section',
        examples=['Test user'],
    )
    description: str | None = Field(
        default=None,
        title='New participant\'s description',
        description='New description of the participant in the electrons section in markdown format',
        examples=['The man who created the magnificent [picture](url_to_picture)'],
    )
    photo_id: int | None = Field(
        default=None,
        title='New photo ID',
        description='New photo ID of the participant on the section page',
        examples=[1],
        gt=0,
    )
