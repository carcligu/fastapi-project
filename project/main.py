from main import Project
from fastapi import FastAPI, Depends
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


@app.post('/project')
def create(request: schemas.Project, db: Session = Depends(get_db)):
    new_project = models.Project(
                        title=request.title,
                        description=request.description
                    )
    db.add(new_project)
    db.commit()
    db.refresh
    return new_project


@app.get('/project')
def all_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects


@app.get('/project/{id}')
def get_project(id, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id).first()
    return project