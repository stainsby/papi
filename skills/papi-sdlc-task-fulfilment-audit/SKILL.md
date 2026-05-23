---
name: papi-sdlc-task-fulfilment-audit
description: Create or work with fulfilment audit tasks that check forward and backward mappings between user stories and the capabilities declared in component specifications. [PAPI SDLC]
---

# SDLC Task - Fulfilment Audit

## Purpose

A fulfilment audit checks alignment between **user stories** and the
**capabilities** declared in component specifications, in both
directions.

It is the middle rung of the PAPI audit ladder:

| Audit | Compares | Forward | Backward |
|-------|----------|---------|----------|
| Charter | charter ↔ stories | charter → stories | stories → charter |
| **Fulfilment** | **stories ↔ capabilities** | **story → capability** | **capability → story** |
| Compliance | capabilities ↔ code | spec → code | code → spec |

The fulfilment audit asks two questions:

1. For every user story, do the capabilities it cites actually exist,
   and do they (together) cover what the story needs?
2. For every capability in scope, is there a user story that needs
   it — or is the capability an orphan?

The output is a findings list with a disposition for each finding:
update the stories, update the component specs, or accept-with-note.

**This needs the PAPI long task skill.**

## This audit examines; it does not execute

This audit *examines* artefacts (user stories, component
specifications, the capability links between them). It does NOT
execute tests, demos, or run the system. Whether stories can be
performed end-to-end through the real interface is a separate
question handled by the `papi-sdlc-task-acceptance-test` skill — not
this audit.

## Two phases are mandatory

A fulfilment audit MUST run in two directions and reconcile the
results:

- **Phase A — Top-down (story → capability):** for each user story in
  scope, take the `**Capabilities:**` field (and any in-body
  references) and check:
  - every cited capability ID exists in the relevant component spec
  - the cited capabilities are plausibly aligned with what the story
    asks for
  - the union of cited capabilities is sufficient to cover the
    story's narrative and acceptance criteria
  - Classify the story as: **Covered**, **Partial**, **Missing**, or
    **Misaligned**.

- **Phase B — Bottom-up (capability → story):** for each capability
  in scope (across the relevant component specs), find the user
  story (or stories) that cite it. Capabilities cited by no story
  are **orphan candidates**.

  An orphan capability is one of three kinds:
  - *scope creep* — the capability exists but no user wants it
  - *missing story* — a user does want it, but the story hasn't
    been written
  - *internal-only capability* — a legitimate sub-capability that
    serves other capabilities, not users directly (these are fine
    but must be explicitly marked, not silently accepted)

- **Phase C — Reconciliation:** merge Phase A gaps and Phase B
  orphan capabilities into a single findings list. For each
  finding, record the agreed disposition:
  - **Update stories** (add, change, fix capability links)
  - **Update specs** (add, change, or remove capabilities)
  - **Accept with note** (a deliberate, recorded exception, e.g.,
    confirmed internal-only capability)

Running only Phase A is a CRITICAL FAILURE: it lets capabilities that
serve no story persist in the specs unchallenged. Both phases must be
evidenced in the report.

### Orphan candidate handling

Every Phase B orphan capability MUST be brought to the user for a
disposition decision before the audit closes. Do NOT auto-classify
the orphan kind — the choice between scope creep, missing story, and
internal-only is a strategic call that belongs with the user.

## Relation to other audits

- **Compliance audit** (`papi-sdlc-task-compliance-audit`) checks
  capabilities ↔ code. A fulfilment audit should generally be run
  **before** compliance, because a capability with no covering story
  may need to be removed from the spec — and there is no point
  auditing dead capabilities against code.
- **Charter audit** (`papi-sdlc-task-charter-audit`) checks charter ↔
  stories. Run this before fulfilment when both are due — fixing
  Charter-level drift first avoids re-doing fulfilment work on
  stories that may need to change.
- **Acceptance test** (`papi-sdlc-task-acceptance-test`) is NOT an
  audit; it exercises stories through the real interface with the
  appropriate role discipline. Run after compliance and fulfilment
  pass, not instead of them.

Recommended order when all are due:

```
Charter audit → Fulfilment audit → Compliance audit → Acceptance test
```

## Dependencies

Reading these skills is REQUIRED to understand and execute this
skill:

- PAPI skill `papi-tasks-understand`
- PAPI skill `papi-templates-understand`
- PAPI skill `papi-sdlc-user-stories`
- PAPI skill `papi-sdlc-component-specification`

Read these as needed:

- PAPI skill `papi-sdlc-task-charter-audit` (peer, often run before)
- PAPI skill `papi-sdlc-task-compliance-audit` (peer, often run after)
- PAPI skill `papi-sdlc-task-acceptance-test` (peer, separate
  activity)

## Actions

- For any reasonably complex audit, it is advisable to develop a
  customised audit template for the project in question, based on
  the default template provided by this skill.
- Check if there is a custom fulfilment audit template (see below);
  if not, use the one in `assets`.
- Copy the template verbatim and edit it section by section.
- For Phase A, work through each story in turn; record findings
  against the capabilities it cites.
- For Phase B, work through each capability in scope; record the
  covering story (or stories). Anything not covered goes to the
  orphan candidates table.
- Bring all orphan capabilities to the user for disposition before
  closing the audit.

## Notes

- Generally this is a full audit unless otherwise specified. For a
  full audit, DO NOT look at older audit docs to work incrementally
  — start fresh.
- This audit reads stories and specs only. If during the audit you
  find yourself wanting to run the code or click through the
  product, you have crossed into acceptance-test territory; switch
  skills.

## Skill artefacts

- **Default audit template**: `assets/fulfilment-audit-task-template.md`
