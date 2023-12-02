from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.database import models
from app.database.settings import database
from app.routers.common.crud import CRUD

router = APIRouter(prefix='/press', tags=['press'])
Session = Annotated[AsyncSession, Depends(database.get_session)]


@router.get('/press_dates')
async def get_all_press_dates(db: Session):
    dates = await CRUD.get_dates(session=db, model=models.Press)
    if dates:
        return dates
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dates not found')


@router.get('/')
async def get_all_press(
    db: Session,
    year: int,
    is_posted: bool = True,
    count: Annotated[int, Query(ge=5, le=50)] = 10,
    offset: Annotated[int, Query(ge=0, le=50)] = 0,
):
    press = await CRUD.get_items(
        session=db, model=models.Press, year=year, is_posted=is_posted, count=count, offset=offset
    )
    if press:
        return press
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Press not found')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_press_article(db: Session, article: schemas.PressCreate):
    article = await CRUD.create_item(session=db, model=models.Press, schema_fields=article)
    return article


@router.delete('/{press_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_press_article(db: Session, press_id: int):
    if not await CRUD.item_exists(session=db, id=press_id, model=models.Press):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Press not found')
    await CRUD.delete_item(session=db, id=press_id, model=models.Press)


@router.patch('/{press_id}', status_code=status.HTTP_200_OK)
async def patch_press_article(db: Session, press_id: int, new_article_fields: schemas.PressUpdate):
    if not await CRUD.item_exists(session=db, id=press_id, model=models.Press):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Press not found')
    article = await CRUD.update_item(
        session=db, id=press_id, model=models.Press, schema_fields=new_article_fields
    )
    return article
