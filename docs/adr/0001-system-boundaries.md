# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
A migration-assessment tool for evaluating schema changes against application compatibility, lock behavior and recovery constraints. Planned workflows cover direct execution, expand/contract changes and selected blue/green migration scenarios. Unknown operations require explicit review.

## Questions
- Risk rubric scope and false-negative handling
- Expand/contract versus blue/green
- Cutover write control and recovery limits

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.
