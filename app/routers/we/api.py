from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.database import models
from app.database.settings import database
from app.routers.common.crud import CRUD as CommonCRUD
from app.routers.we.crud import CRUD

router = APIRouter(prefix='/we/electrons', tags=['electrons'])
Session = Annotated[AsyncSession, Depends(database.get_session)]


@router.get('/')
async def get_participants(
    db: Session,
    count: Annotated[int, Query(ge=5, le=50)] = 10,
    offset: Annotated[int, Query(ge=0, le=50)] = 0,
):
    participants = await CRUD.get_items(session=db, count=count, offset=offset)
    if participants:
        return {'participants': participants}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Electrons not found')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_participant(db: Session, participant: schemas.ElectronsCreate) -> schemas.ElectronsCreate:
    participant = await CommonCRUD.create_item(session=db, model=models.Electron, schema_fields=participant)
    return participant


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_participant(db: Session, id: int):
    if not await CommonCRUD.item_exists(session=db, id=id, model=models.Electron):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Electron with id {id} not found')
    await CommonCRUD.delete_item(session=db, id=id, model=models.Electron)


@router.patch('/{id}', status_code=status.HTTP_200_OK)
async def patch_participant(db: Session, id: int, new_participant_fields: schemas.ElectronsUpdate):
    if not await CommonCRUD.item_exists(session=db, id=id, model=models.Electron):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Electron with id {id} not found')
    participant = await CommonCRUD.update_item(
        session=db, id=id, model=models.Electron, schema_fields=new_participant_fields
    )
    return participant
