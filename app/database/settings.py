from typing import AsyncIterable

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import settings
from app.database.models import Base


class Database:
    def __init__(self):
        self._settings_db = settings.database
        self._url = self._build_url()
        self.engine = create_async_engine(url=self._url, echo=self._settings_db.echo_db)
        self.async_session = async_sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_session(self) -> AsyncIterable[AsyncSession]:
        async with self.async_session() as session:
            yield session

    def _build_url(self) -> str:
        driver = f'+{self._settings_db.driver}' if self._settings_db.driver else ''
        password = f':{self._settings_db.password}' if self._settings_db.password else ''
        port = f':{self._settings_db.port}' if self._settings_db.port else ''
        url = (
            f'{self._settings_db.dbms}'
            f'{driver}'
            f'://{self._settings_db.user}'
            f'{password}'
            f'@{self._settings_db.host}'
            f'{port}'
            f'/{self._settings_db.database}'
        )
        return url

    @property
    def url(self):
        return self._url


database = Database()
