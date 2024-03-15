import dataclasses
from typing import List
from typing import Type

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.api.endpoints.types import Task
from app.api.endpoints.types import TaskPatch
from app.db.models.tasks import TasksModel


@dataclasses.dataclass
class TaskDB:
    db: Session

    def create_row(self, task: Task) -> None:
        row = TasksModel(
            name=task.name, status=task.status, task_id=task.task_id, labels=task.labels
        )
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)

    def get_row(self, task_id: str) -> Type[TasksModel] | None:
        return self.db.query(TasksModel).filter(TasksModel.task_id == task_id).first()

    def get_all_rows(self) -> List[Type[TasksModel]] | List[TasksModel]:
        return self.db.query(TasksModel).order_by(desc(TasksModel.id)).all()

    def delete_row(self, task_id: str) -> None:
        row = self.db.query(TasksModel).filter(TasksModel.task_id == task_id).one()
        self.db.delete(row)
        self.db.commit()

    def update_row(self, task_id: str, task: TaskPatch) -> Type[TasksModel] | None:
        row = self.get_row(task_id=task_id)
        if task.name:
            row.name = task.name
        if task.status:
            row.status = task.status
        if task.labels:
            row.labels = ",".join(task.labels)
        self.db.flush()
        self.db.commit()
        return self.get_row(task_id=task_id)
