from datetime import date

from pydantic import BaseModel, Field

from app.schemas import MediaPreviewPhoto


class PressBase(BaseModel):
    title: str = Field(
        title='Press article title',
        description='Press article title',
        examples=['VOGUE.\nINTERVIEW'],
    )
    description: str = Field(
        title='Press article description',
        description='Brief description of the press article',
        examples=['On a glorious Saturday morning, the Molecule was invited to Zaimka'],
    )
    created_at: date = Field(
        title='Press article release date',
        description='Press article release date',
        examples=['2023-12-24'],
    )
    external_link: str = Field(
        title='Link to article',
        description='Link to article on external site',
        examples=['https://example.com/some-press-article'],
    )


class Press(PressBase):
    id: int = Field(
        title='Press article ID',
        description='Press article ID',
        examples=['1'],
        gt=0,
    )
    is_posted: bool = Field(
        title='Publication of press article',
        description='Has the press article been published?',
        examples=[True],
    )
    preview_photo: MediaPreviewPhoto


class PressMany(BaseModel):
    press: list[Press] = Field(
        title='Press list',
        description='Press list',
        examples=[
            [
                {
                    "title": "VOGUE.\nINTERVIEW",
                    "description": "On a glorious Saturday morning, the Molecule was invited to Zaimka",
                    "created_at": "2023-12-24",
                    "external_link": "https://example.com/some-press-article",
                    "id": 1,
                    "is_posted": True,
                    "preview_photo": {
                        "name": "Some photo name",
                        "description": "Some photo description",
                        "id": 1,
                        "link": "https://somepath-to-media/some-media.png",
                    },
                }
            ]
        ],
    )


class PressCreate(PressBase):
    is_posted: bool = Field(
        default=True,
        title='Publication of press article',
        description='Has the press article been published?',
        examples=[True],
    )
    preview_photo_id: int = Field(
        title='Preview photo ID',
        description='Preview photo ID press article',
        examples=[1],
        gt=0,
    )


class PressUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        title='New press article title',
        description='New press article title',
        examples=['VOGUE.\nINTERVIEW'],
    )
    description: str | None = Field(
        default=None,
        title='New press article description',
        description='New brief description of the press article',
        examples=['On a glorious Saturday morning, the Molecule was invited to Zaimka'],
    )
    created_at: date | None = Field(
        default=None,
        title='New press article release date',
        description='New press article release date',
        examples=['2023-12-24'],
    )
    is_posted: bool = Field(
        default=True,
        title='Publication of press article',
        description='Has the press article been published?',
        examples=[True],
    )
    preview_photo_id: int | None = Field(
        default=None,
        title='New preview photo ID',
        description='New preview photo ID press article',
        examples=[1],
        gt=0,
    )
    external_link: str | None = Field(
        default=None,
        title='New link to article',
        description='New link to article on external site',
        examples=['https://example.com/some-press-article'],
    )
