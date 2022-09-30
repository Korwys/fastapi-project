from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.responses import JSONResponse

from db.models.courses import ContentBlock, CompletedContentBlock
from schemas import completeblock_schemas


async def add_new_student(db: AsyncSession, completeblock: completeblock_schemas.CreateCompleteContentBlock):
    db_content = CompletedContentBlock(student_id=completeblock.student_id,
                                       content_block_id=completeblock.content_block_id, url=completeblock.url,
                                       feedback=completeblock.feedback, grade=completeblock.grade)
    db.add(db_content)
    await db.commit()
    await db.refresh(db_content)
    return db_content


async def list_of_completeblocks(db: AsyncSession):
    return db.query(CompletedContentBlock).all()


async def get_completedblock(db: AsyncSession, completedblock_id: int):
    course = await db.execute(select(CompletedContentBlock).where(CompletedContentBlock.id == completedblock_id))
    return course.scalar_one_or_none()


async def delete_completedblock(completedblock_id: int, db: AsyncSession):
    course = delete(CompletedContentBlock).where(CompletedContentBlock.id == completedblock_id)
    await db.execute(course)
    await db.commit()
    return JSONResponse(status_code=200, content={'Message': 'Data deleted'})


async def edit_completedblock(completedblock_id: int, block: completeblock_schemas.BaseCompleteContentBlock,
                               db: AsyncSession):
    obj_in = block.dict(exclude_unset=True)
    content_update = update(CompletedContentBlock).where(CompletedContentBlock.id == completedblock_id).values(**obj_in)
    await db.execute(content_update)
    await db.commit()
    new_content_block = await db.execute(
        select(CompletedContentBlock).where(CompletedContentBlock.id == completedblock_id))
    return new_content_block.scalar_one_or_none()
