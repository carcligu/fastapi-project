from fastapi import FastAPI, Depends
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