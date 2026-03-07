# PAPI

**PAPI** (*Proceed As Per Instructions*) is an opinionated, 
hand-crafted, collection of agentic skills to facilitate work with AI
agents on substantial and ongoing software engineering tasks. If one-shotting
simple games is your thing, then PAPI is not for you.

## Please, no, not another one!

PAPI is my attempt to distil and share 40+ years of software development
experience into something unique, practical, and designed to work well
with current AIs.

## Opinionated you say

It's opinionated because, for example, it expects code to maintain
links (typically in the  code comments) back to *capabilities* (feature
points, etc.) in the specs, and it expects all work to be planned as
executed as *tasks*.

## The essentials

As AI-assisted devs, our role is becoming more about keeping the specs in sync
with the code, than writing the actual lines. I think the trick to keep
this scalable and avoiding context melt-down is to enable an AI to work
easily on parts of the project, without needing to understand the
whole thing. To facilitate this, PAPI allows AI to navigate between
bite-sized components and their corresponding specs, and to understand
the 'nearest' dependencies between them.

PAPI is designed to:

- Maintain synch between specs and code, documentation, and other artefacts.
- Provide spec-driven and test-driven development (TDD) processes.
- Manage non-trivial projects by breaking them into interdependent components
  - the lowest sub-components are sized appropriately for AI work.
- Use a simple task workflow to manage work.
- Maintain links back from code (and other artefacts) to the relevant part of
  the specs.
- Templates are used to assist with document generations for tasks, specs, etc.

It's my hope that these practices will expedite software development, and
lead to software that's faithful to requirements, understandable,
maintainable, testable, and reliable. Perhaps even more so than traditional
approaches.

### Components

> Components are the building blocks of PAPI projects, and in PAPI 
have a very broad definition: they can be software components, whole
applications, and also databases, runtimes, libraries, even documents
or whole OSes.

Components can be esoteric e.g. an 'MVP Release' can be a component.
The top-level component is typically the whole project.
See the *Reference Architectures* doc for some more examples.

### Capabilities

Capabilities are the features or functions that a component provides.

> All interdependencies between components are specified as a capability in one
component depending on a capability in another.

Each component specification has a *capability matrix* that forms a dependency
DAG. Often this is close to a tree structure. The DAG is what wires the
whole project together. There is a skill (with a script) to check the DAG.

## How to use

Clone or download the project. Add the `instructions` and `skills` directories
to your AI scaffolding settings, and then use as needed.
E.g. "Let's do <some SDLC task> ... use PAPI".

### What to watch out for

Current AI is not always great at following instructions, hence this section.
Be familiar with the core concepts and component model docs (see links below).

For example, correct it and/or revert changes when:

- It tries to do any non-trivial work without creating a task for it.
- It tries to skip the testing (red phase) part of TDD, or
  it's red phase tests are superficial.
- It tries to shortcut template use by just reading the template
  and one-shotting the output doc from memory.
  Certain PAPI skills rely on minimal skill text with a good
  deal of instruction embedded into templates. The AI is supposed
  to copy the template verbatim then edit the copy section-by-section.
- It has a propensity to try to be lazy and write-off some capabilities as
  'non-functional requirements' (and then mostly ignore them). This usually
  means components and/or capabilities are missing that need to be added to
  cover these requirements.

There are also audit skills you should use regularly.

## But does it work?

I'm using it right now. I've honed this over a number of private
projects so far over months—it's not faultless but it's definitely
getting work done.

Please get in touch if you find it useful or have ideas or other feedback.

## Will it work with my project?

PAPI is opinionated: it has its own task workflow, and its own way of
working with specs and files. It probably won't integrate well with ticket
tracking systems and other automations. It expects the code to have refs
(typically in comments) that point to the capabilities it implements in the
component specs.

If all of this sounds OK, then PAPI is an option for you. There is an
assimilation skill to help you move your project to PAPI, but it's pretty
much untested right now.

## More reading

- **[Instructions](./instructions/papi.instructions.md)** — Quick overview of PAPI and its key definitions - the only instruction file.
- **[Core Principles](./skills/papi-sdlc-understand/references/core-principles.md)** — Philosophy and decision-making rules.
- **[Component Model](./skills/papi-sdlc-understand/references/component-model.md)** — How to organize projects as a set of components.
- **[Tasks](./skills/papi-tasks-understand/SKILL.md)** — Understand the task workflow.
- **[Assimilate](./skills/papi-sdlc-assimilate/SKILL.md)** — Integrate existing projects into PAPI methodology.
- **[Autonomous Work](./skills/papi-autonomous-work/SKILL.md)** — Work on all or some planned or active tasks autonomously (as much as is practicable)
- **[Reference Architectures](./skills/papi-sdlc-onboard/references/reference-architectures.md)** — Suggested architectural patterns.

## Skill Catalog

Here is an overview of all skills:

- **[Skills Catalog](./SKILLS_CATALOG.md)** — Complete listing of all instructions and skills with descriptions and contents.

## Yes, it's FOSS

This project is released under the MIT License.

## Was this written by AI?

No, but I do like em-dashes!


## Recommended AI models

Anthropic's models win hands down currently.

**Specification work:** Claude Opus.

**Coding work:** Also Opus if you can afford it. Otherwise Sonnet - but expect a
higher number of missteps, which often negates the savings.
