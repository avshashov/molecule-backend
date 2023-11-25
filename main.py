from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.database.settings import Database
from app.routers.press.api import router as press


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(press)

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
