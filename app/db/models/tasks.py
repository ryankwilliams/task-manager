__all__ = ["TasksModel"]
from sqlalchemy import Column, Integer, String

from app.db.session import Base


class TasksModel(Base):  # type: ignore
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String)
    name = Column(String)
    status = Column(String)
