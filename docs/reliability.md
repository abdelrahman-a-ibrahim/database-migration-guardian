# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Run a schema change while a long transaction holds a lock.
- Fail a backfill midway and resume without duplicate effects.
- Attempt an application rollback after dropping a required column.
- Cut over with replication lag or conflicting writes in a disposable environment.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- Unknown statements cannot be auto-approved.
- Old and new application versions pass compatibility checks during expand/contract.
- Rehearsal records lock duration, latency, row integrity and recovery observations.
- Recovery explicitly accounts for writes accepted after cutover.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
