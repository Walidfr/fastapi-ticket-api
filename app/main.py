"""
FastAPI application entrypoint.
Initializes app, creates DB tables, and includes ticket router.
"""

from fastapi import FastAPI
from . import models, database
from app.routes.router import router

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)
app.include_router(router)
