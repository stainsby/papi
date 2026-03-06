# PAPI

**PAPI** (*Proceed As Per Instructions*) is an opinionated, 
hand-crafted, collection of agentic skills to facilitate work with AI
agents on software engineering tasks.

## Please, no, not another one!

> Be assured: this is not slop.

PAPI is my attempt to distil 40+ years of software development experience
into something unique, practical, and designed to work well with current
AIs. I'd like to share it.

## The essentials

As AI-assisted devs, our role is becoming more about keeping the specs in sync
with the code, than writing the actual lines. I think the trick is to enable
an AI with limited context to work easily on parts of the project, without
needing to understand the whole thing. To facilitate this, PAPI allows AI to
navigate between bite-sized components and pieces of spec, and to understand
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
or whole OSes. The top-level component is typically the whole project.

### Capabilities

Capabilities are the features or functions that a component provides.

> All interdependencies between components are specified as a capability in one
component depending on a capability in another. This is what wires the whole
project together.

## How to use

Clone or download the project. Add the `instructions` and `skills` directories
to your AI scaffolding settings, and then use as needed.
E.g. Let's create an app to do XYZ using PAPI".

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
