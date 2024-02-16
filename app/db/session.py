from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import settings

__all__ = [
    "Base",
    "engine",
    "SessionLocal",
]

engine = create_engine(
    settings.sqlalchemy_database_url,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
