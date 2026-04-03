import uuid
from datetime import date, datetime
from pydantic import BaseModel
from app.models.deadline import DeadlineStatus


class DeadlineBase(BaseModel):
    title: str
    due_date: date
    status: DeadlineStatus = DeadlineStatus.open
    task_id: uuid.UUID | None = None


class DeadlineCreate(DeadlineBase):
    matter_id: uuid.UUID


class DeadlineUpdate(BaseModel):
    title: str | None = None
    due_date: date | None = None
    status: DeadlineStatus | None = None
    task_id: uuid.UUID | None = None


class DeadlineResponse(DeadlineBase):
    id: uuid.UUID
    matter_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
