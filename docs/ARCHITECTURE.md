# AIIU Architecture v1.0

## 1. Investigation lifecycle

```text
NEW -> INTAKE -> TRIAGE -> PLANNING -> ACTIVE_INVESTIGATION
-> EVIDENCE_REVIEW -> HYPOTHESIS_TESTING -> ADVERSARIAL_REVIEW
-> LEGAL_REVIEW -> REPORT_DRAFT -> HUMAN_REVIEW
-> APPROVED -> CLOSED
                     \-> REOPENED -> ACTIVE_INVESTIGATION
```

## 2. Core domain objects

- Case — investigation container and objectives.
- Entity — person, company, organization, location, document, event, or other investigated object.
- Source — origin of information and its reliability metadata.
- Evidence — captured information linked to a source and case.
- Claim — proposition being investigated.
- Hypothesis — competing explanation tested against evidence.
- Task — bounded unit of work assigned to an agent.
- Finding — evidence-supported investigative conclusion with limitations.
- Audit event — immutable record of material system actions.

## 3. Evidence model

Evidence must retain provenance, collection time, source, authenticity state, reliability assessment, and links to claims/hypotheses. A source being reliable does not automatically make every claim from that source true.

## 4. Agent contract

Agents receive a bounded task and explicit capabilities. They return structured results containing evidence, claims, entities, contradictions, limitations, and recommendations. Agents do not directly declare guilt or modify final findings without the orchestration and review workflow.

## 5. Corroboration

The system tracks source independence. Multiple publications derived from one original report are treated as one information chain rather than independent confirmation.

## 6. Adversarial review

The adversarial agent is tasked with finding contradictions, missing evidence, alternative explanations, source duplication, timeline conflicts, and unsupported assumptions.

## 7. Human review

Human approval is required before publishing consequential allegations, releasing sensitive information, or closing high-risk investigations.

## 8. Security

Access follows least privilege. Agents and users receive only the permissions and case data required for their role. Restricted/private information must only be accessed through authorized connectors.
