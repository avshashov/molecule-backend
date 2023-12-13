from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status, File, Form, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models
from app.database.settings import database
from app import schemas
from app.routers.common import files
from app.routers.common.crud import CRUD

router = APIRouter(prefix='/media', tags=['media'])
Session = Annotated[AsyncSession, Depends(database.get_session)]


@router.get('/')
async def get_media_files(
    db: Session,
    count: Annotated[int, Query(ge=5, le=50)] = 10,
    offset: Annotated[int, Query(ge=0, le=50)] = 0,
):
    media = await CRUD.get_media_items(session=db, count=count, offset=offset)
    if media:
        return media
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Media not found')


@router.get('/{media_id}')
async def get_media_file(db: Session, media_id: int):
    media = await CRUD.get_media_items(session=db, id=media_id)
    if media:
        return media
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Media with {media_id} not found')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def upload_media_file(
    db: Session,
    file: Annotated[UploadFile, File()],
    media_name: Annotated[str, Form()],
    media_type_id: Annotated[int, Form()],
    media_description: Annotated[str, Form()],
):
    filepath = await files.save_file(file, media_name)
    media_metadata = schemas.MediaCreate(
        name=media_name, type_id=media_type_id, link=filepath, description=media_description
    )
    file_metadata = await CRUD.create_item(
        session=db, model=models.Media, schema_fields=media_metadata
    )
    return file_metadata


@router.delete('/{media_id}')
async def delete_media_file(db: Session, media_id: int):
    pass
