from pathlib import Path

path = Path("IMPLEMENTATION-BRIEF.md")
text = path.read_text()


def replace_between(source: str, start_heading: str, end_heading: str, replacement: str) -> str:
    start = source.index(start_heading)
    end = source.index(end_heading, start)
    return source[:start] + replacement.rstrip() + "\n\n" + source[end:]


text = text.replace(
    "- Current workflow checkpoint: **Stage 6 — Define or explicitly skip architecture**",
    "- Current workflow checkpoint: **Stage 7 — Create the repository-aware implementation plan**",
)
text = text.replace(
    "- Requirements are approved through `GATE-003`, design intent through `GATE-004`, specification through `GATE-005`, and documentation review through `GATE-006`. Stage 6 is active. The architecture checkpoint concludes that a separate architecture artifact is **not required** for this Lite-profile scope; repository-aware planning, task decomposition, and implementation remain intentionally unstarted pending the Stage 6 gate.",
    "- Requirements are approved through `GATE-003`, design intent through `GATE-004`, specification through `GATE-005`, documentation review through `GATE-006`, and architecture through `GATE-007`. Stage 7 is active. Architecture remains **Not required** and the project remains Lite; this checkpoint now owns repository inspection, implementation structure, ordering, dependencies, risks, and validation planning. Stage 8 adversarial review, task decomposition, and implementation remain intentionally unstarted.",
)
text = text.replace(
    "- At Stage 4 authoring time, document review and later checkpoints were not started. Stage 5 is now approved through `GATE-006`; Stage 6 architecture handling is active, while planning, task decomposition, and implementation remain unstarted.",
    "- Stage 5 is approved through `GATE-006` and Stage 6 architecture through `GATE-007`; Stage 7 repository-aware planning is now active, while task decomposition and implementation remain unstarted.",
)

repository_context = """## 5. Repository Context

### Observed implementation baseline

- The immutable implementation input remains `SRC-REPO-001` at commit `07635a8eafb4323909619a0b62e41a4d8144d764`. Current `main` has advanced through workflow/documentation checkpoints only; no `frontend/` implementation change has replaced that baseline.
- The application boundary is `frontend/`, using Astro `^7.2.2`, Node `>=22.12.0`, pnpm, and the repository-confirmed `dev`, `build`, `preview`, and `astro` scripts. No framework integration, carousel library, state library, test runner, linter, accessibility test package, backend dependency, or API client is present.
- `frontend/src/pages/index.astro` is still the Astro starter page and renders `Welcome.astro` inside `Layout.astro`.
- `frontend/src/components/` contains only starter `Welcome.astro`; `frontend/src/layouts/` contains only `Layout.astro`.
- `frontend/src/assets/` contains only starter `astro.svg` and `background.svg`; portfolio/service/profile/Work assets are not yet in the repository. `frontend/public/` contains only the starter favicons.
- Root and frontend `AGENTS.md` files remain authoritative for repository, accessibility, frontend, branch/PR, and deployment behavior.
- The confirmed automated frontend validation command is `pnpm build` from `frontend/`. No test or lint script exists today, so this plan does not invent one.

### Repository-aware implementation structure

The following paths are proposed by Stage 7; proposed paths are not described as existing.

| Path | Action | Existing? | Responsibility |
|---|---|---:|---|
| `frontend/src/pages/index.astro` | Modify | Yes | Replace starter composition with the approved single-page content order and section integration. |
| `frontend/src/layouts/Layout.astro` | Modify | Yes | Document metadata, global stylesheet loading, and page-level semantic shell. |
| `frontend/src/components/Welcome.astro` | Delete | Yes | Remove unused starter UI after replacement. |
| `frontend/src/assets/astro.svg` | Delete | Yes | Remove unused starter artwork. |
| `frontend/src/assets/background.svg` | Delete | Yes | Remove unused starter artwork. |
| `frontend/src/components/Header.astro` | Create | No | Header/logo and dark consultation link. |
| `frontend/src/components/Hero.astro` | Create | No | Hero copy and six-service responsive composition. |
| `frontend/src/components/About.astro` | Create | No | Portrait-led About content and accent consultation link. |
| `frontend/src/components/Work.astro` | Create | No | Static five-item Work markup, accessible carousel structure, controls, and enhancement hooks. |
| `frontend/src/components/Contact.astro` | Create | No | Dark closing CTA section with responsive copy/action layout. |
| `frontend/src/components/Footer.astro` | Create | No | Footer logo and dark consultation link without new navigation. |
| `frontend/src/components/ConsultationLink.astro` | Create | No | Repeated native `href=\"#\"` consultation action with Dark/Accent visual roles. |
| `frontend/src/scripts/work-carousel.ts` | Create | No | Dependency-free progressive enhancement for cyclic one-step Work navigation and live feedback. |
| `frontend/src/styles/global.css` | Create | No | Base/reset rules, source token mappings, typography, page surface, shared focus/layout primitives. |
| `frontend/src/styles/page.css` | Create | No | Static section and service-card layout/responsive rules. |
| `frontend/src/styles/work-carousel.css` | Create | No | No-JS gallery, enhanced track geometry, controls, transitions, and reduced-motion rules. |
| `frontend/src/assets/portfolio/` | Create | No | Exported source assets; exact filenames/formats follow inspected Figma exports. Logical Work slot 05 uses standalone `Asset/Work/05` (`6:380`). |

### Implementation constraints from the repository

- Keep all static content Astro-rendered. Add client JavaScript only for the Work enhancement; do not introduce a framework island or third-party carousel package for this bounded interaction.
- Keep styles in external CSS files rather than inline style attributes.
- Treat 375px, 768px, and 1440px as visual validation anchors. Select actual media-query thresholds from layout failure conditions, not device-name defaults or copied exemplar widths.
- Do not add routes, APIs, persistence, authentication, project-detail links, autoplay, or consultation behavior beyond the approved `href=\"#\"` placeholder.
- Export source assets without changing Figma. Preserve the owner-approved `AUD-009` Work 05 correction.
- Plus Jakarta Sans delivery must be resolved from a permitted source before typography is considered complete; do not silently add an unreviewed runtime service or dependency.
- Existing Astro/Vercel delivery remains the deployment model; this plan adds no deployment-topology or production-promotion change.
"""

implementation_plan = """## 6. Implementation Plan

### PLAN-001 — Replace the Astro starter with the portfolio foundation

- Objective: Establish the real page shell, external CSS foundation, source asset location, semantic structure, and maintainable source-token mappings before section-specific implementation.
- References: `REQ-FR-001`, `REQ-FR-006`, `REQ-AR-001`, `REQ-AR-005`, `REQ-AR-006`, `REQ-NFR-001`, `REQ-NFR-002`; `SPEC-BEH-001`, `SPEC-BEH-003`, `SPEC-ACC-001`, `SPEC-ACC-005`, `SPEC-ACC-006`, `SPEC-VAL-001`, `SPEC-VAL-003`; `AC-001`, `AC-011`, `AC-012`, `AC-015`, `AC-016`.
- Files: modify existing `frontend/src/pages/index.astro` and `frontend/src/layouts/Layout.astro`; create proposed `frontend/src/styles/global.css`, `frontend/src/styles/page.css`, and `frontend/src/assets/portfolio/`; remove starter-only `Welcome.astro`, `astro.svg`, and `background.svg` once unused.
- Approach:
  - Keep one Astro page and one semantic document flow; add no routing or client framework.
  - Map approved typography/color/spacing/radius roles into reusable CSS custom properties or equivalent external CSS primitives instead of scattering raw values.
  - Encode the approved dark-text contrast correction centrally so Accent CTA and affected service labels inherit compliant foregrounds consistently.
  - Establish resilient page insets, widths, typography, and vertical-growth rules supporting 320 CSS px reflow and 200% zoom without fixed-height clipping.
  - Export the required source assets into the portfolio asset directory without a Figma edit; logical Work 05 must use standalone `Asset/Work/05`.
  - Resolve a permitted Plus Jakarta Sans delivery source before finalizing typography; do not add a package or runtime request by assumption.
- Dependencies/order: First implementation slice; `PLAN-002` and `PLAN-003` depend on its shell/style/asset conventions.
- Validation: `pnpm build`; inspect document outline/landmarks; confirm starter UI/assets are no longer referenced; check the foundation at 320 CSS px for page-level horizontal overflow.
- Risks/assumptions: Exact exported filenames/formats and font delivery are implementation inputs not present in the repository; resolve them from approved source/licensing evidence without changing behavior.

### PLAN-002 — Implement static sections with accessibility and responsive behavior integrated

- Objective: Build Header, Hero/services, About, Contact, and Footer as source-faithful Astro sections while implementing native semantics, image meaning, focus states, contrast fixes, reflow, and content-driven responsive transformations in the same slice.
- References: `REQ-FR-001`–`003`, `REQ-FR-006`, `REQ-AR-001`–`007`, `REQ-NFR-001`–`002`; `SPEC-BEH-001`–`003`, `SPEC-INT-001`, `SPEC-ACC-001`, `SPEC-ACC-002`, `SPEC-ACC-004`–`006`, `SPEC-VAL-001`, `SPEC-VAL-003`; `AC-001`–`003`, `AC-008`, `AC-010`–`013`, `AC-015`, `AC-016`.
- Files: create proposed `Header.astro`, `Hero.astro`, `About.astro`, `Contact.astro`, `Footer.astro`, `ConsultationLink.astro`; modify `index.astro`, `page.css`, and portfolio assets.
- Approach:
  - Preserve Hero → About → Work → Contact → Footer order, with the hero title as `h1` and About/Work/Contact as the next section heading level.
  - Render every source-observed consultation action as a native link with literal `href=\"#\"`, preserving Dark/Accent visual roles and visible `:focus-visible` treatment.
  - Render all six service categories once; keep service artwork decorative and apply the approved dark primary text role to UI/UX, Apps, and Photography labels.
  - Render the profile portrait with the approved meaningful alternative text.
  - Implement source-observed narrow/middle/wide relationships while selecting actual CSS transitions from collision, text-measure, image-emphasis, and overflow failure conditions. Allow blocks to grow under wrapping and zoom.
  - Preserve the dark Contact hierarchy and a visually separate Footer; do not invent footer navigation or new destinations.
- Dependencies/order: After `PLAN-001`; does not depend on carousel JavaScript.
- Validation: `pnpm build`; keyboard Tab/Shift+Tab and visible-focus checks; rendered contrast measurement; meaningful/decorative image inspection; visual comparison at 375px/768px/1440px plus intermediate widths, 320 CSS px reflow, and 200% zoom.
- Risks/assumptions: Breakpoint numbers are implementation evidence, not design facts; approved contrast deviations take precedence over pixel-identical reproduction of failing source pairings.

### PLAN-003 — Implement Work as a progressively enhanced cyclic carousel

- Objective: Deliver all five Work items in initial HTML, then add a dependency-free manual carousel matching item-03 start, cyclic one-step behavior, accessibility, neighboring-content cues, failure recovery, and reduced-motion outcomes.
- References: `REQ-FR-004`, `REQ-FR-005`, `REQ-FR-006`, `REQ-AR-002`–`007`, `REQ-NFR-001`, `REQ-NFR-002`; `SPEC-BEH-003`, `SPEC-BEH-004`, `SPEC-INT-002`–`005`, `SPEC-ACC-002`–`004`, `SPEC-ACC-006`, `SPEC-DATA-001`, `SPEC-VAL-001`–`003`; `AC-004`–`010`, `AC-012`–`015`; `AUD-009`.
- Files: create proposed `Work.astro`, `frontend/src/scripts/work-carousel.ts`, `frontend/src/styles/work-carousel.css`; modify `index.astro` and portfolio assets.
- Approach:
  - Server-render logical order 01→05 with item 03 as initial active item and standalone `Asset/Work/05` at slot 05.
  - Default/no-JavaScript presentation is a horizontally reachable five-item gallery. Keep controls hidden/inert until enhancement succeeds so failed initialization exposes no dead controls.
  - Enhancement reveals native Previous/Next buttons, keeps focus on the activated button, advances exactly one logical item, wraps 01↔05, never auto-rotates, and serializes rapid activations so state cannot stop between items.
  - Keep the five originals as semantic slides. If cyclic edge animation requires duplicate visual neighbors, create only client-side clones marked assistive-hidden/non-focusable and snap back to the matching original after transition; clones never become semantic slides or links.
  - Label the carousel from “My Work”; expose “Previous project”/“Next project” button names, slide position context 1-of-5 through 5-of-5, and a polite “Project N of 5” update after manual navigation without moving focus.
  - Match the specified 270×180 mobile active anchor and 540×360 tablet/desktop active anchors while preserving visible neighbors. Choose actual CSS transition points from fit/intermediate-width testing.
  - Use the specified short 200ms ease-out movement when motion is allowed; under `prefers-reduced-motion: reduce`, produce the same logical result without non-essential interpolation.
- Dependencies/order: After `PLAN-001`; may proceed independently of late `PLAN-002` work only when shared file ownership does not conflict.
- Validation: `pnpm build`; no-JS/failure fallback; Enter/Space, pointer/touch, focus retention; item-03 start; one-step movement; both cyclic edges; rapid-input serialization; live-region/slide-label inspection; reduced motion; 375px/768px/1440px plus intermediate-width visual checks; verify all five assets/alts including Work 05.
- Risks/assumptions: Visual clones are implementation-only and must not duplicate assistive content. Prefer a simpler equivalent technique if testing proves clones unnecessary; no carousel package is justified by current scope.

### PLAN-004 — Integrate and run the regression/preview gate

- Objective: Verify the completed single page as one coherent artifact and correct residual implementation defects before task completion/merge; this verifies concerns already built into `PLAN-001`–`003` rather than introducing accessibility or responsiveness at the end.
- References: all approved current-scope `REQ-*`, `SPEC-*`, `AC-001`–`AC-016`, and owner resolutions `AUD-001`–`AUD-004` plus `AUD-009`.
- Files: modify only affected implementation files from `PLAN-001`–`003` as corrections require; no new product surface or architecture is planned.
- Approach:
  - Recheck semantic order, consultation links, six-service inventory, meaningful/decorative images, carousel state/feedback, contrast, reflow/zoom, reduced motion, and source fidelity as an integrated page.
  - Compare rendered output with scoped Figma exemplars at 375px, 768px, and 1440px, then inspect intermediate widths for failure-driven breakpoint correctness.
  - Verify the no-JavaScript Work fallback separately from the enhanced carousel.
  - Run the repository-confirmed production build and verify the branch Vercel preview before merge; do not manually promote production.
  - Confirm no backend, API, auth, persistence, additional route, modal, Work-detail navigation, autoplay, or unapproved consultation destination entered the implementation.
- Dependencies/order: Final implementation validation slice after `PLAN-001`–`003` integrate.
- Validation: successful `pnpm build`; browser/preview evidence covering `AC-001`–`AC-016`; rendered contrast; keyboard/focus/reduced-motion/no-JS checks; final visual comparison and Vercel preview verification.
- Risks/assumptions: The repository has no automated test/a11y suite today, so evidence-backed browser/manual validation is planned instead of nonexistent commands. Stage 9 may add a narrowly justified test tool only if task-specific risk warrants the dependency and the plan is updated consistently.

### Ordering and coordination

1. `PLAN-001` establishes the shell, assets, CSS conventions, semantics, and buildable foundation.
2. `PLAN-002` implements the static sections and repeated consultation-link behavior.
3. `PLAN-003` implements the isolated Work interaction; overlap with `PLAN-002` is safe only when `index.astro`, shared CSS, and asset ownership do not conflict.
4. `PLAN-004` performs integrated regression and preview verification.

There is no migration, persistence, backend rollout, API contract, or architecture-specific rollback procedure beyond normal Git/PR rollback because Stage 6 established that no architecture-level change is required.
"""

risks = """## 9. Risks, Assumptions, and Questions

### Blocking

- None. Stage 6 is approved through `GATE-007`, `AUD-009` is owner-resolved, and the inspected repository has no structural blocker to Stage 7 planning.

### Non-blocking

- `SRC-DS-001` remains mutable/time-bound and must be reverified before implementation task execution.
- Portfolio image/vector exports and a permitted Plus Jakarta Sans delivery source are not present in the repository. They are implementation asset inputs, not reasons to invent a dependency or runtime service during planning.
- Exact media-query values are intentionally not fixed by the 375px/768px/1440px exemplars. Implementation selects transition points from rendered failure conditions and validates both anchors and intermediate widths.
- The repository currently exposes only the production build as an automated frontend check. Browser-based visual, keyboard, focus, contrast, zoom/reflow, reduced-motion, no-JavaScript, and assistive-structure validation remain explicit evidence requirements.
- The optional visual-clone technique in `PLAN-003` is limited to cyclic edge animation and must remain assistive-hidden/non-interactive; prefer a simpler equivalent implementation if it satisfies the specified geometry and behavior.
- No task IDs exist yet. Stage 9 will decompose the approved plan after the separate Stage 8 adversarial review.
"""

text = replace_between(text, "## 5. Repository Context", "## 6. Implementation Plan", repository_context)
text = replace_between(text, "## 6. Implementation Plan", "## 7. Architecture Decision", implementation_plan)
text = replace_between(text, "## 9. Risks, Assumptions, and Questions", "## 10. Traceability", risks)

traceability_marker = "Repository-aware plan and task identifiers do not exist yet and will be added at their owning later checkpoints rather than invented during Stage 5."
traceability_replacement = """Stage 7 adds repository-aware `PLAN-*` ownership while task IDs remain deferred to Stage 9.

| Plan item | Primary specification coverage | Acceptance coverage |
|---|---|---|
| `PLAN-001` | `SPEC-BEH-001`, `SPEC-BEH-003`, `SPEC-ACC-001`, `SPEC-ACC-005`, `SPEC-ACC-006`, `SPEC-VAL-001`, `SPEC-VAL-003` | `AC-001`, `AC-011`, `AC-012`, `AC-015`, `AC-016` |
| `PLAN-002` | `SPEC-BEH-001`–`003`, `SPEC-INT-001`, `SPEC-ACC-001`, `SPEC-ACC-002`, `SPEC-ACC-004`–`006`, `SPEC-VAL-001`, `SPEC-VAL-003` | `AC-001`–`003`, `AC-008`, `AC-010`–`013`, `AC-015`, `AC-016` |
| `PLAN-003` | `SPEC-BEH-003`, `SPEC-BEH-004`, `SPEC-INT-002`–`005`, `SPEC-ACC-002`–`004`, `SPEC-ACC-006`, `SPEC-DATA-001`, `SPEC-VAL-001`–`003` | `AC-004`–`010`, `AC-012`–`015` |
| `PLAN-004` | All approved current-scope specification areas as integrated verification | `AC-001`–`AC-016` |

`PLAN-001`–`PLAN-004` are the Stage 7 decomposition boundary. Stage 9 will create task IDs that reference these approved plan items rather than re-planning the implementation."""
if traceability_marker not in text:
    raise RuntimeError("Expected Stage 5 traceability marker not found")
text = text.replace(traceability_marker, traceability_replacement)

review_tail = """## 11. Review Pass 1 — Feasibility and Completeness

Stage 7 reviewed the repository-aware plan against the actual frontend and all approved upstream behavior.

- [x] Current repository state is explicit: the frontend is still Astro starter content; existing versus proposed paths are distinguished.
- [x] The plan uses the existing static Astro model and does not add a framework island, backend, state library, carousel package, API, route, or unsupported product behavior.
- [x] File impact covers starter removal, page/layout integration, section components, repeated consultation action, external CSS, Work interaction script, and source asset placement.
- [x] Accessibility is integrated where behavior is created: semantics/focus/contrast/reflow in `PLAN-001`/`PLAN-002`, and carousel names/keyboard/live feedback/reduced motion/fallback in `PLAN-003`.
- [x] Responsive behavior is integrated per plan item and treats source widths as validation anchors rather than automatic breakpoint numbers.
- [x] Failure behavior is explicit: Work content remains available without successful JavaScript and dead controls are not exposed.
- [x] Validation uses the repository-confirmed `pnpm build` plus evidence-backed browser/preview checks; nonexistent lint/test scripts are not claimed.
- [x] The four plan items are concrete, ordered by repository prerequisites, and decomposable into Stage 9 tasks.

## 12. Corrections from Pass 1

- Kept portfolio CSS in external stylesheet files to match project conventions and avoid inline styling while limiting fragmentation for a single page.
- Rejected a third-party carousel/framework dependency; the interaction is bounded enough for a small TypeScript module and the static fallback remains first-class.
- Limited any cyclic visual clones to assistive-hidden/non-focusable client-side presentation so semantic slides are not duplicated.
- Kept media-query selection content-driven instead of copying 375/768/1440 into implementation breakpoints.
- Made asset/font sourcing an explicit implementation input/risk instead of inventing filenames, dependencies, or runtime services absent from the repository.
- Kept final validation as verification/correction only; accessibility, responsiveness, states, and reduced motion are not deferred to cleanup.

## 13. Review Pass 2 — Consistency, Traceability, Risks, and Uncertainty

- [x] `PLAN-001`–`PLAN-004` map to approved `REQ-*`, `SPEC-*`, `AC-*`, and owner-resolved audit decisions without creating new product requirements.
- [x] Stage 6 architecture remains Not required: proposed components/styles/script are local implementation structure, not a new architecture layer.
- [x] Existing and proposed paths are explicitly distinguished; no proposed component, stylesheet, script, or portfolio asset is presented as already present.
- [x] The plan preserves `AUD-001` (`href=\"#\"`), `AUD-002` (standard carousel), `AUD-003`/`AUD-004` (contrast corrections), and `AUD-009` (standalone Work 05 at logical slot 05).
- [x] The carousel plan preserves item 03 start, cyclic one-step navigation, no autoplay, native buttons, focus retention, live position feedback, reduced motion, and non-JavaScript reachability.
- [x] No arbitrary browser matrix, performance budget, breakpoint, dependency, test command, or deployment topology is invented.
- [x] Remaining uncertainty is visible and non-blocking: exact exported asset filenames/formats, permitted font delivery, and final failure-driven media-query values are resolved during implementation from source and rendered evidence.
- [x] The plan remains small enough for the Lite brief; no profile upgrade is warranted.

## 14. Readiness

**Stage 7 content complete; ready for canonical Stage 7 preflight and project-owner approval.** Repository inspection, `PLAN-001` through `PLAN-004`, two required review passes, risks, ordering, and validation are documented. The consolidated brief should remain `Reviewed` for the Stage 7 gate.

The Stage 7 gate is intentionally **not** recorded as passed by this change. Stage 8 — adversarial plan review — must not start until explicit project-owner approval is recorded and the workflow advances.
"""
review_start = text.index("## 11. Review Pass 1")
text = text[:review_start] + review_tail.rstrip() + "\n"

path.write_text(text)
print("Stage 7 plan patch applied")
