from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status, File, Form, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models
from app.database.settings import database
from app import schemas
from app.common import files
from app.common.crud import CRUD as CommonCRUD
from app.routers.media.crud import CRUD

router = APIRouter(prefix='/media', tags=['media'])
Session = Annotated[AsyncSession, Depends(database.get_session)]


@router.get('/media_types')
async def get_media_types(db: Session) -> schemas.MediaTypes:
    types = await CRUD.get_types(session=db)
    if types:
        return {'types': types}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'MediaTypes not found')


@router.get('/')
async def get_media_files(
    db: Session,
    count: Annotated[int, Query(ge=5, le=50)] = 10,
    offset: Annotated[int, Query(ge=0, le=50)] = 0,
) -> schemas.MediaMany:
    media = await CRUD.get_items(session=db, count=count, offset=offset)
    if media:
        return {'media': media}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Media not found')


@router.get('/{media_id}')
async def get_media_file(db: Session, media_id: int) -> schemas.Media:
    media = await CRUD.get_items(session=db, id=media_id)
    if media:
        return media[0]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Media with {media_id} not found')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def upload_media_file(
    db: Session,
    file: Annotated[UploadFile, File()],
    media_name: Annotated[str, Form()],
    media_type_id: Annotated[int, Form()],
    media_description: Annotated[str, Form()],
) -> schemas.MediaCreate:
    filepath = await files.save_file(file, media_name)
    media_metadata = schemas.MediaCreate(
        name=media_name, type_id=media_type_id, link=filepath, description=media_description
    )
    file_metadata = await CommonCRUD.create_item(
        session=db, model=models.Media, schema_fields=media_metadata
    )
    return file_metadata


@router.delete('/{media_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_media_file(db: Session, media_id: int):
    if not await CommonCRUD.item_exists(session=db, id=media_id, model=models.Media):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Media with {media_id} not found')
    await CommonCRUD.delete_item(session=db, id=media_id, model=models.Media)


@router.patch('/{media_id}', status_code=status.HTTP_200_OK)
async def patch_name_or_description_media(db: Session, media_id: int, new_media_fields: schemas.MediaUpdate):
    if not await CommonCRUD.item_exists(session=db, id=media_id, model=models.Media):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Media with {media_id} not found')
    media = await CommonCRUD.update_item(
        session=db, id=media_id, model=models.Media, schema_fields=new_media_fields
    )
    return media
