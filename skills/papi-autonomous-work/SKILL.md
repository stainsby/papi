---
name: papi-autonomous-work
description: Perform work to complete tasks when asked to "work autonomously".
---

## Inputs

- the tasks to consider
  - if not specified, this means ALL planned and active tasks

## Actions

- Analyse the tasks to determine the best order to perform them.
- Implement them all in order if possible:
  - Try to be fully autonomous: if any task is blocked (e.g. by the need for human feedback):
    - note this down for later and
    - proceed to the next possible task instead of stopping for input.
- Present the list of deferred blocking points, feedbacks, or other interactions when you have progressed ALL tasks AS FAR AS POSSIBLE without human interaction.
