[Use this template for defect fix tasks — a reported or observed defect, bug,
or unintended behaviour that needs to be corrected, with improvements to leave
the affected area in a better state.]

[This template is based on `development-task-template.md` and follows the same
SDLC workflow. Fix tasks differ in that they begin with evidence capture and
root-cause analysis, and Goals must address both the defect and related
improvements — not the symptom alone.]

[This template is a guideline:
* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that may
  indicate a need for a new/updated template or process change; record that
  under *Process improvement* in the *Improvement* section.]

# Task: [Fix — short description of the defect]

**External Tracking:** [e.g., JIRA-123, GitHub Issue #456, audit finding ref, or "None"]  
**Impacted Components:** [List CMP codes affected, or "Multiple"]  
**Severity:** [Critical / High / Medium / Low — assess against: correctness, data integrity, usability, cosmetic]  
**Scope:** [Spec only / Implementation only / Both spec and implementation]  
**Status:** [Status indicator]  

## Synopsis

[One-line summary: what is broken and what will be correct after the fix.]

## Template

This document was based on the PAPI template: `fix-task-template.md`.

## Status

[Current status of this task.
Examples: Planned, Active, Blocked, Completed, Abandoned.
If blocked or abandoned, briefly note why.]

## Parent task

[OMIT unless this is a sub-task of another task]

## Tasks this task depends on

[OMIT unless this depends on other tasks being done first.
Note: other fix tasks may be prerequisites if their bugs affect testing here.]

## Subordinate and dependent tasks

[OMIT unless other tasks depend on this one being done first.]

## SDLC Workflow Reminder

This task follows the strict SDLC sequence — do NOT deviate without explicit permission:

1. **Evidence and root cause first** — capture the exact observed behaviour and
   identify the root cause before writing any plan. The root cause drives Goals.
2. **Strategy and documentation** — update or create affected artefacts
   (specs, docs) to reflect the correct intended behaviour before coding.
3. **Testing plans** — define the regression test and any related tests that
   will verify the fix and guard against recurrence.
4. **Architectural alignment check** — confirm the fix location and approach
   match the component spec's module/dependency structure.
5. **Tests before code (TDD)** — write the failing regression test first (RED).
6. **Code** — implement the minimal fix to make tests pass (GREEN).
7. **Improvements** — once the defect is fixed, apply the scoped improvements
   identified in Goals (clarity, consistency, elimination of unnecessary steps).
8. **Refactor** — improve structure while keeping tests passing.

**TDD Loop:**
1. Write/update tests to reproduce the defect (RED)
2. Confirm tests fail for the right reason
3. Implement fix — minimum code needed to pass (GREEN)
4. Run full test suite, confirm all pass
5. Apply improvements; re-run tests
6. Refactor; re-run tests
7. Repeat until all acceptance criteria met

## Observed Behaviour (Evidence)

[REQUIRED before writing the plan. Capture the exact observed behaviour:
- What was done (inputs, steps, call made, action taken)
- What actually happened (error message verbatim, incorrect output, missing field, wrong state, etc.)
- What was expected to happen instead

This evidence is the acceptance test in reverse: the fix is complete when this
behaviour no longer occurs.]

```
[Paste exact error messages, output, or observations here]
```

## Root Cause

[What is the actual cause of the defect — not just the symptom? Identify the
specific artefact (file, line, spec section, process step) where the fault
originates. If root cause is unknown at the time of task creation, mark as
"TBD — see Exploration" and identify it during exploration.]

## Context & Scope

[Why this task exists, what artefacts are affected, and the boundaries of what
it will and will not address.

State explicitly:
- Which artefact(s) contain the defect: spec / code / tests / documentation / process
- What related improvements are in scope (directly caused by or revealed by this defect)
- What is explicitly out of scope (with a follow-on task reference if applicable)]

## Goals

[What this task achieves. Goals for a fix task must cover:

1. **The defect corrected** — the specific broken behaviour no longer occurs.
2. **Root cause resolved** — the underlying fault is fixed, not just the symptom.
3. **Clarity improved** — if the defect caused or was caused by ambiguity
   (naming, description, error message, documentation gap), that ambiguity is removed.
4. **Consistency restored** — if the defect revealed inconsistency across related
   artefacts, that inconsistency is addressed within the bounded scope of this task.
5. **Unnecessary extra steps eliminated** — if the defect forced callers or users
   to perform additional steps to obtain information or state they should have
   received directly, that is fixed.
6. **All affected artefacts in sync** — spec, code, tests, and documentation
   all reflect the corrected behaviour.]

## Who

[Who is accountable for this task; who contributed (human and/or model).]

## References

[Primary sources of truth that define correct behaviour.]

### Component Specifications

[List ALL component specifications that are impacted by this fix.
For each: code, name, one-line summary, link to spec file.]

- **CMP.XXX.YYY** - [Component Name] - [One-line summary] - [Link to spec]

### Other References

[Audit findings, user story IDs, related fix tasks, external standards, etc.]

## Plan

[Describe intent before action. Remember: Evidence → Root cause → Docs/spec → Tests → Code → Improvements → Refactor]

### Alignment

[Identify all artefacts that must be updated to reflect the corrected behaviour:
spec sections, code files, test files, documentation pages. State which will be
updated in this task and which (if any) are deferred to follow-on tasks.]

### Exploration

[What needs to be investigated to confirm the root cause and identify the full
set of affected artefacts. If root cause is already confirmed, state
"Root cause confirmed — no further exploration needed".]

### Assumptions

[Key assumptions about root cause, scope, and fix approach.]

### Acceptance Criteria

[Testable criteria that MUST be met. Include:
- The specific defect behaviour no longer occurs (invert the Evidence)
- Any improvements in scope are delivered
- All affected artefacts updated]

- [ ] [The observed behaviour described in Evidence no longer occurs]
- [ ] [Root cause artefact corrected]
- [ ] [Clarity/consistency improvements delivered — describe specifically]
- [ ] All existing tests pass
- [ ] Regression test(s) added and passing
- [ ] All affected specifications updated and in sync
- [ ] All affected documentation updated

### Testing Strategy

[Describe the testing approach for this fix.]

#### Regression Tests

[What test(s) will be added to prevent this defect from recurring?
Describe: test location, what it exercises, what it asserts.]

#### Related Test Categories

- [ ] **Unit Tests** — [If applicable: describe]
- [ ] **Integration Tests** — [If applicable: describe]
- [ ] **Smoke Tests** — [End-to-end path verification, if applicable]
- [ ] **Browser/E2E Tests** — [If applicable to UI components]

#### Coverage Requirements

- All tests MUST pass before task completion.
- At least one regression test MUST be added that would have caught this defect.
- Deleting any test requires EXPLICIT HUMAN permission.

### Constraints

[Any relevant limits or non-negotiables: must not break existing behaviour,
must maintain backwards compatibility, scope boundaries, etc.]

### Approach

[Step-by-step plan, following the TDD loop. Be specific about which artefacts
are changed in which order.]

## Implementation

[What was actually done. Update as you work.]

### Actions taken

[Summary of the main actions.]

### Evidence

[Data, observations, or artefacts gathered/produced — e.g., test output before
and after, diff summary, spec section updated.]

### Issues

[Notable problems, risks, or deviations encountered.]

## Reflect

[Think about what the results mean.]

### What happened

[What actually occurred.]

### Interpretation

[What this means in relation to the goal and assumptions.]

### Learning

[What is now better understood, including uncertainties and whether the root
cause analysis was correct.]

## Improvement

[Decide what happens next, including how the system itself should change.]

### Outcomes

[Brief statement of the overall outcomes: defect fixed, improvements delivered,
artefacts synchronised.]

### Decisions

[Any decisions made as a result — e.g., naming convention adopted, pattern
chosen for similar tools/artefacts.]

### Next steps

[Any follow-on work — e.g., related defects not in scope, improvements deferred
to another task. Propose as new tasks where appropriate.]

### Process improvement

[Note whether this fix suggests changes to task templates, processes, or ways
of working. If none, state "No changes identified".]

## Completion Checklist

[Before marking this task complete, verify ALL of the following:]

- [ ] The observed behaviour described in Evidence no longer occurs
- [ ] Root cause artefact corrected
- [ ] All acceptance criteria met
- [ ] At least one regression test added and passing
- [ ] Full test suite passes
- [ ] All affected component specifications updated and in sync
- [ ] All affected documentation updated
- [ ] Follow-on tasks created for any out-of-scope issues identified
