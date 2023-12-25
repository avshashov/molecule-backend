from datetime import date

from pydantic import BaseModel, Field

from app.schemas.media import MediaPreviewPhoto


class ProjectCategory(BaseModel):
    id: int = Field(
        title='Project category ID',
        description='Project category ID',
        examples=['1'],
        gt=0,
    )
    name: str = Field(
        title='Project category name',
        description='Project category name',
        examples=['Exhibitions'],
    )


class ProjectCategories(BaseModel):
    categories: list[ProjectCategory] = Field(
        title='List of projects categories',
        description='List of projects categories',
    )


class ProjectBase(BaseModel):
    title: str = Field(
        title='Project title',
        description='Project title',
        examples=['SPACE GAME\nEXHIBITION'],
    )
    description: str = Field(
        title='Project description',
        description='Brief description of the project',
        examples=['This ship has no destination. The path is the goal'],
    )
    text: str = Field(
        title='Project text',
        description='Text of the project in the projects section in markdown format',
        examples=[
            'A living crystalline structure is formed in places of greatest intensity'
            ' and follows the movements of the guest for some time... [picture](url_to_picture)'
        ],
    )
    created_at: date = Field(
        title='Project release date',
        description='Project release date',
        examples=['2023-12-24'],
    )


class Project(ProjectBase):
    id: int = Field(
        title='Project ID',
        description='Project ID',
        examples=['1'],
        gt=0,
    )
    is_posted: bool = Field(
        title='Publication of project',
        description='Has the project been published?',
        examples=[True],
    )
    is_posted_in_bot: bool = Field(
        title='Publication project in a telegram bot',
        description='Has the project been published in a telegram bot?',
        examples=[False],
    )
    preview_photo: MediaPreviewPhoto
    project_category: ProjectCategory


class Projects(BaseModel):
    projects: list[Project] = Field(
        title='List of projects',
        description='List of projects',
    )


class ProjectCreate(ProjectBase):
    is_posted: bool = Field(
        default=True,
        title='Publication of project',
        description='Has the project been published?',
        examples=[True],
    )
    is_posted_in_bot: bool = Field(
        default=False,
        title='Publication project in a telegram bot',
        description='Has the project been published in a telegram bot?',
        examples=[False],
    )
    preview_photo_id: int = Field(
        title='Preview photo ID',
        description='Preview photo ID project',
        examples=[1],
        gt=0,
    )
    project_category_id: int = Field(
        title='Project category ID',
        description='Project category ID',
        examples=['1'],
        gt=0,
    )


class ProjectUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        title='New project title',
        description='New project title',
        examples=['SPACE GAME\nEXHIBITION'],
    )
    description: str | None = Field(
        default=None,
        title='New project description',
        description='New brief description of the project',
        examples=['This ship has no destination. The path is the goal'],
    )
    text: str | None = Field(
        default=None,
        title='New project text',
        description='New text of the project in the projects section in markdown format',
        examples=[
            'A living crystalline structure is formed in places of greatest intensity'
            ' and follows the movements of the guest for some time... [picture](url_to_picture)'
        ],
    )
    project_category_id: int | None = Field(
        default=None,
        title='New project category ID',
        description='New project category ID',
        examples=['1'],
        gt=0,
    )
    created_at: date | None = Field(
        default=None,
        title='New project release date',
        description='New project release date',
        examples=['2023-12-24'],
    )
    is_posted: bool = Field(
        default=True,
        title='Publication of project',
        description='Has the project been published?',
        examples=[True],
    )
    is_posted_in_bot: bool = Field(
        default=False,
        title='Publication project in a telegram bot',
        description='Has the project been published in a telegram bot?',
        examples=[False],
    )
    preview_photo_id: int | None = Field(
        default=None,
        title='New preview photo ID',
        description='New preview photo ID project',
        examples=[1],
        gt=0,
    )
