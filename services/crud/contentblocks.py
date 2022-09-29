from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.responses import JSONResponse

from db.models.courses import ContentBlock
from schemas import contentblock_schemas


async def new_contentblock(db: AsyncSession, contentblock: contentblock_schemas.CreateContentBlock):
    db_content = ContentBlock(title=contentblock.title, description=contentblock.description, type=contentblock.type,
                              url=contentblock.url, content=contentblock.url, section_id=contentblock.section_id)
    db.add(db_content)
    await db.commit()
    await db.refresh(db_content)
    return db_content


async def list_of_contentblocks(db: AsyncSession):
    return db.query(ContentBlock).all()


async def get_contentblock(db: AsyncSession, contentblock_id: int):
    course = await db.execute(select(ContentBlock).where(ContentBlock.id == contentblock_id))
    return course.scalar_one_or_none()


async def delete_contentblock(contentblock_id: int, db: AsyncSession):
    course = delete(ContentBlock).where(ContentBlock.id == contentblock_id)
    await db.execute(course)
    await db.commit()
    return JSONResponse(status_code=200, content={'Message': 'Course deleted'})


async def edit_contentblock(contentblock_id: int, contentblock: contentblock_schemas.BaseContentBlock,
                            db: AsyncSession):
    obj_in = contentblock.dict(exclude_unset=True)
    content_update = update(ContentBlock).where(ContentBlock.id == contentblock_id).values(**obj_in)
    await db.execute(content_update)
    await db.commit()
    new_content_block = await db.execute(select(ContentBlock).where(ContentBlock.id == contentblock_id))
    return new_content_block.scalar_one_or_none()
