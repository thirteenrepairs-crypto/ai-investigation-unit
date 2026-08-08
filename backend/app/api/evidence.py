from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Evidence, EvidenceStatus

router = APIRouter(prefix="/evidence", tags=["evidence"])


class EvidenceCreate(BaseModel):
    case_id: UUID
    evidence_type: str
    source: str | None = None
    claim: str | None = None
    reliability: str | None = None
    metadata_json: dict = {}
    content_hash: str | None = None


class EvidenceRead(EvidenceCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: EvidenceStatus


@router.post("", response_model=EvidenceRead, status_code=201)
def create_evidence(payload: EvidenceCreate, db: Session = Depends(get_db)) -> Evidence:
    evidence = Evidence(**payload.model_dump())
    db.add(evidence)
    db.commit()
    db.refresh(evidence)
    return evidence


@router.get("/case/{case_id}", response_model=list[EvidenceRead])
def list_case_evidence(case_id: UUID, db: Session = Depends(get_db)) -> list[Evidence]:
    return list(db.scalars(select(Evidence).where(Evidence.case_id == case_id)))
