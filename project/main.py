from main import Project
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy import engine
from . import schemas, models, database
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash


app = FastAPI()


models.Project.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST METHODS -----------------------------------------------------------------------------------------------------------------
@app.post('/project', status_code=status.HTTP_201_CREATED, tags=['projects'])
def post_project(request: schemas.Project, db: Session = Depends(get_db)):
    new_project = models.Project(
                        title=request.title,
                        description=request.description,
                        url=request.url,
                        technologies=request.technologies,
                    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project.__dict__


@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
                    name=request.name,
                    email=request.email,
                    password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.__dict__


# DELETE METHODS -----------------------------------------------------------------------------------------------------------------
@app.delete('/project/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['projects'])
def delete_project(id, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id)
    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id {id} not found')
    project.delete(synchronize_session=False)
    db.commit()
    return {f'detail': "Project with id {id} deleted"}


#PUT METHODS -----------------------------------------------------------------------------------------------------------------
@app.put('/project/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['projects'])
def update(id, request: schemas.Project, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id)
    if not project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id {id} not found')
    project.update(request.dict())
    db.commit()
    return request


# GET METHODS -----------------------------------------------------------------------------------------------------------------
@app.get('/project', response_model=List[schemas.ShowProject], tags=['projects'])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects


@app.get('/project/{id}', status_code=200, response_model=schemas.ShowProject, tags=['projects'])
def get_project(id: int, response: Response, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with the id {id} is not available')
    return project

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user