from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.responses import JSONResponse

from db.models.courses import Section
from schemas import sections_schemas


async def section_list(db: AsyncSession):
    return db.query(Section).all()


async def new_section(db: AsyncSession, section: sections_schemas.CreateSection):
    db_section = Section(title=section.title, description=section.description, course_id=section.course_id)
    db.add(db_section)
    await db.commit()
    await db.refresh(db_section)
    return db_section


async def get_section(db: AsyncSession, section_id: int):
    section = await db.execute(select(Section).where(Section.id == section_id))
    return section.scalar_one_or_none()


async def delete_section(db: AsyncSession, section_id: int):
    section = delete(Section).where(Section.id == section_id)
    await db.execute(section)
    await db.commit()
    return JSONResponse(status_code=200, content={'Message': 'Section deleted'})
