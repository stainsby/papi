[Use this template for sprint tasks — bounded cycles of related development
work (fixes, features, infrastructure) that are planned, executed, verified,
and closed as a unit.]

[This template is based on `development-task-template.md` with sprint-specific
sections for sub-task management, verification gates, and post-completion
reflection. It omits the SDLC Workflow Reminder and Testing Strategy sections
because those belong in individual sub-task documents, not the sprint parent.]

# Task: SPRINT-NNN — [Sprint title]

**External Tracking:** [e.g., JIRA epic, GitHub milestone, or "None"]
**Impacted Components:** [List component codes affected]
**Status:** [Planned | Active | Completed]
**Created:** [Date]

## Synopsis

[One-line summary of what this sprint delivers.]

## Template

This document was based on the PAPI SDLC template: `sprint-task-template.md`.

## Status

[Planned | Active | Completed | Abandoned.
If blocked, paused, or abandoned, briefly note why.]

## Subordinate and dependent tasks

| Sub-task | Document | Status | Description |
|---|---|---|---|
| SUB-01 | [link](link) | [status] | [description] |
| SUB-02 | [link](link) | [status] | [description] |

[Sequencing notes: which sub-tasks depend on others, which can be parallelised.]

## Entry Criteria

[Verify these before starting execution:]

- [ ] Prior sprint (if any) is completed or not blocking
- [ ] No uncommitted changes in files affected by this sprint
- [ ] All prerequisite specs are current
- [ ] Sub-task documents created with appropriate templates

## Context & Scope

[Why this sprint exists, what it addresses, and what it will NOT cover.
Include the trigger: audit findings, manual testing session, feature request, etc.]

## Goals

[What this sprint delivers as a coherent unit.]

## Who

- **Accountable:** [human]
- **Contributors:** [AI and/or humans]

## References

[Primary sources of truth: specs, user stories, audit reports, etc.]

## Integration Boundaries

[List every communication boundary between components that is affected by
this sprint's work. For each boundary, note whether an automated test
exercises the real round trip.]

[Examples of boundaries: postMessage iframe protocol, HTTP API calls,
FFI bridges, IPC channels, file-based data exchange.]

| Boundary | Components | Automated real round-trip test? |
|---|---|---|
| [e.g. postMessage] | [UI <-> MCP host] | [Yes: e2e-integration.spec.mjs / No: gap] |

## Plan

### Approach

[High-level description of how sub-tasks will be sequenced and executed.]

### Success indicators

[Observable outcomes that confirm the sprint achieved its goals.]

## Implementation

### Actions taken

[Summary of work done. Can reference individual sub-task documents.]

### Issues

[Problems, risks, or deviations encountered during execution.]

## Sprint Completion Checklist

[ALL of the following must hold before marking this sprint complete.]

### Gate 1 — Automated Tests

- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] All browser/E2E mock-based tests pass
- [ ] All browser/E2E real-server tests pass (if applicable)

### Gate 2 — Manual Smoke Test

[Required if the sprint includes UI or user-facing changes.]

- [ ] Manual walkthrough performed using the actual user interface
- [ ] Walkthrough covers: [list the specific workflows tested]
- [ ] All reported bugs verified as resolved
- [ ] No new issues observed during walkthrough

### Gate 3 — Capabilities DAG Validation

[Use the `papi-sdlc-validate-capabilities-dag` skill.]

- [ ] DAG validation script run against the project's component specs directory
- [ ] Zero issues reported (no cycles, orphans, or invalid references)

### Gate 4 — Compliance Spot-Check

[This is a lightweight check, not a full compliance audit. If significant
drift is found, create a full audit task using the
`papi-sdlc-task-compliance-audit` skill.]

- [ ] Each modified component specification is in sync with the code
- [ ] Capability codes in new/modified code are correct
- [ ] [If significant drift found: compliance audit task created as follow-on]

### Gate 5 — Integration Boundary Check

- [ ] Every boundary listed in the Integration Boundaries section has at
      least one automated test exercising the real round trip
- [ ] [If gaps remain: follow-on tasks created]

## Reflect

[Complete after the sprint is done.]

### What happened

[What actually occurred, including any deviations from the plan.]

### Interpretation

[What this means in relation to the goals and assumptions.]

### Learning

[What is now better understood.]

## Improvement

### Outcomes

[Brief statement of overall outcomes.]

### Decisions

[Decisions made as a result of this sprint.]

### Next steps

[Follow-on work, including any audits to schedule.]

### Process improvement

[Did this sprint reveal gaps in testing, specification, or process?
Should any templates, skills, or instructions be updated?
Were there recurring issues that suggest a systemic problem?
If none identified, state "No changes identified".]
