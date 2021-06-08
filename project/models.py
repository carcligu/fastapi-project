from . import database
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

class Project(database.Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
    technologies = Column(String)

