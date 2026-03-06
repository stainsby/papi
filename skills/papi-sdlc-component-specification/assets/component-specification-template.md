
[Use this template to manage a specification for a component.]

[This template is a guideline:
* Unless otherwise specified, all parts are optional.
* If you find yourself needing to deviate in a meaningful way, that may
  indicate a need for a new/updated template or process change; record that
  under *Process improvement* in the *Improvement* section.]

# Component: [Component Name]

## Synopsis

[One-line summary of what this component does]

## Template

[Copy verbatim]

This document was based on the PAPI SDLC template: `component-specification-template.md`.

## Editions

[Track the specification lifecycle through numbered editions. Edition numbering
starts at 1 and increments with each significant update. Update dates/times
using the Linux `date` command when each status is completed.]

[If the table becomes very long, you may trim older editions, but keep at least
the 3-5 most recent editions for historical reference.]

| Edition | Status   | Completed          | Human Review | Completed          | Implementation | Completed          | Compliance Audit | Completed          | Testing  | Completed          |
|---------|----------|--------------------|--------------|--------------------|----------------|--------------------|------------------|--------------------|----------|--------------------|
| 1       | [status] | [YYYY-MM-DD HH:MM] | [status]     | [YYYY-MM-DD HH:MM] | [status]       | [YYYY-MM-DD HH:MM] | [status]         | [YYYY-MM-DD HH:MM] | [status] | [YYYY-MM-DD HH:MM] |

[DO NOT change the edition without permission]
[DO NOT change the status without permission]

**Status definitions:**
- **Spec Status:** Is this edition of the spec fully written/updated?
  - States: `in progress`, `completed`
- **Human Review:** Has a human reviewed and approved this edition?
  - States: `pending`, `completed`
  - **All new or updated specs should be human-reviewed BEFORE implementation starts**
- **Implementation:** Has the implementation been completed for this edition?
  - States: `not started`, `in progress`, `completed`
- **Compliance Audit:** Has a compliance audit verified the implementation matches the spec?
  - States: `not started`, `in progress`, `completed`
  - See compliance audit task template for details
- **Testing:** Has all required testing been completed and passed for this edition?
  - States: `not started`, `in progress`, `completed`

**NOTE: These actions in there column MUST be performed LEFT TO RIGHT unless otherwise approved by a human.**

**Code:** `CMP.PARENT.COMPONENT`

**Parent:** `CMP.PARENT` - [Parent Component Name]

## Description

[A deep description of what this component is, and what's it's for. Max 1 to 3 paragraphs.]

## Non-Functional Constraints

- **Technology:** [e.g., Must use React 18, Node.js 18+]
- **Performance:** [e.g., Response time < 100ms, handles 10k rows]
- **Security:** [e.g., Must validate all inputs, enforce schema constraints]
- **Compatibility:** [e.g., Modern browsers, Node.js 18+]
- **Other:** [Any other constraints]

## Capabilities

[Only document capabilities that THIS component directly owns and implements.
If this component has sub-components, their capabilities belong in THEIR OWN
specification files, NOT here. This file should only reference sub-component
capabilities in the Sub-Components section below.]

[For an external component, it is sufficient to define high-level, somewhat hand-waving capabilites as needed by by other components.]

[Capability codes are scoped by this component. If this component is CMP.B and
you define CAP.STORAGE below, it is implicitly CMP.B.CAP.STORAGE in the global
dependency graph, but write just CAP.STORAGE here since the component context is known.]

### CAP.DESCRIPTIVE_NAME - [Capability Name]

**Synopsis:** [One-line summary of what this capability does]

**Description:** [Detailed explanation of this capability, its purpose, and how it works. Max 1 to 3 paragraphs.]

**Users:** [Who/what uses this capability - humans, agents, other components]

**Interface/Contract:**
- **Input:** [Parameters, data structures, events]
- **Output:** [Return values, state changes, side effects]
- **Preconditions:** [What must be true before calling]
- **Postconditions:** [What is guaranteed after calling]
- **Errors:** [What can go wrong and how it's signaled]

**Implementation Notes:** [Optional: key implementation details, algorithms, patterns]

### CAP.ANOTHER_CAPABILITY - [Another Capability]

[Repeat structure above for each capability]

## Testing Strategy

[Depending on the nature of the component, different testing strategies may be appropriate. Generally this section is not needed ror external components.]

[Below we describe *Capability Tests* and *Capability Integration Tests* which are **MANDATORY** for EVERY capability provided by this component.
We should not be lazy and skimp on testing here even if it's hard:
- if this requires major tools to be brought in, or for testing scaffolding to be built, then if these are large or much work they can be sub-components,
. higher-level components may need human partticipants in testing: this is OK as long as the tests are well-defined, repeatable, and not just the product of laziness]

### Capability Tests

[MANDATORY FOR **ALL** CAPABILITIES PROVIDED BY THIS COMPONENT.]

[These are unit tests that verify the correct implementation of each capability provided by this component in isolation.
There should be a sub-section per capability. Correctness must cover ALL state goals of functionality, perfomance, security, etc.]

### Capability Integration Tests

[MANDATORY FOR **ALL** CAPABILITIES PROVIDED BY THIS COMPONENT.]

[These are integration tests that verify the correct interaction between this component's capabilities and the capabilities of other components it depends on.
There should be a sub-section per capability. Correctness must examine whether the other comonent's capabilities we state that we depend on here are used and used correctly.]

## Context

[Complete context up to the top-level, but only down to immediate sub-components]

### Dependents

[ALL components that depend on the capabilities of this component, including, but possibly not be limited to, ALL ancestor components.]

#### Ancestors

**[Root Component Code]** - [Component Name] (Top-level)
- **Synopsis:** [One-line summary]
- **Depends on:** [Which of our capabilities]

**[Ancestor Component Code]** - [Component Name]
- **Synopsis:** [One-line summary]
- **Depends on:** [capabilities]

…etc…

#### Others

[Other components that depend on the capabilities of this component.
Same format as above]

## Dependencies

[List ALL components and libraries this component depends on, expressed in
terms of capabilities consumed. Every dependency edge in the capability matrix
should have a corresponding entry here. Capabilities are scoped by the providing component — do NOT embed
component codes in capability names.]

['Leaf' components are components with no sub-components. Leaf components MUST
be small enough in scope to be fully implemented, tested, and completed in a
single human/AI work session. If this component is too large for one work
session, it MUST be broken down into sub-components.]

### Sub-components

[Immediate children of this component. Their capabilities belong in their own
spec files — list here only what this component consumes from them.]

**[Sub-Component Code]** - [Component Name]
- **Synopsis:** [One-line summary]
- **Capabilities consumed:** [capability codes, e.g., CAP.X, CAP.Y]

… etc. …

### Other Component Dependencies

[Other components (not sub-components) whose capabilities this component
consumes.]

- **`CMP.OTHER.COMPONENT`** - [Component Name]
  - **Capabilities consumed:** [e.g., CAP.SOME_CAPABILITY, CAP.ANOTHER_CAPABILITY]

… etc. …

### External Dependencies

- [Library/Framework Name] - [What capabilities we consume from it - these might be informally specified here]
- …

## Capability Matrix

[MANDATORY FOR **ALL** COMPONENTS! THIS WIRES THE WHOLE COMPONENT NETWORK TOGETHER.]

[This is a YAML block designed to be both human and machine-readable.]

[IMPORTANT: Capabilities are scoped by the component that provides them.
The dependency graph uses two node types: component nodes and capability nodes.
Component nodes (e.g., CMP.B) have edges to the capabilities they provide (e.g., CAP.STORAGE).
Capability nodes have edges to other capabilities they depend on.

In this YAML:
- The 'component:' field identifies which component provides the capabilities listed
- Under 'dependencies:', each capability lists which OTHER components it depends on
  and which of their capabilities it needs
- Example: CAP.STORAGE depends on CMP.OTHER's CAP.CACHE means there's an edge
  from CAP.STORAGE to CAP.CACHE in the graph]

[External components can simply list their capabilities here, with empty dependencies, unless
such dependencies are useful to show.]

[Do not self-reference: Other Component should never be *this* component]

```yaml
component: CMP.PARENT.COMPONENT  # MUST match the component code above
dependencies:
  # Format: our_capability_code: list of components and their capabilities we depend on
  CAP.CAPABILITY1:
    - CMP.OTHER1:
      - CAP.SOME_CAPABILITY
      - CAP.ANOTHER_CAPABILITY
    - CMP.OTHER2:
      - CAP.YET_ANOTHER_CAPABILITY
  CAP.CAPABILITY2:
    - X.LIB.NAME:  # External component
      - F.SOME_EXTERNAL_CAP
  # Add all capabilities provided by this component
  # If a capability has no dependencies, use an empty list: []
```

## Addendum

[Optional additional information, references, resources, notes, ….]
