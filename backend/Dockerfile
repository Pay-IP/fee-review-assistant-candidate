FROM python:3.12-slim

WORKDIR /workspace

COPY backend/requirements.txt backend/requirements-dev.txt /workspace/backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend /workspace/backend
COPY data /workspace/data

EXPOSE 8000

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
