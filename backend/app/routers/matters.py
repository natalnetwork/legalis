import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.matter import Matter
from app.models.client import Client
from app.schemas.matter import MatterCreate, MatterUpdate, MatterResponse

router = APIRouter(prefix="/matters", tags=["Mandate"])


@router.get("/", response_model=list[MatterResponse])
def list_matters(client_id: uuid.UUID | None = None, db: Session = Depends(get_db)):
    query = db.query(Matter)
    if client_id:
        query = query.filter(Matter.client_id == client_id)
    return query.all()


@router.post("/", response_model=MatterResponse, status_code=201)
def create_matter(data: MatterCreate, db: Session = Depends(get_db)):
    if not db.get(Client, data.client_id):
        raise HTTPException(status_code=404, detail="Mandant nicht gefunden")
    matter = Matter(**data.model_dump())
    db.add(matter)
    db.commit()
    db.refresh(matter)
    return matter


@router.get("/{matter_id}", response_model=MatterResponse)
def get_matter(matter_id: uuid.UUID, db: Session = Depends(get_db)):
    matter = db.get(Matter, matter_id)
    if not matter:
        raise HTTPException(status_code=404, detail="Mandat nicht gefunden")
    return matter


@router.patch("/{matter_id}", response_model=MatterResponse)
def update_matter(matter_id: uuid.UUID, data: MatterUpdate, db: Session = Depends(get_db)):
    matter = db.get(Matter, matter_id)
    if not matter:
        raise HTTPException(status_code=404, detail="Mandat nicht gefunden")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(matter, field, value)
    db.commit()
    db.refresh(matter)
    return matter


@router.delete("/{matter_id}", status_code=204)
def delete_matter(matter_id: uuid.UUID, db: Session = Depends(get_db)):
    matter = db.get(Matter, matter_id)
    if not matter:
        raise HTTPException(status_code=404, detail="Mandat nicht gefunden")
    db.delete(matter)
    db.commit()
