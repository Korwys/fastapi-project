from db.models.courses import Course, CompletedContentBlock
from schemas.completeblock_schemas import CompletedContentBlockCreate, CompletedContentBlockUpdate
from services.crud.base import CRUDBase


class CRUDCompletedContentBlock(CRUDBase[CompletedContentBlock, CompletedContentBlockCreate, CompletedContentBlockUpdate]):
    ...


completedcb = CRUDCompletedContentBlock(CompletedContentBlock)
