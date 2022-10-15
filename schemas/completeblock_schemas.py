from pydantic import BaseModel, HttpUrl


class CompletedContentBlockBase(BaseModel):
    student_id: int | None
    content_block_id: int | None
    url: HttpUrl | None
    feedback: str | None
    grade: int | None


class CompletedContentBlockCreate(CompletedContentBlockBase):
    ...


class CompletedContentBlockUpdate(CompletedContentBlockBase):
    ...


class CompletedContentBlockInDBBase(CompletedContentBlockBase):
    id: int

    class Config:
        orm_mode = True


class CompletedContentBlock(CompletedContentBlockInDBBase):
    pass
