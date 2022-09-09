
from fastapi import FastAPI

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


@app.get("/")
def read_root():
    return {"Hello": "World"}



