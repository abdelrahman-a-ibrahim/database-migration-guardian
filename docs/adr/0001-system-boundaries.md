# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Build a migration assessment tool for the WorkshopHub PostgreSQL database. Compare direct execution, expand/contract and blue/green migration approaches using synthetic bookings and a workload generator.

## Decision questions
- Risk rubric scope and false-negative handling
- Expand/contract versus blue/green
- Cutover write control and recovery limits

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
