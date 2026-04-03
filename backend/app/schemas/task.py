import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.task import TaskStatus


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.pending


class TaskCreate(TaskBase):
    matter_id: uuid.UUID


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None


class TaskResponse(TaskBase):
    id: uuid.UUID
    matter_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
