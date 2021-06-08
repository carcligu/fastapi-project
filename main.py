from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"data": "project list"}


@app.get('/project/{id}')
async def show(id: int):
    # fetch project with id = id
    return {"data": id}


@app.get('/project/{id}/comments')
async def comments(id: int):
    # fetch comments of project with id = id
    return {'data': {'1', '2'}}
