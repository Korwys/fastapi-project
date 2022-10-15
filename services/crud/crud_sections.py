from db.models.courses import Section
from schemas.sections_schemas import SectionUpdate, CreateSection
from services.crud.base import CRUDBase


class CRUDSections(CRUDBase[Section, CreateSection, SectionUpdate]):
    ...


sections = CRUDSections(Section)
