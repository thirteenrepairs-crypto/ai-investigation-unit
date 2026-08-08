from fastapi import FastAPI

app = FastAPI(
    title="AIIU API",
    version="0.1.0",
    description="AI Investigation & Intelligence Unit API",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "aiiu-api"}
