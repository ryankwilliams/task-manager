from typing import Generator

from sqlalchemy.orm import Session

from app.db import session

__all__ = [
    "create_db",
    "get_db",
]


def get_db() -> Generator[Session, None, None]:
    """Get the database session.

    :return: database session
    """
    database: Session = session.SessionLocal()

    try:
        yield database
    finally:
        database.close()


def create_db() -> None:
    """Create database."""
    # TODO: Only create when database is empty
    session.Base.metadata.create_all(bind=session.engine)
