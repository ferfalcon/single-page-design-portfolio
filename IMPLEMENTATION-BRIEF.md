---
artifact: IMPLEMENTATION-BRIEF
status: Draft
baseline:
  design:
    - SRC-DS-001
  repository:
    - SRC-REPO-001
  runtime: []
  documentation: []
  assets: []
created: 2026-08-18
updated: 2026-08-18
---

# Implementation Brief

## 1. Document Information

- Status: Draft
- Scope: Accessible, responsive implementation of the scoped Single-page design portfolio Home page in the existing Astro frontend.
- Last updated: 2026-08-18
- Project context: `PROJECT-CONTEXT.md`
- Source baseline: `SOURCE-BASELINE.md`
- Evidence baseline: `DESIGN-AUDIT.md`
- Repository snapshot: `SRC-REPO-001`
- Current workflow checkpoint: Stage 2 — Requirements
- Later sections: Design intent, specification, repository-aware planning, architecture decision, and final Lite review are intentionally not started in this checkpoint.

### Stage 2 source check

- `SRC-DS-001` is time-bound. A fresh metadata inspection on 2026-08-18 confirmed that the scoped `🤖 Workflow` page (`2141:862`), Home / Mobile (`2141:14174`), Home / Tablet (`2141:14238`), Home / Desktop (`2141:14302`), responsive section/navigation component sets, carousel controls, and five Work assets remain present under the same node IDs and supplied dimensions.
- This check confirms structural continuity for the requirements checkpoint; it does not convert the mutable Figma source into an immutable snapshot or replace later source verification.
- `SRC-REPO-001` remains an immutable repository baseline. Workflow documentation changes after that input commit are expected workflow output and do not alter the implementation baseline used for product requirements.

## 2. Requirements

### Goals

- Implement the approved single-page portfolio design as one responsive, accessible web page in the existing Astro frontend.
- Preserve the content hierarchy, service offering, About content, Work presentation, consultation actions, Contact section, and footer evidenced by `SRC-DS-001`.
- Make the Work presentation operable as a conventional previous/next carousel, following the project-owner resolution of `AUD-002`.
- Resolve the confirmed implementation accessibility gaps from `AUD-003` and `AUD-004` without modifying Figma during this workflow stage.
- Preserve source fidelity at the supplied mobile, tablet, and desktop exemplars while keeping the page usable between those exemplars.

### Non-goals

- No additional route, project-detail page, modal, overlay, backend, authentication, persistence, or external API is in the current scope.
- Work images are not project links unless later source evidence or an explicit owner decision adds that behavior.
- The consultation destination is not being invented; the current implementation uses the approved placeholder destination.
- Stage 2 does not choose implementation breakpoints, carousel wrap/boundary mechanics, exact contrast-remediation colors, DOM/component architecture, or implementation order.
- No structural or visual change to Figma is part of this requirement checkpoint.

### REQ-FR-001 — Present the complete single-page portfolio content

- Classification: Confirmed
- Priority: Must
- Description: The page must present the scoped portfolio content as one continuous page containing the header/hero area, six service categories, About section, Work section, Contact section, and footer in the source-observed reading sequence.
- Rationale: The three supplied Home frames consistently represent one continuous portfolio page rather than separate routes or screens.
- Snapshot or evidence: `SRC-DS-001`; `EVD-001` through `EVD-006`.
- Acceptance criteria:
  - The implemented page contains all source-observed major sections.
  - The major sections appear in the source-observed sequence: Hero → About → Work → Contact → Footer.
  - No additional route or page-level flow is required to access the supplied portfolio content.

### REQ-FR-002 — Present all six service categories

- Classification: Confirmed
- Priority: Must
- Description: The services presentation must include Graphic Design, UI/UX, Apps, Illustrations, Photography, and Motion Graphics with their corresponding source-provided visual artwork.
- Rationale: The six categories form the core service inventory in the Hero composition.
- Snapshot or evidence: `SRC-DS-001`; `EVD-003`; `EVD-015`.
- Acceptance criteria:
  - All six named service categories are present.
  - Each category retains the corresponding source artwork and remains readable in the supported responsive layouts.

### REQ-FR-003 — Provide consultation actions using the approved placeholder destination

- Classification: Confirmed
- Priority: Must
- Description: Every source-observed “Free Consultation” action must be implemented as a link using `href="#"` until a real consultation destination is supplied.
- Rationale: `AUD-001` identified that Figma does not provide a destination; the project owner explicitly resolved the current behavior with a placeholder link rather than an invented route or external URL.
- Snapshot or evidence: `SRC-DS-001`; `AUD-001`; owner resolution recorded in `DESIGN-AUDIT.md`.
- Acceptance criteria:
  - Each source-observed “Free Consultation” action is rendered as a link.
  - Each such link uses `href="#"` in the current implementation scope.
  - No unapproved route, URL, modal, or booking behavior is introduced.

### REQ-FR-004 — Make the Work section navigable as a previous/next carousel

- Classification: Confirmed
- Priority: Must
- Description: The Work section must provide conventional previous and next controls that allow users to navigate through the five source-provided Work items.
- Rationale: The design supplies five Work assets and previous/next controls; `AUD-002` was explicitly resolved by the project owner as a standard carousel.
- Snapshot or evidence: `SRC-DS-001`; `EVD-005`; `EVD-015`; `AUD-002`.
- Acceptance criteria:
  - Previous and next controls are present and operable.
  - All five source-provided Work items are reachable through the carousel interaction.
  - The precise start position, wrap/boundary behavior, and transition behavior are defined later in Stage 4 rather than invented here.

### REQ-FR-005 — Do not add unsupported Work-item navigation

- Classification: Confirmed
- Priority: Must
- Description: Work preview images must not be made into project-detail links unless later evidence or an explicit owner decision adds that capability.
- Rationale: The audit found no demonstrated project-detail destination or clickable Work-image behavior.
- Snapshot or evidence: `SRC-DS-001`; `DESIGN-AUDIT.md` Questions and Owner Resolutions.
- Acceptance criteria:
  - Activating a Work image does not navigate to an invented project-detail destination.
  - Carousel controls remain the only required Work interaction in the current scope.

### REQ-FR-006 — Remain usable across supplied and intermediate viewport conditions

- Classification: Confirmed
- Priority: Must
- Description: The page must reproduce the observed mobile, tablet, and desktop compositions at the supplied 375px, 768px, and 1440px exemplars and remain usable at intermediate widths without layout breakage, clipped essential content, or page-level horizontal scrolling caused by the implementation.
- Rationale: Figma supplies three responsive exemplars but does not define implementation breakpoints or every intermediate width.
- Snapshot or evidence: `SRC-DS-001`; `EVD-007`; `EVD-008`; `AUD-005`; `PROJECT-CONTEXT.md` quality baseline.
- Acceptance criteria:
  - At the three supplied exemplar widths, the page preserves the corresponding source layout intent.
  - Between supplied exemplars, essential content and controls remain readable and operable.
  - The implementation does not rely on arbitrary device breakpoints solely because they are common defaults; breakpoint choices are deferred to design/specification based on observed layout behavior.

### REQ-AR-001 — Preserve semantic document structure independent of visual styling

- Classification: Confirmed
- Priority: Must
- Description: The implementation must use semantic page structure and a coherent heading hierarchy based on content relationships rather than visual text size alone.
- Rationale: The project quality baseline requires semantic accessibility, while Figma typography guidance explicitly warns that responsive visual style changes must not change semantic hierarchy.
- Snapshot or evidence: `SRC-DS-001`; `EVD-010`; `PROJECT-CONTEXT.md` quality baseline; root `AGENTS.md`.
- Acceptance criteria:
  - The page has a coherent semantic landmark/content structure.
  - Heading levels follow document hierarchy rather than responsive font-size variants.
  - Visual style changes across responsive layouts do not alter the semantic meaning of the same content.

### REQ-AR-002 — Provide keyboard-operable interactive controls with visible focus

- Classification: Confirmed
- Priority: Must
- Description: Consultation links and carousel controls must be keyboard operable and expose a clearly visible focus indication.
- Rationale: The design includes explicit focus variants, and the repository accessibility baseline requires keyboard access and focus visibility.
- Snapshot or evidence: `SRC-DS-001`; `EVD-009`; `PROJECT-CONTEXT.md`; root `AGENTS.md`.
- Acceptance criteria:
  - Every consultation link and carousel control can be reached and activated with a keyboard using native interaction expectations.
  - Keyboard focus is visibly distinguishable on all required interactive controls.
  - Focus order follows the meaningful document interaction order.

### REQ-AR-003 — Provide meaningful accessible names for interactive graphics and carousel controls

- Classification: Confirmed
- Priority: Must
- Description: Interactive graphical controls must have accessible names that communicate their purpose, including the logo when used as a link and the Work previous/next controls.
- Rationale: Figma component descriptions include accessible-name guidance for the logo and carousel controls.
- Snapshot or evidence: `SRC-DS-001`; `EVD-010`.
- Acceptance criteria:
  - The previous control exposes a purpose equivalent to “Previous project”.
  - The next control exposes a purpose equivalent to “Next project”.
  - If the brand logo is implemented as a link, it exposes a meaningful accessible name rather than only an unlabeled graphic.

### REQ-AR-004 — Apply appropriate image alternatives

- Classification: Confirmed
- Priority: Must
- Description: Decorative service artwork must not add redundant screen-reader content, while the meaningful profile portrait and Work imagery must receive context-appropriate alternative text.
- Rationale: The design component descriptions explicitly classify service illustrations as decorative and portrait/Work imagery as meaningful, but do not provide final alternative-text wording.
- Snapshot or evidence: `SRC-DS-001`; `EVD-010`; `EVD-015`.
- Acceptance criteria:
  - Decorative service artwork is ignored by assistive technologies.
  - The profile portrait has meaningful alternative text appropriate to its role.
  - Each meaningful Work image has alternative text appropriate to the visible project imagery/context.
  - Final wording may be refined during specification/implementation, but images are not left with misleading or redundant alternatives.

### REQ-AR-005 — Meet applicable text contrast requirements in implemented states

- Classification: Confirmed
- Priority: Must
- Description: Text in the implemented interface must meet the applicable WCAG AA contrast threshold for its rendered size and weight in default, hover, and focus-relevant states. The implementation must specifically correct the known contrast failures identified for the Accent CTA and the UI/UX, Apps, and Photography service labels.
- Rationale: `AUD-003` and `AUD-004` were confirmed by the project owner as implementation accessibility requirements rather than Figma edits.
- Snapshot or evidence: `SRC-DS-001`; `EVD-012`; `EVD-013`; `AUD-003`; `AUD-004`.
- Acceptance criteria:
  - Accent CTA label contrast passes the applicable threshold in every implemented visual state.
  - UI/UX, Apps, and Photography service-label contrast passes the applicable threshold.
  - Contrast remediation preserves the intended hierarchy and recognizable design direction as closely as possible without retaining a known failure.
  - The exact compliant visual treatment is selected in the later design/specification/planning stages.

### REQ-AR-006 — Preserve text reflow and readable content at responsive and zoomed conditions

- Classification: Confirmed
- Priority: Must
- Description: Text and essential controls must remain readable and operable as layout width changes and when text/reflow conditions increase content demand; visual typography size alone must not carry structural meaning.
- Rationale: Figma does not prove zoom or reflow behavior, while the project accessibility baseline and typography guidance require resilient text/reflow behavior.
- Snapshot or evidence: `SRC-DS-001`; `AUD-005`; `EVD-010`; `PROJECT-CONTEXT.md` quality baseline.
- Acceptance criteria:
  - Essential content is not clipped or made unreachable when text occupies more space.
  - Responsive layout adaptations preserve reading and interaction order.
  - The implementation does not depend on fixed-height text containers that truncate required copy under normal reflow conditions.

### REQ-AR-007 — Respect reduced-motion preferences for non-essential transitions

- Classification: Confirmed
- Priority: Must
- Description: Non-essential hover/carousel transition motion must not create an accessibility barrier and must respect the user’s reduced-motion preference while preserving the perceivable state change and carousel functionality.
- Rationale: The design demonstrates 200ms dissolve hover transitions but supplies no reduced-motion guidance; the repository contract explicitly requires reduced-motion consideration.
- Snapshot or evidence: `SRC-DS-001`; `EVD-016`; `AUD-006`; root `AGENTS.md`.
- Acceptance criteria:
  - Interactive controls remain fully understandable and operable when non-essential motion is reduced or suppressed.
  - Reduced-motion handling does not remove required hover/focus distinction or carousel functionality.
  - Exact transition mechanics remain a Stage 4 specification responsibility.

### REQ-NFR-001 — Keep the result lightweight and appropriate for a static Astro page

- Classification: Confirmed
- Priority: Must
- Description: The implementation must remain a lightweight static Astro page and must avoid unnecessary client-side JavaScript outside behavior that genuinely requires it, such as the Work carousel.
- Rationale: The project is classified as a static page, and the project quality baseline explicitly favors lightweight Astro output and avoiding unnecessary client JavaScript.
- Snapshot or evidence: `SRC-REPO-001`; `PROJECT-CONTEXT.md`.
- Acceptance criteria:
  - Static content does not require client-side JavaScript solely for rendering.
  - Client-side JavaScript is limited to interaction needs that cannot be fulfilled by static markup/CSS alone.
  - No backend or persistence layer is introduced for current-scope behavior.

### REQ-NFR-002 — Preserve visual fidelity to the authoritative scoped design

- Classification: Confirmed
- Priority: Must
- Description: The implemented page must preserve the visual hierarchy, typography intent, spacing relationships, imagery, responsive composition, and recognizable interaction states evidenced by `SRC-DS-001`, except where an approved accessibility correction requires a documented deviation.
- Rationale: Design fidelity is a repository-wide quality requirement, while `AUD-003` and `AUD-004` explicitly require accessibility corrections that may need controlled visual adjustment.
- Snapshot or evidence: `SRC-DS-001`; `EVD-001` through `EVD-016`; root `AGENTS.md`.
- Acceptance criteria:
  - Visual comparison at the supplied exemplar widths shows the same major composition and hierarchy as the approved source.
  - Any intentional visual deviation required for accessibility is traceable to an approved requirement/finding.
  - Unrelated redesign is not introduced.

### Existing project constraints carried forward

The following constraints are already defined in `PROJECT-CONTEXT.md` and remain authoritative without renumbering or redefining them here:

- `REQ-CON-001` — Implement inside `frontend/` and follow repository and nested `AGENTS.md` instructions.
- `REQ-CON-002` — Figma inspection/editing scope is `🤖 Workflow`; do not modify other pages without explicit request.
- `REQ-CON-003` — Use Gated workflow progression and do not advance stages without explicit approval.
- `REQ-CON-004` — The Figma input is time-bound and must be reverified before material downstream work.

### Assumptions, recommendations, and deferred decisions

#### Blocking

- None identified for Stage 2 requirements.

#### Non-blocking / deferred

- Carousel start position, boundary behavior, wrap/loop behavior, and visual transition mechanics are intentionally deferred to Stage 4 specification under the approved “standard carousel” direction.
- Exact implementation breakpoint values are intentionally deferred; supplied viewport widths are exemplars, not automatically breakpoints.
- Exact compliant color/token changes for `AUD-003` and `AUD-004` are deferred to design intent/specification/planning.
- Final alternative-text wording for meaningful imagery is deferred to specification/implementation because Figma provides intent but not copy.
- No browser-support matrix is invented at this stage; later specification/planning may define one only from real project constraints or explicit owner direction.

### Stage 2 Review Pass 1 — Completeness and correctness

- [x] Goals and non-goals match the approved project scope.
- [x] Functional requirements cover the complete one-page content, six services, placeholder consultation behavior, Work carousel behavior, unsupported Work-link exclusion, and responsive usability.
- [x] Accessibility requirements cover semantics, keyboard/focus, accessible names, image alternatives, known contrast failures, text/reflow resilience, and reduced motion.
- [x] Quality requirements cover lightweight static delivery and design fidelity without inventing performance thresholds.
- [x] Existing `REQ-CON-*` identifiers are reused rather than duplicated or renumbered.
- [x] No backend, authentication, persistence, security policy, browser target, arbitrary breakpoint, or unsupported route behavior was invented.

### Corrections from Stage 2 Review Pass 1

- Clarified that Work images are not links in current scope rather than leaving project-detail behavior ambiguous.
- Kept carousel edge/wrap mechanics out of requirements while preserving the owner-approved standard-carousel outcome.
- Separated contrast compliance as an outcome from the exact visual remediation, which belongs to later design/specification work.
- Made intermediate-width usability testable without converting supplied Figma widths directly into implementation breakpoint values.

### Stage 2 Review Pass 2 — Consistency, traceability, source integrity, risks, and uncertainty

- [x] Every material requirement references approved project context, `SRC-DS-001`, `SRC-REPO-001`, `EVD-*`, `AUD-*`, or an explicit owner resolution as applicable.
- [x] Requirement ownership remains distinct from later design, specification, and plan responsibilities.
- [x] The fresh Stage 2 Figma metadata check confirms structural continuity while preserving the snapshot’s time-bound limitation.
- [x] No requirement silently depends on newer implementation code than `SRC-REPO-001`.
- [x] Known uncertainty is visible and deferred to the correct later stage rather than presented as confirmed behavior.
- [x] The work remains Lite-eligible: one static page, no material routing/shared-state/persistence/authentication/integration architecture introduced by Stage 2.

### Stage 2 readiness

**Ready for gated Stage 2 approval.** Stage 3 — Design Intent has not been started.

## 3. Design Intent

Not started. Reserved for Stage 3 after explicit Stage 2 approval.

## 4. Specification

Not started. Reserved for Stage 4 after the preceding gated approval.

## 5. Repository Context

Detailed repository inspection for planning has not started. Current project constraints remain governed by `SRC-REPO-001`, `PROJECT-CONTEXT.md`, root `AGENTS.md`, and the nearest scoped instructions.

## 6. Implementation Plan

Not started. Reserved for the Lite planning checkpoint after requirements, design intent, specification, and documentation review are approved.

## 7. Architecture Decision

- Separate architecture needed: Not evaluated yet.
- Reason: Architecture handling remains reserved for its workflow checkpoint; Stage 2 introduces no new architecture-driving concern.

## 8. Source-change Handling

- Snapshot verification required before task execution: Yes, including re-verification of time-bound `SRC-DS-001` and the applicable repository task-start snapshot.
- Material changes that invalidate this brief: Changes to scoped page structure, content, responsive compositions, component behavior, Work assets/interactions, consultation behavior, or approved accessibility direction.
- Earliest workflow section or stage to revisit: The earliest ownership stage affected by the changed evidence; create new `SRC-*` records and perform impact assessment rather than silently reusing `SRC-DS-001`.

## 9. Risks, Assumptions, and Questions

### Blocking

- None for the Stage 2 requirements checkpoint.

### Non-blocking

- `SRC-DS-001` remains mutable and time-bound.
- Exact carousel mechanics, breakpoint placement, compliant contrast treatment, and final image-alt wording remain intentionally unresolved until their owning later stages.
- Workflow CLI preflight has not been executed in this runtime; no Stage 2 gate is claimed as passed.

## 10. Traceability

Stage 2 traceability is captured directly in each `REQ-*` item above. The consolidated cross-section traceability table will be completed as Stage 3, Stage 4, and planning identifiers are added.

## 11. Review Pass 1 — Completeness and Correctness

Overall Lite review not started. Stage 2-specific review passes are recorded in the Requirements section.

## 12. Corrections from Pass 1

Overall Lite review corrections not started.

## 13. Review Pass 2 — Consistency, Traceability, Source Integrity, Risks, and Uncertainty

Overall Lite review not started. Stage 2-specific consistency review is recorded in the Requirements section.

## 14. Readiness

Not evaluated for task decomposition. The current gated checkpoint is **Stage 2 requirements ready for approval**.
