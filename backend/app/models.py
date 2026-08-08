from datetime import datetime
from enum import StrEnum
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class CaseStatus(StrEnum):
    NEW = "NEW"
    INTAKE = "INTAKE"
    TRIAGE = "TRIAGE"
    PLANNING = "PLANNING"
    ACTIVE = "ACTIVE"
    EVIDENCE_REVIEW = "EVIDENCE_REVIEW"
    HYPOTHESIS_TESTING = "HYPOTHESIS_TESTING"
    ADVERSARIAL_REVIEW = "ADVERSARIAL_REVIEW"
    LEGAL_REVIEW = "LEGAL_REVIEW"
    REPORT_DRAFT = "REPORT_DRAFT"
    HUMAN_REVIEW = "HUMAN_REVIEW"
    CLOSED = "CLOSED"
    REOPENED = "REOPENED"


class EvidenceStatus(StrEnum):
    DISCOVERED = "DISCOVERED"
    COLLECTED = "COLLECTED"
    REGISTERED = "REGISTERED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    DISPUTED = "DISPUTED"
    CORROBORATED = "CORROBORATED"


class Case(Base):
    __tablename__ = "cases"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text())
    jurisdiction: Mapped[str | None] = mapped_column(String(100))
    priority: Mapped[str] = mapped_column(String(20), default="NORMAL")
    status: Mapped[CaseStatus] = mapped_column(Enum(CaseStatus, name="case_status"), default=CaseStatus.NEW)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class Evidence(Base):
    __tablename__ = "evidence"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    case_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("cases.id"), index=True)
    evidence_type: Mapped[str] = mapped_column(String(50))
    source: Mapped[str | None] = mapped_column(Text())
    claim: Mapped[str | None] = mapped_column(Text())
    reliability: Mapped[str | None] = mapped_column(String(20))
    status: Mapped[EvidenceStatus] = mapped_column(Enum(EvidenceStatus, name="evidence_status"), default=EvidenceStatus.DISCOVERED)
    metadata_json: Mapped[dict] = mapped_column(JSONB, default=dict)
    content_hash: Mapped[str | None] = mapped_column(String(128), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
