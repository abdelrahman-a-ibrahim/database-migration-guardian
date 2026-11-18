# Database Migration Guardian

PostgreSQL migration risk assessment, compatibility checks and controlled cutover planning.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

A migration-assessment tool for evaluating schema changes against application compatibility, lock behavior and recovery constraints. Planned workflows cover direct execution, expand/contract changes and selected blue/green migration scenarios. Unknown operations require explicit review.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Migration assessment with a documented risk rubric and supported operation set.
- Lock, rewrite and compatibility analysis with review for unknown statements.
- Expand/contract change workflows and resumable backfill planning.
- Blue/green cutover planning with explicit write and replication constraints.
- Integrity checks and recovery reports tied to rehearsed changes.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Migration proposal -> risk assessment -> chosen strategy -> rehearsal
                                           |
                                    validation / cutover / recovery
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

PostgreSQL · Python · Migration risk · Blue/green · Compatibility.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/database-migration-guardian.git
cd database-migration-guardian
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/database_migration_guardian/interfaces.py`](src/database_migration_guardian/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- Unknown statements cannot be auto-approved.
- Old and new application versions pass compatibility checks during expand/contract.
- Rehearsal records lock duration, latency, row integrity and recovery observations.
- Recovery explicitly accounts for writes accepted after cutover.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/database_migration_guardian/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://www.postgresql.org/docs/current/explicit-locking.html
- https://www.postgresql.org/docs/current/logical-replication.html
