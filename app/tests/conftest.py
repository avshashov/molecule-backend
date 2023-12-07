import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.database.models import Base
from app.database.settings import Database
from app.routers.press.api import Session
from main import app


class TestDatabase(Database):
    def __init__(self):
        self._url = "sqlite+aiosqlite://"
        self.engine = create_async_engine(url=self._url, connect_args={"check_same_thread": False})
        self.async_session = async_sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)

    async def drop_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


_test_db = TestDatabase()


@pytest.fixture(scope='session')
async def db_session() -> AsyncSession:
    async for session in _test_db.get_session():
        yield session


# app.dependency_overrides[Session] = db_session


@pytest.fixture(autouse=True, scope='session')
async def prepare_database() -> None:
    await _test_db.create_tables()
    yield
    await _test_db.drop_tables()


@pytest.fixture(scope='session')
async def async_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client
