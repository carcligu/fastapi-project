from main import Project
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy import engine
from . import schemas
from . import models
from . import database
from sqlalchemy.orm import Session


app = FastAPI()


models.Project.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST METHODS -----------------------------------------------------------------------------------------------------------------
@app.post('/project', status_code=status.HTTP_201_CREATED)
def post_project(request: schemas.Project, db: Session = Depends(get_db)):
    print(f"This is the title: {request.title}")
    print(f"This is the description: {request.description}")
    print(f"This is the technology: {request.technologies}")
    print(f"This is the url: {request.url}")
    new_project = models.Project(
                        title=request.title,
                        description=request.description,
                        url=request.url,
                        technologies=request.technologies,
                    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

# DELETE METHODS -----------------------------------------------------------------------------------------------------------------
@app.delete('/project/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_project(id, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id)
    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id {id} not found')
    project.delete(synchronize_session=False)
    db.commit()
    return {f'detail': "Project with id {id} deleted"}


#PUT METHODS -----------------------------------------------------------------------------------------------------------------
@app.put('/project/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Project, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id)
    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id {id} not found')
    project.update(request.dict())
    db.commit()
    return request


# GET METHODS -----------------------------------------------------------------------------------------------------------------
@app.get('/project')
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects


@app.get('/project/{id}', status_code=200)
def get_project(id, response: Response, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with the id {id} is not available')
    return project
