from fastapi import FastAPI
from app.core.database import engine, Base
import app.models  # noqa: F401 – alle Modelle registrieren
from app.routers import clients, matters, tasks, deadlines, documents

app = FastAPI(
    title="Legalis API",
    description="Digitales Betriebsmodell für brasilianische Kanzleien",
    version="0.1.0",
)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health", tags=["System"])
def health():
    return {"status": "ok"}


app.include_router(clients.router)
app.include_router(matters.router)
app.include_router(tasks.router)
app.include_router(deadlines.router)
app.include_router(documents.router)
