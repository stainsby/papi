---
name: papi-long-task
description: Manage a task with many repeated steps, or a long running task with many steps, so that it is tracked and resumable over more than one session if needed.
---

# Long Task

## Inputs

Any of these:

* A sub-task that is repeated many times possibly with a list of items such that the sub-task should be applied to each item.
* A specification that generates such a list, either up front, or as the task progresses (dynamic list).

## Actions

Steps:

1. If possible, initially create (and then maintain) the list of items or steps as a simple checklist.
  * If the list is dynamic, this can just be wahtever is known initially.
2. For each item:
  (a) Perform the sub-task for THIS item BEFORE moving to the next item:
    * THIS is CRITICALLY IMPORTANT TO KEEP FOCUS AND NOT MISS DETAILS:
    * slow and steady, one at a time
    * do not try to 'batch' for performance/efficiency
    * checkpoint after each aub-task
  (b) Check the item off on the list.
  (c) Add any newly discovered items to the list if the list is dynamic.

## Stepwise gated tasks

ONLY if the user asks for it, gate each subsequent subtask by:

* summarising the results of the task just done
* asking a multi-choice question on whether to continue to the next sub-task
  * should equate to a Yes/No/Other-style question
* use the same gating mechanism if you have any queries that block progress

## Track additional items

ONLY if the user asks for it, track additional items and/or sub-tasks in a file:

* create a non-tracked file if file is not specified, otherwise use their file
* items may be added to the file dynamically by users, so keep rechecking the file for new items
  * don't be surprised if the file changes without your knowledge
  * items might disappear if the user leans up the list - this does not mean the corresponding sub-tasks should be deleted or undone
  * typically this works best with stepwise gated tasks (so perhaps ask if this has not been specified)
