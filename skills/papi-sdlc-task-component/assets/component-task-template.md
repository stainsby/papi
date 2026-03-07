[Use this template for some kind of development work on a **SINGLE** component.
For work requiring changes to multiple components, use a development task template instead,
UNLESS those changes to other components do not change the *function* of those components.
For example adding a extra parameter to an existing exposed method in this component may require
changes to other components.]

[This template is a guideline:
* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that may
  indicate a need for a new/updated template or process change; record that
  under *Process improvement* in the *Improvement* section.]

# Task: [Task name]

**Component:** CMP.XXX.YYY  
**Capabilities:** [List capability codes being implemented]  
**Dependencies:** [List prerequisite tasks/components]  
**Estimated Effort:** [X work sessions]  
**Status:** [Status indicator]

## Synopsis

[One-line summary of what this task should achieve]

## Template

This document was based on the PAPI SDLC template: `component-task-template.md`.

## Status

[Current status of this task.
Examples: Proposed, Active, Blocked, Completed, Abandoned.
If the task is blocked, paused, or abandoned, briefly note why.]

## Parent task

[OMIT unless this is a sub-task of another task.
Often this will be a higher level development task.]

## SDLC Workflow Reminder

[This task follows the strict SDLC sequence - do NOT deviate without explicit permission:]

1. **Strategy and documentation first**
   - Ensure this task is properly defined and all affected component specs are current
   - If something isn't documented, it may as well not exist
2. **Testing plans second**
   - Define comprehensive testing strategy covering all relevant test categories (see Testing Strategy section)
3. **Architectural alignment check — before tests**
   - Before writing tests, verify the planned implementation structure against the component specification
   - Confirm: module/file boundaries, dependency directions, design patterns, and interface contracts match the spec
   - Document any proposed deviations in the Specification Deviations section — deviations require human approval
   - This is a lightweight pre-flight check, not a full compliance audit
4. **Tests next — before code (TDD)**
   - Implement tests prior to implementing code (RED phase)
   - Any untested code will be rejected
5. **Code next**
   - Implement code that passes the tests (GREEN phase)
   - Link code to capability codes where applicable
6. **Refactor**
   - Improve structure while maintaining passing tests

**TDD Loop:**
1. Add/update tests according to requirements
2. Run tests, confirm they fail for the right reason (RED)
3. Implement minimal code to make tests pass (GREEN)
   - **Architectural constraint:** implementation MUST follow the module structure, dependency directions, and patterns specified in the component specification. If the minimal path to GREEN would violate the spec's architecture, update the approach or seek approval — do not take architectural shortcuts.
4. Run full test suite, confirm all pass
5. Refactor to improve structure/readability
6. Re-run tests to ensure behaviour preserved
7. Repeat until all acceptance criteria met

## Description

[A detailed description of the task, its purpose, and how it fits into the overall component/system. Max 1 to 3 paragraphs.]

## Tasks this task depends on

[OMIT unless this depends on other tasks being done first]

## Subordinate and dependent tasks

[OMIT unless other tasks depend on this one being done first]

[This can include sub-tasks or other dependent tasks.]

[Sequencing, prioritisation and other supervisory information may be
included here. This can include coordination strategies of dependent tasks.]

[Dynamically created dependent tasks, such as recurring subordinate tasks can be
described here - these have a task template that is instantiated as needed,
along with scheduling information for these tasks.]

[Optional: Describe how subordinate work is organised over time:
* externally driven constraints (deadlines, windows, dependencies)
* internally driven structure (regular reviews/maintenance/planning and their frequency)
* one-off vs recurring work patterns
* interaction and precedence rules (how conflicts are resolved)]

## Context & Scope

[Why this task exists, what it is trying to address,
and the boundaries of what it will and will not cover.]

## Goals

[What this task is trying to achieve or decide.]

## Who

[Include things like: who is accountable for this task, who contributed
(human and/or model)]

## References

[Identify the primary sources of truth that exist outside this task.
These define what correctness, completion, or success means.
Especially this is the component specificationss, but may include designs,
reference documents, standards, compliance rules, and so on.]

### The Component

**Code:** `CMP.XXX.YYY`  
**Name:** [Component Name]  
**Synopsis:** [One-line component summary]  
**Last Updated:** YYYY-MM-DD HH:MM:SS  

#### Capabilities Being Implemented

[List SUMMARIES of ALL capabilities involved in this task. If implementing the full component, include ALL of its capabilities. For each, include: code, name, and synopsis.]

- **CAP.XXX.YYY.CAPABILITY1** - [Capability Name] - [One-line synopsis]
- **CAP.XXX.YYY.CAPABILITY2** - [Capability Name] - [One-line synopsis]

### Dependents

[ALL components that depend on the capabilities we are touching in this task, including, but possibly not be limited to, ALL ancestor components.]

#### Ancestors

**[Root Component Code]** - [Component Name] (Top-level)
- **Synopsis:** [One-line summary]
- **Depends on:** [Which of our capabilities]
- **Last Updated:** YYYY-MM-DD HH:MM:SS

**[Ancestor Component Code]** - [Component Name]
- **Synopsis:** [One-line summary]
- **Depends on:** [Which of our capabilities]
- **Last Updated:** YYYY-MM-DD HH:MM:SS

…etc…

#### Others

[Other components that depend on the capabilities we are touching in this task. Same format as above]

### Providers

[ALL components that provide the capabilities needed for the capabilities we are touching in this task, including, but possibly not be limited to, ALL immediate child components.]

#### Children

**[Child Component Code]** - [Component Name]
- **Synopsis:** [One-line summary]
- **Provides:** [capabilities]
- **Last Updated:** YYYY-MM-DD HH:MM:SS

… etc. …

#### Other Providers

[Other components that provide the capabilities we are touching in this task. Same format as above]

## Plan

[A TDD-based plan for the work to be done, including red and green phase steps.]
[This is a single-component task - if it seems like more work than can be done
in one session, suggest splitting the component or creating sub-tasks.]

### Alignment

[Any work described in this plan should strive to keep the references
synchronised with what is actually produced. This may involve adjusting
the implementation to match the references, updating the references to
reflect what was built, or both.]

[This is especially true for the component specifications and capability codes.]

[Outline how this task will work towards synchronising references
with what is done in this task.]

### Exploration

[What needs to be researched, explored, or better understood before acting.
If none, state "No exploration needed".]

### Assumptions

[Key assumptions being made at the start.]

### Acceptance Criteria

[Testable criteria that MUST be met for task completion. These should be specific,
measurable, and verifiable through tests. Update this list as you work to track progress.]

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] All tests pass
- [ ] Code coverage meets requirements
- [ ] Component specs updated and in sync
- [ ] Documentation updated

### Testing Strategy

[Detail your comprehensive testing approach. All components MUST have test coverage
including relevant categories below. Check all that apply and describe approach.]

#### Test Categories

- [ ] **Unit Tests**
  - Individual functions, methods, pure logic in isolation
  - [Describe approach, tools, coverage targets]

- [ ] **Integration Tests**
  - Component interactions, API contracts, data flow between modules
  - [Describe approach, tools, test scenarios]

- [ ] **Browser/E2E Tests** (if applicable)
  - Full user workflows in actual browser environment (Playwright, Puppeteer, etc.)
  - [Describe critical user paths to test]

- [ ] **Visual Regression Tests** (for UI components)
  - Screenshots to catch UI changes
  - [Describe approach, baseline management]

- [ ] **Accessibility Tests** (for UI components)
  - ARIA, keyboard navigation, screen reader compatibility
  - [Describe compliance targets, tools]

- [ ] **Performance Tests** (where applicable)
  - Load times, responsiveness, memory usage
  - [Describe benchmarks, acceptable thresholds]

- [ ] **Smoke Tests**
  - Critical path verification that component works end-to-end
  - [Describe critical paths, may require human verification]

- [ ] **Architecture Checks**
  - Verify module/file structure matches spec's component boundaries
  - Verify dependency directions (no prohibited cross-module imports)
  - Verify design patterns used match spec's implementation notes
  - Can be implemented as lint rules, import checks, or structural assertions
  - [Describe approach, tools]

#### GUI/Web UI Special Constraints

[CRITICAL FOR UI COMPONENTS: As an AI, I have ZERO visual understanding. I cannot
"see" the GUI or understand visual layout intuitively. Therefore:]

- [ ] UI components demand EXCEPTIONALLY thorough testing strategies
- [ ] Browser/E2E tests are MANDATORY for Web UI components
- [ ] Tests MUST verify:
  - [ ] Layout
  - [ ] Visibility
  - [ ] Positioning
  - [ ] User interactions
  - [ ] Responsive behaviour
  - [ ] Empty states
  - [ ] Error states
- [ ] Unit tests alone are INSUFFICIENT - they test JavaScript, not what users see
- [ ] Every visual feature MUST have corresponding browser test validating rendered HTML/CSS

#### Coverage Requirements

- Test coverage target: [e.g., 80%, 90%, 100% for critical paths]
- Coverage reports will be generated: [Yes/No, tool to use]
- All tests MUST pass before task completion
- No component can be marked complete without passing tests
- Deleting any test requires EXPLICIT HUMAN permission

### Constraints

[Any relevant limits or non-negotiables.]

### Approach

[High-level description of how you intend to proceed.]

### Specification Deviations

[MANDATORY: Document any deviations between the implementation and the component
specification. Such deviation must be human-approved. For each deviation, record:
- What the spec says
- What was implemented differently
- Why the deviation was necessary
- Whether the spec should be updated (new edition) or the code should be brought into alignment

If no deviations: state "Implementation matches specification — no deviations."

**Deviations from architectural design require explicit human approval.**]

## Implementation

[What was actually done.]

### Actions taken

[Summary of the main actions.]

### Evidence

[Data, observations, or artefacts gathered/produced.]

### Issues

[Notable problems, risks, or deviations encountered.]

## Reflect

[Think about what the results mean.]

### What happened

[What actually occurred.]

### Interpretation

[What this means in relation to the goal and assumptions.]

### Learning

[What is now better understood, including uncertainties.]

## Improvement

[Decide what happens next, including how the system itself should change.]

### Outcomes

[Brief statement of the overall outcomes.]

### Decisions

[Any decisions being made as a result.]

### Next steps

[Any follow-on work, if relevant.
These can be proposed as new tasks.]

### Process improvement

[Note whether this task suggests changes to task templates,
processes, or ways of working. If none, state "No changes identified".]

## Completion Checklist

[Before marking this task complete, verify ALL of the following:]

- [ ] All acceptance criteria are met
- [ ] All relevant tests implemented and passing
- [ ] Code linked to appropriate capability codes
- [ ] Component specifications updated and in sync with code
- [ ] Documentation (README, component specs, etc.) updated
- [ ] No untested code paths remain
- [ ] Test coverage meets requirements
- [ ] All test categories relevant to this work are covered

[REMEMBER: You MAY NOT mark this task complete unless it has passed all tests.]

## Addendum

[Optional additional information, references, resources, notes, ….]
