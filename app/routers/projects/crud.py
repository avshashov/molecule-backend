from sqlalchemy import select, asc, extract, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Project, ProjectCategory


async def get_categories(session: AsyncSession) -> list[ProjectCategory] | None:
    stmt = select(ProjectCategory.name).order_by(asc(ProjectCategory.name))
    dates = await session.scalars(stmt)
    return list(dates)


async def get_items(
    session: AsyncSession, year: int, category: str, is_posted: bool = True, count: int = 10, offset: int = 0
) -> list[Project] | None:
    stmt = (
        select(Project)
        .join(ProjectCategory)
        .where(
            ProjectCategory.name == category,
            Project.is_posted.is_(is_posted),
            extract('YEAR', Project.created_at) == year,
        )
        .order_by(desc(Project.created_at))
    ).slice(offset, offset + count)

    item = await session.scalars(stmt)
    return list(item)
