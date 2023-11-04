from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import settings
from app.database.models import Base


class Database:
    def __init__(self):
        self._settings_db = settings.database
        url = self._build_url()
        self.engine = create_async_engine(url=url, echo=self._settings_db.echo_db)
        self.async_session = async_sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_session(self) -> AsyncSession:
        async with self.async_session() as session:
            yield session

    def _build_url(self) -> str:
        url = (
            f'{self._settings_db.dbms}+'
            f'{self._settings_db.driver}://'
            f'{self._settings_db.user}:'
            f'{self._settings_db.password}@'
            f'{self._settings_db.host}:'
            f'{self._settings_db.port}/'
            f'{self._settings_db.database}'
        )
        return url
