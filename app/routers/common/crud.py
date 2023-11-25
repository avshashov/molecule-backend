from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession


class CRUD:
    @staticmethod
    async def get_dates(session: AsyncSession, model):  # -> list[model_name] | None:
        stmt = select(model.created_at).distinct()
        dates = await session.scalars(stmt)
        return list(dates)

    @staticmethod
    async def get_item(session: AsyncSession, id: int, model):  # -> model_name | None:
        stmt = select(model).where(model.id == id)
        item = await session.execute(stmt)
        return item.scalar()

    @staticmethod
    async def get_items(session: AsyncSession, model):  # -> list[models_name] | None:
        stmt = select(model)
        item = await session.scalars(stmt)
        return list(item)

    @staticmethod
    async def item_exists(session: AsyncSession, id: int, model) -> bool:
        stmt = select(model.id).where(model.id == id).exists()
        result = await session.execute(stmt)
        return result.scalar()

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
