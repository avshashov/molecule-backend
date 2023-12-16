from pydantic import BaseModel, Field


class Dates(BaseModel):
    years: list[int] = Field(
        title='List items dates',
        description='List unique dates of available elements in YEAR format',
        examples=[[2022, 2023, 2024]]
    )
