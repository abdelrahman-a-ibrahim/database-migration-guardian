# Implementation backlog

Status: all milestones unstarted. Check a task only when its evidence exists.

## M1 — Design and contracts

Define a small explicit migration grammar and risk rubric covering locks, rewrites, destructive changes and version compatibility. Unknown SQL requires review.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M2 — Build the first path

Build a synthetic database and workload generator. Rehearse additive changes and capture lock/wait behavior and query latency.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M3 — Integrate deliberately

Implement expand/contract with old/new application compatibility tests and an explicit data-backfill step.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M4 — Handle failure

Design a blue/green experiment including replication lag, sequence state, cutover and writes arriving during cutover. Document feasibility limits before implementation.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

## M5 — Demonstrate and operate

Rehearse a failure and validate recovery against a declared data-loss tolerance. Produce a decision report with measured results and manual gates.

- [ ] Turn this milestone into a small design/task note with inputs and outputs.
- [ ] Implement the smallest complete behavior for this milestone.
- [ ] Add positive, negative and recovery checks relevant to this behavior.
- [ ] Record commands, environment and observed results in the learning journal.
- [ ] Update the README status and architecture if the implementation changes them.

**Review gate:** demonstrate the behavior, explain a tradeoff and link actual evidence. Do not mark complete using foundation checks alone.

