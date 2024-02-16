from pydantic import BaseModel


class Task(BaseModel):
    task_id: str | None = None
    name: str
    status: str | None = None


class TaskPatch(BaseModel):
    name: str | None = None
    status: str | None = None


class TaskCreate(BaseModel):
    id: str
