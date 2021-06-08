from fastapi import FastAPI
from . import schemas

app = FastAPI()


@app.post('/project')
def create(request: schemas.Project):
    return {'title': request.title, 'description': request.description}