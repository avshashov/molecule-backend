from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database.models import Electron


class CRUD:
    @staticmethod
    async def get_items(session: AsyncSession, count: int = 10, offset: int = 0) -> list[Electron] | list:
        stmt = select(Electron).options(joinedload(Electron.preview_photo)).slice(offset, offset + count)
        items = await session.scalars(stmt)
        return list(items)
