import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.task import Task
from app.models.matter import Matter
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Aufgaben"])


@router.get("/", response_model=list[TaskResponse])
def list_tasks(matter_id: uuid.UUID | None = None, db: Session = Depends(get_db)):
    query = db.query(Task)
    if matter_id:
        query = query.filter(Task.matter_id == matter_id)
    return query.all()


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    if not db.get(Matter, data.matter_id):
        raise HTTPException(status_code=404, detail="Mandat nicht gefunden")
    task = Task(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: uuid.UUID, data: TaskUpdate, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    db.delete(task)
    db.commit()
