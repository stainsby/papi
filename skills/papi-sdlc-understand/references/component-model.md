# Component Model

## Components and capabilities

- We define *components* as the building blocks of the *software project*:
   - exposing *capabilities* (features/functions/behaviours) to other components
- Component types:
   - Internal software component: what we implement and maintain in a project
   - External software component: third-party libraries, frameworks, services and environments
- Components are structural units organised by containment.
- Dependencies other than containment may exist.
- Components can have sub-components.
- Capabilities are what components provide to their users, which may be humans, agents, or other components.
- Capabilities are in turn what components use from other components to function.

Traceability is enforced via hierarchical dot-notation codes for both components and capabilities.

## Permitted Component and Capability Codes

- Component codes use hierarchical dot-notation with this set of allowed prefixes:

|Type of Component|Code Prefix|Description|
|---|---|---|
|generic|`CMP`|An unclassified internal component|
|service|`SRV`|A service component|
|user interface|`UI`|A user interface component|
|library|`LIB`|A library component|
|binary|`BIN`|A binary component|
|application|`APP`|An application component|
|database|`DB`|A database component|
|runtime|`RT`|A runtime component|
|operating system|`OS`|An operating system component|
|environment|`ENV`|An generic environment component (but prefer more sopecific code if possible: RT, OS, ...)|
|document|`DOC`|A documentation component|
|External software component - various|`X.`*type*|Various external components using the above prefixes prepended with `X.`|

- note that any code not prefixed with `X.` is a component we are building or maintaining in the project.
  - eg. `OS.MYOWNIX` is a whole operating system we are building or maintaining!

- Similarly, the allowed capability code prefixes are:

|Type of Capability|Code Prefix|Description|
|---|---|---|
|generic|`CAP`|A generic capability|
|function|`F`|A singular function|
|feature|`FE`|A collection of related functions|
|feature set|`FS`|A collection of related features|

- This ontology is for readability, and not that vital:
  - Use `CMP` & `CAP` if unsure.
  - However, to prevent clashes, do NOT use prefixes that are not in the table above.

- Capability codes are scoped by their component, so there is no specific need to include the component code in the capability code itself. 

## Code Structure

- A component/capability code is dot-delimited hierarchy eg. `CMP.PARENT.CHILD.… .LEAF`.
- Example: `UI.GRID` represents the grid component within a UI component.
- Codes MUST be in `UPPER_SNAKE_CASE`.

## Code-to-Capability Linking

- Any source code not so linked will be DELETED.

It is CRITICAL that in source code:

- Every non-private function, method, class, module, package, API endpoint etc. MUST link to the capability code(s) it:
  - fully or partly implements
  - uses to function
- source code not so linked will be considered 'dangling' and DELETED
- Comments, doc strings, or other metadata can be used to link code to capabilities.

## 5. Internal Software Components

Internal software components are components that are defined, owned, and implemented within the codebase governed by this methodology.

### 5.1 Requirements for Internal Components

Internal software components MUST:

- Have their leaf components sized so they can be fully implemented, tested, and completed in a single human/AI work session.
- Document dependencies as capabilities consumed from other components (not from their own sub-components).
- Be covered by the required test categories (unit, integration, browser/E2E, visual regression, accessibility, performance, smoke) where relevant.
- Have implementation work carried out under tasks that reference their component specs and capability codes.
- Adhere to DRY, immutability, TDD, and the requirement that nothing is complete until all tests pass.
- Not be considered complete if any required documentation, component specification entry, or test is missing.

## 6. External Software Components

External software components are third-party libraries, frameworks, services, and environments that are not implemented within this codebase but are used by internal components.

### 6.1 Code Prefixes for External Components

- External software components use code prefix `X.`*type* where *type* is any of the internal component prefixes (e.g., `X.LIB`, `X.SRV`, `X.RT`).
- External component capabilities use the same prefix as internal capabilities but are namespaced under the external component code.
- Example: `X.LIB.TOKIO` for the Tokio async runtime library.

### 6.2 Documentation Requirements

External software components directly used by our components MUST:

- Have a specification document expressing the interfaces our components use in terms of capabilities.
- Include a capability matrix as per the component specification template.
- Be placed in the appropriate location within `docs/components/` following the containment hierarchy.

### 6.3 Selection Criteria and Approval

For any external software component to be adopted:

- It MUST NOT be added without careful consideration.
- It REQUIRES explicit human approval before adoption.
- It MUST be a "good" library or system according to human judgement.
- The latest stable version MUST be used where possible.
- The latest stable version MUST be determined by searching, not by relying on memory.

### 6.4 Integration with Internal Components

- Usage of external software components MUST be clearly reflected in the dependencies section of internal component specifications.
- External software components DO NOT replace the requirement for internal components to have their own capabilities and tests defined.
- External software components MUST be considered when designing tests for integration and system behaviour, especially where their capabilities lie on critical paths.
- Environment or platform constraints relevant to external software components SHOULD be recorded in their specification documents.

## 7. Environments

Environments are the distinct contexts in which software and agents operate.

### 7.1 Environment Types

- **Execution environments**: Concrete contexts where code is executed, such as local machine processes, containers, server processes, or agent runtimes.
- **Runtime environments**: Combinations of language runtime, libraries, configuration, and operating system under which components and capabilities are executed.
- **Development environments**: Used by humans and agents to write, modify, and maintain code, documentation, and tasks.
- **Test environments**: Configured specifically to run automated and manual tests, including unit, integration, browser/E2E, performance, and other defined categories.
- **Production environments**: Used to run software for actual end users or production workloads.
- **Agent environments**: Contexts in which AI agents operate, including their available tools, instructions, and access to code and documentation.

### 7.2 Environment Requirements and Constraints

Internal software components:

- MUST declare or assume at least one target runtime environment under which they are expected to execute correctly.
- User-facing components MUST consider production environment constraints as part of their non-functional constraints in their component specification.
- SHOULD record environment-specific constraints (such as language runtime versions, operating systems, or container images) in the non-functional constraints of their specifications.

External software components:

- MUST be compatible with the runtime environments of the internal components that depend on them.

Test environments:

- MUST be configured so that all required test categories (unit, integration, browser/E2E, visual regression, accessibility, performance, smoke) can be executed reliably and repeatedly.
- Browser/E2E tests for Web UI components MUST run in test environments that reflect relevant aspects of the production environment (e.g. browser versions, major platform behaviours) as far as practical.
- Performance tests MUST run in test environments that are sufficiently representative of the production environment to provide meaningful results for load times, responsiveness, and memory usage.

Development environments:

- MUST support the tools and workflows required to maintain documentation sync (`README.md` ↔ Component Specs ↔ Tasks ↔ Code).
- For agents, MUST ensure that agents have access to component specifications, tasks, and instructions necessary to respect component-capability rules and testing rules.

Agent environments:

- MUST enforce or surface the constraints that all work is done under tasks and that nothing is complete until tests have passed.

General:

- Environment differences between development, test, and production SHOULD be considered when defining test strategies for components, especially where external software components behave differently across environments.
- Environments that involve external software components SHOULD explicitly document any dependency on external systems, services, or agents in the dependencies section of component specifications.
- Changes to components or tasks that depend on specific environments SHOULD include updates to any environment-related documentation or configuration referenced in component specs or tasks.

## 8. Subcomponents and Containment

- Components are organised by containment, and may have sub-components (children).
- For projects with many components, specifications MUST be organised in a file hierarchy reflecting the containment structure under `docs/components/`.
- The project is always the top-level component that binds all others together.
