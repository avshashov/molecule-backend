import datetime

from sqlalchemy import select

from app.database import models
from app.tests.conftest import async_client, _test_db


async def test_get_all_press():
    async with async_client:
        response = await async_client.get('/')
        assert response.status_code == 404


async def test_add_press_to_db():
    session = _test_db.get_session()
    item = models.Press(
        title='test',
        description='test',
        created_at=datetime.date(2023, 12, 7),
        preview_photo_id=1,
        external_link='link',
    )
    session.add(item)
    await session.commit()
    assert True


async def test_get_item():
    session = _test_db.get_session()
    stmt = select(models.Press).where(models.Press.title == 'test')
    item = await session.execute(stmt)
    assert item.scalar() == ('test', 'test', datetime.date(2023, 12, 7), 1, 'link')
