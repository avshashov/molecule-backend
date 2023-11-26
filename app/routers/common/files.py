import os
from datetime import datetime

import aiofiles
from fastapi import UploadFile

from config import settings


async def save_file(file: UploadFile, media_name: str) -> str:
    file_format = file.content_type.split('/')[-1]
    created_at_date = datetime.today().strftime('%Y-%m-%d %H-%M')
    filename = f'{media_name}_{created_at_date}.{file_format}'
    path = os.path.join(settings.files.temp_dir, filename)

    async with aiofiles.open(file=path, mode='wb') as aiofile:
        content = await file.read()
        await aiofile.write(content)

    return path
