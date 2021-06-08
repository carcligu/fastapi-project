from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



app = FastAPI()


@app.get("/")
async def root():
    return {"data": "project list"}


@app.get("/project")
async def all_projects(limit=10, sort: Optional[str] = None):
    # fletch all projects. limit is used to not pull all data, so it is executed faster
    # the query parameter can be introduced in the path:
    #   /project?limit=10
    return {'data': f'{limit} projects from the db'}


@app.get('/project/{id}')
async def show(id: int):
    # fetch project with id = id
    return {"data": id}



@app.get('/project/{id}/technologies')
async def comments(id: int):
    # fetch comments of project with id = id
    return {'data': {'1', '2'}}


# POST METHODS
class Project(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    url: Optional[str]
    technologies: Optional[list]

@app.post('/project')
async def create_project(request: Project):
    return {'data': f'Project is created with id: {request.id}', 'response': request}
