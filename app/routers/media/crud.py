from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database.models import Media, MediaType


class CRUD:
    @staticmethod
    async def get_items(
        session: AsyncSession, count: int = 10, offset: int = 0, id: int = None
    ) -> list[Media] | list:
        if id:
            stmt = select(Media).where(Media.id == id)
        else:
            stmt = select(Media)
        stmt = (stmt.options(joinedload(Media.media_type))).slice(offset, offset + count)
        media = await session.scalars(stmt)
        return list(media)

    @staticmethod
    async def get_types(session: AsyncSession) -> list[MediaType] | list:
        stmt = select(MediaType)
        types = await session.scalars(stmt)
        return list(types)
