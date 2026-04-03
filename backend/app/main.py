from fastapi import FastAPI
from app.core.database import engine, Base
import app.models  # noqa: F401 – alle Modelle registrieren

app = FastAPI(
    title="Legalis API",
    description="Digitales Betriebsmodell für brasilianische Kanzleien",
    version="0.1.0",
)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}
