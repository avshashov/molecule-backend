from datetime import date

from pydantic import BaseModel, Field

from app.schemas.media import MediaPreviewPhoto


class NewsBase(BaseModel):
    description: str = Field(
        title='News description',
        description='Brief description of the news',
        examples=[
            'The shooting of paintings and artists continues. '
            'Today we filmed the first part of our promo.'
        ],
    )
    text: str = Field(
        title='News text',
        description='Text of the news in the news section in markdown format',
        examples=[
            'Aggressive luxury is trying to trample the Molecule '
            'already at the entrance... [picture](url_to_picture)'
        ],
    )
    created_at: date = Field(
        title='News release date',
        description='News release date',
        examples=['2023-12-24'],
    )


class News(NewsBase):
    id: int = Field(
        title='News ID',
        description='News ID',
        examples=['1'],
        gt=0,
    )
    is_posted: bool = Field(
        title='Publication of news',
        description='Has the news been published?',
        examples=[True],
    )
    is_posted_in_bot: bool = Field(
        title='Publication news in a telegram bot',
        description='Has the news been published in a telegram bot?',
        examples=[False],
    )
    preview_photo: MediaPreviewPhoto


class NewsMany(BaseModel):
    news: list[News] = Field(
        title='News list',
        description='News list',
    )


class NewsCreate(NewsBase):
    is_posted: bool = Field(
        default=True,
        title='Publication of news',
        description='Has the news been published?',
        examples=[True],
    )
    is_posted_in_bot: bool = Field(
        default=False,
        title='Publication news in a telegram bot',
        description='Has the news been published in a telegram bot?',
        examples=[False],
    )
    preview_photo_id: int = Field(
        title='New preview photo ID',
        description='New preview photo ID news',
        examples=[1],
        gt=0,
    )


class NewsUpdate(BaseModel):
    description: str | None = Field(
        default=None,
        title='New news description',
        description='New brief description of the news',
        examples=[
            'The shooting of paintings and artists continues. '
            'Today we filmed the first part of our promo.',
        ],
    )
    text: str | None = Field(
        default=None,
        title='New news text',
        description='New text of the news in the news section in markdown format',
        examples=[
            'Aggressive luxury is trying to trample the Molecule '
            'already at the entrance... [picture](url_to_picture)',
        ],
    )
    created_at: date | None = Field(
        default=None,
        title='New news release date',
        description='New news release date',
        examples=['2023-12-24'],
    )
    is_posted: bool | None = Field(
        default=None,
        title='Publication of news',
        description='Has the news been published?',
        examples=[True],
    )
    preview_photo_id: int | None = Field(
        default=None,
        title='New preview photo ID',
        description='New preview photo ID news',
        examples=[1],
        gt=0,
    )
    is_posted_in_bot: bool | None = Field(
        default=None,
        title='Publication news in a telegram bot',
        description='Has the news been published in a telegram bot?',
        examples=[False],
    )
