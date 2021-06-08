from pydantic import BaseModel

class Project(BaseModel):
    title: str
    description: str
