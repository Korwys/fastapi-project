import fastapi
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db, get_db
from schemas import studen_course_schemas
from services.crud.sections import new_section, section_list, get_section, delete_section
from services.crud.studentcourses import new_student, list_of_student_on_courses, select_student, \
    delete_selected_student, edit_studentcourse_info

router = fastapi.APIRouter()


@router.post('/add_student_on_course', response_model=studen_course_schemas.StudentCourse)
async def add_student_in_course(course: studen_course_schemas.CreateStudentCourse, db: AsyncSession = Depends(async_get_db)):
    return await new_student(db=db, course=course)


@router.get('/student_courses', response_model=list[studen_course_schemas.StudentCourse])
async def get_list_of_studentcourses(db: AsyncSession = Depends(get_db)):
    return await list_of_student_on_courses(db=db)


@router.get('/student_on_course/{student_id}', response_model=studen_course_schemas.StudentCourse)
async def get_student_on_course(student_id: int, db: AsyncSession = Depends(async_get_db)):
    return await select_student(student_id=student_id, db=db)


@router.delete('/delete_student/{student_id}', response_model=studen_course_schemas.StudentCourse)
async def delete_student_on_course(student_id: int, db: AsyncSession = Depends(async_get_db)):
    return await delete_selected_student(student_id=student_id, db=db)


@router.put('/student_course/{student_id}', response_model=studen_course_schemas.BaseStudentCourse)
async def edit_selected_course(student_id: int, course: studen_course_schemas.BaseStudentCourse,
                               db: AsyncSession = Depends(async_get_db)):
    return await edit_studentcourse_info(student_id=student_id, course=course, db=db)
