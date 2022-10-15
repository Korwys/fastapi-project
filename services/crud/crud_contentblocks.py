from sqlalchemy.ext.asyncio import AsyncSession

from db.models.courses import ContentBlock
from schemas.contentblock_schemas import ContentBlockCreate, ContentBlockUpdate
from services.crud.base import CRUDBase, CreateSchemaType, ModelType


class CRUDContentBlock(CRUDBase[ContentBlock, ContentBlockCreate, ContentBlockUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        db_content = self.model(title=obj_in.title, description=obj_in.description,
                                  type=obj_in.type,
                                  url=obj_in.url, content=obj_in.url, section_id=obj_in.section_id)
        db.add(db_content)
        await db.commit()
        await db.refresh(db_content)
        return db_content


contentblock = CRUDContentBlock(ContentBlock)
