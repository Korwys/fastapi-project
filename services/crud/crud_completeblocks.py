from db.models.courses import Course, CompletedContentBlock
from schemas.completeblock_schemas import CompletedContentBlockCreate, CompletedContentBlockUpdate
from services.crud.base import CRUDBase


class CRUDCompletedContentBlock(
    CRUDBase[CompletedContentBlock, CompletedContentBlockCreate, CompletedContentBlockUpdate]):
    """Класс наследует все методы CREATE,READ,UPDATE,DELETE. Реализует CRUD операции над моделью CompletedContenBlock"""
    ...


completedcb = CRUDCompletedContentBlock(CompletedContentBlock)
