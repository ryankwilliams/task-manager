import secrets
import uuid
from typing import Annotated
from typing import List

from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session

from app.api.common import get_db
from app.api.endpoints.types import Task
from app.api.endpoints.types import TaskCreate
from app.api.endpoints.types import TaskCreateResponse
from app.api.endpoints.types import TaskPatch
from app.db.crud import TaskDB

router: APIRouter = APIRouter()

security = HTTPBasic()


def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"admin"
    is_correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"password"
    is_correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@router.get("/")
def list_tasks(
    credentials: Annotated[HTTPBasicCredentials, Depends(get_current_username)],
    db: Session = Depends(get_db),
) -> List[Task]:
    task_db = TaskDB(db)
    rows = task_db.get_all_rows()

    tasks: List[Task] = []
    for row in rows:
        tasks.append(Task(**row.__dict__))
    return tasks


@router.get("/{task_id}")
def get_task(task_id: str, db: Session = Depends(get_db)) -> Task:
    task_db = TaskDB(db)
    row = task_db.get_row(task_id=task_id)
    return Task(**row.__dict__)


@router.put("/{task_id}")
def update_task(
    task_id: str,
    task: TaskPatch,
    db: Session = Depends(get_db),
) -> Task:
    task_db = TaskDB(db)
    row = task_db.update_row(task_id=task_id, task=task)
    return Task(**row.__dict__)


@router.post("/")
async def create(
    task_create: TaskCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
) -> TaskCreateResponse:
    labels = task_create.__dict__.pop("labels")
    task = Task(**task_create.__dict__)
    task.task_id = uuid.uuid4().__str__()
    if labels:
        task.labels = ",".join(labels)
    background_tasks.add_task(create_task, task=task, db=db)
    return TaskCreateResponse(id=task.task_id)


@router.delete("/{task_id}")
def delete(
    task_id: str,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
) -> None:
    background_tasks.add_task(delete_task, task_id=task_id, db=db)


def create_task(task: Task, db: Session) -> None:
    tasks_db = TaskDB(db)
    if task.status is None or task.status == "":
        task.status = "todo"
    tasks_db.create_row(task=task)


def delete_task(task_id: str, db: Session) -> None:
    tasks_db = TaskDB(db)
    tasks_db.delete_row(task_id=task_id)
