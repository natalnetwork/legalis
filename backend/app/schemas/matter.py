import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.matter import MatterStatus, PracticeArea


class MatterBase(BaseModel):
    title: str
    description: str | None = None
    practice_area: PracticeArea = PracticeArea.geral
    status: MatterStatus = MatterStatus.open
    opened_at: datetime | None = None
    closed_at: datetime | None = None


class MatterCreate(MatterBase):
    client_id: uuid.UUID


class MatterUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    practice_area: PracticeArea | None = None
    status: MatterStatus | None = None
    opened_at: datetime | None = None
    closed_at: datetime | None = None


class MatterResponse(MatterBase):
    id: uuid.UUID
    client_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
