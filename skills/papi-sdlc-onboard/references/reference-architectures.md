# PAPI Reference Architectures

When onboarding a new project or assimilating an existing one into the PAPI methodology, choosing the right component hierarchy is critical. The hierarchy must reflect containment, manage dependencies cleanly, and avoid "virtual" or empty grouping namespaces.

Below are example hierarchies illustrating how the PAPI component model can be applied to common project types. These are starting points for discussion, not prescriptive rules — adapt them to the project at hand.

## 1. The Application with Release Cycles

For applications that have distinct release versions (e.g., MVP, v1.0, v2.0) where features are shared or evolve across releases.

**Key Pattern:** `RELEASE`, `USER_STORIES`, and `DOCS` all sit at the project level as siblings to the application. `RELEASE` sub-components are **composition components** — they declare no capabilities of their own, but depend on capabilities from `COOLAPP.APP`. `USER_STORIES` captures BA-level stories and audits how well the current system fulfils them. `DOCS` owns human-facing project documentation. The Editions table on `COOLAPP.RELEASE` tracks the overall lifecycle of release management.

```text
COOLAPP                                     # The Project (Top-level)
├── COOLAPP.APP                             # The Application itself
│   ├── COOLAPP.APP.AUTH                    # Feature: Authentication
│   │   └── CAP.LOGIN
│   └── COOLAPP.APP.SEARCH                  # Feature: Search
│       ├── CAP.BASIC_SEARCH
│       └── CAP.ADVANCED_SEARCH
├── COOLAPP.RELEASE                         # Release container
│   ├── COOLAPP.RELEASE.MVP                 # MVP Release
│   │   # depends on: COOLAPP.APP.AUTH.CAP.LOGIN
│   │   # depends on: COOLAPP.APP.SEARCH.CAP.BASIC_SEARCH
│   └── COOLAPP.RELEASE.V2                  # V2 Release
│       # depends on: COOLAPP.APP.AUTH.CAP.LOGIN
│       # depends on: COOLAPP.APP.SEARCH.CAP.BASIC_SEARCH
│       # depends on: COOLAPP.APP.SEARCH.CAP.ADVANCED_SEARCH
├── COOLAPP.USER_STORIES                    # BA-level user stories & fulfilment audit
│   ├── CAP.STORY_CATALOGUE                 # The full set of use-case stories
│   └── CAP.FULFILMENT_AUDIT               # How well the current system covers them
└── COOLAPP.DOCS                            # Project documentation
    ├── COOLAPP.DOCS.README                 # Project README
    │   └── CAP.README
    └── COOLAPP.DOCS.LICENSE                # License (optional)
        └── CAP.LICENSE
```

### Deep Dive: The Release Component

`COOLAPP.RELEASE` and its sub-components contain no feature implementation code. They are pure **composition components** — their specifications declare which capabilities from `COOLAPP.APP` are included in that release.

1.  **The Spec Files:**
    - `COOLAPP.RELEASE` spec (`docs/components/coolapp/release/release.md`) describes the release management structure and lists sub-components.
    - `COOLAPP.RELEASE.MVP` spec (`docs/components/coolapp/release/mvp.md`) lists exactly which `COOLAPP.APP.*` capabilities constitute the MVP.
    - `COOLAPP.RELEASE.V2` spec adds additional capabilities on top.
2.  **Dependencies are the point:** `COOLAPP.RELEASE.MVP` depends on `COOLAPP.APP.AUTH.CAP.LOGIN` and `COOLAPP.APP.SEARCH.CAP.BASIC_SEARCH`. This is the formal definition of what ships in the MVP.
3.  **Testing:** Each release component has E2E/smoke tests that verify the *composed* set of capabilities works together. Feature-level tests live in `COOLAPP.APP.*`, not here.
4.  **Bug Fixes:** A bug fix touches `COOLAPP.APP.AUTH` (a new Edition of that spec if the contract changes, otherwise just the code). The `COOLAPP.RELEASE.MVP` spec is unchanged — the dependency it declares is still `AUTH.CAP.LOGIN`, which now has a correct implementation.
5.  **New Releases:** Adding V3 means creating a new `COOLAPP.RELEASE.V3` spec that declares its dependencies. `COOLAPP.RELEASE` itself gains a new sub-component entry, but its own spec stays thin.

**Why this works:**
- `RELEASE` sits at project level - releases are a project concern, not buried inside the app.
- Feature components (`COOLAPP.APP.*`) have their own independent lifecycle, tested and specced without any knowledge of releases.
- A release is nothing more than a formal declaration of which feature capabilities it composes.
- Bug fixes to features never require changes to release specs — the dependency contract stays the same, only the implementation improves.

### Deep Dive: The User Stories Component

`COOLAPP.USER_STORIES` is a **cross-cutting analysis component**. It does not implement any product feature; instead it holds the BA-level use cases for the entire project and provides a formal mechanism for auditing how well the implemented capabilities satisfy those stories.

1.  **`CAP.STORY_CATALOGUE`:** The authoritative list of user stories, written at BA level (actor + goal + outcome). Stories reference the `COOLAPP.APP.*` capabilities that are expected to fulfil them, but do not own or duplicate those capabilities.
2.  **`CAP.FULFILMENT_AUDIT`:** A structured audit report (or living document) produced by examining `COOLAPP.APP.*` capabilities against each story. For each story it records: *Fully Met*, *Partially Met*, or *Not Met*, with notes on gaps.
3.  **Lifecycle:** The story catalogue evolves as product requirements change. The fulfilment audit is re-run whenever a significant batch of capabilities is delivered — typically at release boundaries. This makes coverage gaps visible before shipping.
4.  **No sub-components by default:** Unless the story set is very large, keep `COOLAPP.USER_STORIES` flat. If stories naturally cluster by domain (e.g., `USER_STORIES.CHECKOUT`, `USER_STORIES.ACCOUNT`), sub-components may be added — but only when the grouping genuinely aids navigation.
5.  **Relationship to releases:** A release spec may declare an _informative_ dependency on a story to show traceability ("this release fulfils story X"), but the story component never owns feature capabilities and can never block a release.

**Why this works:**
- Stories live in one authoritative place rather than scattered across tickets or wikis.
- The audit is a first-class PAPI artefact — it has a spec, can be assigned, and has a completion state.
- Separating story ownership from feature ownership means the BA can evolve stories independently of the engineering team.

### Deep Dive: The Docs Component

`COOLAPP.DOCS` owns human-facing project documentation — the kind of content that lives in a repository root and is read by contributors, users, or legal stakeholders, not by the runtime system.

1.  **`COOLAPP.DOCS.README` / `CAP.README`:** The project's top-level `README.md`. Covers what the project is, how to get started, and where to find more detail. This sub-component is always present.
2.  **`COOLAPP.DOCS.LICENSE` / `CAP.LICENSE`** *(optional):* The `LICENSE.md` (or `LICENSE`) file. Include this sub-component when the licence file itself must be tracked as a managed artefact (e.g., for open-source or dual-licence projects). For internal tools where there is no licence file, omit it.
3.  **Other sub-components:** Additional sub-components may be added for substantive documentation artefacts — e.g., `COOLAPP.DOCS.ARCHITECTURE` for an architecture decision record index, `COOLAPP.DOCS.CHANGELOG` for a curated changelog. Only add sub-components when the content is significant enough to warrant its own lifecycle.
4.  **Not a dumping ground:** `DOCS` is for *project-level* documentation. Feature-level documentation (inline docs, API references) belongs in the relevant `COOLAPP.APP.*` component. Do not move component specs here — they remain with their component.

**Why this works:**
- Documentation artefacts become first-class PAPI components — they get specs, owners, and completion states.
- The README and LICENSE are no longer forgotten: if `CAP.README` is incomplete, the project's PAPI health reflects that.
- Keeps the `APP` sub-tree clean by giving documentation a dedicated home at project level.

## 2. The Monorepo / Multi-Service System

For projects that contain multiple independent deployable services, shared libraries, and frontends.

**Key Pattern:** Group by deployable unit. Shared code is extracted into components that the services depend on.

```text
ECOMMERCE                           # The Project
├── ECOMMERCE.STOREFRONT            # The Web Frontend
│   └── CAP.BROWSE_PRODUCTS
├── ECOMMERCE.CATALOG               # The Backend API
│   └── CAP.PRODUCT_LOOKUP
├── ECOMMERCE.PAYMENT               # Another Backend API
│   └── CAP.PROCESS_CHARGE
└── ECOMMERCE.SHARED_MODELS         # Shared data structures
    └── CAP.DATA_TYPES
```

**Why this works:**
- Clear boundaries between deployable artifacts.
- `ECOMMERCE.STOREFRONT` depends on `ECOMMERCE.CATALOG.CAP.PRODUCT_LOOKUP`.
- Both services depend on `ECOMMERCE.SHARED_MODELS.CAP.DATA_TYPES`.

## 3. The Standalone Library / Package

For projects whose sole purpose is to be consumed by other projects (e.g., an npm package, a Rust crate).

**Key Pattern:** The project root is the top-level component. Its sub-components represent the internal modules of the library.

```text
DATA_PARSER                         # The Project / Package
├── DATA_PARSER.CSV                 # Internal module
│   └── CAP.PARSE_CSV
├── DATA_PARSER.JSON                # Internal module
│   └── CAP.PARSE_JSON
└── DATA_PARSER.CORE                # Shared internal logic
    └── CAP.STREAM_READER
```

**Why this works:**
- External consumers will depend on `X.LIB.DATA_PARSER.CAP.PARSE_CSV`.
- Internal containment reflects the module structure of the code.

## 4. The Small App (No Release Cycle)

For a small application that is deployed as a single unit with no formal release versioning — a personal tool, internal dashboard, or simple service.

**Key Pattern:** Flat hierarchy. No `RELEASE` component needed. The project root directly contains the functional sub-components.

```text
MYTOOL                              # The Project (Top-level)
├── MYTOOL.CLI                      # CLI interface
│   └── CAP.RUN_COMMAND
├── MYTOOL.CORE                     # Business logic
│   └── CAP.PROCESS_INPUT
└── MYTOOL.CONFIG                   # Configuration handling
    └── CAP.LOAD_CONFIG
```

**Why this works:**
- No release ceremony needed — the project *is* the thing being shipped.
- Keeps the hierarchy shallow and easy to navigate.
- If the project grows and release management becomes needed, `MYTOOL.RELEASE` can be added later.

## 5. The One-Off Script / Single-Component Tool

For a simple script or utility with no meaningful internal structure worth decomposing.

**Key Pattern:** The project root is the only component. Capabilities are documented directly on it.

```text
BACKUP_SCRIPT                       # The Project and only component
    └── CAP.BACKUP_FILES
    └── CAP.RESTORE_FILES
```

**Why this works:**
- Overhead of sub-components is not justified for a single-file tool.
- Still gets full PAPI traceability (spec, capabilities, tests) without artificial structure.
- If the tool grows, sub-components can be introduced at that point.

## 6. The App with Releases but No Multi-Artifact Deployment

For a moderately sized app with release versions, but where each release is a single deployable artifact (e.g., a single binary or single web app). A simplified variant of Example 1.

```text
COOLAPP                             # The Project (Top-level)
├── COOLAPP.APP                     # The Application
│   ├── COOLAPP.APP.AUTH            # Feature: Authentication
│   │   └── CAP.LOGIN
│   └── COOLAPP.APP.SEARCH          # Feature: Search
│       ├── CAP.BASIC_SEARCH
│       └── CAP.ADVANCED_SEARCH
├── COOLAPP.RELEASE                 # Release component (single deployable per release)
│   ├── COOLAPP.RELEASE.MVP         # depends on: AUTH.CAP.LOGIN, SEARCH.CAP.BASIC_SEARCH
│   └── COOLAPP.RELEASE.V2          # depends on: AUTH.CAP.LOGIN, SEARCH.CAP.ADVANCED_SEARCH
├── COOLAPP.USER_STORIES            # BA-level user stories & fulfilment audit
│   ├── CAP.STORY_CATALOGUE
│   └── CAP.FULFILMENT_AUDIT
└── COOLAPP.DOCS                    # Project documentation
    ├── COOLAPP.DOCS.README
    │   └── CAP.README
    └── COOLAPP.DOCS.LICENSE        # (optional)
        └── CAP.LICENSE
```

This is the same as Example 1 but without the `API`/`WEB` split under each release. Use this when there is only one deployable artifact per release.

## Anti-Patterns to Avoid

1. **The "Virtual" Folder:** Creating a dot-notation path like `MYAPP.FEATURES.AUTH` where `FEATURES` has no specification file and provides no capabilities. Every segment in the dot-notation MUST be a real component.
2. **Release Capabilities Duplicating Feature Capabilities:** Defining `COOLAPP.RELEASE.MVP.CAP.LOGIN` when `COOLAPP.APP.AUTH.CAP.LOGIN` already exists. Release components compose capabilities — they do not re-define them.
3. **Features Owned by Releases:** Putting feature components *inside* a release component (e.g., `COOLAPP.RELEASE.MVP.AUTH`). Features outlive any single release and belong in the app, not the release sub-tree.
4. **Release Buried Inside the App:** Nesting releases under `COOLAPP.APP.RELEASE` implies releases are an internal implementation detail of the app. They are a project-level concern and belong at `COOLAPP.RELEASE`.
