[Use this template to bring existing, non-PAPI project artefacts (or a subset)
under PAPI methodology control. This applies to any component type — code,
services, databases, documentation, UIs, environments, and so on. It involves
discovering and documenting components, capabilities, and dependencies so that
ongoing work can follow PAPI SDLC processes.]

[When to use this template:
* Existing project artefacts need to be brought under PAPI control
* You need to work with part of a project that isn't yet PAPI-managed
* You have a task (bug fix, feature, documentation update, etc.) against
  artefacts that have no component specs yet
* You are onboarding a new service, database, environment, or other
  component type that pre-dates PAPI adoption]

[This template is derived from `basic-task-template.md`.]

[This template supports two modes:
* **Full assimilation:** Suitable for small projects. Discover, map, and spec
  everything in one pass.
* **Incremental assimilation (default):** Suitable for most projects. Driven by
  real incoming work. Spec only what you need now, plus the structural
  scaffolding (ancestor components up to root) to keep the hierarchy coherent.]

[This template is a guideline:
* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that may
  indicate a need for a new/updated template or process change; record that
  under *Process improvement* in the *Improvement* section.]

# Task: Assimilation - [Scope Name]

**Project/Artefact:** [Repository, service, system, or other scope identifier]  
**Mode:** [Full / Incremental]  
**Trigger:** [e.g., "Bug fix JIRA-123", "New feature X", "Initial onboarding",
"Database migration", "Service integration", etc.]  
**Status:** [Proposed, In Progress, Completed]

## Template

This document was based on the PAPI SDLC template: `codebase-assimilation-task-template.md`.

## Status

[Current status of this task.
Examples: Proposed, In Progress, Completed, Abandoned.]

## Context & Scope

[Why this assimilation is being done and what is in scope.

For full assimilation: describe the entire project or system.

For incremental assimilation: describe the incoming work that triggered this,
and identify the target component(s) you need to work with.]

## Goals

[What this assimilation task aims to achieve. Typically:
* Establish the component hierarchy (full or partial) under PAPI
* Create component specifications for target components
* Document external dependencies
* Enable subsequent work to use PAPI SDLC templates]

---

## Phase 1: Discovery

[Explore the project to understand its structure and identify components.
Components can be of any type: code modules, services, databases, UIs,
documentation sets, environments, binaries, libraries, etc.]

### Project Overview

[High-level description of the project or system:
* What it does and who it serves
* Component types present (code, services, databases, UIs, docs, etc.)
* Languages, frameworks, and technologies used
* Directory/organisational structure
* Existing tests, documentation, CI/CD, infrastructure
* Rough scale and complexity]

### Identified Components

[List the logical components discovered.

For full assimilation: list all significant components of any type.

For incremental assimilation: identify at minimum:
1. The target component(s) needed for the incoming work
2. All ancestor components up to the project root
3. Any out-of-tree dependencies (external or internal) that the target
   component(s) directly rely on]

| Discovered Artefact | Proposed Component Code | Type | Notes |
|---------------------|------------------------|------|-------|
| [e.g., src/api/]          | [e.g., SRV.API]        | [Internal/External] | [REST API service] |
| [e.g., PostgreSQL store]  | [e.g., DB.STORE]       | [Internal] | [Main data store] |
| [e.g., user-guide/]       | [e.g., DOC.USER_GUIDE] | [Internal] | [End-user documentation] |
| [e.g., tokio]             | [e.g., X.LIB.TOKIO]   | [External] | [Dependency of SRV.API] |

### Component Hierarchy

[Draw the containment tree, even if partial. Mark skeleton entries clearly.
Components of any type can appear in the tree.

For incremental assimilation, the path from root to target must be complete,
other branches can be noted but left as "not yet assimilated".]

```
APP.PROJECT (root)
├── SRV.API (target)          <-- full spec needed
│   └── ...
├── DB.STORE                  <-- skeleton spec
├── DOC.USER_GUIDE            <-- skeleton spec
├── [other artefacts...]       <-- not yet assimilated
```

### External Dependencies

[List out-of-tree dependencies that need to be documented.
Focus on direct dependencies of the target component(s).
These become X.* component specs.

Per PAPI requirements for external components:
* Each external component REQUIRES explicit human approval before adoption
* The latest stable version MUST be used where possible
* The latest stable version MUST be determined by searching, not from memory
* Each MUST be compatible with the runtime environments of the internal
  components that depend on it]

| Dependency | Proposed Code | Used By | Version | Human Approved? | Capabilities Consumed |
|------------|--------------|---------|---------|-----------------|----------------------|
| [e.g., tokio 1.x] | [X.LIB.TOKIO] | [SRV.API] | [latest stable] | [Yes/Pending] | [async runtime, networking] |

---

## Phase 2: Structural Mapping

[Map discovered components into the PAPI component hierarchy.]

### Proposed Component Tree

[Finalise the component codes, containment, and hierarchy.
Refer to the Component Model reference document for code conventions.]

### Capability Identification

[For each component being fully specced (not skeletons), identify its
capabilities — what it provides to its users/consumers.

For skeleton specs, a brief one-line summary is sufficient.]

| Component Code | Capability Code | Description |
|---------------|----------------|-------------|
| [SRV.API]     | [CAP.AUTH]     | [Authenticates API requests] |
| [SRV.API]     | [F.PARSE_REQ]  | [Parses incoming request bodies] |

---

## Phase 3: Specification Generation

[Create the actual component specification documents.
This applies equally to code components, services, databases,
documentation sets, environments, and any other component type.

Following PAPI methodology, specification creation is done under tasks.
Create component or development tasks (from the appropriate SDLC task templates)
to produce the specifications. Those tasks will then use the component
specification template to create the actual spec documents.]

### Skeleton Specs (Ancestors / Context)

[For incremental assimilation: create tasks to produce skeleton specs for
ancestor components and any siblings needed for context. Work **top-down**
from the project root toward the target.

A skeleton spec contains at minimum:
* Component code and name
* Parent component reference
* One-line summary
* Sub-components list (even if incomplete, marked as such)
* A note that this is a skeleton needing expansion later

Each task uses the component specification template, filling in only the
minimum required fields and marking the rest as TBD.]

**Skeleton spec tasks to create:**

- [ ] Task: Create skeleton spec for [APP.PROJECT] (Project root)
  - Template: `component-task-template.md` or `development-task-template.md`
  - Output: Component spec using `component-specification-template.md`
- [ ] Task: Create skeleton spec for [CMP.PARENT] — [One-line summary]
- [ ] ...

### Full Specs (Target Components)

[Create tasks to produce proper, detailed component specifications for the
target component(s). These tasks use the component specification template
and fill it in thoroughly.

These specs should include:
* Full capability matrix
* Dependencies (including the X.* externals identified above)
* Testing strategy
* Non-functional constraints]

**Full spec tasks to create:**

- [ ] Task: Create full spec for [SRV.API] — [Description]
  - Template: `component-task-template.md`
  - Output: Component spec using `component-specification-template.md`
- [ ] ...

### External Component Specs

[Create tasks to produce specs for external dependencies (X.* components).
Per PAPI requirements, these specs MUST:
* Express the interfaces our components use in terms of capabilities
* Include a capability matrix
* Record version information (verified by searching for latest stable)
* Be placed in `docs/components/` following the containment hierarchy
* Record any environment or platform constraints

External components DO NOT replace the requirement for internal components
to have their own capabilities and tests defined. External components MUST
be considered when designing integration and system-level tests, especially
where their capabilities lie on critical paths.]

**External spec tasks to create:**

- [ ] Task: Create external spec for [X.LIB.TOKIO] — [Description]
  - Template: `component-task-template.md` or `development-task-template.md`
  - Output: Component spec using `component-specification-template.md`
- [ ] ...

---

## Phase 4: Artefact Linking

[Link existing artefacts to their capability codes.
For source code, this means annotations in comments/docstrings.
For other component types (services, databases, docs, environments, etc.),
this means recording the mapping in the component specification or in
the artefact's own metadata where possible.]

[For full assimilation: systematically link all artefacts.

For incremental assimilation: link the target component(s) only.
Other artefacts can be linked when those components are assimilated later.]

### Linking Approach

[Describe how capability codes will be associated with artefacts:
* For code: comment style/format (language-dependent), placement
  (function level, module level, etc.)
* For services/APIs: where capability references live (OpenAPI docs,
  README, spec document)
* For databases: schema documentation, migration files
* For documentation: metadata, front matter, or cross-references
* For environments: configuration documentation
* How to handle artefacts that serve multiple capabilities]

### Linking Checklist

- [ ] All public interfaces in target component(s) linked to capabilities
- [ ] Component-level documentation updated with component codes
- [ ] Any "dangling" artefacts (no clear capability) flagged for review

---

## Phase 5: Gap Analysis

[Identify what is missing or needs improvement.]

### Documentation Gaps

[What documentation exists vs. what PAPI requires:]

| Requirement | Status | Notes |
|-------------|--------|-------|
| README.md   | [Exists/Missing/Incomplete] | |
| Component specs | [Partial - X of Y created] | |
| Testing strategy | [Exists/Missing/N/A] | |
| API documentation | [Exists/Missing/N/A] | |
| Schema documentation | [Exists/Missing/N/A] | |
| External component specs | [Partial - X of Y created] | |
| Internal specs reflect external deps | [Yes/Partial/No] | [Do internal component specs list their X.* dependencies?] |

### Test / Verification Gaps

[What test or verification coverage exists vs. what the component specs
require. Not all component types have traditional tests — for non-code
components, consider what verification means (e.g., schema validation
for databases, link checking for docs, health checks for services):]

| Component | Type | Verification Status | Notes |
|-----------|------|---------------------|-------|
| [SRV.API] | Code | [Partial unit tests, no integration] | |
| [DB.STORE] | Database | [No schema validation] | |
| [DOC.USER_GUIDE] | Documentation | [No link checking] | |

### Known Issues

[Problems discovered during adoption that need addressing:]

- [ ] [Issue description]
- [ ] ...

---

## Outcomes

[Summary of what was achieved by this assimilation task.]

### Specs Created

[List all specification documents created, with their status:]

| Spec | Type | Status |
|------|------|--------|
| [APP.PROJECT] | Skeleton | Created |
| [SRV.API] | Full | Created |
| [X.LIB.TOKIO] | External | Created |

### Ready for PAPI Work

[Confirm which components are now ready for standard PAPI SDLC workflow.
The original triggering work (bug fix, feature, etc.) can now proceed
using the appropriate SDLC task template.]

## Next Steps

[What follows this assimilation task:
* Create the actual SDLC task for the triggering work
* Schedule expansion of skeleton specs as those areas are worked on
* Plan further incremental assimilation as future work touches new components]

## Improvement

[Decide what happens next, including how the system itself should change.]

### Process improvement

[Note whether this task suggests changes to task templates,
processes, or ways of working. If none, state "No changes identified".]

### Future Enhancements

[Ideas for improving the assimilation process or expanding its scope.]

## Addendum

[Optional: Additional notes, references, raw data, etc.]
