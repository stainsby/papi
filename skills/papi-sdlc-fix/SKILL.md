---
name: papi-sdlc-fix
description: Create or work with defect fix tasks — diagnose a defect, plan the fix, and identify improvements to leave the affected area in a better state. [PAPI]
---

- Read, copy and use the template.
- Assets within this skill:
  - **Template**: `assets/fix-task-template.md`

## When to use this skill

Use this skill whenever a defect, bug, or unintended behaviour is being
addressed as a task, regardless of whether the defect is in code, a
specification, documentation, tooling, or a process.

## Core principles

### Fix + improve

A defect fix task is not a minimal patch. It is an opportunity to leave the
affected area in a better state than before the defect was introduced. Every
fix task MUST consider and, where feasible, incorporate:

1. **Root cause addressed** — not just the symptom. Document the root cause
   explicitly; if it cannot be fixed in this task, record it as a follow-on.

2. **Clarity improvement** — if the defect caused confusion (e.g., ambiguous
   naming, missing documentation, unhelpful error messages, misleading
   descriptions), improve the relevant artefact so the same confusion cannot
   recur. This applies equally to code interfaces, specification language,
   process descriptions, and user-facing copy.

3. **Consistency improvement** — if the defect reveals an inconsistency across
   related artefacts (e.g., naming conventions, structural patterns, response
   contracts, formatting), address the inconsistency as part of the task, not
   just the specific broken instance.

4. **Eliminate unnecessary extra steps** — if the defect forced users or
   callers to perform an additional action to obtain information or state that
   should have been available in the first place, fix the artefact so that
   extra step is no longer needed.

5. **Artefacts in sync** — every fix that changes observable behaviour or
   structure **must** update all affected artefacts: specification, code,
   tests, and documentation. A fix without corresponding artefact updates is
   incomplete.

### Scope discipline

"Leave it better" does not mean "also fix everything else you notice".
Improvements included in a fix task must be:
- **Directly related** to the defect or its root cause.
- **Bounded** — if an improvement is significant enough to risk scope creep,
  create a separate task and note it as a follow-on.

### Evidence first

Before writing the plan, capture the exact observed behaviour as evidence.
This serves as the acceptance test: the fix is done when the evidence
condition no longer occurs.

### Test-Driven Development

Use proper TDD: write a failing test that directly captures the observed
evidence, then implement the fix to make that test pass. This ensures the
fix is verifiable and prevents regressions.

## Checklist when creating a fix task

- [ ] Root cause identified and documented (not just the symptom)
- [ ] Severity assessed: critical correctness / usability / consistency / cosmetic
- [ ] Scope stated: which artefacts are affected — spec, code, tests, docs, or combination
- [ ] Related consistency issues identified and scoped in (or explicitly noted
      as out of scope with a follow-on task reference)
- [ ] Related clarity improvements identified and included
- [ ] Unnecessary extra-step patterns eliminated where the fix makes this possible
- [ ] All affected artefact updates listed in Goals and Approach
- [ ] Acceptance criteria are concrete and testable — directly inverting the
      observed evidence
- [ ] TDD approach was planned and used
- [ ] Regression/verification tests included in Approach where applicable
- [ ] Dependencies on other fix tasks noted
