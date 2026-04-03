import enum
import uuid
from sqlalchemy import String, Enum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class Task(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "tasks"

    matter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("matters.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus), nullable=False, default=TaskStatus.pending
    )

    matter: Mapped["Matter"] = relationship(back_populates="tasks")
    deadlines: Mapped[list["Deadline"]] = relationship(back_populates="task")
