---
name: papi-sdlc-task-acceptance-test
description: Plan and perform user-acceptance testing for user stories - exercise each story end-to-end through the real user interface in the appropriate role, with evidence. [PAPI SDLC]
---

# SDLC Task - Acceptance Test

## Purpose

An acceptance test exercises each user story through the **real
user-facing interface** (UI, CLI, API, document, etc.) in the named
role, and records evidence that the story can in fact be performed
end-to-end.

This is **not an audit**. PAPI audits (charter, fulfilment, compliance)
examine artefacts for drift between adjacent layers. An acceptance
test instead **performs** the system: it asks whether the experience
the user is supposed to get actually exists and works.

It typically runs **after** a successful fulfilment audit (stories
↔ capabilities aligned) and a successful compliance audit
(capabilities ↔ code aligned). If those audits have not passed,
acceptance testing usually has nothing useful to say yet.

**This needs the PAPI long task skill.**

## Role discipline

For each user story, the tester MUST assume the matching role(s)
and attempt to perform the story **only through the interfaces and
capabilities that would be available to that role in the real
world**.

This means:

- MUST use the production-equivalent interface (the actual UI, CLI,
  API, document, etc.) rather than internal tools, debug shims, or
  back-channel commands.
- MUST NOT consult implementation code, internal documents or other
  artefacts that the role would not normally have occasion to see.
- MUST reason in good faith whether the role would have the
  knowledge, context and access needed to discover and perform the
  steps unaided.
- Human assistance is allowable when the agent cannot physically
  reach the interface (e.g. a human clicks while the agent watches
  via screenshots); the role-discipline rules still apply.

If the role discipline is breached during a test, the test does NOT
count as passing and the breach MUST be recorded.

## Evidence

Each story attempt MUST produce evidence sufficient for an
independent reader to judge the result. Acceptable evidence
includes:

- Screenshots or screen recordings of the relevant UI flow
- Terminal transcripts for CLI flows
- Request/response captures for API flows
- Demo recordings
- Witness sign-off from a human performing or observing the flow

The classification of each story is:

- **Pass** — story performed end-to-end in role with evidence.
- **Partial** — story partially performed; specific steps blocked
  or unsatisfactory; evidence shows where.
- **Fail** — story cannot be performed in role.
- **Blocked** — cannot test (e.g., environment unavailable);
  explain.

## Relation to audits

- **Charter / fulfilment / compliance audits** check that documents
  and code line up. They do not run the system.
- **Acceptance test** runs the system. It is downstream of all
  three audits.
- A passing audit set with failing acceptance tests is meaningful:
  it suggests the alignment is correct on paper but the execution
  is broken somewhere outside the audited mappings (e.g.,
  integration, environment, UX).
- A passing acceptance test with failing audits is suspicious: it
  may indicate the audits found drift but the drift didn't (yet)
  break the user experience — the drift still needs resolving.

## Dependencies

Reading these skills is REQUIRED to understand and execute this
skill:

- PAPI skill `papi-tasks-understand`
- PAPI skill `papi-templates-understand`
- PAPI skill `papi-sdlc-user-stories`

Read these as needed:

- PAPI skill `papi-sdlc-task-fulfilment-audit` (typically run before)
- PAPI skill `papi-sdlc-task-compliance-audit` (typically run before)

## Actions

- Check if there is a custom acceptance-test template for the project;
  if not, use the one in `assets`.
- Copy the template verbatim and edit it section by section.
- For each story, identify the role(s) and the real interface(s)
  available to that role.
- Perform the story in role; capture evidence.
- Record Pass / Partial / Fail / Blocked with evidence and notes.

## Notes

- An acceptance test is NOT a substitute for automated unit,
  integration or end-to-end tests in the dev pipeline. It is a
  human-meaningful demonstration that the user-visible promise
  actually holds.
- If during testing you find yourself reading code or specs to
  decide whether something should work, stop: you are no longer
  doing acceptance testing. Either complete the test in role with
  what is visible, or switch to a fulfilment or compliance audit.

## Skill artefacts

- **Default acceptance-test template**: `assets/acceptance-test-task-template.md`
