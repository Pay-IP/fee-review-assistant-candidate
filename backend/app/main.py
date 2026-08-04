from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routes import router as fees_router


app = FastAPI(
    title="Fee Review Assistant API",
    description="Starter API for the AI-assisted development interview.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(fees_router)

