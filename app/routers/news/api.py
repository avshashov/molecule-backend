from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.database import models
from app.database.settings import database
from app.common.crud import CRUD

router = APIRouter(prefix='/news', tags=['news'])
Session = Annotated[AsyncSession, Depends(database.get_session)]


@router.get('/news_dates')
async def get_all_news_dates(db: Session) -> schemas.Dates:
    dates = await CRUD.get_dates(session=db, model=models.News)
    if dates:
        return {'years': dates}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dates not found')


@router.get('/')
async def get_all_news(
    db: Session,
    year: int,
    is_posted: bool = True,
    count: Annotated[int, Query(ge=5, le=50)] = 10,
    offset: Annotated[int, Query(ge=0, le=50)] = 0,
) -> schemas.NewsMany:
    news = await CRUD.get_items(
        session=db, model=models.News, year=year, is_posted=is_posted, count=count, offset=offset
    )
    if news:
        return {'news': news}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='News not found')


@router.get('/{news_id}')
async def get_news_article(db: Session, news_id: int) -> schemas.News:
    article = await CRUD.get_item(session=db, id=news_id, model=models.News)
    if article:
        return article
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'News article with id {news_id} not found'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_news_article(db: Session, article: schemas.NewsCreate) -> schemas.NewsCreate:
    article = await CRUD.create_item(session=db, model=models.News, schema_fields=article)
    return article


@router.delete('/{news_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_news_article(db: Session, news_id: int):
    if not await CRUD.item_exists(session=db, id=news_id, model=models.News):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'News article with id {news_id} not found'
        )
    await CRUD.delete_item(session=db, id=news_id, model=models.News)


@router.patch('/{news_id}', status_code=status.HTTP_200_OK)
async def patch_news_article(db: Session, news_id: int, new_article_fields: schemas.NewsUpdate):
    if not await CRUD.item_exists(session=db, id=news_id, model=models.News):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'News article with id {news_id} not found'
        )
    article = await CRUD.update_item(
        session=db, id=news_id, model=models.News, schema_fields=new_article_fields
    )
    return article
