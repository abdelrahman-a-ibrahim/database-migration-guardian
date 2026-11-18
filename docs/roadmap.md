# Delivery roadmap

Status: planned. No delivery stage is complete.

### 1. Contracts and system boundaries

Define a small explicit migration grammar and risk rubric covering locks, rewrites, destructive changes and version compatibility. Unknown SQL requires review.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 2. Core implementation

Build a synthetic database and workload generator. Rehearse additive changes and capture lock/wait behavior and query latency.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 3. Integrations and access controls

Implement expand/contract with old/new application compatibility tests and an explicit data-backfill step.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 4. Recovery and operational behavior

Design a blue/green experiment including replication lag, sequence state, cutover and writes arriving during cutover. Document feasibility limits before implementation.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 5. Release validation

Rehearse a failure and validate recovery against a declared data-loss tolerance. Produce a decision report with measured results and manual gates.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

## Future scope

- Migration lint rule corpus
- Large-table backfill with checkpoints
- Logical replication compatibility study
- Risk assessment integrated with release evidence

Select and pin implementation dependencies when introduced. Scope is refined through architecture decisions; completion requires working behavior and verification evidence.
