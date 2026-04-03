import enum
import uuid
from datetime import date
from sqlalchemy import String, Enum, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class DeadlineStatus(str, enum.Enum):
    open = "open"
    met = "met"
    missed = "missed"


class Deadline(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "deadlines"

    matter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("matters.id"), nullable=False)
    task_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("tasks.id"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[DeadlineStatus] = mapped_column(
        Enum(DeadlineStatus), nullable=False, default=DeadlineStatus.open
    )

    matter: Mapped["Matter"] = relationship(back_populates="deadlines")
    task: Mapped["Task | None"] = relationship(back_populates="deadlines")
