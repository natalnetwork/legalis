import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.document import DocumentType


class DocumentBase(BaseModel):
    title: str
    filename: str
    file_path: str
    document_type: DocumentType = DocumentType.outros


class DocumentCreate(DocumentBase):
    matter_id: uuid.UUID


class DocumentUpdate(BaseModel):
    title: str | None = None
    document_type: DocumentType | None = None


class DocumentResponse(DocumentBase):
    id: uuid.UUID
    matter_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
