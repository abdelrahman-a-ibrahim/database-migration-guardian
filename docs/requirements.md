# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
A migration-assessment tool for evaluating schema changes against application compatibility, lock behavior and recovery constraints. Planned workflows cover direct execution, expand/contract changes and selected blue/green migration scenarios. Unknown operations require explicit review.

## Target capabilities
- Define a small explicit migration grammar and risk rubric covering locks, rewrites, destructive changes and version compatibility. Unknown SQL requires review.
- Build a synthetic database and workload generator. Rehearse additive changes and capture lock/wait behavior and query latency.
- Implement expand/contract with old/new application compatibility tests and an explicit data-backfill step.
- Design a blue/green experiment including replication lag, sequence state, cutover and writes arriving during cutover. Document feasibility limits before implementation.
- Rehearse a failure and validate recovery against a declared data-loss tolerance. Produce a decision report with measured results and manual gates.

## Acceptance criteria
- Unknown statements cannot be auto-approved.
- Old and new application versions pass compatibility checks during expand/contract.
- Rehearsal records lock duration, latency, row integrity and recovery observations.
- Recovery explicitly accounts for writes accepted after cutover.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.
