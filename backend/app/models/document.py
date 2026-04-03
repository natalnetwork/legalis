import enum
import uuid
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class DocumentType(str, enum.Enum):
    contrato = "contrato"          # Vertrag
    peticao = "peticao"            # Schriftsatz
    procuracao = "procuracao"      # Vollmacht
    documento_cliente = "documento_cliente"  # Kundendokument
    outros = "outros"              # Sonstiges


class Document(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "documents"

    matter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("matters.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
    document_type: Mapped[DocumentType] = mapped_column(
        Enum(DocumentType), nullable=False, default=DocumentType.outros
    )

    matter: Mapped["Matter"] = relationship(back_populates="documents")
