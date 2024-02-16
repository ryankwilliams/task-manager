from pydantic import BaseModel


class Task(BaseModel):
    task_id: str | None = None
    name: str
    status: str | None = None


class TaskCreate(BaseModel):
    id: str
