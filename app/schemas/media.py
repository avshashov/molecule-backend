from pydantic import BaseModel, Field


class MediaType(BaseModel):
    id: int = Field(title='Media type ID', description='Media type ID', examples=[1], gt=0)
    name: str = Field(title='Media type name', description='Media type name', examples=['photo'])


class MediaTypes(BaseModel):
    types: list[MediaType] = Field(
        title='List of media types',
        description='List of media types',
        examples=[[{"id": 1, "name": "photo"}, {"id": 2, "name": "video"}]],
    )


class MediaBase(BaseModel):
    name: str = Field(
        title='Media name',
        description='Media file name',
        examples=['Some photo name'],
    )
    description: str = Field(
        title='Media description',
        description='Media file description',
        examples=['Some photo description'],
    )


class MediaCreate(MediaBase):
    type_id: int = Field(
        title='Type ID',
        description='Type ID',
        examples=['1'],
        gt=0,
    )
    link: str = Field(
        title='Link to media',
        description='Link to media file',
        examples=['https://somepath-to-media/some-media.png'],
    )


class Media(MediaBase):
    id: int = Field(
        title='Media ID',
        description='Media file ID',
        examples=['1'],
        gt=0,
    )
    link: str = Field(
        title='Link to media',
        description='Link to media file',
        examples=['https://somepath-to-media/some-media.png'],
    )
    media_type: MediaType


class MediaPreviewPhoto(MediaBase):
    id: int = Field(
        title='Preview Photo ID',
        description='Preview Photo file ID',
        examples=['1'],
        gt=0,
    )
    link: str = Field(
        title='Link to preview photo',
        description='Link to preview photo file',
        examples=['https://somepath-to-media/some-media.png'],
    )


class MediaMany(BaseModel):
    media: list[Media] = Field(
        title='Media list',
        description='List of media files',
        examples=[
            [
                {
                    "name": "Some photo name",
                    "description": "Some photo description",
                    "id": 1,
                    "link": "https://somepath-to-media/some-media-photo.png",
                    "media_type": {"id": 1, "name": "photo"},
                },
                {
                    "name": "Some video name",
                    "description": "Some video description",
                    "id": 1,
                    "link": "https://somepath-to-media/some-media-video.mp4",
                    "media_type": {"id": 2, "name": "video"},
                },
            ]
        ],
    )


class MediaUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        title='New media name',
        description='New media file name',
        examples=['Some photo name'],
    )
    description: str | None = Field(
        default=None,
        title='New media description',
        description='New media file description',
        examples=['Some photo description'],
    )
