from fastapi import FastAPI

app = FastAPI(title="Legalis")

@app.get("/")
def read_root() -> dict[str, str]:
    return {"status": "ok", "app": "Legalis via VS Code"}
