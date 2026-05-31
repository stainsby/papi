---
name: papi-sdlc-sprint
description: Create or work with sprint-like tasks — plan, execute, verify, and close a bounded cycle of development work . [PAPI SDLC]
---

# SDLC Task - Sprint

## Purpose

A sprint is a bounded cycle of related development work (fixes, features,
infrastructure changes) that is planned, executed, verified, and closed as a
unit. Sprints are the primary mechanism for grouping related sub-tasks and
ensuring that a cohesive set of changes is delivered with full quality
verification.

A sprint is **not** a time-boxed iteration in the Scrum sense. It is a
logically bounded batch of work with explicit entry criteria, execution
phases, and exit gates.

## Dependencies

Reading these skills is REQUIRED to understand and execute this skill:

- PAPI skill `papi-tasks-understand`
- PAPI skill `papi-templates-understand`
- PAPI skill `papi-long-task`

Read these as needed:

- PAPI skill `papi-sdlc-task-compliance-audit`
- PAPI skill `papi-sdlc-validate-capabilities-dag`

Use the `papi-long-task` skill.

## When to use this skill

Use this skill when:

- Multiple related tasks (fixes, features, spec updates) should be delivered
  together as a coherent unit.
- Work is being collected after an audit, investigation, or manual testing
  session that produced multiple findings.
- A set of changes spans multiple components and needs coordinated
  verification.

## Sprint Lifecycle

A sprint proceeds through four phases. Each phase has mandatory activities
and exit criteria.

### Planning

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

When creating individual tasks, do not link them to the sprint
either by name or by content UNLESS there is a special reason. The sprint can
list tasks, not visa-versa. At time we may dynamically reallocate tasks
between sprints, so task-to-sprint links are discouraged. Thus, sub-task
names here generally DON'T refer to the sprint.

**IMPORTANT: To create sub-tasks ONE AT A TIME, following the PAPI copy first,
and edit section-by-section method for EACH one.**

### Execution

Work sub-tasks in the sequenced order. After each sub-task completes,
update the sprint status table. If a sub-task reveals new issues:

- Minor and directly related: fold into the current sub-task.
- Significant or out of scope: create a new sub-task or note as a
  follow-on. Do not expand sprint scope without human approval.

### Verification (Post-Implementation)

After all sub-tasks are complete, run the full verification checklist before
declaring the sprint complete. 

## Skill artefacts

- **Sprint task template**: `assets/sprint-task-template.md`
