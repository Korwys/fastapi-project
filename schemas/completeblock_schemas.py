from pydantic import BaseModel, HttpUrl


class BaseCompleteContentBlock(BaseModel):
    student_id: int | None
    content_block_id: int | None
    url: HttpUrl | None
    feedback: str | None
    grade: int | None


class CreateCompleteContentBlock(BaseCompleteContentBlock):
    ...


class CompleteContentBlock(BaseCompleteContentBlock):
    id: int

    class Config:
        orm_mode = True
