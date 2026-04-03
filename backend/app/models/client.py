import enum
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class ClientType(str, enum.Enum):
    pessoa_fisica = "pessoa_fisica"      # Privatperson
    pessoa_juridica = "pessoa_juridica"  # Unternehmen


class Client(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "clients"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255))
    phone: Mapped[str | None] = mapped_column(String(50))
    cpf_cnpj: Mapped[str | None] = mapped_column(String(20), unique=True)
    client_type: Mapped[ClientType] = mapped_column(
        Enum(ClientType), nullable=False, default=ClientType.pessoa_fisica
    )

    matters: Mapped[list["Matter"]] = relationship(back_populates="client")
