---
artifact: PROJECT-CONTEXT
project: Single-page design portfolio
profile: Lite
execution_mode: Gated
created: 2026-08-18
updated: 2026-08-18
---

# Project Context

## 1. Project

- Project name: Single-page design portfolio
- Goal: Implement the scoped Figma design as an accessible, responsive single-page portfolio in the existing Astro frontend.
- Project type: Static page
- Selected profile: Lite
- Profile rationale: The result is one static responsive page with several tightly related sections and reusable patterns. It exceeds Express's one-task constraint, while current evidence shows no routing, persistence, authentication, external API, migration, or other architectural risk that requires Standard or Full.
- Created: 2026-08-18
- Last updated: 2026-08-18

## 2. Active Source Baseline

- Source baseline: `SOURCE-BASELINE.md`
- Design snapshots: `SRC-DS-001`
- Repository snapshots: `SRC-REPO-001`
- Runtime snapshots: None
- Documentation snapshots: None
- Asset snapshots: None

## 3. Design Scope

- Included: Figma page `🤖 Workflow` (`2141:862`), responsive Home frames, section/navigation components, local states, design-system documentation, and referenced assets needed to reproduce the page.
- Explicitly excluded: Other Figma pages and unrelated file-global visual changes.
- Access limitations: The Figma URL is mutable and no named immutable version was supplied.
- Known design-source dependencies: Local Figma components, styles/variables, image/vector assets, and responsive variants contained in the scoped page.

## 4. Repository Scope

- Target branch policy: Work on a dedicated branch and merge through pull request; `main` is the baseline, not the implementation work branch.
- Relevant application, package, or directory: `frontend/`
- Existing implementation state: Astro starter page; `frontend/src/pages/index.astro` renders `Welcome.astro`.
- Known technical constraints: Astro + TypeScript, pnpm, Node 24.x; follow root and `frontend/AGENTS.md`, including background Astro dev-server guidance when local runtime work begins.
- Access or tooling limitations: Workflow initialization is being committed through the connected GitHub interface; later implementation must use the repository's normal branch/PR/preview verification policy.

## 5. Runtime References

- Production snapshot: None registered
- Preview or staging snapshot: None
- Local runtime snapshot: None

## 6. Scope

### Included

- Design audit of the scoped Figma source.
- Requirements, design intent, behavior specification, implementation planning, task decomposition, Astro implementation, accessibility/responsive work, and final validation for the single portfolio page.
- Existing repository and deployment constraints required to integrate the page safely.

### Excluded

- Structural or visual edits to Figma pages outside `🤖 Workflow`.
- New product features not supported by the design/source evidence.
- Backend, authentication, persistence, or API work unless later evidence explicitly expands scope.

### Deferred

- Runtime/deployment snapshot registration until it is needed for preview or final validation.
- Architecture decision until the workflow reaches its architecture checkpoint.

## 7. Authoritative Sources

| Snapshot ID | Authority | Scope | Notes |
|---|---|---|---|
| `SRC-DS-001` | Design | Visual hierarchy, responsive layouts, components, states, and design-system evidence | Time-bound Figma scope |
| `SRC-REPO-001` | Current implementation / Technical constraint | Astro project structure, tooling, repository policy, existing starter state | Immutable commit baseline |

## 8. Quality Baseline

- Accessibility: Semantic, keyboard-accessible, contrast-aware implementation with visible focus and resilient text/reflow behavior; exact acceptance checks will be defined from source evidence.
- Responsive coverage: Reproduce the observed mobile, tablet, and desktop compositions; derive implementation breakpoints from design evidence and layout behavior rather than arbitrary device presets.
- Browser/device coverage: To be made explicit during specification/planning from project constraints; do not invent unsupported browser targets.
- Performance: Preserve a lightweight static Astro implementation and avoid unnecessary client JavaScript.
- Security/privacy: No sensitive data flow is in current scope.
- Testing: Build plus targeted accessibility, responsive, and visual verification appropriate to the implementation tasks.
- Deployment: Use branch → pull request → Vercel preview → verification → merge. Do not manually promote production unless explicitly requested.

## 9. Constraints and Dependencies

| ID | Constraint or dependency | Evidence or snapshot | Impact | Status |
|---|---|---|---|---|
| `REQ-CON-001` | Implement inside `frontend/` and follow repository/nested AGENTS instructions | `SRC-REPO-001` | Governs code structure and commands | Confirmed |
| `REQ-CON-002` | Figma editing/inspection scope is `🤖 Workflow`; do not modify other pages without explicit request | `SRC-DS-001`, `SRC-REPO-001` | Prevents source drift | Confirmed |
| `REQ-CON-003` | Use gated workflow progression and do not advance stages without explicit approval | `SRC-REPO-001` | Requires user gate between stages | Confirmed |
| `REQ-CON-004` | Figma input is time-bound and must be reverified before material downstream work | `SRC-DS-001` | Requires source-change checks | Confirmed |

## 10. Known Decisions

| Decision | Owner | Evidence or snapshot | Status |
|---|---|---|---|
| Use Lite profile | Workflow | `SRC-DS-001`, `SRC-REPO-001` | Proposed for Stage 0 approval |
| Use Gated execution mode | Project contract | `SRC-REPO-001` | Confirmed |
| Treat Figma `🤖 Workflow` as design authority | Project contract | `SRC-DS-001`, `SRC-REPO-001` | Confirmed |

## 11. Initial Risks and Questions

### Blocking

- Canonical verification records for `SRC-DS-001` and `SRC-REPO-001` are still required before Stage 0 can close.
- Stage 0 artifacts and gate require explicit approval before advancement.

### Non-blocking

- The design source is time-bound rather than immutable, so later source verification is mandatory.
- Runtime evidence is intentionally not active yet; it can be registered when preview/final validation needs it.

## 12. Stage 0 Completion

- [x] Scope is explicit.
- [x] `SOURCE-BASELINE.md` exists.
- [x] Design and repository snapshot IDs and pin strengths are explicit.
- [x] Repository baseline uses a commit SHA.
- [x] Lite profile and Gated mode are justified.
- [x] Quality expectations are evidence-based and avoid unsupported details.
- [x] Source limitations are visible.
- [x] `WORKFLOW-STATE.md` uses the same baseline.
- [ ] Canonical source verifications are recorded.
- [ ] Stage 0 approval/gate is recorded.
