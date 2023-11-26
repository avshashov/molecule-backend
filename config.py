from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings


class Database(BaseModel):
    dbms: str
    driver: str | None
    host: str
    port: int | None
    user: str
    password: str | None
    database: str
    echo_db: bool


class Files(BaseModel):
    temp_dir: str


class Settings(YamlBaseSettings):
    database: Database
    files: Files

    model_config = SettingsConfigDict(yaml_file='config.yaml')


settings = Settings()
