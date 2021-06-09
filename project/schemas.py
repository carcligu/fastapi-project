from project.database import Base
from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    title: str
    description: str
    url: Optional[str] = None
    technologies: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "This is the project Title",
                "description": "This is the project description",
                "url": "wwww.hola.com",
                "technologies": "Python"
            }
        }

class ShowProject(BaseModel):
    title: str
    description: str
    url: Optional[str] = None
    technologies: Optional[str] = None
    class Config():
        orm_mode = True