import os
from datetime import datetime

import aiofiles
from fastapi import UploadFile

from app import schemas
from config import settings


async def save_file(file: UploadFile, media_metadata: schemas.MediaBase) -> str:
    created_at_date = datetime.today().strftime('%Y-%m-%d %H-%M')
    filename = f'{media_metadata.name}_{created_at_date}'
    path = os.path.join(settings.files.temp_dir, filename)

    async with aiofiles.open(file=path, mode='wb') as aiofile:
        content = await file.read()
        await aiofile.write(content)

    return path
