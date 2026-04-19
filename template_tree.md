# PAPI Template Hierarchy

All templates are stored under `skills/<skill-name>/assets/`.
Each template records its derivation in its preamble instructions block.

```text
base-template.md                               (papi-templates-understand)
├── basic-task-template.md                     (papi-tasks-understand)
│   ├── development-task-template.md           (papi-sdlc-task-development)
│   │   ├── fix-task-template.md               (papi-sdlc-fix)
│   │   ├── sprint-task-template.md            (papi-sdlc-sprint)
│   │   └── component-task-template.md         (papi-sdlc-task-component)
│   ├── codebase-assimilation-task-template.md (papi-sdlc-assimilate)
│   ├── process-improvement-audit-task-template.md  (papi-process-improvement)
│   ├── compliance-audit-task-template.md      (papi-sdlc-task-compliance-audit)
│   └── fulfilment-audit-task-template.md      (papi-sdlc-task-fulfilment-audit)
├── component-specification-template.md        (papi-sdlc-component-specification)
├── user-stories-template.md                   (papi-sdlc-user-stories)
└── user-story-template.md                     (papi-sdlc-user-stories)
```

## Notes

- user-stories-template.md is the parent INDEX document for a product/epic;
  user-story-template.md is for individual story entries. Both derive from
  base-template.md but are used together in a parent-child document relationship.
- fulfilment-audit-task-template.md mirrors the structure of
  compliance-audit-task-template.md and both derive independently from
  basic-task-template.md. A compliance audit must precede a fulfilment
  audit in the SDLC process, but this is a workflow ordering, not a
  template derivation relationship.
