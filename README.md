# Legalis

Initial development scaffold for the Legalis project.

## Current status

- Debian development VM ready
- Python virtual environment configured
- PostgreSQL development database configured
- FastAPI test application running successfully

## Development

Activate the virtual environment:

```bash
source backend/.venv/bin/activate
```

Start the dev server:

```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
