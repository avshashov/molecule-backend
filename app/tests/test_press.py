import datetime

import pytest
from fastapi import Depends
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models
from app.tests.conftest import _test_db


@pytest.mark.asyncio(scope='session')
async def test_get_all_press(async_client: AsyncClient):
    response = await async_client.get('/press/press_dates')
    print(response.json())
    assert response.status_code == 404


@pytest.mark.asyncio(scope='session')
async def test_create_press_article(async_client: AsyncClient, db_session: AsyncSession):
    response = await async_client.post(
        '/press/',
        json={
            'title': 'test21',
            'description': 'test1',
            'created_at': '2023-12-07',
            'preview_photo_id': 2,
            'external_link': 'link1',
        },
    )
    print(response.json())
    assert response.status_code == 201


# @pytest.mark.asyncio(scope='session')
# async def test_add_press_to_db(db_session: AsyncSession):
#     item1 = models.Press(
#         title='test1',
#         description='test1',
#         created_at=datetime.date(2023, 12, 7),
#         preview_photo_id=1,
#         external_link='link1',
#     )
#     item2 = models.Press(
#         title='test2',
#         description='test2',
#         created_at=datetime.date(2023, 10, 27),
#         preview_photo_id=2,
#         external_link='link2',
#     )
#     db_session.add_all([item1, item2])
#     await db_session.commit()
#     assert True


@pytest.mark.asyncio(scope='session')
async def test_get_all_press1(async_client: AsyncClient):
    response = await async_client.get('/press/press_dates')
    print(response.json())
    assert response.status_code == 404


# @pytest.mark.asyncio(scope='session')
# async def test_get_item(db_session: AsyncSession):
#     session = _test_db.get_session()
#     stmt = select(models.Press).where(models.Press.title == 'test')
#     item = await session.execute(stmt)
#     assert item.scalar() == ('test', 'test', datetime.date(2023, 12, 7), 1, 'link')
