---
applyTo: '**'
---

# PAPI Instructions

## PAPI

**PAPI = 'Proceed As Per Instructions'.**

PAPI is a methodology for structuring work with AI assistants. It uses a combination of agent instructions and skills, along with process-guiding task templates to ensure faithful adherence to business requirements and maintainability.

## PAPI SDLC

PAPI SDLC is a specification-driven, test-driven development framework that extends basic PAPI.

Specifications are the primary source of truth: code is written to satisfy specs, meaningful tests are written before code, and bidirectional synchronisation between specifications and all output artefacts (code, documentation, configuration, etc.) is continuously maintained. All work proceeds under human-in-the-loop oversight.

## Guidelines

- Decision-making priority: use sources of truth (requirements, specs, references, …) first, then repository artefacts, web searches, other docs, and your own knowledge last.
- Avoid creating code or docs over 1000 lines - suggest splitting any that exceed this, or may exceed this after editing.
- When you identify ambiguities, gaps, or mistakes, INFORM THE USER with suggested improvements.
- Work autonomously: continue working as long as possible; only stop when truly necessary and leave project in resumable state.
- File operations: use `--update=none` option for `cp` and `mv` commands
  - these avoid overwriting existing files, and
  - are typically auto approved, saving us all time.
- Date, time, and timestamps: always use the `date` command for these EVERY time; do not guess or estimate or work from memory.
- Language and style: maintain professionalism, avoid emojis.

## Definitions

- **Session:**  A single contiguous span of work, up to approx. 20 minutes for a human or 5 minutes for pure, uninterrupted AI work.
- **Task:** The fundamental unit of work in this methodology.
