# Task: Fulfilment Audit - [Scope Name]

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

* **US-XX** - [Story title]
* **US-YY** - [Story title]

### Component Specs in Scope

[List the component specifications whose capabilities are in scope.]

* **CMP.XXX.YYY** - [Component Name] - Edition [N]
* **CMP.AAA.BBB** - [Component Name] - Edition [N]

## Parent task

[OMIT unless this is a sub-audit of a larger audit task.]

## Tasks this task depends on

[List any prerequisite tasks. Charter audits often precede this one
because Charter-level drift will change which stories should exist.]

* [Task: Charter audit, if recently due]

## Subordinate and dependent tasks

[OMIT unless other audits or tasks depend on this one being done first.
A compliance audit often follows this one.]

## Required reading

* All user stories in scope
* All component specifications in scope (capabilities only — not code)
* The `**Users:**` field of each in-scope user-facing capability (this is
  where stories are cited)
* Any charter or roadmap document that frames the stories

## Context & Scope

This audit ensures fulfilment integrity by:

1. Verifying every user story is supported by capabilities that exist
   and plausibly cover what the story asks for.
2. Verifying every user-facing capability in scope cites at least one
   real user story (or is explicitly marked internal-only / composition).
3. Producing a reconciled findings list with a disposition for each
   finding.

This audit examines artefacts. It does NOT:

* Execute tests, demos, or any part of the dev/release pipeline.
* Click through the product or call APIs to verify stories work.
  (That is the role of the acceptance-test skill.)
* Review code or implementation quality. (That is the role of the
  compliance audit.)
* Re-evaluate whether the stories themselves are the right stories
  to have. (That is the role of the charter audit.)

## Goals

* Produce a fulfilment audit report with Phase A and Phase B findings.
* Surface every orphan capability and obtain a user disposition.
* Produce a reconciled findings list with agreed dispositions.
* Identify any stories that need updating, any capabilities that need
  adding/changing/removing, and any deliberate exceptions.

## Who

[Who is accountable; who contributed (human and/or model).]

## References

### User Stories

* [USER_STORIES component spec](path/to/user_stories.md)
* [Story US-XX](path/to/story/or/anchor)
* ...

### Component Specifications

* [CMP.XXX.YYY Specification](path/to/spec.md) - Edition N
* [CMP.AAA.BBB Specification](path/to/spec.md) - Edition N

## Audit Plan

### Alignment

[This audit ensures that user stories and the user-facing capabilities
that cite them are perfectly aligned. Any discrepancy must result in:

1. Updating the story (e.g., adding criteria, splitting scope), or
2. Updating the spec (e.g., adding, changing or removing a capability, or
   fixing the story citations in its `**Users:**` field), or
3. A recorded accept-with-note exception (e.g., a capability confirmed
   as internal-only).]

### Audit Procedure

This audit runs in two directions and reconciles the results. Both
phases are MANDATORY (see the `papi-sdlc-task-fulfilment-audit` skill).

**This audit examines; it does not execute.** Do not run, click,
demo, or invoke any part of the product as part of this audit.

#### Pre-pass — Template conformance

Before Phase A, do a lightweight structural check of every in-scope
source document against its current template:

* Each in-scope user story file vs `user-story-template.md`
* The user-stories index vs `user-stories-template.md`
* Each component spec referenced by a cited or in-scope capability vs
  `component-specification-template.md`

Record any structural drift (missing sections, renamed fields, stale
guidance, undocumented additions) as findings with a disposition:
update document / update template / accept with note. Running this
first separates "format outdated" from "content wrong" before Phase A
goes deeper.

#### Phase A — Top-down (story → capability)

For each user story in scope:

1. **Read the story**
   * [ ] Read the story's narrative, acceptance criteria, and any
         linked notes.
   * [ ] Gather the user-facing capabilities whose `**Users:**` field
         cites this story.

2. **Verify each citing capability**
   For each capability that cites the story:
   * [ ] Confirm the capability lives in a component spec in scope.
   * [ ] Confirm the capability is **user-facing** — its `**Users:**`
         field cites one or more user stories. (`internal` and
         `composition` capabilities MUST NOT cite stories.)
   * [ ] Confirm the role recorded against this story in the
         capability's `**Users:**` field matches the story's `**Role:**`.
   * [ ] Confirm the capability's description plausibly contributes
         to what this story needs.
   * [ ] Note any obvious misalignment between capability description
         and story intent.

3. **Verify collective coverage**
   * [ ] Decide whether the cited capabilities, taken together, cover
         what the story asks for.
   * [ ] If anything the story asks for is not covered by any cited
         capability, record a gap.

4. **Classify the story**
   * [ ] **Covered** — every cited capability exists; aligned; full coverage.
   * [ ] **Partial** — some coverage but at least one gap.
   * [ ] **Missing** — no capability cites the story, or the citing
         capabilities do not exist, or coverage is essentially absent.
   * [ ] **Misaligned** — cited capabilities exist but describe
         something materially different from what the story asks for.

#### Phase B — Bottom-up (capability → story)

Phase B sweeps only **user-facing capabilities** (those whose
`**Users:**` field cites at least one user story). Capabilities marked
`internal` or `composition` are out of scope; list them in the
Excluded table with the reason. Within scope, capabilities citing no
real in-scope story are **orphan candidates** — do NOT auto-classify;
bring each to the user.

1. **Enumerate user-facing capabilities in scope**
   * [ ] For each component spec in scope, list every capability
         (CAP.\*) whose `**Users:**` field cites ≥1 user story.
   * [ ] List capabilities marked `internal` or `composition` in the
         Excluded table; do not include them in Phase B mapping.

2. **Resolve the stories each user-facing capability cites**
   * [ ] For each user-facing capability, resolve the user stories its
         `**Users:**` field cites.
   * [ ] Every cited story exists and is in scope: covered (subject to
         role check below).
   * [ ] Capability citing no real in-scope story: **orphan
         candidate**.

3. **Role check**
   * [ ] For each story the capability cites, confirm the role recorded
         against it matches that story's `**Role:**` field.
   * [ ] Any mismatch is a **role-coverage gap**.

4. **Capture orphan candidates**
   * [ ] List every orphan capability with ID + brief description.
   * [ ] Propose a likely orphan kind (scope creep / missing story)
         — but do NOT decide.
   * [ ] If you suspect a capability is *mismarked* as user-facing
         (i.e., should really be `internal` or `composition`), record
         it as a *mismarked* finding instead of an orphan.
   * [ ] Bring the list to the user for disposition decisions.

5. **Excluded capabilities**
   * [ ] List every capability (or capability pattern) excluded from
         the sweep, with a stated reason. Capabilities marked
         `internal` or `composition` go here automatically. Component
         specs explicitly out of scope go here too. An empty list is
         fine; a missing list is not.

#### Phase C — Reconciliation

* [ ] Merge Phase A gaps, Phase B orphan capabilities, Phase B
      role-coverage gaps, and any *mismarked* findings into one
      consolidated findings list.
* [ ] Confirm every orphan capability and every mismarked finding
      has a recorded user disposition.
* [ ] Translate each finding into one of:
      - **Update stories** — add/change/fix a story or its `**Role:**`;
        add a missing story for a role
      - **Update specs** — add/change/remove a capability; mark a
        capability `internal` or `composition`; fix the story
        citations in a `**Users:**` field
      - **Accept with note** — recorded deliberate exception

### Audit Report Structure

The audit will produce a single document with:

1. **Executive Summary**
   * Overall pass/fail status
   * Counts of Covered / Partial / Missing / Misaligned stories
   * Orphan capability count
   * Recommendations

2. **Per-Story Findings (Phase A)**
   * Story ID, title, citing capabilities, classification, gap notes

3. **Per-Capability Findings (Phase B)**
   * Capability ID, covering stories, orphan status, proposed kind

4. **Reconciliation (Phase C)**
   * Consolidated findings with disposition and follow-up

5. **Conclusion**
   * Are stories and capabilities in alignment for the audited scope?
   * Required actions before closure.

## Audit Execution

### Pre-pass — Template Conformance Findings

[Structural drift of in-scope source documents from their current
templates: user stories vs `user-story-template.md`, user-stories
index vs `user-stories-template.md`, component specs vs
`component-specification-template.md`. Record findings here before
doing Phase A so structural drift doesn't get confused with content
findings.]

| # | Document | Template | Drift | Disposition | Follow-up |
|---|----------|----------|-------|-------------|-----------|
| T1 | [path] | user-story-template.md / user-stories-template.md / component-specification-template.md | [missing / renamed / stale guidance / undocumented addition] | update document / update template / accept with note | [task ref] |
| … | … | … | … | … | … |

### Per-Story Findings (Phase A)

| Story | Role | Title | Citing capabilities | Roles match | Classification | Gap notes |
|-------|------|-------|---------------------|-------------|----------------|-----------|
| US-XX | [role] | [title] | CAP.A, CAP.B | Yes / No | Covered / Partial / Missing / Misaligned | [notes] |
| US-YY | ... | ... | ... | ... | ... | ... |

### Per-Capability Findings (Phase B)

[Include every **user-facing** capability in scope. A capability with no
covering story goes also into the orphan candidates table below. Role-
coverage gaps (capability cited but not by every claimed role) are flagged
here.]

| Capability | Cited stories (role) | Stories exist & in scope | Roles match | Status |
|------------|----------------------|--------------------------|-------------|--------|
| CAP.X.Y.Z  | US-XX (role-1), US-YY (role-2) | Yes | Yes | Covered |
| CAP.A.B.C  | (none)               | —                        | —    | Orphan candidate |
| CAP.D.E.F  | US-ZZ (role-4)       | Yes                      | No (story role is role-1) | Role-coverage gap |

### Orphan Capabilities (Phase B)

[List every user-facing capability with no covering user story.
Propose a likely orphan kind but do NOT decide; bring to the user.
If you believe a capability is *mismarked* as user-facing, list it
here with proposed kind `mismarked`.]

| ID | Capability | Cited stories | Description | Proposed kind | User decision | Rationale |
|----|------------|---------------|-------------|---------------|---------------|-----------|
| O1 | CAP.A.B.C  | (none)        | [desc]      | scope creep / missing story / mismarked | [user] | [why] |
| O2 | ...        | ...           | ...         | ...           | ...           | ...       |

### Role-Coverage Gaps (Phase B)

[List every user-facing capability that cites a story whose recorded
role does not match that story's own `**Role:**` field.]

| ID | Capability | Cited story | Role recorded by capability | Story's actual role |
|----|------------|-------------|-----------------------------|---------------------|
| RG1 | CAP.D.E.F | US-ZZ | role-4 | role-1 |

### Excluded Capabilities (Phase B)

[List every capability (or capability pattern) excluded from the
Phase B sweep, with a stated reason. Capabilities marked `internal`
or `composition` belong here automatically. An empty list is fine;
a missing list is not.]

| Pattern / ID | Reason for exclusion |
|--------------|----------------------|
| CAP.QQQ.INTERNAL_THING | Marked `internal` |
| CAP.RRR.MVP   | Marked `composition` |
| [e.g. CMP.ZZZ.*] | Component out of scope for this audit |

## Audit Report

### Executive Summary

**Audit Date:** YYYY-MM-DD
**Auditor:** [Name/ID]
**Scope:** [Summary of what was audited]
**Overall Result:** [PASS / FAIL]

**Statistics:**
* Stories Audited: X
* Covered: A
* Partial: B
* Missing: C
* Misaligned: D
* User-Facing Capabilities Audited: Y
* Capabilities Excluded (internal / composition / out-of-scope): Y_excl
* Orphan Capabilities Raised: Z
* Role-Coverage Gaps Raised: R
* Findings Resolved As — Update Stories: U, Update Specs: V, Accept-with-Note: W
* Template Conformance Findings Raised: T (Update Document: T1, Update Template: T2, Accept-with-Note: T3)

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

* [ ] All stories in scope have been classified (Covered / Partial / Missing / Misaligned)
* [ ] Each story's `**Role:**` matched against the role recorded for it in each citing capability's `**Users:**`
* [ ] Gap notes are specific and actionable for all non-Covered stories
* [ ] Phase B bottom-up sweep performed across all in-scope **user-facing** capabilities
* [ ] Role check performed for every story cited by a user-facing capability
* [ ] Excluded-capabilities list provided (internal/composition caps included; empty is fine; missing is not)
* [ ] Every orphan capability and every mismarked finding has a recorded user disposition
* [ ] Phase C reconciliation table completed
* [ ] Pre-pass: each in-scope user story and the stories index checked against their templates; each referenced spec checked against `component-specification-template.md`; drift recorded with a disposition
* [ ] Follow-up tasks created for any gap requiring implementation or spec work
* [ ] Audit report is complete with executive summary and recommendations

## Addendum

[Optional additional information, references, resources, notes, ...]
