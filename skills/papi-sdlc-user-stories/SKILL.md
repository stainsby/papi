---
name: papi-sdlc-user-stories
description: Create or work with user stories — define a single actor goal, its interface, and falsifiable acceptance criteria. [PAPI SDLC]
---

# SDLC Task - User Stories

## When to use this skill

Use this skill whenever a unit of product or system behaviour needs to be
captured from the perspective of a specific actor — whether for backlog
grooming, epic decomposition, or as the specification source for a development
or component task.

## When to use this skill (continued)

- Read, copy and use the appropriate template.
- Create the parent document first if one does not yet exist for the product/epic.
- Each individual story document links back to its parent, and the parent indexes all child stories.

## Dependencies

Reading these skills is REQUIRED to understand and execute this skill:

- PAPI skill `papi-sdlc-understand`
- PAPI skill `papi-templates-understand`

## Core principles

### One story, one actor, one goal

A user story describes a single outcome for a single role. If the narrative
requires more than one actor or more than one goal, split it into separate
stories. Compound stories indicate unclear scope and produce untestable
acceptance criteria.

### Specific roles, not "user"

The actor must identify a real, distinguishable role with distinct needs
(e.g., "authenticated administrator", "background job scheduler",
"third-party API consumer"). Generic actors like "user" or "system" are
not acceptable — they obscure who actually benefits and make the story
harder to prioritise and validate.

### Goals state *what*, not *how*

The "I want to" clause must describe a goal, not an implementation. If the
narrative specifies a UI control, an API endpoint, or an algorithm, it has
crossed into solution space. Reserve implementation decisions for the
development or component task that fulfils the story.

### Falsifiable benefit

The "so that" clause must describe an outcome that can be confirmed or
refuted through the interface described in the story. If the benefit cannot
be observed or measured, it is not a valid acceptance criterion anchor and
the story needs to be rewritten.

### Interface before criteria

Before writing acceptance criteria, the Interface section must clearly
describe how the actor initiates the interaction and what observable
response or state change they receive. Acceptance criteria must assert
outcomes expressed in terms of that interface — not internal system state
or implementation details.

### Negative and boundary cases are required

Every story must include at least one acceptance criterion covering a
negative case (e.g., invalid input, unauthorised access, resource not found)
or a boundary condition. Stories with only happy-path criteria are
incomplete.

### Stories are not tasks, and carry no evidence

A user story is a specification artefact, not a work item. Once a story
reaches **Ready** status, one or more development or component tasks are
created to fulfil it. The story remains as the authoritative statement of
intent and is linked from those tasks.

The story document must not contain implementation notes, test results,
fulfilment status, or audit findings. Those belong in task, testing,
release, or audit artefacts. The story's only lifecycle signal is its
**Status** field.

### Stories know nothing about component specifications

A user story is an upstream statement of intent and MUST NOT reference
component specifications, capability codes, or any other solution
structure. The dependency points the other way: the user-facing
components that fulfil a story reference *it* from their capability
`**Users:**` fields (see the `papi-sdlc-component-specification` skill),
never the reverse. This keeps stories stable when the architecture is
refactored.

### Stories are written in the actor's language

Narrative, interface, and acceptance criteria must use vocabulary the
named role would actually use. Reviewer check: would this role read the
story and recognise their own world? If not, rewrite.

### Status reflects scope

A story's **Status** must be consistent with the scope of its parent
epic/release. Stories outside current scope stay **Draft** (or are
removed). Do not mark a story **Ready** unless its scope agrees with
that of its parent epic/release.

## Checklist when creating a user story

- [ ] ID assigned (unique within the epic or backlog)
- [ ] Actor is specific and distinguishable — not "user" or "system"
- [ ] Goal states what the actor achieves, not how the system implements it
- [ ] Benefit is falsifiable — it can be confirmed through the interface
- [ ] Interface section describes the observable interaction and response
- [ ] At least two acceptance criteria written in Given / When / Then form
- [ ] At least one negative or boundary acceptance criterion included
- [ ] All criteria are assertable through the interface, not internal state
- [ ] Story contains exactly one actor and one primary goal (split if not)
- [ ] `**Role:**` field set, matches the narrative actor, and matches a role defined in the parent user-stories document
- [ ] Story body is free of capability codes and component-spec references
- [ ] Wording uses language the named role would recognise
- [ ] No implementation / test / fulfilment / audit evidence in story body
- [ ] Status (Draft / Ready / In Progress / Done) matches parent scope
- [ ] Notes section used for dependencies or constraints (omit if none)

## Skill artefacts

- **Parent template** (overarching index + roles): `assets/user-stories-template.md`
- **Child template** (individual story): `assets/user-story-template.md`
