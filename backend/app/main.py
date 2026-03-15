from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_ask import router as ask_router
from app.api.routes_concepts import router as concepts_router
from app.api.routes_daily_wisdom import router as daily_wisdom_router
from app.api.routes_practices import router as practices_router
from app.api.routes_sources import router as sources_router
from app.api.routes_verses import router as verses_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="API for scriptures, concepts, practices, daily wisdom, and grounded spiritual Q&A.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sources_router)
app.include_router(verses_router)
app.include_router(concepts_router)
app.include_router(practices_router)
app.include_router(daily_wisdom_router)
app.include_router(ask_router)


@app.get("/")
def root() -> dict:
    return {"message": "Spiritual Wisdom API is running", "environment": settings.app_env}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
