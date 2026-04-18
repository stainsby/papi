---
name: papi-autonomous-work
description: Perform work to complete tasks when asked to "work autonomously".
---

## Dependencies

These skills should also be read to use the current skill.

- PAPI skill `papi-tasks-understand`

## Inputs

- the tasks to consider
  - if not specified, this means ALL planned and active tasks

## Actions

- Check and update the statuses of all planned and active tasks
- Analyse the tasks to determine the best order to perform them.
- Implement them all in order if possible:
  - Try to be fully autonomous: if any task is blocked (e.g. by the need for human feedback):
    - note this down for later and
    - proceed to the next possible task instead of stopping for input.
- Ensure all tasks statuses are updated to reflect any work done
- Present the list of deferred blocking points, feedbacks, or other interactions when you have progressed ALL tasks AS FAR AS POSSIBLE without human interaction.
  - Also note down any bugs, or irregularities, gaps, possible improvements, … in anything you see, even if not related to the scope.


## Finishing

At the end of an autonomous work session, you MUST declare that either:

1. You have completed all work within the scope of the original request
  - if no scope was given (e.g. just "work autonomously"), this means declaring that THE ENTIRE PROJECT IS COMPLETED
  - the project CANNOT be complete unless both compliance and fulfilment audits pass.
2  OR, you have progressed all tasks as far as possible without human interaction
  - you must detail every deferred blocking point that requires human interaction to proceed further
