from main import Project
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy import engine
from . import schemas
from . import models
from . import database
from sqlalchemy.orm import Session

import project

app = FastAPI()


models.Project.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/project', status_code=status.HTTP_201_CREATED)
def post_project(request: schemas.Project, db: Session = Depends(get_db)):
    new_project = models.Project(
                        title=request.title,
                        description=request.description
                    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@app.delete('/project/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_project(id, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id).delete(synchronize_session=False)
    db.commit()
    #db.refresh()
    return {'detail': f'Project with id {id} has been deleted'}
    

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
