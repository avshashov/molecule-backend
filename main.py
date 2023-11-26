from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.routers.press.api import router as press
from app.routers.media.api import router as media


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(media)
app.include_router(press)

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
