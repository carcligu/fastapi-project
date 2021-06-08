from fastapi import FastAPI
from typing import Optional

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
