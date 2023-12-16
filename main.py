from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.routers.media.api import router as media
from app.routers.news.api import router as news
from app.routers.press.api import router as press
from app.routers.projects.api import router as projects
from app.routers.we.api import router as electrons


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(media)
app.include_router(news)
app.include_router(press)
app.include_router(projects)
app.include_router(electrons)

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
