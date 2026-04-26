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
  - However be proactive with flagging pre-existing errors or issues, or adding suggestions, in the final output
- File operations: use `--update=none` option for `cp` and `mv` commands
  - these avoid overwriting existing files
  - if source control such as `git` is in use, use `git mv` for moving tracked files
- Date, time, and timestamps: always use the `date` command for these EVERY time; do not guess or estimate or work from memory.
- Language and style: maintain professionalism, avoid emojis.

## Definitions

- **Session:**  A single contiguous span of work, up to approx. 20 minutes for a human or 5 minutes for pure, uninterrupted AI work.
- **Task:** The fundamental unit of work in this methodology.


## Using a template

- FIRST: ALWAYS COPY the template verbatim to create the initial output document
  - DO NOT attempt to rewrite the document from memory
  - DO NOT attempt to edit the output during the copy stage
  - DO use an tools (CLI command, IDE tool, etc.) to copy the template verbatim
- NEXT: READ 100% of the template
- THEN: proceed INCREMENTALLY through the template:
    - Read ONE section ONLY
    - Follow the section's instructions and fill in any details requested
    - Proceed to the next section and repeat until all sections are completed
- When editing a section, follow the process outlined in the template:
  - Guidelines that are in `[…]` delimiters should be deleted from the output.
  - ANY text not in `[…]` should be retained.
  - Sometimes guidelines are not in `[…]` — these should be retained to guide future edits.
- REMEMBER: go slow and steady: complete one section at a time

## Skill artefacts

Skill artefacts (assets, references, scripts,…) listed in a skill are listed 
in the skill with a path that is relative to the directory containing the
`SKILL.md` file.

### Checklists

- Use the following for the status of items in a checklist:
  - non-final states:
    - [ ] To do, not considered, not started or not checked yet. Optional agency indicators:
      - [ ] ✨ intended for an AI
      - [ ] 🏃 intended for a human
    - ⏳ in progress or under consideration. Optional agency indicators:
      - ⏳ ✨ by an AI
      - ⏳ 🏃 by a human
    - ⏸️ paused. Optional agency indicators:
      - ⏸️ ✨ awaiting an AI
      - ⏸️ 🏃 awaiting a human
  - Finalised checklists should only contain these final states:
    - ✅ Completed
    - ❌ Failed, or not completed fully or satisfactorily
    - ❓ Uncertain, unknown or unable to be determined
    - 🚫 Blocked, or won't do, or not applicable
