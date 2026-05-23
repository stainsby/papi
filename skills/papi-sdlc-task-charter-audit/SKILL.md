---
name: papi-sdlc-task-charter-audit
description: Create or work with charter audit tasks that check alignment between the project's Charter and its user stories — both top-down and bottom-up. [PAPI SDLC]
---

# SDLC Task - Charter Audit

## Purpose

A charter audit is a task that checks alignment between the project's
**Charter** and its **user stories** — in both directions.

It asks two questions:

1. Does the story corpus, taken as a whole, pull the project toward
   the Charter (its Purpose, Vision, Ethos, Scope, and Success
   indicators)?
2. Does every story fit somewhere under the Charter — or is some
   story off-Charter (scope creep, ethos violation, or a sign the
   Charter itself has drifted)?

The output is a findings list with a disposition for each finding:
update the stories, update the Charter, or accept-with-note.

**This needs the PAPI long task skill.**

## What this audit is and is not

This audit:

- Examines alignment of *intent* (Charter) against *story-level work*
  (user stories).
- May recommend **changes to the Charter** as well as changes to the
  stories. The Charter is not assumed correct — it is one side of the
  comparison, not the reference. If reality has moved past the
  Charter, the audit should say so.
- Does NOT write code or execute anything (tests, demos, pipelines).

## Two phases are mandatory

A charter audit MUST run in two directions and reconcile the results:

- **Phase A — Top-down (Charter → stories):** for each section of the
  Charter, ask whether the current story corpus pulls toward it.
  Record findings as: covered / partial / missing / contradicted.

  Note: this is coverage and direction, not 1:1 item matching. The
  Charter does not enumerate stories; it sets the destination and the
  way of working. Phase A asks whether the stories are heading there
  and behaving accordingly.

- **Phase B — Bottom-up (stories → Charter):** for each story (or
  coherent group of stories), identify which part(s) of the Charter
  it serves. Stories that don't fit anywhere are **orphan
  candidates**.

  An orphan candidate is one of three kinds:
  - *scope creep* — the story is outside the Charter's Scope
  - *ethos violation* — the story would have us work in a way the
    Ethos rules out
  - *Charter-drift signal* — the story is reasonable work, but the
    Charter no longer describes the project the stories are building

- **Phase C — Reconciliation:** merge Phase A gaps and Phase B orphan
  candidates into a single findings list. For each finding, record
  the agreed disposition:
  - **Update stories** (add, change, or remove)
  - **Update Charter** (the Charter needs to catch up to reality, or
    was wrong)
  - **Accept with note** (a deliberate, recorded exception)

Running only Phase A is a CRITICAL FAILURE: it lets unaligned work
hide. Both phases must be evidenced in the report.

### Orphan candidate handling

Every Phase B orphan candidate MUST be brought to the user for a
disposition decision before the audit closes. Do NOT auto-classify a
story as scope creep, ethos violation, or Charter-drift — the choice
between those is a strategic call that belongs with the user.

## When to run

Run a charter audit:

- Once early in the project, after the Charter and a first cut of
  stories both exist.
- Once per release (or at a similar cadence).
- Whenever the story set shifts substantially (large story additions,
  scope expansion, pivot).
- Whenever someone suspects the Charter no longer describes the
  project.

## Dependencies

Reading these skills is REQUIRED to understand and execute this skill:

- PAPI skill `papi-tasks-understand`
- PAPI skill `papi-templates-understand`
- PAPI skill `papi-sdlc-charter`
- PAPI skill `papi-sdlc-user-stories`

## Actions

- Read the project's Charter and the user-stories index (and each
  story as needed).
- Copy the default audit template (see below) verbatim and edit it
  section by section.
- For Phase A, work through each Charter section in turn and record
  findings against the story corpus.
- For Phase B, work through each story (or coherent group of stories)
  and record which Charter section(s) it serves. Anything that fits
  nowhere goes to the orphan candidates table.
- Bring all orphan candidates to the user for disposition before
  closing the audit.
- For each Phase C finding, record the agreed disposition (update
  stories / update Charter / accept with note) and follow-on actions.

## Notes

- A Charter audit can legitimately recommend that the **Charter
  itself** be updated. The Charter is not a reference document for
  this audit; it is one side of the comparison. Treat both sides
  with equal scrutiny.
- Generally this is a full audit unless otherwise specified. Do not
  read older charter audit docs to work incrementally — start fresh.

## Skill artefacts

- **Default audit template**: `assets/charter-audit-task-template.md`
