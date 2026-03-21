---
name: papi-templates-understand
description: Understand and manage templates—read this EACH time you consider/encounter them or wish to update them, delete them, or create new ones. [PAPI]
---

- A PAPI template is both a template for creating a document, and a process outline.
- Process *guidelines* are provided in the template.
- Guidelines can include:
  - Instructions on how to fill in the template.
  - Placeholders that need to be replaced with relevant content.
  - Questions to be answered.
  - Other relevant information.
  - Often, guidelines are in `[…]` delimiters, but not if they need to be retained in the output doc.
- If your instruction do not EXPLICITLY include the locations for template docs, inform the user.
- Assets within this skill:
  - **Base template**: `assets/base-template.md`

## Managing templates

- Creating, updating, or deleting templates is typically a basic task.

### Creating a new template.

- The basis should be the least generic existing template that accommodates your specific requirements.
- If no existing template fits well, fall back to `base-template.md`.
- As a general rule, keep everything in from the template being used as the basis.
- In the new template, note the template it was based on.

### Updating an existing template.

- If the template is based on another template, keep the updated template as close as possible to the basis template, while still meeting requirements.
  - If this is not possible, consider if the updated template
    - needs to be 'rebased' on a new existing template, or
    - if a new base template is needed.

### Deleting a template.

- If other templates are based on the template being deleted, they each will need to be updated.
