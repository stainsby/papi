[TO CREATE A NEW FULFILMENT AUDIT TASK: **COPY** THIS TEMPLATE, THEN **EDIT** THE COPY
**ONE SECTION AT A TIME**, FOLLOWING THE INSTRUCTIONS IN EACH SECTION]

[Use this template to assess how well implemented capabilities satisfy user stories.]

[Use this template only when appropriate:
* If a more specific template exists, use that instead.
* If no suitable template exists, propose creating a new one or updating an
  existing one.
* If this template seems obsolete or not useful, propose deleting it.]

[This template is a guideline:
* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that may
  indicate a need for a new/updated template or process change; record that
  under *Process improvement* in the *Improvement* section.]

# Task: Fulfilment Audit - [Release/Scope Name]

**Audit Scope:** [Release milestone, e.g., "MVP" or "Edition 2", OR a subset of stories]
**Audit Date:** YYYY-MM-DD
**Status:** [Proposed, In Progress, Completed]

## Synopsis

[One-line summary of what this audit is verifying]

## Template

This document was based on the PAPI SDLC template: `fulfilment-audit-task-template.md`.

## Status

[Current status of this audit task.
Examples: Proposed, In Progress, Completed, Failed, Abandoned.]

## Purpose

See the skill.

## Audit Scope

### Stories to Audit

[List the user stories in scope.]

**Stories in scope:**

[List the story IDs and titles. If auditing all stories, state "All stories in the catalogue".]

- US-XX: [Story title]
- US-YY: [Story title]
- ...

### Release Context

[Which release milestone does this audit relate to? This determines which
capabilities are expected to be available and which stories may have known
MVP-scope limitations.]

**Release:** [e.g., `PROJECT.RELEASE.MVP`]
**Release Spec:** [Path to release spec]

## Parent task

[OMIT unless this is a sub-task of a larger audit or release task]

## Tasks this task depends on

[List compliance audits or implementation tasks that should be complete first]

- [Compliance audit task, if one exists]
- [Implementation tasks for capabilities referenced by stories]

## Subordinate and dependent tasks

[OMIT unless other tasks depend on this being done first]

## Required reading

* Architectural overview
* Release specification [if tied to a release]
* Component specifications for capabilities referenced by stories

## Context & Scope

This audit takes the user's perspective: for each story, can the described
workflow actually be performed end-to-end using the current implementation?

The audit examines:

1. **Functional coverage:** Does the implementation provide the behaviour the story describes?
2. **Test coverage:** Are there tests that verify the story's acceptance criteria?
3. **End-to-end viability:** Can the story be exercised through the actual user interface (UI, CLI, API, etc.), not just via unit tests?

This audit does NOT:
- Re-verify implementation correctness (that is the compliance audit's job)
- Evaluate code quality or architecture
- Run the automated tests

## Goals

- Assess fulfilment status for each story in scope
- Document gaps between story requirements and current implementation

## Who

[Include things like: who is accountable for this audit, who contributed
(human and/or model)]

## References

- [User stories](path/to/USER_STORIES.md)
- [Release spec](path/to/RELEASE/MILESTONE.md) - defining scope for
  this audit [If this audit is tied to a specific release.]

## Audit Plan

### Audit Procedure

For each story in scope:

- **Read the story** — understand the actor, goal, and outcome
- **Check acceptance criteria** — list the specific criteria that must hold
- **End-to-end verification:**
   - Where feasible, exercise the story through the actual user interface (GUI, CLI, API, etc.)
   - External dependencies might be unavailable (or unusable because of protocol), and may require the use of realistic mocked interfaces (mocked APIs/services, etc.)
   - For stories that cannot be automated and require human interaction (e.g., AI-guided workflows), guide a a manual walkthrough
- **Classify the story:** Fully Met, Partially Met, or Not Met. Document reason if not fully met.

### Special Considerations

[Note any stories that require special handling
* Stories with known limitations due to release scope (annotated in the story catalogue)
* Stories that depend on external systems not available in the test environment]

## Audit Execution

### Per-Story Results

[For each story, document the assessment. Use the structure below.]

#### US-XX: [Story Title]

**Status:** [Fully Met / Partially Met / Not Met]

**Acceptance Criteria Check:**

| Criterion | Met? | Evidence |
|-----------|------|----------|
| [criterion from story] | Yes/No/Partial | [test name, manual observation, or gap note] |
| ... | ... | ... |

**Functional Coverage:** [Brief assessment — does the implementation provide what the story describes?]

**Test Coverage:** [Brief assessment — are there tests for the acceptance criteria?]

**End-to-End Viability:** [Brief assessment — can this be exercised through the real interface?]

**Gap Notes:** [Specific gaps, or "None"]

[Repeat for each story in scope]

## Audit Report

### Summary

**Audit Date:** YYYY-MM-DD
**Auditor:** [Name/ID]
**Scope:** [Summary of what was audited]
**Release:** [Release milestone]

**Statistics:**
- Stories Audited: X
- Fully Met: A
- Partially Met: B
- Not Met: C
- Coverage: A/X (percentage)

**Conclusion:**
[Overall assessment. Are we ready to ship this release from a story-fulfilment
perspective? What are the critical gaps?]

### Fulfilment Status Summary

[This table should be copied back into the USER_STORIES component spec to
update the fulfilment status table there.]

| Story | Title | Status | Gap Notes |
|-------|-------|--------|-----------|
| US-XX | [title] | [status] | [gaps or "None"] |
| ... | ... | ... | ... |

### Critical Gaps

[List any stories that are Not Met or Partially Met with significant gaps.
For each, note whether the gap requires:
* Implementation work (create a follow-up task)
* Story revision (the story needs updating)
* Acceptance as a known limitation (document and defer)]

### Recommendations

1. [Priority recommendation]
2. [Priority recommendation]
3. ...

### Next Steps

[What needs to happen as a result of this audit?
* Create implementation tasks for gaps
* Update stories if requirements have changed
* Update the USER_STORIES fulfilment status table
* Schedule re-audit after gaps are addressed
* Proceed with release if coverage is acceptable]

## Improvement

### Outcomes

[Brief statement of the overall outcomes of this audit.]

### Decisions

[Any decisions being made as a result of this audit.]

### Process improvement

[Note whether this audit suggests changes to:
* USER_STORIES component or story format
* Fulfilment audit task template
* Relationship between compliance audits and fulfilment audits
* Testing strategies
* Story-writing practices

If none, state "No changes identified".]

### Future Enhancements

[Ideas for improving the fulfilment audit process.]

## Completion Checklist

[Before marking this audit task complete, verify ALL of the following:]

- [ ] All stories in scope have been assessed
- [ ] Each story has a clear Fully Met / Partially Met / Not Met classification
- [ ] Gap notes are specific and actionable for all non-Fully-Met stories
- [ ] End-to-end verification has been performed where feasible
- [ ] Follow-up tasks have been created for critical gaps
- [ ] Audit report is complete with summary and recommendations

## Addendum

[Optional additional information, references, resources, notes, ...]
