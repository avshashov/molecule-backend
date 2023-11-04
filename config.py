from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings


class Database(BaseModel):
    dbms: str
    driver: str
    host: str
    port: int
    user: str
    password: str
    database: str
    echo_db: bool


class Settings(YamlBaseSettings):
    database: Database

    model_config = SettingsConfigDict(yaml_file='config.yaml')


settings = Settings()
