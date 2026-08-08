# AIIU — AI Investigation & Intelligence Unit

AIIU is a modular, evidence-driven multi-agent investigation platform.

## Mission

Transform investigative leads, allegations, questions, and evidence packages into structured, auditable investigations without treating allegations as established facts.

## Core principles

- Evidence before conclusions.
- Claims, facts, inferences, and hypotheses are distinct objects.
- Important claims require source attribution and corroboration.
- Agents must actively search for contradictory evidence.
- High-impact findings require human review.
- Every material action is auditable.
- Agents operate only within explicitly granted permissions.

## Initial architecture

```text
Web Dashboard
      |
      v
API / Backend
      |
      v
Investigation Orchestrator
      |
      +-- Intake Agent
      +-- Case Manager
      +-- OSINT Agent
      +-- Document Agent
      +-- Timeline Agent
      +-- Corroboration Agent
      +-- Adversarial Agent
      +-- Report Agent
      |
      v
Evidence Engine
      |
      +-- Sources
      +-- Claims
      +-- Hypotheses
      +-- Entities / Relationships
      +-- Audit Log
      |
      v
Human Review
```

## MVP scope

1. Case management
2. Evidence ledger
3. Claims and hypotheses
4. Task and agent registry
5. Audit logging
6. Investigation orchestration
7. Evidence corroboration
8. Adversarial review
9. Structured investigation reports

## Project status

Foundation phase — architecture and repository initialization.

## Safety and integrity

AIIU is intended for lawful research and investigation. It must not bypass authentication, access private systems without authorization, impersonate individuals, fabricate evidence, or autonomously determine criminal guilt.
