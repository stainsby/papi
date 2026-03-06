# Core Principles

This methodology defines how work is structured, specified, implemented, tested, and documented across the entire project. It coordinates components, capabilities, tasks, environments, tests, and documentation so that every change is traceable, well-specified, and verifiable.

## System Philosophy

- DON'T BE LAZY: Assume you have near infinite resources: choose the right solution, not the easiest one.
  - the same applies to testing: don't skimp on tests or test coverage.

## Continuous Process Improvement (CPI)

- When ambiguities, gaps, or mistakes are identified in documentation or processes, the root cause MUST be identified and a recommendation communicated to the human.
- Templates, instructions, and documentation MUST be updated to prevent the same mistake from happening again.

## Work Sequencing and Priorities

Work follows a strict priority order:

1. Strategy and documentation first.
   - If something is not documented according to the formalism, then the code may as well not exist and will be deleted.
2. Testing plans second.
3. Architectural alignment check — before tests.
   - Verify the planned implementation structure (module boundaries, dependency directions, patterns) matches the component specification.
   - Document any proposed deviations — architectural deviations require human approval.
4. Tests next — before code (TDD).
   - Any untested code will be rejected (deleted).
5. Code next.
   - Any code not linked (by explicitly mentioning the relevant capability codes) to the full set of capabilities it provides may as well not exist and will be deleted.
   - Implementation MUST follow the architectural design in the component specification — do not take architectural shortcuts.
6. Verify spec compliance and (if correct) do final testing.

## Definition of "Complete"

- No component or task can be deemed complete without all relevant tests passing.
- You are FORBIDDEN from marking anything complete unless it has passed all tests.
- Deleting any test requires explicit human permission.

## Scope of Work and Tasks

- All work — including planning, documenting (e.g. components), coding/implementing, debugging, and testing — MUST be performed under a task.
- Tasks are the fundamental unit of work governed by this methodology.

## Engineering Practices

- Test-driven development (TDD) is a hard requirement.
- DRY (Don’t Repeat Yourself) MUST be used extensively to avoid duplication.
  - Code and design SHOULD be checked and re-checked for duplicate logic or structures whenever possible.
- Immutability is a primary design principle and SHOULD be used as much as possible.
- The latest stable versions of libraries and frameworks SHOULD be used, and these SHOULD be found by searching rather than relying on memory.

## Autonomy and Ongoing Work

- Work MUST proceed according to these instructions, continuing for as long as possible unless help or input is needed.
- Before finishing work:
  - You MUST ask whether you really need to finish at this point.
  - If you truly need to finish, you MUST ensure that the relevant task documents are up to date.
  - If you truly need to finish, you MUST leave the project in a state that can easily be resumed by others.

## Language and Style Rules

- Communication and documentation MUST remain professional.
- Emojis should not be used in documentation.

## Decision-Making and Information Sources

When making decisions, consult relevant process documents (Core Principles, Component Model), and base outputs on this priority order:

1. **Sources of truth (e.g. specifications)** (highest priority)
2. **Other repository docs and artefacts (e.g. plans)**
3. **Web searches on reputable sources**
4. **Other documentation**
5. **Your own knowledge** (last resort - clearly state when relying on this)

## Documentation Framework

### Size and Splitting Rules

- Documents SHOULD be split if they are longer than 1000 lines.
- For tasks, documents SHOULD be split if they would take a human developer more than one work day to complete.
- Documents MUST ONLY be split with explicit permission.

### Documentation Categories

The documentation framework is strict. Maintain clear separation between:

- Project README at the repository root
- Component specifications
- Task documents
- Templates
- Process documentation

New documentation categories MUST NOT be created without explicit permission. When uncertain about documentation location, ask: "This documentation belongs in [location]. Should I add it there or does it need a new location?"

## High-Level SDLC Philosophy

The overall Software Development Life Cycle (SDLC) embodied by this methodology is:

1. Define strategy and documentation first, ensuring all work is under tasks and components are fully specified.
2. Define testing plans second, including comprehensive coverage for all relevant test categories.
3. Verify architectural alignment: before writing tests, confirm that the planned implementation structure (module boundaries, dependency directions, patterns) matches the component specification. Document any deviations — architectural deviations require human approval.
4. Implement tests before code, following TDD.
5. Implement code that:
   - Is immutable where possible.
   - Respects DRY.
   - Uses the latest stable libraries and frameworks (verified by searching).
   - Is fully linked to capabilities and component specs using the defined code and metadata conventions.
   - Follows the architectural design in the component specification — do not take architectural shortcuts even if functionally correct.
6. Maintain strict documentation sync and environment awareness throughout.
7. Do not mark anything complete until all tests have passed and all documentation is consistent and up to date.

## Methodology Structure

This methodology is split into focused modules:

### Core Principles (this document)

Defines the overarching philosophy of the system, including continuous process improvement, work sequencing, and the strict rules for when something is considered "complete".  
Describes global engineering practices (TDD, DRY, immutability, latest stable dependencies), autonomy rules, language and style requirements, and the high-level SDLC flow.

### Task Templates

Templates embed SDLC workflow, TDD methodology, and testing strategies.
Templates enforce task structure, acceptance criteria, alignment procedures, and testing rigor at the point of execution.

## Glossary

- **Component**  
  A structural unit of the system organised by containment, which provides one or more capabilities to users (humans, agents, or other components).

- **Internal component**  
  A component that is defined, owned, and implemented within this codebase, using `CMP.` and `CAP.` codes and following the component specification standard.

- **External component**  
  An external library, system, or agent that is not implemented within this codebase but is modelled as a component using `X.` code prefixes and documented via a specification.

- **Capability**  
  A specific behaviour or service provided by a component, identified by a capability code and used to drive tests, implementation, and traceability.

- **Environment**  
  A context in which software or agents operate (e.g. execution, runtime, development, test, production, or agent environments) with constraints that affect components and tests.

- **Task**  
  The fundamental unit of work in this methodology, documented under `docs/tasks/`, describing a concrete change or implementation linked to component specs and capabilities.

- **Leaf component**  
  A component with no sub-components that is small enough to be fully implemented, tested, and completed in a single human/AI work session.

- **Spec**  
  A specification document (typically under `docs/components/` or `docs/tasks/`) that formally defines a component, its capabilities and constraints, or a task, its context and acceptance criteria.
