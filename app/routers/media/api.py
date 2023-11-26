from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import models
from app.database.settings import database
from app import schemas
from app.routers.common import files
from app.routers.common.crud import CRUD

router = APIRouter(prefix='/media', tags=['media'])
Session = Annotated[AsyncSession, Depends(database.get_session)]


@router.get('/')
async def get_media_files(db: Session):
    pass


@router.get('/{media_id}')
async def get_media_file(db: Session, media_id: int):
    pass


@router.post('/')
async def upload_media_file(db: Session, file: UploadFile, media_metadata: schemas.MediaBase):
    filepath = await files.save_file(file, media_metadata)
    media_metadata = schemas.MediaCreate(**media_metadata.model_dump(), link=filepath)
    await CRUD.create_item(session=db, model=models.Media, schema_fields=media_metadata)


@router.delete('/{media_id}')
async def delete_media_file(db: Session, media_id: int):
    pass
