import uvicorn
from fastapi import FastAPI

from api import users_endpoints,courses_endpoints
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

app.include_router(users_endpoints.router)
app.include_router(courses_endpoints.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
