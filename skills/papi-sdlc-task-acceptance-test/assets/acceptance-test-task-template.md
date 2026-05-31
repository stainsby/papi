# Task: Acceptance Test - [Scope Name]

[TO CREATE A NEW ACCEPTANCE-TEST TASK: **COPY** THIS TEMPLATE, THEN **EDIT** THE COPY
**ONE SECTION AT A TIME**, FOLLOWING THE INSTRUCTIONS IN EACH SECTION]

[Use this template to plan and execute acceptance testing of user
stories through the **real user interface** in the appropriate role,
with evidence. This is NOT an audit. It performs the system; it does
not examine artefacts.]

[Use this template only when appropriate:

* If a more specific template exists, use that instead.
* If no suitable template exists, propose creating a new one or
  updating an existing one.
* If this template seems obsolete or not useful, propose deleting it.]

[This template is derived from `basic-task-template.md`.]

[This template is a guideline:

* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that
  may indicate a need for a new/updated template or process change;
  record that under *Process improvement* in the *Improvement* section.]

**Test Scope:** [Which stories / which release / which role(s)]
**Test Date:** YYYY-MM-DD
**Status:** [Proposed, In Progress, Completed, Failed]

## Synopsis

[One-line summary of what this acceptance test is exercising.]

## Template

This document was based on the PAPI SDLC template: `acceptance-test-task-template.md`.

## Status

[Current status of this task.
Examples: Proposed, In Progress, Completed, Failed, Abandoned.]

## Purpose

See the skill.

## Test Scope

[Define what is being acceptance-tested. Typically:

* All current user stories in their named roles
* A specific release / milestone slice of stories
* A specific role or persona's slice of stories]

### Stories in Scope

[List the user stories included in this acceptance test, with IDs and roles.]

* **US-XX** - [Story title] - Role: [role name]
* **US-YY** - [Story title] - Role: [role name]

## Parent task

[OMIT unless this is a sub-task of a larger acceptance-test campaign.]

## Tasks this task depends on

[Acceptance testing typically requires the fulfilment and compliance
audits to have passed. List them here if recently performed.]

* [Task: Fulfilment audit covering these stories]
* [Task: Compliance audit covering the supporting capabilities]
* [Task: Implementation tasks for the relevant capabilities]

## Subordinate and dependent tasks

[OMIT unless other tasks depend on this one being done first.]

## Required reading

* Each in-scope user story (narrative + acceptance criteria)
* Any role / persona definitions referenced by the stories
* End-user-facing documentation that the role would have access to

[Do NOT pre-read implementation code or internal specifications.
That breaches role discipline.]

## Context & Scope

This acceptance test verifies, through the real user interface, that:

1. Each story can be performed end-to-end by its named role.
2. The role has the knowledge, context and access required.
3. The experience is acceptable (not just possible).

This test is NOT:

* An audit of stories vs. capabilities (that is the fulfilment audit).
* An audit of capabilities vs. code (that is the compliance audit).
* A substitute for automated tests in the dev pipeline.

## Goals

* Produce an acceptance test report with one Pass / Partial / Fail /
  Blocked result per story, each backed by evidence.
* Surface any role-discipline breaches.
* Identify any blocking issues preventing release sign-off.

## Who

[Who is accountable; who performed each test; whether a human
assisted the agent in reaching the interface.]

## References

### User Stories

* [USER_STORIES component spec](path/to/user_stories.md)
* [Story US-XX](path/to/story/or/anchor)
* ...

### Interfaces Used

[List the actual user-facing interfaces exercised — URLs of the UI,
CLI invocations, API endpoints, document locations, etc.]

* [Production-equivalent UI URL]
* [CLI binary and version]
* [API base URL]

## Test Plan

### Role Discipline

[Restate the role-discipline rules from the skill: only the
interfaces, knowledge and documents that the role would have in the
real world. Note any deliberate, recorded exceptions (e.g., a human
performs clicks at the agent's direction).]

### Evidence Standard

[State what evidence will be captured for each story attempt.
Examples: screenshots stored at `./evidence/US-XX/`, terminal
transcripts, request/response captures, demo recordings, witness
sign-off.]

### Per-Story Procedure

For each story in scope:

1. **Identify role and interface**
   * [ ] Note the named role.
   * [ ] Note the real-world interface available to that role.

2. **Perform the story in role**
   * [ ] Attempt each acceptance criterion through the named interface.
   * [ ] Do NOT consult code, specs, or internal artefacts.
   * [ ] Capture evidence at each step.

3. **Classify the result**
   * [ ] **Pass** — story performed end-to-end with evidence.
   * [ ] **Partial** — some steps performed; specific blocker(s) noted.
   * [ ] **Fail** — story cannot be performed in role.
   * [ ] **Blocked** — could not test (environment, access, ...); explain.

4. **Record any role-discipline breaches**
   * [ ] Note any moment the tester stepped outside the role.
   * [ ] A breach means the story does NOT count as Pass.

## Test Execution

### Per-Story Results

| Story | Title | Role | Interface | Result | Evidence | Notes |
|-------|-------|------|-----------|--------|----------|-------|
| US-XX | [title] | [role] | [UI/CLI/API/doc] | Pass / Partial / Fail / Blocked | [link or path] | [notes] |
| US-YY | ... | ... | ... | ... | ... | ... |

### Role-Discipline Breaches

[List any cases where the tester used knowledge, access or interfaces
that the role would not have. An empty list is fine; a missing list
is not.]

| Story | Breach | Why it happened | Impact on result |
|-------|--------|-----------------|------------------|
| US-XX | [desc] | [why] | [downgrade Pass → Partial, etc.] |

## Test Report

### Executive Summary

**Test Date:** YYYY-MM-DD
**Tester:** [Name/ID]
**Scope:** [Summary of what was tested]
**Overall Result:** [PASS / FAIL]

**Statistics:**
* Stories Tested: X
* Pass: A
* Partial: B
* Fail: C
* Blocked: D
* Role-Discipline Breaches: E

**Conclusion:**
[Is the audited scope ready for release from a user-experience
standpoint? What blockers remain?]

### Critical Issues

[List Fail or Partial stories with significant blockers. For each,
note whether the fix needs:

* Implementation work (create a follow-up task)
* Spec change (signal to a future fulfilment or compliance audit)
* Story revision (story does not match what users actually need)
* Acceptance as a known limitation (document and defer)]

### Recommendations

1. [Priority recommendation]
2. [Priority recommendation]
3. ...

### Next Steps

[What needs to happen as a result of this acceptance test?

* Create implementation tasks for blockers
* Update stories if the test revealed they were wrong
* Schedule a re-test after fixes
* Proceed with release if results are acceptable]

## Improvement

### Outcomes

[Brief statement of the overall outcomes of this test.]

### Decisions

[Any decisions being made as a result of this test.]

### Process improvement

[Note whether this test suggests changes to:

* Story format or acceptance-criteria style
* Role / persona definitions
* This acceptance-test task template
* The relationship between audits and acceptance testing

If none, state "No changes identified".]

### Future Enhancements

[Ideas for improving the acceptance-test process.]

## Completion Checklist

[Before marking this task complete, verify ALL of the following:]

* [ ] All stories in scope have been classified (Pass / Partial / Fail / Blocked)
* [ ] Evidence has been captured and linked for every attempted story
* [ ] All role-discipline breaches recorded (or list explicitly empty)
* [ ] Notes for Partial and Fail results are specific and actionable
* [ ] Follow-up tasks created for blockers
* [ ] Report is complete with executive summary and recommendations

## Addendum

[Optional additional information, references, resources, notes, ...]
