from sqlalchemy import select, asc, extract, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database.models import Project, ProjectCategory, Media


class CRUD:
    @staticmethod
    async def get_categories(session: AsyncSession) -> list[ProjectCategory] | list:
        stmt = select(ProjectCategory).order_by(asc(ProjectCategory.name))
        categories = await session.scalars(stmt)
        return list(categories)

    @staticmethod
    async def get_items(
        session: AsyncSession,
        year: int,
        category: str,
        is_posted: bool = True,
        count: int = 10,
        offset: int = 0,
    ) -> list[Project] | list:
        stmt = (
            select(Project)
            .join(ProjectCategory)
            .join(Media)
            .options(joinedload(Project.preview_photo), joinedload(Project.project_category))
            .where(
                ProjectCategory.name == category,
                Project.is_posted.is_(is_posted),
                extract('YEAR', Project.created_at) == year,
            )
            .order_by(desc(Project.created_at))
        ).slice(offset, offset + count)
        item = await session.scalars(stmt)
        return list(item)

    @staticmethod
    async def get_item(session: AsyncSession, id: int) -> Project | None:
        stmt = (
            select(Project)
            .join(ProjectCategory)
            .join(Media)
            .options(joinedload(Project.preview_photo), joinedload(Project.project_category))
            .where(Project.id == id)
        )
        item = await session.execute(stmt)
        return item.scalar()
