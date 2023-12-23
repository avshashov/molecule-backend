from datetime import date

from pydantic import BaseModel

from app.schemas.media import MediaPreviewPhoto


class ProjectCategory(BaseModel):
    id: int
    name: str


class ProjectCategories(BaseModel):
    categories: list[ProjectCategory]


class ProjectBase(BaseModel):
    title: str
    description: str
    text: str
    created_at: date


class Project(ProjectBase):
    id: int
    is_posted: bool
    is_posted_in_bot: bool
    preview_photo: MediaPreviewPhoto
    project_category: ProjectCategory


class Projects(BaseModel):
    projects: list[Project]


class ProjectCreate(ProjectBase):
    is_posted: bool = True
    is_posted_in_bot: bool = False
    preview_photo_id: int
    project_category_id: int


class ProjectUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    text: str | None = None
    project_category_id: int | None = None
    created_at: date | None = None
    is_posted: bool = True
    is_posted_in_bot: bool = False
    preview_photo_id: int | None = None
