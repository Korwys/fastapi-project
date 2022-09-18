from fastapi import FastAPI

from api import users_endpoints,courses_endpoints
from db.db_setup import engine, async_engine
from db.models import user, courses

user.Base.metadata.create_all(bind=engine)
courses.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Fast API Video Hosting",
    description="Hosting for videos",
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



