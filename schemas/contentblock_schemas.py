from pydantic import BaseModel, HttpUrl

from db.models.courses import ContentType


class BaseContentBlock(BaseModel):
    title: str | None
    description: str | None
    type: ContentType | None
    url: HttpUrl | None
    content: str | None
    section_id: int | None


class CreateContentBlock(BaseContentBlock):
    ...


class ContentBlock(BaseContentBlock):
    id: int

    class Config:
        orm_mode = True
