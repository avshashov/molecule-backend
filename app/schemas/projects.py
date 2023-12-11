from datetime import date

from pydantic import BaseModel


class ProjectsBase(BaseModel):
    title: str
    description: str
    text: str
    project_category_id: int
    created_at: date
    preview_photo_id: int


class Projects(ProjectsBase):
    id: int
    is_posted: bool
    is_posted_in_bot: bool


class ProjectsCreate(ProjectsBase):
    is_posted: bool = True
    is_posted_in_bot: bool = False


class ProjectsUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    text: str | None = None
    project_category_id: int | None = None
    created_at: date | None = None
    is_posted: bool = True
    is_posted_in_bot: bool = False
    preview_photo_id: int | None = None
