import uvicorn
from fastapi import FastAPI

from api import users_endpoints, courses_endpoints, sections_endpoints, contentblock_endpoints, studentcourse_endpoints, completeblock_endpoints
from db.db_setup import engine, async_engine
from db.models import users, courses

users.Base.metadata.create_all(bind=engine)
courses.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FastAPI LMS Application",
    description="LMS contains teachers which can manage students,and students which can see their courses and feedbacks",
    version="0.0.1",
    contact={
        "name": "Daniil Sidorenko",
        "email": "sidorenko@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users_endpoints.router, tags=['users'], prefix='/users')
app.include_router(courses_endpoints.router,tags=['courses'], prefix='/courses')
app.include_router(sections_endpoints.router, tags=['sections'], prefix='/sections')
app.include_router(contentblock_endpoints.router, tags=['contentblocks'], prefix='/contentblocks')
app.include_router(studentcourse_endpoints.router, tags=['studentcourses'], prefix='/studentcourses')
app.include_router(completeblock_endpoints.router, tags=['completeblocks'], prefix='/completeblocks')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
