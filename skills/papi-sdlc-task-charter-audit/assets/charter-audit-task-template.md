[TO CREATE A NEW CHARTER AUDIT TASK: **COPY** THIS TEMPLATE, THEN **EDIT** THE COPY
**ONE SECTION AT A TIME**, FOLLOWING THE INSTRUCTIONS IN EACH SECTION]

[Use this template to assess alignment between the project Charter and
the user stories — in both directions.]

[Use this template only when appropriate:
* If a more specific template exists, use that instead.
* If no suitable template exists, propose creating a new one or updating an
  existing one.
* If this template seems obsolete or not useful, propose deleting it.]

[This template is derived from `basic-task-template.md`.]

[This template is a guideline:
* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that may
  indicate a need for a new/updated template or process change; record that
  under *Process improvement* in the *Improvement* section.]

# Task: Charter Audit - [Scope Name]

**Audit Date:** YYYY-MM-DD
**Status:** [Proposed, In Progress, Completed]

## Synopsis

[One-line summary of what this audit is checking.]

## Template

This document was based on the PAPI SDLC template: `charter-audit-task-template.md`.

## Status

[Current status of this audit task.
Examples: Proposed, In Progress, Completed, Failed, Abandoned.]

## Purpose

See the skill.

## Audit Scope

### Charter under audit

**Charter:** [path to the Charter document]
**Charter last reviewed:** YYYY-MM-DD

### Stories in scope

[List the user stories in scope. Usually all stories, unless a specific
subset is being audited.]

- US-XX: [Story title]
- US-YY: [Story title]
- …

(or: "All stories in the catalogue")

## Parent task

[OMIT unless this is a sub-task of a larger audit or release task.]

## Tasks this task depends on

[OMIT unless this audit depends on prior work.]

## Subordinate and dependent tasks

[OMIT unless other tasks depend on this being done first.]

## Required reading

* The project Charter
* The user-stories index and the stories themselves
* Any higher-level documents the Charter aligns with (consulted as needed)

## Context & Scope

This audit checks alignment between intent (Charter) and story-level
work (user stories). Both sides are treated as mutable: a discrepancy
may mean the stories need to change, or the Charter does.

This audit does NOT write code, or execute tests, demos, or pipelines

## Goals

- Confirm the story corpus pulls toward each part of the Charter
- Identify stories that don't fit under any part of the Charter
- Surface any Charter drift — places where the Charter no longer
  describes the project the stories are building
- Produce a findings list with an agreed disposition per finding

## Who

[Who is accountable for this audit, who contributed (human and/or model).]

## References

- [Charter](path/to/CHARTER.md)
- [User stories index](path/to/USER_STORIES.md)

## Audit Plan

### Audit Procedure

This audit runs in two directions and reconciles the results. Both
phases are MANDATORY (see the `papi-sdlc-task-charter-audit` skill).

#### Pre-pass — Template conformance

Check the Charter file against the current `charter-template.md`.
Record any structural drift (missing sections, renamed fields, stale
guidance, undocumented additions) as findings with a disposition:
update document / update template / accept with note. Run this before
Phase A so that "format outdated" findings don't get confused with
"content wrong" findings.

#### Phase A — Top-down (Charter → stories)

For each section of the Charter, ask whether the current story corpus
pulls toward it. This is coverage and direction, not 1:1 item
matching.

For each Charter section in turn:

- **Purpose** — do the stories collectively serve this purpose?
- **Vision** — are the stories pointing the project toward this
  destination?
- **Ethos** — do the stories respect the way of working and the
  listed value statements? Any stories that pull against the ethos?
- **Scope** — are the stories all within the declared scope? Any
  drifting out?
- **Higher-level alignment** — do the stories respect the
  bigger-picture documents the project sits under?
- **Success indicators** — are the stories shaping the project so
  that these indicators are likely to be achievable?

For each section, classify the situation as: **Covered**, **Partial**,
**Missing**, or **Contradicted**. Record specific stories or gaps as
evidence.

#### Phase B — Bottom-up (stories → Charter)

For each story (or coherent group of stories), identify which part(s)
of the Charter it serves. Stories that fit nowhere are **orphan
candidates**.

1. **Map stories to Charter sections**
   - [ ] For each story (or group), record the Charter section(s) it
         serves
   - [ ] Stories that don't fit anywhere → record as **orphan
         candidate**

2. **Classify each orphan candidate** (proposed, not decided):
   - *scope creep* — outside the Charter's Scope
   - *ethos violation* — would have us work against the Ethos
   - *Charter-drift signal* — reasonable work, but the Charter no
     longer describes what the stories are building

3. **Bring orphan candidates to the user**
   - [ ] List every orphan candidate with description and proposed
         kind
   - [ ] For each, the user decides the disposition (update stories /
         update Charter / accept with note)

#### Phase C — Reconciliation

- [ ] Merge Phase A findings (gaps, partials, contradictions) and
      Phase B orphan candidates into a single findings list
- [ ] Confirm every orphan candidate has a recorded user disposition
- [ ] For each finding, record the agreed action: update stories /
      update Charter / accept with note
- [ ] Translate actions into follow-on tasks or document updates

## Audit Execution

### Pre-pass — Template Conformance Findings

[Structural drift of the Charter file from `charter-template.md`.
Record findings before doing Phase A so structural drift doesn't get
confused with content findings.]

| # | Where | Drift | Disposition | Follow-on |
|---|-------|-------|-------------|-----------|
| T1 | [section / field] | [missing / renamed / stale guidance / undocumented addition] | update document / update template / accept with note | [task ref] |
| … | … | … | … | … |

### Phase A — Per-Section Findings

[For each Charter section, document the assessment.]

#### Purpose

**Status:** [Covered / Partial / Missing / Contradicted]

**Evidence:**

| Story or group | Pulls toward Purpose? | Notes |
|----------------|-----------------------|-------|
| US-XX | Yes / Partial / No | [why] |
| … | … | … |

**Notes:** [observations, gaps]

#### Vision

**Status:** [Covered / Partial / Missing / Contradicted]

[Same shape as above.]

#### Ethos

**Status:** [Covered / Partial / Missing / Contradicted]

[For each value statement listed in the Charter, optionally a row:]

| Value statement | Honoured by stories? | Notes |
|-----------------|----------------------|-------|
| [value 1] | Yes / Mixed / No | [evidence] |
| … | … | … |

#### Scope

**Status:** [Covered / Partial / Missing / Contradicted]

[Identify any stories drifting out of scope.]

#### Higher-level alignment

**Status:** [Covered / Partial / Missing / Contradicted / N/A]

[Note any stories that conflict with the bigger-picture documents the
project sits under. If the Charter lists no higher-level alignment,
mark N/A.]

#### Success indicators

**Status:** [Covered / Partial / Missing / Contradicted]

[For each Charter-level success indicator, note whether the stories
are likely to move it.]

### Phase B — Story-to-Charter Map

[One row per story or coherent group of stories. Mark stories that
fit nowhere as orphan candidates and move them to the table below.]

| Story / group | Charter section(s) served | Notes |
|---------------|---------------------------|-------|
| US-XX | Purpose, Scope | [why] |
| … | … | … |

### Phase B — Orphan Candidates

[Every story that didn't fit under any Charter section. Bring this
list to the user for disposition decisions before closing the audit.]

| ID | Story | Proposed kind | Description | User decision | Rationale |
|----|-------|---------------|-------------|---------------|-----------|
| O1 | US-XX | scope creep / ethos violation / Charter-drift | [what it does] | update stories / update Charter / accept | [why] |
| O2 | … | … | … | … | … |

### Phase C — Reconciliation

[The single findings list, combining Phase A gaps and Phase B orphan
candidates.]

| # | Source | Finding | Agreed action | Follow-on task / change |
|---|--------|---------|---------------|-------------------------|
| 1 | Phase A — Vision | [gap] | update stories | [task ref] |
| 2 | Phase B — orphan | [story] | update Charter | [edit ref] |
| 3 | Phase A — Ethos | [contradiction] | accept with note | [note ref] |
| … | … | … | … | … |

## Audit Report

### Summary

**Audit Date:** YYYY-MM-DD
**Auditor:** [Name/ID]
**Scope:** [Summary of what was audited]

**Statistics:**

- Charter sections audited: X
- Sections fully covered: A
- Sections partial / missing / contradicted: B
- Stories audited: Y
- Orphan candidates raised: O
- Findings overall: F
- Findings resolved as "update Charter": F1
- Findings resolved as "update stories": F2
- Findings resolved as "accept with note": F3
- Template conformance findings raised: T
- Template conformance findings resolved as "update document": T1
- Template conformance findings resolved as "update template": T2
- Template conformance findings resolved as "accept with note": T3

**Conclusion:**

[Overall assessment. Is the Charter still describing the project the
stories are building? Are the stories pulling toward the Charter?
What are the critical findings, and what changes have been agreed?]

### Investigative notes (optional)

[Anything that came up during the audit that doesn't fit elsewhere.]

## Completion Checklist

- [ ] All Charter sections assessed (Phase A)
- [ ] All stories mapped or marked as orphan candidates (Phase B)
- [ ] Every orphan candidate has a recorded user disposition
- [ ] Phase A and Phase B findings reconciled into one list (Phase C)
- [ ] Each finding has an agreed action (update stories / update
      Charter / accept with note)
- [ ] Pre-pass: Charter file checked against `charter-template.md`
      and any structural drift recorded with a disposition
- [ ] Follow-on tasks created for actions that require work
- [ ] Charter and / or stories updated as agreed (or follow-on tasks
      created to do so)

## Improvement

### Outcomes

[What outcomes did this audit achieve? Any meta-findings about the
audit process itself?]

### Process improvement

[Any suggestions for improving this audit template, the Charter
template, the user-stories template, or the surrounding skills.]
