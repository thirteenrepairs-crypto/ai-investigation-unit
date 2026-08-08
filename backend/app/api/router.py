from fastapi import APIRouter

from app.api.cases import router as cases_router
from app.api.evidence import router as evidence_router

router = APIRouter()
router.include_router(cases_router)
router.include_router(evidence_router)
