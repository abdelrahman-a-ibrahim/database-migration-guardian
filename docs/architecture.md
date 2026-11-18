# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
A migration-assessment tool for evaluating schema changes against application compatibility, lock behavior and recovery constraints. Planned workflows cover direct execution, expand/contract changes and selected blue/green migration scenarios. Unknown operations require explicit review.

## Component view
```text
Migration proposal -> risk assessment -> chosen strategy -> rehearsal
                                           |
                                    validation / cutover / recovery
```

## Design decisions
- Risk rubric scope and false-negative handling
- Expand/contract versus blue/green
- Cutover write control and recovery limits

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/database_migration_guardian/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
