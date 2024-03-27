__all__ = ["UsersModel"]

from sqlalchemy import Column, Integer, String

from app.db.session import Base


class UsersModel(Base):  # type: ignore
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    username = Column(String)
    password = Column(String)
