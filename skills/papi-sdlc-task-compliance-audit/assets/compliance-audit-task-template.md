[TO CREATE A NEW COMPLIANCE AUDIT TASK: **COPY** THIS TEMPLATE, THEN **EDIT** THE COPY
**ONE SECTION AT A TIME**, FOLLOWING THE INSTRUCTIONS IN EACH SECTION]

[Use this template to verify that implemented components match their specifications.
This is a separate consideration from testing: code and other component
artefacts must be examined in detail to determine if they at least attempt
to implement the capabilities of the specifications.]

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

# Task: Compliance Audit - [Component/Scope Name]

**Audit Scope:** [Single component code OR multiple component codes OR entire system]  
**Audit Date:** YYYY-MM-DD  
**Status:** [Proposed, In Progress, Completed, Failed]

## Synopsis

[One-line summary of what this audit is verifying]

## Template

This document was based on the PAPI SDLC template: `compliance-audit-task-template.md`.

## Status

[Current status of this audit task.
Examples: Proposed, In Progress, Completed, Failed, Abandoned.
If the audit fails, note critical issues preventing completion.]

## Purpose

See the skill.

## Audit Scope

[Define what is being audited. This can be:
* A single component and all its capabilities
* Multiple related components
* An entire system/subsystem
* External dependencies only
* A specific edition of a component specification]

**IMPORTANT: Task Organization**

[If auditing MANY components (say more than a approx. a dozen, or more for simple components), break the work down:

* Create ONE parent audit task that coordinates the overall audit
* Create separate sub-audit tasks for each component or logical group of components
* Each sub-task should reference the parent task
* The parent task tracks overall progress and consolidates findings
* This keeps individual audit tasks manageable and focused

Otherwise, a single audit task is sufficient.]

### Components to Audit

[List all components included in this audit scope]

- **CMP.XXX.YYY** - [Component Name] - Edition [N]
- **CMP.AAA.BBB** - [Component Name] - Edition [N]

### External Components to Audit (Optional)

[List any external components/libraries to audit for version compliance]

- **X.LIB.NAME** - [Library Name] - Specified version vs Latest stable

## Parent task

[OMIT unless this is a sub-audit of a larger audit task]

## Tasks this task depends on

[List implementation tasks that must be complete before audit can proceed]

- [Task: Implementation of CMP.XXX.YYY]
- [Task: Testing of CMP.XXX.YYY]

## Subordinate and dependent tasks

[OMIT unless other audits or tasks depend on this one being done first]

## Required reading

* All component specifications being audited
* All relevant implementation code
* Test suites (consult only as an investigative aid — do not execute)

## Context & Scope

This audit ensures implementation integrity by:
1. Verifying all claimed capabilities are actually implemented
2. Checking that implementations match specification contracts
3. Confirming capability code linkage in source code
4. (Optional) Ensuring external dependencies are current

This audit examines artefacts. It does NOT:
- Execute tests, demos, or any normal dev/release pipeline step
  (test execution is a dev/release workflow concern, not a compliance one)
- Evaluate code quality or style (unless specified as non-functional constraint)
- Test performance unless specified in component constraints
- Review design decisions (those belong in spec reviews)

## Goals

- Produce a compliance audit report documenting all findings
- Identify any gaps between specification and implementation
- Confirm component can be marked as 'completed' in its edition table
- (For external components) Document version status and any upgrade considerations

## Who

[Include things like: who is accountable for this audit, who contributed
(human and/or model)]

## References

### Component Specifications

[Link to all component specifications being audited, noting the specific edition]

- [CMP.XXX.YYY Specification](path/to/spec.md) - Edition N
- [CMP.AAA.BBB Specification](path/to/spec.md) - Edition N

### Implementation Locations

[Link to implementation code locations]

- [Component XXX.YYY Implementation](path/to/code/)
- [Component AAA.BBB Implementation](path/to/code/)

### Test Locations (reference only)

[Link to test suite locations. Tests are not a compliance target; these
links exist so the auditor can consult test code as an investigative
aid and so test files appear in the Phase B artefact sweep.]

- [Component XXX.YYY Tests](path/to/tests/)
- [Component AAA.BBB Tests](path/to/tests/)

## Audit Plan

### Alignment

[This audit ensures that implementation, tests, and specifications are
perfectly aligned. Any discrepancies must be documented and either:
1. Implementation updated to match specification, or
2. Specification updated to reflect intentional changes (creating new edition)]

### Audit Procedure

This audit runs in two directions and reconciles the results. Both
phases are MANDATORY (see the `papi-sdlc-task-compliance-audit` skill).

**This audit examines; it does not execute.** Do not run tests, demos
or pipelines as part of this audit. Test code may be consulted as an
investigative aid only.

#### Pre-pass — Template conformance

Before Phase A, do a lightweight structural check of every component
spec referenced by an in-scope capability against
`component-specification-template.md`. Record any structural drift
(missing sections, renamed fields, stale guidance, undocumented
additions) as findings with a disposition: update document / update
template / accept with note. Running this first separates "format
outdated" from "content wrong" before Phase A goes deeper.

#### Phase A — Top-down (spec → code)

For each component in scope:

1. **Specification Review**
   - [ ] Read complete component specification for edition being audited
   - [ ] Extract all capability codes and their interface contracts
   - [ ] Note all non-functional constraints

2. **Capability Implementation Verification**
   For each capability:
   - [ ] Locate implementation in source code
   - [ ] Verify code references capability code (in comments, docstrings, or metadata)
   - [ ] Check interface matches specification (inputs, outputs, preconditions, postconditions)
   - [ ] Verify error handling matches specification
   - [ ] Confirm implementation satisfies described functionality

3. **Capability Matrix Verification**
   - [ ] Verify all dependencies listed in capability matrix exist
   - [ ] Check that consumed capabilities are actually used in implementation
   - [ ] Confirm no unlisted dependencies exist

4. **Capabilities DAG Validation**
   - [ ] Run the DAG validation script (see `papi-sdlc-validate-capabilities-dag` skill) against the project's component specifications directory
   - [ ] Confirm zero issues: no cycles, no orphans, no invalid references
   - [ ] If issues found: resolve in the affected specification files before proceeding

5. **Non-Functional Constraints Verification**
   - [ ] Verify technology constraints are met
   - [ ] Check performance constraints (examine for evidence; do not run)
   - [ ] Verify security constraints
   - [ ] Confirm compatibility constraints
   - [ ] If the spec mandates test-coverage or test-kind constraints,
         verify by examining for existence and linkage (do not execute)

6. **External Dependencies Audit** (Optional)
   For each external component:
   - [ ] Identify current version in use
   - [ ] Look up latest stable version (MUST SEARCH, not from memory)
   - [ ] Document version discrepancy if any
   - [ ] Explain reason for not using latest (if applicable)
   - [ ] Note any security vulnerabilities in current version

#### Phase B — Bottom-up (code → spec)

Enumerate the in-scope artefact surface and map each unit back to a
covering capability. Anything with no covering capability is an
**orphan candidate** — do NOT auto-classify; bring each to the user.

**In-scope artefacts:** every file within the component's scope that is
— or would normally be — under version control, regardless of kind.

1. **Enumerate the artefact surface** (non-exhaustive prompt list)
   - [ ] Source files / modules / public functions / classes
   - [ ] Tests (unit, integration, E2E, fixtures, test data)
   - [ ] Scripts (build, ops, migration, utility, dev tooling)
   - [ ] Config and schema files (app config, lint/format, editor,
         environment templates)
   - [ ] CI/CD definitions (workflow files, pipeline configs)
   - [ ] Infrastructure-as-code (Terraform, K8s manifests, Docker/Compose)
   - [ ] Dependency manifests and lockfiles
   - [ ] Data assets (seed data, sample inputs, fixtures, migration output)
   - [ ] Static assets (images, fonts, media, icons)
   - [ ] Component-level docs (READMEs, design notes, ADRs, changelogs)
   - [ ] Licence, contributor and meta files
   - [ ] Any other in-scope tracked file not covered above

2. **Map each unit to a covering capability**
   - [ ] Capability ID found in code/comments/metadata: record it
   - [ ] No capability ID found: record as **orphan candidate**

3. **Capture orphan candidates**
   - [ ] List every orphan candidate with location + brief description
   - [ ] For each, propose a likely disposition (remove, cover with new
         capability/spec edition, accept as known) — but do NOT decide
   - [ ] Bring the list to the user for disposition decisions

4. **Excluded artefacts**
   - [ ] List every artefact (or artefact pattern) intentionally
         excluded from the sweep, with a stated reason (e.g., vendored
         third-party code covered by the external-dependencies audit,
         generated files reproducible from sources). An empty list is
         fine; a missing list is not.

#### Phase C — Reconciliation

- [ ] Merge Phase A gaps (specified-but-missing/incorrect) and Phase B
      orphan candidates (present-but-unspecified) into one findings list
- [ ] Confirm every orphan candidate has a recorded user disposition
- [ ] Translate findings into follow-up tasks or spec/edition updates

### Audit Report Structure

The audit will produce a single document with:

1. **Executive Summary**
   - Overall pass/fail status
   - Critical issues count
   - Warning issues count
   - Recommendations

2. **Component-by-Capability Findings**
   For each capability:
   - Compliance status (Pass/Fail/Partial)
   - Evidence of implementation
   - Issues found (if any)
   - Investigative notes (e.g., test code consulted) — optional

3. **Issues Log**
   - Issue ID
   - Severity (Critical/Major/Minor)
   - Capability affected
   - Description
   - Recommendation

4. **External Dependencies Status** (if applicable)
   - Library name
   - Current version
   - Latest stable version
   - Status (Current/Outdated)
   - Upgrade recommendation

5. **Conclusion**
   - Can component edition be marked complete? (Yes/No)
   - Required actions before completion
   - Next audit recommendations

## Audit Execution

### Pre-pass — Template Conformance Findings

[Structural drift of in-scope component specs from
`component-specification-template.md`. Record findings here before
doing the per-component audit so structural drift doesn't get
confused with content findings.]

| # | Spec | Drift | Disposition | Follow-up |
|---|------|-------|-------------|-----------|
| T1 | [path] | [missing / renamed / stale guidance / undocumented addition] | update document / update template / accept with note | [task ref] |
| … | … | … | … | … |

### Component: [CMP.XXX.YYY]

#### Specification Details

**Edition:** N  
**Edition Status:** [from edition table]  
**Number of Capabilities:** X  
**Last Modified:** YYYY-MM-DD HH:MM:SS

#### Capability Audit Results

##### CAP.XXX.YYY.CAPABILITY1 - [Capability Name]

**Status:** [Pass/Fail/Partial]

**Specification Contract:**
- Input: [from spec]
- Output: [from spec]
- Preconditions: [from spec]
- Postconditions: [from spec]

**Implementation Evidence:**
- Location: [file path:line number]
- Capability code referenced: [Yes/No]
- Contract compliance: [Pass/Fail - note discrepancies]

**Investigative notes:** [OMIT unless relevant. Note any test code,
fixtures, or other artefacts consulted as an aid to understanding the
implementation. This audit does not execute tests.]

**Issues:**
- [List any issues found, or "None"]

##### CAP.XXX.YYY.CAPABILITY2 - [Capability Name]

[Repeat structure for each capability]

#### Capability Matrix Verification

**Status:** [Pass/Fail]

**Findings:**
- [All dependencies accounted for: Yes/No]
- [No unlisted dependencies: Yes/No]
- [All consumed capabilities exist: Yes/No]

**Issues:**
- [List any issues, or "None"]

#### Non-Functional Constraints Verification

**Status:** [Pass/Fail]

**Findings:**
- Technology constraints: [Pass/Fail - details]
- Performance constraints: [Pass/Fail - details]
- Security constraints: [Pass/Fail - details]
- Compatibility constraints: [Pass/Fail - details]

**Issues:**
- [List any issues, or "None"]

#### Component Summary

**Overall Status:** [Pass/Fail/Partial]  
**Critical Issues:** X  
**Major Issues:** Y  
**Minor Issues:** Z  
**Can be marked complete:** [Yes/No]

### Component: [CMP.AAA.BBB]

[Repeat structure for each component being audited]

### Bottom-up Orphan Candidates (Phase B)

[List every artefact unit found in the in-scope code/test/script/config/doc
surface that has no covering capability ID. One row per unit. Bring this
list to the user for disposition decisions before closing the audit.]

| ID | Location | Kind | Description | Proposed disposition | User decision | Rationale |
|----|----------|------|-------------|----------------------|---------------|-----------|
| O1 | [path:line] | code/test/script/config/doc | [what it is] | remove / cover / accept | [user] | [why] |
| O2 | ... | ... | ... | ... | ... | ... |

### Excluded Artefacts (Phase B)

[List every artefact (or artefact pattern) intentionally excluded from
the Phase B sweep, with a stated reason. An empty list is fine; a
missing list is not.]

| Pattern / Path | Reason for exclusion |
|----------------|----------------------|
| [e.g. `vendor/**`] | Third-party code covered by external-dependencies audit |

### External Dependencies Audit

[OMIT this section if not auditing external dependencies]

#### X.LIB.NAME - [Library Name]

**Current Version:** [version number]  
**Latest Stable Version:** [version number - MUST SEARCH]  
**Search Date:** YYYY-MM-DD HH:MM:SS  
**Status:** [Current/Outdated/Vulnerable]

**Version Discrepancy Explanation:**
[If versions differ, explain why we're not using latest stable.
Valid reasons: breaking changes, incompatibility, intentional pinning]

**Security Status:**
[Note any known vulnerabilities in current version]

**Recommendation:**
[Upgrade/Stay current/Monitor]

## Audit Report

### Executive Summary

**Audit Date:** YYYY-MM-DD HH:MM:SS  
**Auditor:** [Name/ID]  
**Scope:** [Summary of what was audited]  
**Overall Result:** [PASS/FAIL]

**Statistics:**
- Components Audited: X
- Capabilities Audited: Y
- Critical Issues: A
- Major Issues: B
- Minor Issues: C
- Template Conformance Findings Raised: T (Update Document: T1, Update Template: T2, Accept-with-Note: T3)

**Conclusion:**
[Can the audited components be marked as complete in their edition tables?
What actions are required before they can be marked complete?]

### Detailed Findings

[Consolidated findings from all components audited - can reference sections above
or provide summary view]

### Issues Log

| ID | Severity | Component | Capability | Description | Recommendation |
|----|----------|-----------|------------|-------------|----------------|
| 1  | Critical | CMP.X.Y   | CAP.X.Y.Z  | [description] | [action needed] |
| 2  | Major    | CMP.A.B   | CAP.A.B.C  | [description] | [action needed] |

### External Dependencies Summary

[If external dependencies were audited, provide summary table]

| Library | Current | Latest | Status | Recommendation |
|---------|---------|--------|--------|----------------|
| X.LIB.A | 1.2.3   | 1.5.0  | Outdated | Upgrade to 1.5.0 |
| X.LIB.B | 2.0.1   | 2.0.1  | Current  | No action |

### Reconciliation (Phase C)

[Merge Phase A gaps (specified-but-missing/incorrect) and Phase B orphan
candidates (present-but-unspecified) into one consolidated findings list.
The audit cannot close until every orphan candidate has a recorded user
disposition.]

| Finding | Source phase | Component / Capability | Disposition | Follow-up |
|---------|--------------|------------------------|-------------|-----------|
| [desc]  | A or B       | [code]                 | [agreed]    | [task / spec update / none] |

### Recommendations

1. [Priority recommendation]
2. [Priority recommendation]
3. [etc.]

### Next Steps

[What needs to happen as a result of this audit?
* Fix critical/major issues
* Create follow-up tasks
* Update edition tables
* Schedule next audit]

## Improvement

### Process improvement

[Note whether this audit suggests changes to:
* Component specification template
* Audit task template
* Implementation processes
* Testing requirements
* Documentation practices

If none, state "No changes identified".]

## Completion Checklist

[Before marking this audit task complete, verify ALL of the following:]

- [ ] All components in scope have been audited
- [ ] All capabilities have been verified against specifications
- [ ] All issues have been logged with severity and recommendations
- [ ] External dependencies checked (if applicable)
- [ ] Phase B bottom-up sweep performed across the full in-scope surface
- [ ] Excluded-artefacts list provided (empty is fine; missing is not)
- [ ] Every orphan candidate has a recorded user disposition
- [ ] Phase C reconciliation table completed
- [ ] Pre-pass: each in-scope component spec checked against `component-specification-template.md`; drift recorded with a disposition
- [ ] Audit report is complete with executive summary
- [ ] Clear pass/fail determination made for each component
- [ ] Edition tables have been updated with audit completion date
- [ ] Any follow-up tasks have been created

## Addendum

[Optional additional information, references, resources, notes, ….]