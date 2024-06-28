from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.session import metadata, engine
from api import wheater_data, locations, users


metadata.create_all(engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(wheater_data.router)
app.include_router(locations.router)
app.include_router(users.router)
