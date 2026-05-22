---
name: papi-sdlc-task-compliance-audit
description: Create or work with compliance audit tasks to verify implementations match specifications. [PAPI SDLC]
---

# SDLC Task - Compliance Audit

## Purpose

This compliance audit verifies that, within the provided scope (e.g., a release):
- the implementation matches the relevant capabilities in the component specifications
- all code is properly linked to capabilities
- all capabilities are linked to some code
- the capability DAG is valid
- any test-related non-functional constraints declared in the spec are met

**CRITICAL:** No component specification can be considered 'completed' until a compliance audit has been conducted and passed.

**This needs the PAPI long task skill.**

## This audit examines; it does not execute

This audit *examines* artefacts (specs, code, links, related docs and
config). It does NOT execute tests, demos, or any normal dev/release
pipeline step. Whether the test suite currently passes is a dev/release
workflow concern, not a compliance concern.

Test code may be *consulted as an investigative aid* when it helps
clarify what the implementation does or what its public contract looks
like. It is not a compliance target in its own right. If a component
spec mandates particular tests or coverage as a non-functional
constraint, that constraint is checked by the standard non-functional
constraints step — by examining for existence and linkage, not by
execution.

## Two phases are mandatory

A compliance audit MUST run in two directions and reconcile the results:

- **Phase A — Top-down (spec → code):** for each capability in scope, find
  its implementation, verify the contract against the spec, and confirm
  the code is linked back to the capability ID.
- **Phase B — Bottom-up (code → spec):** enumerate every artefact within
  the component's scope that is — or would normally be — under version
  control (source, tests, scripts, config, CI/CD, infra-as-code,
  dependency manifests, data assets, static assets, docs, meta files);
  for each, identify the covering capability ID. Anything with no
  covering capability is an **orphan candidate**. Anything intentionally
  excluded from the sweep MUST be listed with a stated reason.
- **Phase C — Reconciliation:** merge Phase A gaps and Phase B orphan
  candidates into a single findings list.

Running only Phase A is a CRITICAL FAILURE: it lets dead or undocumented
code persist indefinitely. Both phases must be evidenced in the report.

### Orphan candidate handling

Every Phase B orphan candidate MUST be brought to the user for a
disposition decision before the audit closes. Do NOT auto-classify.
Record the decision and rationale against each candidate in the report.

## Dependencies

Reading these skills is REQUIRED to understand and execute this skill:

- PAPI skill `papi-sdlc-validate-capabilities-dag`
- PAPI skill `papi-tasks-understand`
- PAPI skill `papi-templates-understand`

## Action

- Copy and use the template (provided here under `assets`) if appropriate.
- the audit REQUIRES that you verify that implementation matches
  specification for every capability in scope
  - evidence types appropriate to examination include: capability links
    found in code (comments / docstrings / metadata), spec-to-code
    mapping tables, code excerpts showing the contract is honoured,
    references to existing CI / release records where execution
    evidence already lives
  - do NOT run tests, demos, or pipelines as part of this audit
  - it is a CRITICAL FAILURE if the spec-to-code verification is not done
- The audit MUST include a capabilities DAG validation step (using the skill). A compliance audit cannot
  pass if the DAG has cycles, orphans, or invalid references.
- Generally, this is a full audit, unless otherwise specified.
  - For a full audit, DO NOT look at older audit docs to work
    incrementally—start from scratch.
- An audit may be a large task, and sub-tasks (even a tree) may be warranted
  - The output doc (from the template) can also be made into parts if it is anticipated to get too long
    - Always follow PAPI and copy the template structure and sections, and then edit section-by-section, even if you split it into parts.
    - You may need to skeleton the components in the output doc(s) first, and then flesh them out section by section

## Outputs

- some artefact produced during the audit may be valuable to maintain for future audits (scripts, test data etc.)
  - if so, these shoudl be tracked a PAPI components

## Skill artefacts

- **Audit template**: `assets/compliance-audit-task-template.md`

