# Backend starter

This directory contains the supported default Python 3.12 FastAPI starter for the Fee Review Assistant. Candidates may replace it with an equivalent backend stack. The application loads fictional fee records from `../data/fee_records.json`. The health route works; fee services and routes are deliberately incomplete and marked with `TODO(candidate)`.

## Native setup

Run these commands from the repository root. On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` instead.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r backend/requirements-dev.txt
```

Start the API:

```bash
python -m uvicorn backend.app.main:app --reload --port 8000
```

Then open <http://localhost:8000/health> or the interactive API documentation at <http://localhost:8000/docs>.

## Tests

From the repository root, with the virtual environment active:

```bash
python -m pytest backend
```

One health test passes initially. The skipped tests describe expected behavior and may be replaced or completed.

## Layout

- `app/main.py`: application creation, health route, and local CORS configuration
- `app/models.py`: Pydantic response and domain models
- `app/sample_data.py`: JSON loading and validation
- `app/services.py`: incomplete business logic
- `app/api/routes.py`: incomplete fee endpoints
- `tests/`: one passing smoke test and candidate-facing test prompts

No cloud credentials, database, or external services are required.
