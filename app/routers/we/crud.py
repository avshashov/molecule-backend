from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Electron


class CRUD:
    @staticmethod
    async def get_items(session: AsyncSession, count: int = 10, offset: int = 0) -> list[Electron] | list:
        stmt = select(Electron).slice(offset, offset + count)
        items = await session.scalars(stmt)
        return list(items)
