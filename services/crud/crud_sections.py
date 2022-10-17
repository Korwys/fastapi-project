from db.models.courses import Section
from schemas.sections_schemas import SectionUpdate, CreateSection
from services.crud.base import CRUDBase


class CRUDSections(CRUDBase[Section, CreateSection, SectionUpdate]):
    """Класс наследует все методы CREATE,READ,UPDATE,DELETE. Реализует CRUD операции над моделью Section"""
    ...


sections = CRUDSections(Section)
