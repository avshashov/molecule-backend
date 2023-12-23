from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.database import models
from app.database.settings import database
from app.common.crud import CRUD as CommonCRUD
from app.routers.projects.crud import CRUD

router = APIRouter(prefix='/projects', tags=['projects'])
Session = Annotated[AsyncSession, Depends(database.get_session)]


@router.get('/projects_dates')
async def get_all_projects_dates(db: Session) -> schemas.Dates:
    dates = await CommonCRUD.get_dates(session=db, model=models.Project)
    if dates:
        return {'years': dates}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dates not found')


@router.get('/project_categories')
async def get_project_categories(db: Session) -> schemas.ProjectCategories:
    categories = await CRUD.get_categories(session=db)
    if categories:
        return {'categories': categories}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Categories not found')


@router.get('/')
async def get_all_projects(
    db: Session,
    year: int,
    category: str,
    is_posted: bool = True,
    count: Annotated[int, Query(ge=5, le=50)] = 10,
    offset: Annotated[int, Query(ge=0, le=50)] = 0,
) -> schemas.Projects:
    projects = await CRUD.get_items(
        session=db, year=year, category=category, is_posted=is_posted, count=count, offset=offset
    )
    if projects:
        return {'projects': projects}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Projects not found')


@router.get('/{project_id}')
async def get_project(db: Session, project_id: int) -> schemas.Project:
    project = await CRUD.get_item(session=db, id=project_id)
    if project:
        return project
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id {project_id} not found'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_project(db: Session, fields: schemas.ProjectCreate) -> schemas.ProjectCreate:
    project = await CommonCRUD.create_item(session=db, model=models.Project, schema_fields=fields)
    return project


@router.delete('/{project_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(db: Session, project_id: int):
    if not await CommonCRUD.item_exists(session=db, id=project_id, model=models.Project):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id {project_id} not found'
        )
    await CommonCRUD.delete_item(session=db, id=project_id, model=models.Project)


@router.patch('/{project_id}', status_code=status.HTTP_200_OK)
async def patch_project(db: Session, project_id: int, new_project_fields: schemas.ProjectUpdate):
    if not await CommonCRUD.item_exists(session=db, id=project_id, model=models.Project):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id {project_id} not found'
        )
    project = await CommonCRUD.update_item(
        session=db, id=project_id, model=models.Project, schema_fields=new_project_fields
    )
    return project
