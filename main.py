from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.database.settings import Database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Database().create_tables()
    yield


app = FastAPI(lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
