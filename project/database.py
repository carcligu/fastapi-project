from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHAEMY_DATABASE_URL = 'sqlite:///./project.db'

engine = create_engine(SQLALCHAEMY_DATABASE_URL, connect_args={
                        "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

