from sqlalchemy import select, delete, update, extract, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database.models import Media


class CRUD:
    @staticmethod
    async def get_dates(session: AsyncSession, model):  # -> list[model_name] | None:
        stmt = select(extract('YEAR', model.created_at).label('year')).distinct().order_by(asc('year'))
        dates = await session.scalars(stmt)
        return list(dates)

    @staticmethod
    async def get_item(session: AsyncSession, id: int, model):  # -> model_name | None:
        stmt = select(model).where(model.id == id)
        item = await session.execute(stmt)
        return item.scalar()

    @staticmethod
    async def get_items(
        session: AsyncSession, model, year: int, is_posted: bool = True, count: int = 10, offset: int = 0
    ):  # -> list[models_name] | None:
        stmt = (
            select(model)
            .where(extract('YEAR', model.created_at).label('year') == year, model.is_posted.is_(is_posted))
            .order_by(desc(model.created_at))
        ).slice(offset, offset + count)

        items = await session.scalars(stmt)
        return list(items)

    @staticmethod
    async def item_exists(session: AsyncSession, id: int, model) -> bool:
        # TODO: через метод .exists() выдает ошибку
        # stmt = select(model).where(model.id == id).exists()
        # result = await session.execute(text(str(stmt)), {'id': id})
        stmt = select(model).where(model.id == id)
        item = await session.execute(stmt)
        return bool(item.scalar())

    @staticmethod
    async def create_item(session: AsyncSession, model, schema_fields):  # -> model_name:
        item = model(**schema_fields.model_dump())
        session.add(item)
        await session.commit()
        return item

    @staticmethod
    async def delete_item(session: AsyncSession, id: int, model) -> None:
        stmt = delete(model).where(model.id == id)
        await session.execute(stmt)
        await session.commit()

    @staticmethod
    async def update_item(session: AsyncSession, id: int, model, schema_fields):  # -> model_name:
        stmt = (
            update(model)
            .where(model.id == id)
            .values(**schema_fields.model_dump(exclude_none=True))
            .returning(model)
        )
        item = await session.execute(stmt)
        await session.commit()
        return item.scalar()

    @staticmethod
    async def get_media_items(
        session: AsyncSession, count: int = 10, offset: int = 0, id: int = None
    ) -> list[Media] | list:
        if id:
            stmt = select(Media).where(Media.id == id)
        else:
            stmt = select(Media)
        stmt = (stmt.options(joinedload(Media.media_type))).slice(offset, offset + count)
        media = await session.scalars(stmt)
        return list(media)
