from fastapi import FastAPI

from app.api.router import router

app = FastAPI(
    title="AIIU API",
    version="0.1.0",
    description="AI Investigation & Intelligence Unit API",
)

app.include_router(router, prefix="/api/v1")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "aiiu-api"}
