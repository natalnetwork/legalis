import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.document import Document
from app.models.matter import Matter
from app.schemas.document import DocumentCreate, DocumentUpdate, DocumentResponse

router = APIRouter(prefix="/documents", tags=["Dokumente"])


@router.get("/", response_model=list[DocumentResponse])
def list_documents(matter_id: uuid.UUID | None = None, db: Session = Depends(get_db)):
    query = db.query(Document)
    if matter_id:
        query = query.filter(Document.matter_id == matter_id)
    return query.all()


@router.post("/", response_model=DocumentResponse, status_code=201)
def create_document(data: DocumentCreate, db: Session = Depends(get_db)):
    if not db.get(Matter, data.matter_id):
        raise HTTPException(status_code=404, detail="Mandat nicht gefunden")
    document = Document(**data.model_dump())
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: uuid.UUID, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    return document


@router.patch("/{document_id}", response_model=DocumentResponse)
def update_document(document_id: uuid.UUID, data: DocumentUpdate, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(document, field, value)
    db.commit()
    db.refresh(document)
    return document


@router.delete("/{document_id}", status_code=204)
def delete_document(document_id: uuid.UUID, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    db.delete(document)
    db.commit()
