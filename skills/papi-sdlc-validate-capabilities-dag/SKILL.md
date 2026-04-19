---
name: papi-sdlc-validate-capabilities-dag
description: Validate that capability dependencies defined across component specifications form a valid Directed Acyclic Graph (DAG). [PAPI SDLC]
---

# SDLC Task - Validate Capabilities DAG

- Run `validate_capability_dag.py` against the project's component specifications directory.
- The tool checks for:
  - **Cycles** — circular dependencies between capabilities (must be resolved before specs can be considered complete)
  - **Orphans** — nodes with no incoming or outgoing edges (likely missing dependency declarations or dead capabilities)
  - **Invalid references** — capabilities referenced in dependencies that are not defined in any spec
- Pass `--specs-dir` pointing to the directory containing component specification markdown files.
- Pass `--output` to write the report to a file, or omit to print to stdout.
- A non-zero exit code means validation failed; a zero exit code means the DAG is valid.
- Run this after authoring or editing component specifications, and before marking any specification as completed.
- If issues are found, work with the user to resolve them in the affected specification files before proceeding.
- Script within this skill:
  - `scripts/validate_capability_dag.py`

## Dependencies

These skills should also be read to use the current skill.

- PAPI skill `papi-sdlc-understand`
