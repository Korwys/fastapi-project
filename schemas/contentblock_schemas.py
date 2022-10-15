from pydantic import BaseModel, HttpUrl

from db.models.courses import ContentType


class ContentBlockBase(BaseModel):
    title: str
    description: str
    type: ContentType | None
    url: HttpUrl
    content: str
    section_id: int


class ContentBlockCreate(ContentBlockBase):
    ...


class ContentBlockUpdate(ContentBlockBase):
    ...


class ContentBlockInDBBase(ContentBlockBase):
    id: int

    class Config:
        orm_mode = True


class ContentBlock(ContentBlockInDBBase):
    ...
