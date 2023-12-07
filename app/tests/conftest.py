from contextlib import asynccontextmanager
from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

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


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    await _test_db.create_tables()
    yield
    await _test_db.drop_tables()


@pytest.fixture(scope='session')
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await _test_db.create_tables()
#     yield
#     await _test_db.drop_tables()


# @app.on_event("startup")
# async def startup():
#     await _test_db.create_tables()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await _test_db.drop_tables()

app.dependency_overrides[Session] = _test_db.get_session

# async_client = AsyncClient(app=app, base_url="http://test")
