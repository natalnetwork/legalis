import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.deadline import Deadline
from app.models.matter import Matter
from app.schemas.deadline import DeadlineCreate, DeadlineUpdate, DeadlineResponse

router = APIRouter(prefix="/deadlines", tags=["Fristen"])


@router.get("/", response_model=list[DeadlineResponse])
def list_deadlines(matter_id: uuid.UUID | None = None, db: Session = Depends(get_db)):
    query = db.query(Deadline)
    if matter_id:
        query = query.filter(Deadline.matter_id == matter_id)
    return query.all()


@router.post("/", response_model=DeadlineResponse, status_code=201)
def create_deadline(data: DeadlineCreate, db: Session = Depends(get_db)):
    if not db.get(Matter, data.matter_id):
        raise HTTPException(status_code=404, detail="Mandat nicht gefunden")
    deadline = Deadline(**data.model_dump())
    db.add(deadline)
    db.commit()
    db.refresh(deadline)
    return deadline


@router.get("/{deadline_id}", response_model=DeadlineResponse)
def get_deadline(deadline_id: uuid.UUID, db: Session = Depends(get_db)):
    deadline = db.get(Deadline, deadline_id)
    if not deadline:
        raise HTTPException(status_code=404, detail="Frist nicht gefunden")
    return deadline


@router.patch("/{deadline_id}", response_model=DeadlineResponse)
def update_deadline(deadline_id: uuid.UUID, data: DeadlineUpdate, db: Session = Depends(get_db)):
    deadline = db.get(Deadline, deadline_id)
    if not deadline:
        raise HTTPException(status_code=404, detail="Frist nicht gefunden")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(deadline, field, value)
    db.commit()
    db.refresh(deadline)
    return deadline


@router.delete("/{deadline_id}", status_code=204)
def delete_deadline(deadline_id: uuid.UUID, db: Session = Depends(get_db)):
    deadline = db.get(Deadline, deadline_id)
    if not deadline:
        raise HTTPException(status_code=404, detail="Frist nicht gefunden")
    db.delete(deadline)
    db.commit()
