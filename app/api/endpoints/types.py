from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    status: str | None = None


class Task(TaskBase):
    task_id: str | None = None
    labels: str | None = ""


class TaskCreate(TaskBase):
    labels: list[str] | None = None


class TaskPatch(BaseModel):
    name: str | None = None
    status: str | None = None
    labels: list[str] | None = None


class TaskCreateResponse(BaseModel):
    id: str
