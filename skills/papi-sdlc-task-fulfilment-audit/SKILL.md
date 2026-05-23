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

Before the two phases, the audit MUST run a lightweight structural
pre-pass:

- **Pre-pass — Template conformance:** check that each in-scope user
  story conforms to `papi-sdlc-user-stories`' `user-story-template.md`,
  the user-stories index conforms to `user-stories-template.md`, and
  each component spec referenced by a cited or in-scope capability
  conforms to `papi-sdlc-component-specification`'s
  `component-specification-template.md`. Record any structural drift
  (missing sections, renamed fields, stale guidance, undocumented
  additions) as findings with a disposition: **update document** /
  **update template** / **accept with note**. This pass separates
  "format outdated" from "content wrong" before Phase A goes deeper.

A fulfilment audit MUST then run in two directions and reconcile the
results:

- **Phase A — Top-down (story → capability):** for each user story in
  scope, take the `**Capabilities:**` field (and any in-body
  references) and check:
  - every cited capability ID exists in the relevant component spec
  - every cited capability is **user-facing** (its `**Users:**` field
    names one or more user-story role names; `internal` and
    `composition` capabilities MUST NOT be cited directly by stories)
  - the story's `**Role:**` appears in the `**Users:**` field of each
    cited capability
  - the cited capabilities are plausibly aligned with what the story
    asks for
  - the union of cited capabilities is sufficient to cover the
    story's narrative and acceptance criteria
  - Classify the story as: **Covered**, **Partial**, **Missing**, or
    **Misaligned**.

- **Phase B — Bottom-up (capability → story):** Phase B sweeps only
  **user-facing capabilities**, i.e. those whose `**Users:**` field
  names at least one role (capabilities marked `internal` or
  `composition` are out of scope for this audit and belong in the
  Excluded list).

  For each user-facing capability in scope, find the user story (or
  stories) that cite it. Check:
  - the capability is cited by at least one in-scope story
  - for every role named in the capability's `**Users:**` field,
    at least one citing story has that role in its `**Role:**` field

  Capabilities failing the first check are **orphan candidates**.
  Capabilities failing only the second check are **role-coverage
  gaps** (the capability is in use, but not for every role it claims
  to serve).

  An orphan capability is one of two kinds:
  - *scope creep* — the capability exists but no user wants it
  - *missing story* — a user does want it, but the story hasn't
    been written

  (A capability that is genuinely not user-facing should never reach
  this list — if one does, the finding is *mismarked user-facing*:
  update the spec to mark it `internal` or `composition`.)

- **Phase C — Reconciliation:** merge Phase A gaps, Phase B orphan
  capabilities, and Phase B role-coverage gaps into a single
  findings list. For each finding, record the agreed disposition:
  - **Update stories** (add, change, fix capability links, add a
    missing story for a role)
  - **Update specs** (add, change, or remove capabilities; mark a
    capability `internal` or `composition`; correct a `**Users:**`
    role list)
  - **Accept with note** (a deliberate, recorded exception)

Running only Phase A is a CRITICAL FAILURE: it lets user-facing
capabilities that serve no story persist in the specs unchallenged.
Both phases must be evidenced in the report.

### Orphan candidate handling

Every Phase B orphan capability MUST be brought to the user for a
disposition decision before the audit closes. Do NOT auto-classify
the orphan kind — the choice between scope creep and missing story
is a strategic call that belongs with the user.

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
