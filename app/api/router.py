from fastapi import APIRouter

from app.api.endpoints import tasks
from app.api.endpoints import users

__all__ = [
    "api_router",
]

api_router: APIRouter = APIRouter()

api_router.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
