from fastapi import FastAPI
from sqlalchemy import engine
from . import schemas
from . import models
from . import database

app = FastAPI()


models.Project.metadata.create_all(database.engine)

@app.post('/project')
def create(request: schemas.Project):
    return {'title': request.title, 'description': request.description}