from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Case, CaseStatus

router = APIRouter(prefix="/cases", tags=["cases"])


class CaseCreate(BaseModel):
    title: str
    description: str
    jurisdiction: str | None = None
    priority: str = "NORMAL"


class CaseRead(CaseCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: CaseStatus


@router.post("", response_model=CaseRead, status_code=201)
def create_case(payload: CaseCreate, db: Session = Depends(get_db)) -> Case:
    case = Case(**payload.model_dump())
    db.add(case)
    db.commit()
    db.refresh(case)
    return case


@router.get("/{case_id}", response_model=CaseRead)
def get_case(case_id: UUID, db: Session = Depends(get_db)) -> Case:
    case = db.scalar(select(Case).where(Case.id == case_id))
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return case
