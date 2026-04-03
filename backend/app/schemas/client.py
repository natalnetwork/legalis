import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.client import ClientType


class ClientBase(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    cpf_cnpj: str | None = None
    client_type: ClientType = ClientType.pessoa_fisica


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    cpf_cnpj: str | None = None
    client_type: ClientType | None = None


class ClientResponse(ClientBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
