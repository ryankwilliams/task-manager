from fastapi import APIRouter

from app.api.endpoints import tasks

__all__ = [
    "api_router",
]

api_router: APIRouter = APIRouter()

api_router.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
