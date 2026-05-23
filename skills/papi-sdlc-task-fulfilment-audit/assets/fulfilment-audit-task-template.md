[TO CREATE A NEW FULFILMENT AUDIT TASK: **COPY** THIS TEMPLATE, THEN **EDIT** THE COPY
**ONE SECTION AT A TIME**, FOLLOWING THE INSTRUCTIONS IN EACH SECTION]

[Use this template to verify alignment between **user stories** and the
**capabilities** declared in component specifications, in both directions.
This audit examines artefacts only. It does NOT run the system or
exercise stories through their interface — that is a separate activity
covered by the `papi-sdlc-task-acceptance-test` skill.]

[Use this template only when appropriate:
* If a more specific template exists, use that instead.
* If no suitable template exists, propose creating a new one or updating
  an existing one.
* If this template seems obsolete or not useful, propose deleting it.]

[This template is derived from `basic-task-template.md`.]

[This template is a guideline:
* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that may
  indicate a need for a new/updated template or process change; record
  that under *Process improvement* in the *Improvement* section.]

# Task: Fulfilment Audit - [Scope Name]

**Audit Scope:** [User stories vs. component capabilities for: scope description]
**Audit Date:** YYYY-MM-DD
**Status:** [Proposed, In Progress, Completed, Failed]

## Synopsis

[One-line summary of what this audit is verifying.]

## Template

This document was based on the PAPI SDLC template: `fulfilment-audit-task-template.md`.

## Status

[Current status of this audit task.
Examples: Proposed, In Progress, Completed, Failed, Abandoned.
If the audit fails, note critical issues preventing completion.]

## Purpose

See the skill.

## Audit Scope

[Define what is in scope. Typical choices:
* All current user stories vs. all current component capabilities
* A specific release / milestone slice of stories
* A specific component's capabilities and the stories that should
  cover them
* A specific epic or story cluster and the supporting capabilities]

### Stories in Scope

[List the user stories included in this audit, with IDs.]

- **US-XX** - [Story title]
- **US-YY** - [Story title]

### Component Specs in Scope

[List the component specifications whose capabilities are in scope.]

- **CMP.XXX.YYY** - [Component Name] - Edition [N]
- **CMP.AAA.BBB** - [Component Name] - Edition [N]

## Parent task

[OMIT unless this is a sub-audit of a larger audit task.]

## Tasks this task depends on

[List any prerequisite tasks. Charter audits often precede this one
because Charter-level drift will change which stories should exist.]

- [Task: Charter audit, if recently due]

## Subordinate and dependent tasks

[OMIT unless other audits or tasks depend on this one being done first.
A compliance audit often follows this one.]

## Required reading

* All user stories in scope
* All component specifications in scope (capabilities only — not code)
* The `**Capabilities:**` field of each story
* Any charter or roadmap document that frames the stories

## Context & Scope

This audit ensures fulfilment integrity by:

1. Verifying every user story is supported by capabilities that exist
   and plausibly cover what the story asks for.
2. Verifying every capability in scope serves at least one user story
   (or is explicitly marked internal-only).
3. Producing a reconciled findings list with a disposition for each
   finding.

This audit examines artefacts. It does NOT:

- Execute tests, demos, or any part of the dev/release pipeline.
- Click through the product or call APIs to verify stories work.
  (That is the role of the acceptance-test skill.)
- Review code or implementation quality. (That is the role of the
  compliance audit.)
- Re-evaluate whether the stories themselves are the right stories
  to have. (That is the role of the charter audit.)

## Goals

- Produce a fulfilment audit report with Phase A and Phase B findings.
- Surface every orphan capability and obtain a user disposition.
- Produce a reconciled findings list with agreed dispositions.
- Identify any stories that need updating, any capabilities that need
  adding/changing/removing, and any deliberate exceptions.

## Who

[Who is accountable; who contributed (human and/or model).]

## References

### User Stories

- [USER_STORIES component spec](path/to/user_stories.md)
- [Story US-XX](path/to/story/or/anchor)
- ...

### Component Specifications

- [CMP.XXX.YYY Specification](path/to/spec.md) - Edition N
- [CMP.AAA.BBB Specification](path/to/spec.md) - Edition N

## Audit Plan

### Alignment

[This audit ensures that user stories and the capabilities cited by
those stories are perfectly aligned. Any discrepancy must result in:
1. Updating the story (e.g., fixing capability links, adding criteria), or
2. Updating the spec (e.g., adding, changing or removing a capability), or
3. A recorded accept-with-note exception (e.g., a capability confirmed
   as internal-only).]

### Audit Procedure

This audit runs in two directions and reconciles the results. Both
phases are MANDATORY (see the `papi-sdlc-task-fulfilment-audit` skill).

**This audit examines; it does not execute.** Do not run, click,
demo, or invoke any part of the product as part of this audit.

#### Phase A — Top-down (story → capability)

For each user story in scope:

1. **Read the story**
   - [ ] Read the story's narrative, acceptance criteria, and any
         linked notes.
   - [ ] Read the `**Capabilities:**` field and any inline capability
         references in the body.

2. **Verify each cited capability**
   For each capability ID cited by the story:
   - [ ] Confirm the capability ID exists in a component spec in scope.
   - [ ] Confirm the capability's description plausibly contributes
         to what this story needs.
   - [ ] Note any obvious misalignment between capability description
         and story intent.

3. **Verify collective coverage**
   - [ ] Decide whether the cited capabilities, taken together, cover
         what the story asks for.
   - [ ] If anything the story asks for is not covered by any cited
         capability, record a gap.

4. **Classify the story**
   - [ ] **Covered** — every cited capability exists; aligned; full coverage.
   - [ ] **Partial** — some coverage but at least one gap.
   - [ ] **Missing** — story has no capability links, or cited
         capabilities do not exist, or coverage is essentially absent.
   - [ ] **Misaligned** — cited capabilities exist but describe
         something materially different from what the story asks for.

#### Phase B — Bottom-up (capability → story)

Enumerate the capabilities in scope and map each one back to the
covering story (or stories). Capabilities with no covering story are
**orphan candidates** — do NOT auto-classify; bring each to the user.

1. **Enumerate capabilities in scope**
   - [ ] For each component spec in scope, list every capability
         (CAP.\*) declared.

2. **Map each capability to covering stories**
   - [ ] For each capability, list the user stories (if any) that
         cite it.
   - [ ] Capability cited by ≥1 in-scope story: covered.
   - [ ] Capability not cited by any in-scope story: **orphan
         candidate**.

3. **Capture orphan candidates**
   - [ ] List every orphan capability with ID + brief description.
   - [ ] Propose a likely orphan kind (scope creep / missing story /
         internal-only) — but do NOT decide.
   - [ ] Bring the list to the user for disposition decisions.

4. **Excluded capabilities**
   - [ ] List every capability (or capability pattern) intentionally
         excluded from the sweep, with a stated reason (e.g., a
         component spec explicitly out of scope for this audit).
         An empty list is fine; a missing list is not.

#### Phase C — Reconciliation

- [ ] Merge Phase A gaps (story not adequately covered) and Phase B
      orphan capabilities (capability with no covering story) into
      one findings list.
- [ ] Confirm every orphan capability has a recorded user disposition.
- [ ] Translate each finding into one of:
      - **Update stories** — add/change/fix story or its capability links
      - **Update specs** — add/change/remove a capability
      - **Accept with note** — recorded deliberate exception

### Audit Report Structure

The audit will produce a single document with:

1. **Executive Summary**
   - Overall pass/fail status
   - Counts of Covered / Partial / Missing / Misaligned stories
   - Orphan capability count
   - Recommendations

2. **Per-Story Findings (Phase A)**
   - Story ID, title, cited capabilities, classification, gap notes

3. **Per-Capability Findings (Phase B)**
   - Capability ID, covering stories, orphan status, proposed kind

4. **Reconciliation (Phase C)**
   - Consolidated findings with disposition and follow-up

5. **Conclusion**
   - Are stories and capabilities in alignment for the audited scope?
   - Required actions before closure.

## Audit Execution

### Per-Story Findings (Phase A)

| Story | Title | Cited capabilities | Classification | Gap notes |
|-------|-------|--------------------|----------------|-----------|
| US-XX | [title] | CAP.A, CAP.B | Covered / Partial / Missing / Misaligned | [notes] |
| US-YY | ... | ... | ... | ... |

### Per-Capability Findings (Phase B)

[Include every capability in scope. A capability with no covering
story goes also into the orphan candidates table below.]

| Capability | Description | Covering stories | Status |
|------------|-------------|------------------|--------|
| CAP.X.Y.Z  | [desc]      | US-XX, US-YY     | Covered |
| CAP.A.B.C  | [desc]      | (none)           | Orphan candidate |

### Orphan Capabilities (Phase B)

[List every capability with no covering user story. Propose a likely
orphan kind but do NOT decide; bring to the user.]

| ID | Capability | Description | Proposed kind | User decision | Rationale |
|----|------------|-------------|---------------|---------------|-----------|
| O1 | CAP.A.B.C  | [desc]      | scope creep / missing story / internal-only | [user] | [why] |
| O2 | ...        | ...         | ...           | ...           | ...       |

### Excluded Capabilities (Phase B)

[List every capability (or capability pattern) intentionally excluded
from the Phase B sweep, with a stated reason. An empty list is fine;
a missing list is not.]

| Pattern / ID | Reason for exclusion |
|--------------|----------------------|
| [e.g. CMP.ZZZ.*] | Component out of scope for this audit |

## Audit Report

### Executive Summary

**Audit Date:** YYYY-MM-DD
**Auditor:** [Name/ID]
**Scope:** [Summary of what was audited]
**Overall Result:** [PASS / FAIL]

**Statistics:**
- Stories Audited: X
- Covered: A
- Partial: B
- Missing: C
- Misaligned: D
- Capabilities Audited: Y
- Orphan Capabilities Raised: Z
- Findings Resolved As — Update Stories: U, Update Specs: V, Accept-with-Note: W

**Conclusion:**
[Are stories and capabilities aligned for this scope? What actions
are needed before this audit can close?]

### Detailed Findings

[Consolidated findings; can reference the per-story and per-capability
tables above or provide a summary view.]

### Reconciliation (Phase C)

[Merge Phase A gaps (story not adequately covered) and Phase B orphan
capabilities (capability with no covering story) into one consolidated
findings list. The audit cannot close until every orphan capability
has a recorded user disposition.]

| Finding | Source phase | Story / Capability | Disposition | Follow-up |
|---------|--------------|--------------------|-------------|-----------|
| [desc]  | A or B       | [id]               | update stories / update specs / accept-with-note | [task / story update / spec update / none] |

### Recommendations

1. [Priority recommendation]
2. [Priority recommendation]
3. ...

### Next Steps

[What needs to happen as a result of this audit?
* Create follow-up tasks for story or spec updates
* Update USER_STORIES and/or component specs in place
* Schedule a compliance audit once spec changes are complete
* Schedule a re-audit if disposition was deferred]

## Improvement

### Outcomes

[Brief statement of the overall outcomes of this audit.]

### Decisions

[Any decisions being made as a result of this audit.]

### Process improvement

[Note whether this audit suggests changes to:
* USER_STORIES component or story format
* Component specification or capability format
* This audit task template
* Story-writing or capability-writing practices

If none, state "No changes identified".]

### Future Enhancements

[Ideas for improving the fulfilment audit process.]

## Completion Checklist

[Before marking this audit task complete, verify ALL of the following:]

- [ ] All stories in scope have been classified (Covered / Partial / Missing / Misaligned)
- [ ] Gap notes are specific and actionable for all non-Covered stories
- [ ] Phase B bottom-up sweep performed across the full in-scope capability surface
- [ ] Excluded-capabilities list provided (empty is fine; missing is not)
- [ ] Every orphan capability has a recorded user disposition
- [ ] Phase C reconciliation table completed
- [ ] Follow-up tasks created for any gap requiring implementation or spec work
- [ ] Audit report is complete with executive summary and recommendations

## Addendum

[Optional additional information, references, resources, notes, ...]
