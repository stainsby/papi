---
name: papi-sdlc-sprint
description: Create or work with sprint tasks — plan, execute, verify, and close a bounded cycle of development work with post-completion quality gates. [PAPI SDLC]
---

## Dependencies

These skills should also be read to use the current skill.

- PAPI skill `papi-tasks-understand`
- PAPI skill `papi-templates-understand`
- PAPI skill `papi-sdlc-task-compliance-audit`
- PAPI skill `papi-sdlc-validate-capabilities-dag`

## Purpose

A sprint is a bounded cycle of related development work (fixes, features,
infrastructure changes) that is planned, executed, verified, and closed as a
unit. Sprints are the primary mechanism for grouping related sub-tasks and
ensuring that a cohesive set of changes is delivered with full quality
verification.

A sprint is **not** a time-boxed iteration in the Scrum sense. It is a
logically bounded batch of work with explicit entry criteria, execution
phases, and exit gates.

## When to use this skill

Use this skill when:

- Multiple related tasks (fixes, features, spec updates) should be delivered
  together as a coherent unit.
- Work is being collected after an audit, investigation, or manual testing
  session that produced multiple findings.
- A set of changes spans multiple components and needs coordinated
  verification.

## Assets

- **Sprint task template**: `assets/sprint-task-template.md`

## Sprint Lifecycle

A sprint proceeds through four phases. Each phase has mandatory activities
and exit criteria.

### Phase 1 — Planning

1. **Define scope**: list the sub-tasks, grouped by theme or dependency.
2. **Sequence**: identify dependencies between sub-tasks and define execution
   order. Independent sub-tasks may be parallelised.
3. **Entry criteria**: verify all prerequisites are met (e.g. prior sprint
   completed, specs current, no uncommitted changes in affected files).
4. **Create sub-task documents**: each sub-task must have its own task document
   using the appropriate template (fix, component, development, etc.).
5. **Identify integration boundaries**: for any work that spans communication
   boundaries between components (postMessage, HTTP, FFI, IPC, etc.), note
   these explicitly. At least one automated test must exercise the real round
   trip across each identified boundary by the end of the sprint.

### Phase 2 — Execution

1. Work sub-tasks in the sequenced order.
2. Follow the SDLC workflow within each sub-task (spec -> tests -> code ->
   refactor).
3. After each sub-task completes:
   - Run the full automated test suite and confirm it passes.
   - Update the sprint status table.
4. If a sub-task reveals new issues:
   - Minor and directly related: fold into the current sub-task.
   - Significant or out of scope: create a new sub-task or note as a
     follow-on. Do not expand sprint scope without human approval.

### Phase 3 — Verification (Post-Implementation)

After all sub-tasks are complete, run the full verification checklist before
declaring the sprint complete. The checklist is in the sprint task template
and includes the following mandatory gates:

#### Gate 1 — Automated Tests

- All unit tests pass.
- All integration tests pass.
- All browser/E2E tests pass (both mock-based and, if applicable,
  tests against a real server).

#### Gate 2 — Manual Smoke Test

- If the sprint includes UI or user-facing changes: perform a brief manual
  walkthrough of the affected workflows using the actual user interface (not
  tool-level calls or mock data).
- Record what was tested and the outcome.
- This gate exists because automated tests that use mocked boundaries cannot
  catch integration-level defects that only manifest in a real environment.

#### Gate 3 — Capabilities DAG Validation

- Use the `papi-sdlc-validate-capabilities-dag` skill: run the DAG
  validation script against the project's component specifications directory.
- Confirm zero issues (no cycles, no orphans, no invalid references).

#### Gate 4 — Compliance Spot-Check

- For each component specification modified during the sprint: verify the
  spec is in sync with the code.
- Verify capability codes referenced in new or modified code are correct.
- This is a lightweight check, not a full compliance audit (see
  `papi-sdlc-task-compliance-audit` skill). If the spot-check reveals
  significant drift, create a compliance audit task as a follow-on.

#### Gate 5 — Integration Boundary Check

- For every integration boundary identified in Phase 1: confirm at least one
  automated test exercises the real round trip (not mocks).
- If no such test exists, either add one (as a sub-task) or document the gap
  and create a follow-on task.

### Phase 4 — Close

1. Complete the Reflect and Improvement sections of the sprint document.
2. Record process improvement observations:
   - Did this sprint reveal gaps in testing, specification, or process?
   - Should any templates, skills, or instructions be updated?
   - Were there recurring issues that suggest a systemic problem?
3. Move the sprint task (and all sub-tasks) to the completed directory.
4. If the sprint addressed audit findings: note that a follow-up audit should
   be scheduled to confirm the findings are resolved.

## Relationship to Audits

- Sprints and audits are complementary but distinct:
  - A sprint **delivers** changes.
  - A compliance audit (see `papi-sdlc-task-compliance-audit`) **verifies**
    that code matches specs.
  - A fulfilment audit (see `papi-sdlc-task-fulfilment-audit`) **verifies**
    that the user stories are satisfied.
- After a sprint that fixes audit findings, a follow-up audit should be
  planned (not necessarily immediately, but before the next release).
- Sprints should NOT include full compliance or fulfilment audits as
  sub-tasks. The sprint's Gate 4 (compliance spot-check) is sufficient
  for in-sprint verification. Full audits are separate tasks created
  using their respective skills.

## Anti-Patterns to Avoid

1. **Mock-only verification**: declaring the sprint complete because all
   unit/mock-based tests pass, without verifying real integration. This is
   the single most common failure mode and the reason this skill exists.
2. **Skipping the manual smoke test**: automated tests can only catch what
   they are designed to catch. A 30-second manual walkthrough after
   completing UI work has repeatedly caught critical defects that passed
   all automated checks.
3. **Scope creep without approval**: adding tasks to a sprint mid-flight
   without human approval. Create follow-on tasks instead.
4. **Closing without reflection**: the Reflect and Improvement sections are
   not optional. Every sprint teaches something about the process.
