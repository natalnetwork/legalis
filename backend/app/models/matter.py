import enum
import uuid
from datetime import datetime
from sqlalchemy import String, Enum, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class PracticeArea(str, enum.Enum):
    imobiliario = "imobiliario"        # Immobilienrecht
    trabalhista = "trabalhista"        # Arbeitsrecht
    empresarial = "empresarial"        # Gesellschaftsrecht
    golden_visa = "golden_visa"        # Golden Visa / Ausländer
    geral = "geral"                    # Allgemein


class MatterStatus(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"
    archived = "archived"


class Matter(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "matters"

    client_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("clients.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    practice_area: Mapped[PracticeArea] = mapped_column(
        Enum(PracticeArea), nullable=False, default=PracticeArea.geral
    )
    status: Mapped[MatterStatus] = mapped_column(
        Enum(MatterStatus), nullable=False, default=MatterStatus.open
    )
    opened_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    closed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    client: Mapped["Client"] = relationship(back_populates="matters")
    tasks: Mapped[list["Task"]] = relationship(back_populates="matter")
    deadlines: Mapped[list["Deadline"]] = relationship(back_populates="matter")
    documents: Mapped[list["Document"]] = relationship(back_populates="matter")
