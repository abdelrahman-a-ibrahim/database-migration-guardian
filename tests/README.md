# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- Unknown statements cannot be auto-approved.
- Old and new application versions pass compatibility checks during expand/contract.
- Rehearsal records lock duration, latency, row integrity and recovery observations.
- Recovery explicitly accounts for writes accepted after cutover.

## Failure coverage
- Run a schema change while a long transaction holds a lock.
- Fail a backfill midway and resume without duplicate effects.
- Attempt an application rollback after dropping a required column.
- Cut over with replication lag or conflicting writes in a disposable environment.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
