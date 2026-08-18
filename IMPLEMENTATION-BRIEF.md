---
artifact: IMPLEMENTATION-BRIEF
status: Reviewed
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

- Status: Reviewed
- Scope: Accessible, responsive implementation of the scoped Single-page design portfolio Home page in the existing Astro frontend.
- Last updated: 2026-08-18
- Project context: `PROJECT-CONTEXT.md`
- Source baseline: `SOURCE-BASELINE.md`
- Evidence baseline: `DESIGN-AUDIT.md`
- Repository snapshot: `SRC-REPO-001`
- Current workflow checkpoint: **Stage 7 — Create the repository-aware implementation plan**
- Requirements are approved through `GATE-003`, design intent through `GATE-004`, specification through `GATE-005`, documentation review through `GATE-006`, and architecture through `GATE-007`. Stage 7 is active. Architecture remains **Not required** and the project remains Lite; this checkpoint now owns repository inspection, implementation structure, ordering, dependencies, risks, and validation planning. Stage 8 adversarial review, task decomposition, and implementation remain intentionally unstarted.

### Stage 5 source challenge

- A fresh read-only Figma metadata and Plugin API check on 2026-08-18 confirmed the same scoped `🤖 Workflow` page (`2141:862`), Home exemplars, responsive components, control states, and standalone Work assets; no material upstream design drift was observed.
- A GitHub comparison from immutable `SRC-REPO-001` to current `main` shows workflow/documentation changes only and no `frontend/` changes.
- The deeper Work-instance check uncovered `AUD-009`: every viewport variant's layer named `Work Image / 05` currently instances `Asset/Work/02` (`6:377`), while standalone `Asset/Work/05` (`6:380`) exists unused. This was present in the active source but missed by earlier review; it is not treated as source drift.
- The project owner resolved `AUD-009` by selecting **Option 2**: logical Work position 05 uses standalone `Asset/Work/05` (`6:380`). The current repeated Work 02 instance remains recorded as observed Figma evidence and is treated as a source-assembly mistake for implementation purposes. This owner resolution does not authorize or imply a Figma edit.

### Stage 2 source check

- `SRC-DS-001` is time-bound. A fresh metadata inspection on 2026-08-18 confirmed that the scoped `🤖 Workflow` page (`2141:862`), Home / Mobile (`2141:14174`), Home / Tablet (`2141:14238`), Home / Desktop (`2141:14302`), responsive section/navigation component sets, carousel controls, and five standalone Work assets remain present under the same node IDs and supplied dimensions.
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
- Description: The Work section must provide conventional previous and next controls that allow users to navigate through five logical Work positions.
- Rationale: The design supplies five logical Work slots, standalone Work assets 01–05, and previous/next controls; `AUD-002` was explicitly resolved as a standard carousel. Stage 5 later found that the scoped slot named 05 currently instances Work 02 rather than the standalone Work 05 asset (`AUD-009`), and the project owner resolved the implementation mapping to standalone `Asset/Work/05` (`6:380`).
- Snapshot or evidence: `SRC-DS-001`; `EVD-005`; `EVD-015`; `EVD-017`; `AUD-002`; `AUD-009`.
- Acceptance criteria:
  - Previous and next controls are present and operable.
  - All five logical Work positions are reachable through the carousel interaction.
  - Logical position 05 renders standalone `Asset/Work/05` (`6:380`) under the owner-approved `AUD-009` correction.
  - The precise start position, wrap/boundary behavior, and transition behavior are defined in Stage 4 rather than invented here.

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
- Description: Decorative service artwork must not add redundant screen-reader content, while the meaningful profile portrait and rendered Work imagery must receive context-appropriate alternative text matching the actual asset shown.
- Rationale: The design component descriptions explicitly classify service illustrations as decorative and portrait/Work imagery as meaningful, but do not provide final alternative-text wording. `AUD-009` requires the slot-05 text to follow the resolved asset rather than the layer name alone.
- Snapshot or evidence: `SRC-DS-001`; `EVD-010`; `EVD-015`; `EVD-017`; `AUD-009`.
- Acceptance criteria:
  - Decorative service artwork is ignored by assistive technologies.
  - The profile portrait has meaningful alternative text appropriate to its role.
  - Each rendered Work position has alternative text appropriate to the actual visible imagery/context.
  - Logical slot 05 renders standalone `Asset/Work/05` and therefore uses the corresponding Work 05 alternative text defined in Stage 4.
  - Images are not left with misleading or redundant alternatives.

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
- Description: Non-essential hover/carousel transition motion must not create an accessibility barrier and must respect the user's reduced-motion preference while preserving the perceivable state change and carousel functionality.
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
- Description: The implemented page must preserve the visual hierarchy, typography intent, spacing relationships, imagery, responsive composition, and recognizable interaction states evidenced by `SRC-DS-001`, except where an approved accessibility correction or an explicitly resolved source inconsistency requires a documented deviation.
- Rationale: Design fidelity is a repository-wide quality requirement, while `AUD-003`, `AUD-004`, and `AUD-009` require controlled, traceable handling instead of silent divergence.
- Snapshot or evidence: `SRC-DS-001`; `EVD-001` through `EVD-017`; root `AGENTS.md`.
- Acceptance criteria:
  - Visual comparison at the supplied exemplar widths shows the same major composition and hierarchy as the approved source.
  - Any intentional visual deviation required for accessibility or the `AUD-009` owner decision is traceable to its approved finding/decision.
  - Unrelated redesign is not introduced.

### Existing project constraints carried forward

The following constraints are already defined in `PROJECT-CONTEXT.md` and remain authoritative without renumbering or redefining them here:

- `REQ-CON-001` — Implement inside `frontend/` and follow repository and nested `AGENTS.md` instructions.
- `REQ-CON-002` — Figma inspection/editing scope is `🤖 Workflow`; do not modify other pages without explicit request.
- `REQ-CON-003` — Use Gated workflow progression and do not advance stages without explicit approval.
- `REQ-CON-004` — The Figma input is time-bound and must be reverified before material downstream work.

### Assumptions, recommendations, and deferred decisions

#### Blocking

- No blocking product/content decision remains from `AUD-009`. The project owner selected Option 2: logical Work position 05 uses standalone `Asset/Work/05` (`6:380`).

#### Non-blocking / deferred

- Carousel start position, boundary behavior, wrap/loop behavior, and visual transition mechanics were deferred to Stage 4 specification under the approved “standard carousel” direction and are now specified.
- Exact implementation breakpoint values remain deferred; supplied viewport widths are exemplars, not automatically breakpoints.
- Exact compliant color/token changes for `AUD-003` and `AUD-004` were deferred and are now specified.
- Final alternative-text wording for meaningful imagery was defined in Stage 4 from direct asset inspection; logical slot 05 uses the standalone Work 05 wording under the resolved `AUD-009` decision.
- No browser-support matrix is invented; later planning may define one only from real project constraints or explicit owner direction.

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
- [x] The fresh Stage 2 Figma metadata check confirms structural continuity while preserving the snapshot's time-bound limitation.
- [x] No requirement silently depends on newer implementation code than `SRC-REPO-001`.
- [x] Known uncertainty is visible and deferred to the correct later stage rather than presented as confirmed behavior.
- [x] The work remains Lite-eligible: one static page, no material routing/shared-state/persistence/authentication/integration architecture introduced by Stage 2.

### Stage 2 readiness

**Approved through `GATE-003`.**

## 3. Design Intent

### Stage 3 source check

- `SRC-DS-001` remains time-bound. A fresh metadata inspection on 2026-08-18 again confirmed the scoped `🤖 Workflow` page (`2141:862`), the 375px, 768px, and 1440px Home exemplars, responsive Header/Footer/Hero/About/Work/Contact component sets, Default/Hover/Focus control variants, the profile portrait, and five standalone Work assets.
- The supplied widths remain design exemplars rather than implementation breakpoint instructions. Stage 3 describes intended transformations and failure conditions; Stage 4 and planning may make them testable and select concrete implementation values where necessary.
- The immutable implementation baseline remains `SRC-REPO-001`. Stage 3 does not prescribe repository architecture or implementation paths.

### Design principles

- Preserve the source's friendly portfolio character: warm neutral page surface, bold Plus Jakarta Sans typography, colorful service cards, large imagery, rounded controls, generous whitespace, and a dark closing call-to-action.
- Preserve the one-page narrative order and visual pacing rather than flattening the page into equally weighted blocks.
- Treat accessibility corrections from `AUD-003` and `AUD-004` as controlled design deviations: preserve recognizable color roles and hierarchy while changing a failing foreground/background pairing when required for compliant text contrast.
- Keep responsive changes content-driven. Layout transforms when the current arrangement can no longer preserve readable copy, meaningful image prominence, comfortable controls, or the source-observed visual relationships.

### DES-001 — Preserve the single-page narrative hierarchy

- Classification: Confirmed
- Confidence: High
- Intent: Maintain the source-observed progression Hero → About → Work → Contact → Footer. Hero establishes the service offer, About introduces the designer, Work shifts emphasis to portfolio imagery, and Contact closes with the strongest conversion surface before the footer.
- Snapshot and evidence: `SRC-DS-001`; `EVD-001` through `EVD-006`.
- Requirement references: `REQ-FR-001`, `REQ-NFR-002`.
- Design boundary: Do not introduce extra routes, project-detail surfaces, modal layers, or navigation sections solely to elaborate the visual design.

### DES-002 — Preserve the source visual system as the default design language

- Classification: Observed
- Confidence: High
- Intent: Use the Figma typography styles, semantic/primitives color roles, spacing scale, radius scale, imagery, and component-state styling as the visual baseline. The warm neutral surface and dark primary text remain the dominant page canvas; accent colors remain concentrated in service cards and action states.
- Snapshot and evidence: `SRC-DS-001`; `EVD-012` through `EVD-015`; Figma design-system documentation on `2141:862`.
- Requirement references: `REQ-NFR-002`, `REQ-AR-005`, `REQ-AR-006`.
- Design boundary: This is a design-source mapping, not a CSS-token or component-file prescription.

### DES-003 — Keep typography hierarchy semantically stable while visual scale changes

- Classification: Confirmed
- Confidence: High
- Intent: The hero remains the dominant page heading. About, Work, and Contact remain section-level headings. Service labels remain subordinate to the hero introduction. Mobile may use the source's compact large heading treatment while larger layouts use larger heading styles, but visual size changes must not change document meaning or reading hierarchy.
- Snapshot and evidence: `SRC-DS-001`; `EVD-002` through `EVD-006`; Figma Typography usage guidance.
- Requirement references: `REQ-AR-001`, `REQ-AR-006`, `REQ-NFR-002`.
- Content edge intent: Heading and paragraph containers may grow vertically when text wraps; typography must not depend on fixed heights that clip required content.

### DES-004 — Keep the six service cards individually recognizable and visually grouped

- Classification: Observed
- Confidence: High
- Intent: Preserve all six service categories as distinct colored cards with their paired decorative illustrations. The cards remain a deliberately varied visual group rather than six generic identical list rows. Graphic Design remains a prominent anchor while the other categories retain the source's grouped mosaic character as available width changes.
- Snapshot and evidence: `SRC-DS-001`; `EVD-003`, `EVD-008`, `EVD-013`, `EVD-015`.
- Requirement references: `REQ-FR-002`, `REQ-FR-006`, `REQ-AR-004`, `REQ-AR-005`, `REQ-NFR-002`.
- Accessibility intent: Service illustrations remain decorative; label readability takes priority over retaining a known failing text/background combination.

### DES-005 — Keep About portrait-led and relationship-focused

- Classification: Observed
- Confidence: High
- Intent: Preserve the strong relationship between Amy's portrait and the About copy. At narrower supplied layouts the portrait precedes the text; at the wide composition the portrait and copy form a side-by-side relationship. The portrait remains meaningful content rather than decorative texture.
- Snapshot and evidence: `SRC-DS-001`; `EVD-004`, `EVD-008`, `EVD-010`, `EVD-015`.
- Requirement references: `REQ-FR-001`, `REQ-FR-006`, `REQ-AR-004`, `REQ-NFR-002`.
- Content edge intent: If copy expansion creates collision or excessive compression, preserve readable text and portrait recognition by allowing the layout to stay or return to the stacked relationship sooner.

### DES-006 — Make Work imagery the dominant portfolio evidence

- Classification: Confirmed
- Confidence: High
- Intent: Keep Work visually image-first: large project imagery carries the section, with previous/next controls visibly associated with the gallery but not competing with it. Work images remain presentation content, not project-detail links, in the current scope. Under the owner-resolved `AUD-009` correction, logical position 05 uses standalone `Asset/Work/05` (`6:380`) rather than the duplicated Work 02 instance currently assembled in Figma.
- Snapshot and evidence: `SRC-DS-001`; `EVD-005`, `EVD-010`, `EVD-015`, `EVD-017`; `AUD-002`; `AUD-009`.
- Requirement references: `REQ-FR-004`, `REQ-FR-005`, `REQ-AR-003`, `REQ-AR-004`, `REQ-NFR-002`.
- Design boundary: The owner-approved slot-05 correction is a traceable implementation deviation; it is not presented as current Figma assembly and does not itself authorize a Figma change.

### DES-007 — Preserve the closing Contact hierarchy and separate Footer role

- Classification: Observed
- Confidence: High
- Intent: Retain the dark Contact card as the strongest closing surface, with “Book a call with me”, supporting copy, and an accent consultation action. Keep the footer visually separate below it while aligning both regions to the same responsive content system.
- Snapshot and evidence: `SRC-DS-001`; `EVD-006`, `EVD-007`, `EVD-008`.
- Requirement references: `REQ-FR-001`, `REQ-FR-003`, `REQ-FR-006`, `REQ-NFR-002`.
- Design boundary: The footer does not become a new navigation system or introduce destinations not present in the approved scope.

### DES-008 — Use controlled visual deviations to resolve known contrast failures

- Classification: Confirmed
- Confidence: High
- Intent: Correct the Accent CTA text pairing and the UI/UX, Apps, and Photography service-label pairings while preserving the source's recognizable palette roles, hierarchy, and state distinction as closely as practical. A compliant pairing is more important than pixel-identical reproduction of a known accessibility failure.
- Snapshot and evidence: `SRC-DS-001`; `EVD-012`, `EVD-013`; `AUD-003`, `AUD-004` and their owner resolutions.
- Requirement references: `REQ-AR-005`, `REQ-NFR-002`.
- Deferred detail: Stage 4/planning will make the compliant treatment testable and select concrete values or token mappings; Stage 3 does not invent replacement colors without implementation-context validation.

### DES-009 — Preserve image meaning and decorative boundaries

- Classification: Confirmed
- Confidence: High
- Intent: Service artwork remains visual ornament attached to already visible service labels. The profile portrait and Work imagery remain meaningful visual content. Alternative text should communicate meaningful images' role without duplicating nearby text or turning decorative service artwork into screen-reader noise. Logical Work position 05 uses the standalone Work 05 asset and its corresponding alternative text under `AUD-009`.
- Snapshot and evidence: `SRC-DS-001`; `EVD-010`, `EVD-015`, `EVD-017`.
- Requirement references: `REQ-AR-004`, `REQ-NFR-002`.
- Deferred detail: Final implementation must preserve asset-specific alternative text and keep the `AUD-009` correction traceable.

### Responsive intent

#### DES-RWD-001 — Treat 375px, 768px, and 1440px as composition anchors, not hardcoded breakpoint rules

- Classification: Confirmed
- Confidence: High
- Intent: Match source relationships at the three supplied exemplars and interpolate between them without device-name-driven layout decisions. A transition is justified when the current arrangement would cause overlap, unreadably compressed copy, clipped essential content, broken image emphasis, or implementation-induced page-level horizontal scrolling.
- Snapshot and evidence: `SRC-DS-001`; `EVD-007`, `EVD-008`; `AUD-005`.
- Requirement references: `REQ-FR-006`, `REQ-AR-006`, `REQ-NFR-002`.
- Deferred detail: Numeric implementation breakpoints are not selected in Stage 3.

#### DES-RWD-002 — Let Hero and services expand from a narrow mosaic to the full wide composition

- Classification: Observed
- Confidence: High
- Intent: Keep the hero introduction visually centered and separate from the service-card group. At narrow widths service cards form a compact vertical/mosaic composition; at the middle exemplar they use a wider multi-column arrangement; at the wide exemplar they form the full desktop service grid. Preserve category order and visual prominence while allowing the grouping to wrap/recompose before labels or artwork collide.
- Snapshot and evidence: `SRC-DS-001`; `EVD-002`, `EVD-003`, `EVD-008`.
- Requirement references: `REQ-FR-002`, `REQ-FR-006`, `REQ-AR-006`, `REQ-NFR-002`.

#### DES-RWD-003 — Let About switch from portrait-first stacking to a wide side-by-side relationship

- Classification: Observed
- Confidence: High
- Intent: Preserve portrait-first reading at supplied narrow and middle compositions, then use the supplied wide side-by-side composition when there is sufficient room for both portrait and comfortable text measure. Do not force the wide relationship into a width where either element becomes cramped.
- Snapshot and evidence: `SRC-DS-001`; `EVD-004`, `EVD-008`; `Section/About` responsive variants.
- Requirement references: `REQ-FR-006`, `REQ-AR-004`, `REQ-AR-006`, `REQ-NFR-002`.

#### DES-RWD-004 — Preserve the Work carousel's intentional neighboring-image visibility

- Classification: Observed
- Confidence: High
- Intent: The Work viewport should communicate that more projects exist beyond the currently emphasized imagery. The narrow composition shows a cropped/partial horizontal gallery, the middle composition emphasizes a large central image with neighboring imagery visible at the edges, and the wide composition exposes three large items across. Preserve that “more content exists” cue rather than collapsing the section into a single isolated image at every width.
- Snapshot and evidence: `SRC-DS-001`; `EVD-005`, `EVD-008`, `EVD-015`, `EVD-017`; `Section/Work` responsive variants.
- Requirement references: `REQ-FR-004`, `REQ-FR-006`, `REQ-NFR-002`.
- Deferred detail: Stage 4 defines observable slide positioning, clipping, reachability, boundary behavior, and transition mechanics. The owner-resolved `AUD-009` correction changes only logical slot 05's asset mapping.

#### DES-RWD-005 — Let Contact move from centered stacking to horizontal wide-layout emphasis

- Classification: Observed
- Confidence: High
- Intent: Keep Contact content centered and vertically composed at supplied mobile/tablet layouts. At the wide layout, place copy and consultation action in a horizontal relationship within the dark panel. Header and Footer similarly grow from the narrow 343px content treatment through the 704px middle treatment to the 1110px wide treatment while preserving balanced page insets.
- Snapshot and evidence: `SRC-DS-001`; `EVD-006`, `EVD-007`, `EVD-008`; responsive component metadata.
- Requirement references: `REQ-FR-003`, `REQ-FR-006`, `REQ-AR-006`, `REQ-NFR-002`.

#### DES-RWD-006 — Scale typography visually without changing semantic hierarchy

- Classification: Observed
- Confidence: High
- Intent: Use the compact large treatment where the supplied mobile composition needs it and larger heading treatments when space supports them. Preserve readable line lengths and allow wrapping before reducing text to a scale that weakens hierarchy.
- Snapshot and evidence: `SRC-DS-001`; Figma Typography usage guidance; `EVD-002`, `EVD-004`, `EVD-005`, `EVD-006`.
- Requirement references: `REQ-AR-001`, `REQ-AR-006`, `REQ-NFR-002`.

### Interaction and motion intent

#### DES-INT-001 — Keep consultation actions as link semantics with button-like visual variants

- Classification: Confirmed
- Confidence: High
- Intent: Preserve the source's Dark and Accent action roles and their Default/Hover/Focus visual distinction while implementing consultation controls as links. Dark actions remain appropriate in header/footer contexts; Accent actions remain appropriate in About/Contact contexts, subject to the approved contrast correction.
- Snapshot and evidence: `SRC-DS-001`; `EVD-009`, `EVD-012`, `EVD-016`; `AUD-001` owner resolution.
- Requirement references: `REQ-FR-003`, `REQ-AR-002`, `REQ-AR-005`, `REQ-AR-007`.
- Design boundary: The placeholder `href="#"` is a product requirement, not a new destination or interaction flow.

#### DES-INT-002 — Treat Work controls as a conventional paired previous/next carousel control

- Classification: Confirmed
- Confidence: High
- Intent: Keep the circular previous/next controls visually paired with the Work gallery, with distinct Default/Hover/Focus presentations and directional iconography. Their accessible meaning remains equivalent to “Previous project” and “Next project”. The source base components are 64×64; the mobile Work composition scales the instances to 48×48.
- Snapshot and evidence: `SRC-DS-001`; `EVD-005`, `EVD-009`, `EVD-010`, `EVD-011`; `AUD-002` owner resolution.
- Requirement references: `REQ-FR-004`, `REQ-AR-002`, `REQ-AR-003`.
- Deferred detail: Stage 4 owns exact activation results, start state, wrap/boundary behavior, and disabled-state decisions if any.

#### DES-INT-003 — Keep interaction feedback restrained and reduced-motion-safe

- Classification: Recommended from observed source behavior
- Confidence: Medium
- Intent: Preserve the source's quick dissolve-style feedback as a restrained visual cue where useful, but reduce or suppress non-essential interpolation for users who prefer reduced motion. Visual distinction between states must remain perceivable even when motion is absent.
- Snapshot and evidence: `SRC-DS-001`; `EVD-016`; `AUD-006`.
- Requirement references: `REQ-AR-007`, `REQ-NFR-002`.
- Deferred detail: Stage 4 owns exact transition properties and carousel motion behavior.

#### DES-INT-004 — Treat focus as a first-class visual state, not a hover substitute

- Classification: Confirmed
- Confidence: High
- Intent: Every required interactive control keeps a clearly visible keyboard-focus treatment distinct enough to be recognized on its surrounding surface. Hover may enhance pointer feedback but must never be the only visible interaction state.
- Snapshot and evidence: `SRC-DS-001`; `EVD-009`; component Focus variants.
- Requirement references: `REQ-AR-002`, `REQ-AR-003`.
- Design boundary: Exact focus-ring implementation belongs to specification/planning; Stage 3 preserves visual intent and requirement.

### Content and edge-case intent

- Longer or zoomed text should increase block height or trigger an earlier responsive transformation rather than overlap imagery, clip text, or hide required actions. This carries `REQ-AR-006` into design intent without inventing fixed content limits.
- Service names remain fixed to the six approved labels. Decorative service artwork should never become more semantically prominent than those labels.
- Meaningful portrait and Work imagery should preserve recognizability when cropped; arbitrary cropping that removes the subject or makes a portfolio image unintelligible is outside the intended design.
- Work images remain non-interactive presentation content. Carousel controls are the current scope's Work interaction.
- Consultation actions retain their source label and visual prominence even though their destination is temporarily `#`.

### Design-system mapping and deviations

| Design concern | Source intent | Stage 3 mapping | Deviation status |
|---|---|---|---|
| Typography | Seven local text styles using Plus Jakarta Sans | Preserve role-based typography and responsive scale relationships | None expected |
| Page surface/text | Semantic neutral surface and primary text roles | Preserve as page baseline | None expected |
| Dark actions | Dark default with blue hover role and Focus variant | Preserve role/state hierarchy when contrast remains compliant | None expected |
| Accent actions | Light-red default / yellow hover role with light label | Preserve accent-action identity but correct failing text contrast | Approved accessibility deviation required (`AUD-003`) |
| Service cards | Six accent surfaces with white labels and decorative artwork | Preserve category color identity while correcting failing label pairings | Approved accessibility deviation required for UI/UX, Apps, Photography (`AUD-004`) |
| Spacing/radius | Local primitive spacing and radius scales | Preserve spacing rhythm and rounded geometry | No repository mapping chosen yet |
| Work imagery | Five logical Work slots and five standalone 540×360 assets; slot 05 currently instances Work 02 | Preserve image-first gallery and neighboring-item cue; logical slot 05 uses standalone Work 05 under the owner resolution | Approved source-correction deviation (`AUD-009`) |

### Deferred Stage 4 decisions

The following were intentionally **not** resolved as precise behavior in Stage 3:

- Numeric implementation breakpoints and exact interpolation thresholds.
- Carousel initial item/position, step size, wrap/loop or boundary behavior, disabled states if any, and exact transition mechanics.
- Exact compliant foreground/background token or color values for `AUD-003` and `AUD-004`.
- Final alternative-text wording for the profile portrait and Work assets.
- Exact focus-ring CSS, keyboard event implementation, or announcement behavior.
- Browser-support targets or performance thresholds not established by an authoritative project source.

Stage 5 later identified and resolved `AUD-009`: logical Work slot 05 uses standalone `Asset/Work/05` (`6:380`) for implementation, while the current Work 02 duplicate remains documented as source evidence.

### Stage 3 Review Pass 1 — Completeness and correctness

- [x] Information hierarchy and one-page reading order are explicit.
- [x] Visual system, typography, service cards, About, Work, Contact, imagery, and design-system mapping are covered at intent level rather than as a property dump.
- [x] Responsive intent explains transformations among supplied compositions and failure conditions that justify transitions without selecting arbitrary breakpoint numbers.
- [x] Consultation-link, carousel, hover, focus, and reduced-motion intent are separated from precise Stage 4 behavior.
- [x] Accessibility intent covers contrast deviations, focus visibility, image meaning, text reflow, and reduced motion.
- [x] Content edge cases and meaningful/decorative image boundaries are visible.

### Corrections from Stage 3 Review Pass 1

- Kept the Work “neighboring content” cue as a design intent while deferring exact carousel geometry and movement to Stage 4.
- Described contrast remediation as controlled deviation rather than inventing replacement token values before implementation-context validation.
- Made responsive transitions depend on content/layout failure instead of treating 375px, 768px, and 1440px as implementation breakpoints.
- Kept semantic heading stability separate from responsive typography sizing.
- Explicitly kept Work images non-interactive so visual affordance does not imply an unsupported project-detail flow.

### Stage 3 Review Pass 2 — Consistency, traceability, source integrity, risks, and uncertainty

- [x] All `DES-*`, `DES-RWD-*`, and `DES-INT-*` decisions reference approved `REQ-*` requirements and source/audit evidence.
- [x] Confirmed, Observed, Recommended, and deferred information remain visibly distinct.
- [x] No implementation architecture, component-file structure, arbitrary breakpoint, carousel business rule, or browser target is presented as design-source fact.
- [x] The fresh Stage 3 Figma metadata check is consistent with the canonical source-verification history and does not silently redefine the time-bound `SRC-DS-001` snapshot.
- [x] Approved owner resolutions for `AUD-001` through `AUD-004` remain intact and are not reframed as Figma-observed behavior.
- [x] The project remains Lite-eligible: Stage 3 introduces no routing, persistence, authentication, integration, or cross-cutting state architecture.

### Stage 3 readiness

**Approved through `GATE-004`.**

## 4. Specification

### Stage 4 source check

- `SRC-DS-001` remains time-bound. A fresh read-only Figma inspection on 2026-08-18 confirmed the scoped `🤖 Workflow` page (`2141:862`), the three Home exemplars, `Section/Work` (`2171:3199`), five standalone Work assets (`6:376` through `6:380`), and the Default/Hover/Focus variants of both carousel controls.
- The supplied Work geometry establishes logical Work position 03 as the initially centered/emphasized item at all three exemplars: 375px, 768px, and 1440px.
- The carousel controls expose no Disabled variant. Combined with the owner-approved “standard previous/next carousel” direction, Stage 4 specifies cyclic manual navigation rather than inventing a disabled visual state at the two ends.
- No autoplay, timed rotation, project-detail navigation, or consultation destination beyond `href="#"` is demonstrated by the source; none is added by this specification.
- Stage 5 later established that the scoped position named `Work Image / 05` instances `Asset/Work/02` in all three Work variants while `Asset/Work/05` exists unused. The project owner resolved this source inconsistency for implementation by selecting standalone `Asset/Work/05` (`6:380`) for logical position 05. The current Figma assembly remains unchanged and separately traceable as the observed source.
- `SRC-REPO-001` remains the immutable implementation baseline. Stage 4 defines observable behavior and acceptance criteria, not repository file structure or implementation order.

### Behavioral specification

#### SPEC-BEH-001 — Preserve one continuous page and source content order

- Requirement references: `REQ-FR-001`, `REQ-NFR-002`.
- Design references: `DES-001`, `DES-007`.
- Behavior:
  - Render one continuous page in the sequence Hero → About → Work → Contact → Footer.
  - Keep the header/hero composition, six service categories, About portrait/copy/action, five logical Work positions, Contact card, and footer available in the same page.
  - Do not require a route change, modal, overlay, or project-detail surface to access any current-scope content.

#### SPEC-BEH-002 — Preserve the six fixed service categories

- Requirement references: `REQ-FR-002`, `REQ-AR-004`, `REQ-AR-005`.
- Design references: `DES-004`, `DES-008`, `DES-009`.
- Behavior:
  - Render Graphic Design, UI/UX, Apps, Illustrations, Photography, and Motion Graphics once each with their corresponding source artwork.
  - Treat the service artwork as decorative because each card already exposes its category name in text.
  - Preserve the source card backgrounds and illustrations; only the text-color pairings explicitly corrected by `SPEC-ACC-005` may deviate for accessibility.

#### SPEC-BEH-003 — Interpolate responsively without treating exemplar widths as device breakpoints

- Requirement references: `REQ-FR-006`, `REQ-AR-006`, `REQ-NFR-002`.
- Design references: `DES-RWD-001` through `DES-RWD-006`.
- Behavior:
  - Match the source composition at 375px, 768px, and 1440px.
  - Between those widths, change layout before content overlaps, required text becomes unreadably narrow, controls collide, meaningful imagery loses its intended prominence, or the implementation creates page-level horizontal scrolling.
  - Heading and paragraph blocks may grow vertically; required copy must not be clipped by fixed-height text containers.
  - At 200% browser zoom, required content and controls remain available and operable.
  - At narrow reflow conditions down to 320 CSS px, the document itself does not require horizontal scrolling. Intentional horizontal overflow is contained within the Work gallery rather than leaking to the page.

#### SPEC-BEH-004 — Keep portfolio content available if carousel enhancement fails

- Requirement references: `REQ-FR-004`, `REQ-NFR-001`.
- Design references: `DES-006`, `DES-RWD-004`.
- Behavior:
  - The initial HTML contains all five logical Work positions; client JavaScript is not required to render the portfolio content.
  - If carousel JavaScript does not initialize, the five logical positions remain reachable through a static horizontally scrollable gallery or equivalent non-scripted fallback.
  - Logical position 05 uses standalone `Asset/Work/05` (`6:380`) under the owner-resolved `AUD-009` correction in both enhanced and fallback presentation.
  - Previous/next controls must not remain exposed as dead controls when their behavior is unavailable.
  - Failure of the Work enhancement must not affect Hero, About, Contact, footer, consultation links, or normal page scrolling.

### Interaction specification

#### SPEC-INT-001 — Consultation actions are native placeholder links

- Requirement references: `REQ-FR-003`, `REQ-AR-002`.
- Design references: `DES-INT-001`.
- Behavior:
  - Every source-observed “Free Consultation” action is a native link with the literal destination `href="#"`.
  - No route, booking flow, modal, external URL, or JavaScript destination is introduced.
  - Activation follows native link behavior; the implementation does not replace link semantics with a button.

#### SPEC-INT-002 — Work carousel starts on item 03 and never auto-rotates

- Requirement references: `REQ-FR-004`, `REQ-FR-005`.
- Design references: `DES-006`, `DES-RWD-004`, `DES-INT-002`.
- Data reference: `SPEC-DATA-001`.
- Behavior:
  - Logical Work order is 01 → 02 → 03 → 04 → 05.
  - On initial page load, Work item 03 is the active, centered/emphasized item at the supplied mobile, tablet, and desktop compositions.
  - The carousel changes only after an explicit user action. It does not autoplay, auto-advance, or add a rotation timer.
  - Work images are presentation content, not links.

#### SPEC-INT-003 — Previous and next move one item and wrap cyclically

- Requirement references: `REQ-FR-004`, `REQ-AR-002`, `REQ-AR-003`.
- Design references: `DES-INT-002`.
- Behavior:
  - “Previous project” moves the active item exactly one position backward.
  - “Next project” moves the active item exactly one position forward.
  - From item 01, Previous wraps to item 05.
  - From item 05, Next wraps to item 01.
  - The controls therefore remain available at every logical position; no Disabled state is introduced.
  - A single activation causes a single logical step even if multiple items are visible at once.
  - Pointer, touch, Enter, and Space activation of the control buttons produce the same logical result.

#### SPEC-INT-004 — Preserve centered active-item geometry and neighboring-content cues

- Requirement references: `REQ-FR-004`, `REQ-FR-006`, `REQ-NFR-002`.
- Design references: `DES-006`, `DES-RWD-004`.
- Behavior at source exemplars:
  - At 375px, the active Work item is 270×180 and centered; small portions of the previous and next logical items remain visible at the left and right edges.
  - At 768px, the active Work item is 540×360 and centered; neighboring items remain partially visible at both edges.
  - At 1440px, the active Work item is 540×360 and centered; substantial portions of both neighboring items remain visible, preserving the source's broad three-item gallery impression.
  - When navigation wraps at item 01 or item 05, the logical neighboring item on the opposite end of the ordered set supplies the corresponding edge cue.
  - Intermediate widths preserve the same relationship proportionally rather than snapping to a generic one-image-only layout.

#### SPEC-INT-005 — Keep motion restrained and deterministic

- Requirement references: `REQ-AR-007`, `REQ-NFR-002`.
- Design references: `DES-INT-003`.
- Behavior:
  - Default manual carousel movement may animate as one short 200ms translation using an ease-out timing curve, derived from the source's established short interaction timing.
  - Repeated activations are serialized so the active logical item changes one step per accepted activation; the carousel must not end in an indeterminate half-position.
  - Hover/focus state feedback may preserve the source's short dissolve-style feedback.
  - Under `prefers-reduced-motion: reduce`, non-essential interpolation is removed and the new carousel position/state appears without motion while preserving the same logical result.

### Accessibility specification

#### SPEC-ACC-001 — Preserve semantic page and heading structure

- Requirement references: `REQ-AR-001`, `REQ-AR-006`.
- Design references: `DES-003`, `DES-RWD-006`.
- Behavior:
  - The hero title “Design solutions made easy” is the page-level heading.
  - About, Work, and Contact headings introduce their page sections at the next semantic level.
  - Visual typography changes across viewports do not change those semantic relationships.
  - Service labels remain semantic text; their heading level, if any, is chosen from the document outline rather than the `Typography/Heading/Medium` visual style alone.
  - The main content is exposed through appropriate document landmarks without adding redundant landmark regions.

#### SPEC-ACC-002 — Use native keyboard behavior and a visible focus state

- Requirement references: `REQ-AR-002`, `REQ-AR-003`.
- Design references: `DES-INT-001`, `DES-INT-002`, `DES-INT-004`.
- Behavior:
  - Consultation actions remain native links and carousel controls remain native buttons.
  - `Tab` and `Shift+Tab` follow normal document order; no script overrides the page tab sequence.
  - Carousel buttons activate with Enter or Space.
  - Activating Previous or Next does not move keyboard focus away from the activated button.
  - Required interactive elements expose the source-observed focus presentation through a visible `:focus-visible` treatment.
  - Hover is never the only perceivable interaction state.

#### SPEC-ACC-003 — Expose understandable carousel names, structure, and manual updates

- Requirement references: `REQ-AR-003`, `REQ-AR-002`.
- Design references: `DES-INT-002`.
- Behavior:
  - The Work carousel is programmatically identified as a carousel and is labelled from the visible “My Work” heading.
  - The previous and next buttons expose accessible names equivalent to “Previous project” and “Next project”.
  - Each Work item is exposed as a slide/group with a position label equivalent to “1 of 5” through “5 of 5”.
  - After manual navigation, assistive technology receives a polite update equivalent to “Project N of 5” for the newly active item.
  - Because the carousel does not auto-rotate, there is no rotation-control button.
  - Partially visible current/neighbor items are not incorrectly hidden from assistive technology solely because they are clipped visually.

#### SPEC-ACC-004 — Use final alternative text for meaningful imagery

- Requirement references: `REQ-AR-004`.
- Design references: `DES-005`, `DES-006`, `DES-009`.
- Behavior:
  - Service artwork is decorative (`alt=""` for image elements, or equivalent assistive-technology exclusion for inline decorative graphics).
  - Profile portrait alternative text: **“Portrait of Amy smiling against a colorful geometric background.”**
  - Work 01 alternative text: **“Abstract blue folded forms over a light blue textured background.”**
  - Work 02 alternative text: **“Purple geometric pattern with circles, arrows, arches, and starbursts.”**
  - Work 03 alternative text: **“Hand holding a colorful illustrated newspaper over a geometric background.”**
  - Work 04 alternative text: **“Black graphic design booklet on yellow papers beside vinyl records.”**
  - Work 05 alternative text for standalone `Asset/Work/05` (`6:380`): **“Hand holding a smartphone displaying a designer portfolio beside a drink and small plant.”**
  - Under the owner-resolved `AUD-009` correction, logical slot 05 renders standalone `Asset/Work/05` and uses the Work 05 alternative text above. The current Figma Work 02 duplicate remains source evidence only.
  - Alternative text is not duplicated as a visible caption unless a later product requirement adds captions.

#### SPEC-ACC-005 — Correct the known text contrast failures with the existing dark text role

- Requirement references: `REQ-AR-005`, `REQ-NFR-002`.
- Design references: `DES-002`, `DES-008`.
- Behavior:
  - Use the existing primary text role (`color/text/primary`, observed as `#030303`) for the Accent CTA label in Default and Hover states while retaining the source action backgrounds.
  - Use the same primary text role for UI/UX, Apps, and Photography service labels while retaining their source card backgrounds and artwork.
  - Keep currently passing source pairings unchanged unless implementation token binding requires an equivalent compliant value.
- Measured target pairings:
  - Accent CTA Default: `#030303` on `#E16B5B` ≈ **6.34:1**.
  - Accent CTA Hover: `#030303` on `#F6A560` ≈ **10.28:1**.
  - UI/UX mobile/tablet: `#030303` on observed `#EC9B56` ≈ **9.22:1**.
  - UI/UX desktop: `#030303` on observed `#F6A560` ≈ **10.28:1**.
  - Apps: `#030303` on `#F39E9E` ≈ **10.01:1**.
  - Photography: `#030303` on `#61C4B7` ≈ **9.91:1**.
- Validation threshold:
  - Normal-size action text must meet at least 4.5:1.
  - Large-scale service-label text must meet at least 3:1.
  - The implementation is validated from rendered colors, not only token names.

#### SPEC-ACC-006 — Preserve reflow and reduced-motion behavior

- Requirement references: `REQ-AR-006`, `REQ-AR-007`.
- Design references: `DES-RWD-001`, `DES-RWD-003`, `DES-INT-003`.
- Behavior:
  - Text resizing or wrapping may increase section height or trigger an earlier responsive transformation; it must not overlap required imagery or controls.
  - At 200% zoom, consultation links, Work controls, headings, and required body content remain available.
  - Reduced-motion preference removes non-essential track/state interpolation but does not remove state distinction, focus indication, or navigation functionality.

### Data specification

#### SPEC-DATA-001 — Work carousel has one fixed ordered five-position dataset

| Position | Implementation mapping | Meaning |
|---:|---|---|
| 1 | `Asset/Work/01` (`6:376`) | Meaningful Work image |
| 2 | `Asset/Work/02` (`6:377`) | Meaningful Work image |
| 3 | `Asset/Work/03` (`6:378`) | Meaningful Work image and initial active item |
| 4 | `Asset/Work/04` (`6:379`) | Meaningful Work image |
| 5 | `Asset/Work/05` (`6:380`) | Meaningful Work image; owner-resolved `AUD-009` correction from the current assembled Work 02 duplicate |

- No position has a project-detail destination in current scope.
- The ordered logical dataset is cyclic for Previous/Next navigation only; position order remains 01–05.
- The position-05 deviation from the current Figma `Section/Work` assembly must remain traceable to `AUD-009` / `EX-002` during implementation and validation.

### Validation specification

#### SPEC-VAL-001 — Visual and responsive validation

Validate the rendered page against `SRC-DS-001` at:
- 375px: mobile composition, active Work 03 centered at 270×180, 48×48 mobile carousel controls, source hierarchy preserved.
- 768px: tablet composition, active Work 03 centered at 540×360, neighboring-image cue preserved.
- 1440px: desktop composition, active Work 03 centered at 540×360, wide neighboring-image cue and desktop section relationships preserved.
- At least one width between each supplied exemplar must be checked for overlap, clipping, control collision, and implementation-induced page-level horizontal scrolling.
- Accessibility corrections from `SPEC-ACC-005` and the owner-approved `AUD-009` slot-05 correction are expected traceable deviations; unrelated redesign is a failure.

#### SPEC-VAL-002 — Interaction and accessibility validation

Validate at minimum:
- Keyboard traversal reaches consultation links and both carousel buttons in meaningful document order.
- Enter activates links; Enter and Space activate carousel buttons.
- Focus remains on the activated Previous/Next button after a slide change.
- Five consecutive logical positions can be reached in each direction, including 01↔05 wrap.
- No autoplay occurs.
- Accessible names, carousel/slide structure, slide-position context, meaningful image alternatives matching actual rendered assets, and polite manual-change feedback are exposed to assistive technology.
- Logical position 05 renders standalone `Asset/Work/05` (`6:380`) and exposes the corresponding Work 05 alternative text.
- Default, Hover, and Focus states remain visually distinct.
- Contrast is measured from rendered colors and meets the applicable threshold.
- `prefers-reduced-motion: reduce` removes non-essential motion while preserving operation and state changes.
- 200% zoom does not hide or clip required content or controls.

#### SPEC-VAL-003 — Progressive-enhancement and recovery validation

- With carousel JavaScript prevented from initializing, all five logical Work positions remain present and reachable, including standalone Work 05 at logical position 05.
- Dead previous/next controls are not exposed in the failed/uninitialized state.
- All non-carousel page content remains readable and operable.
- A carousel script error must not block page rendering or normal document scrolling.

### Acceptance criteria

| ID | Testable acceptance |
|---|---|
| `AC-001` | One page contains Hero, About, Work, Contact, and Footer in that order with no required route change. |
| `AC-002` | All six named services and their corresponding source artwork are present; service artwork is excluded from redundant assistive-technology output. |
| `AC-003` | Every “Free Consultation” action is a native link whose current destination is exactly `#`; no invented booking/navigation behavior is present. |
| `AC-004` | On initial load at 375px, 768px, and 1440px, Work item 03 is the centered/emphasized logical item. |
| `AC-005` | Previous/Next changes exactly one logical item, wraps 01↔05, never auto-rotates, and never requires a Disabled control state. |
| `AC-006` | All five logical Work positions are reachable in both directions, none is a project-detail link, and slot 05 uses standalone `Asset/Work/05` (`6:380`) under the owner-resolved `AUD-009` correction. |
| `AC-007` | Work preserves a centered active item and visible neighboring-content cue at the three supplied exemplars and usable interpolation between them. |
| `AC-008` | Consultation links and carousel buttons use native keyboard semantics, have visible focus, and carousel activation does not move focus. |
| `AC-009` | The carousel is programmatically labelled from “My Work”; controls have Previous/Next project names; items expose position context; manual changes produce polite position feedback. |
| `AC-010` | Decorative service graphics are hidden from assistive technology; the profile and each rendered Work position use alternative text matching the actual asset, including standalone Work 05 at logical slot 05. |
| `AC-011` | Accent CTA, UI/UX, Apps, and Photography text uses the specified dark text role and meets applicable WCAG AA contrast thresholds in rendered states. |
| `AC-012` | At supplied and intermediate widths, at 200% zoom, and down to 320 CSS px reflow conditions, required content is not clipped or made unreachable and page-level horizontal overflow is not introduced. |
| `AC-013` | With reduced motion requested, the same control/state outcomes occur without non-essential carousel or dissolve interpolation. |
| `AC-014` | Without successful carousel JavaScript initialization, all five logical Work positions remain reachable, including standalone Work 05 at position 05, and no dead carousel controls are exposed. |
| `AC-015` | Visual comparison at 375px, 768px, and 1440px preserves source hierarchy, spacing relationships, image emphasis, and component-state intent except for approved contrast deviations and the explicit `AUD-009` Work 05 correction. |
| `AC-016` | No backend, persistence, authentication, external API, extra route, modal, or Work-detail destination is introduced. |

### Stage 4 non-goals and deferred implementation detail

- Numeric CSS breakpoint values remain a planning/implementation choice constrained by `SPEC-BEH-003` and the three visual anchors; the supplied widths are validation anchors, not mandatory media-query values.
- DOM/component file boundaries, CSS organization, carousel implementation technique, clone/virtualization strategy for cyclic edges, and JavaScript module structure remain repository-aware planning decisions.
- No browser-support matrix or performance budget is invented because no authoritative project source establishes one.
- No additional Figma edits are required by this specification or by the owner-resolved `AUD-009` implementation correction.
- Stage 5 is approved through `GATE-006` and Stage 6 architecture through `GATE-007`; Stage 7 repository-aware planning is now active, while task decomposition and implementation remain unstarted.

### Stage 4 Review Pass 1 — Completeness and correctness

- [x] Every approved functional, accessibility, and quality requirement has an observable Stage 4 behavior or validation path.
- [x] Carousel initial state, one-step movement, cyclic edge behavior, no-autoplay rule, focus behavior, accessible naming, position feedback, and reduced-motion outcome are defined.
- [x] Responsive behavior is testable at all supplied anchors and at intermediate/reflow conditions without turning the Figma widths into arbitrary implementation breakpoints.
- [x] Alternative-text wording was defined from direct asset inspection; Stage 5 later corrected logical slot 05 to use the standalone Work 05 asset and its corresponding text under `AUD-009`.
- [x] Known contrast failures have concrete compliant text-role mappings and measurable rendered targets.
- [x] Failure/recovery behavior keeps the static portfolio content available when client enhancement is unavailable.
- [x] No project-detail behavior, consultation destination, backend, persistence, authentication, or unsupported product flow was invented.

### Corrections from Stage 4 Review Pass 1

- Replaced the previously unresolved carousel start position with Work item 03 after verifying that its center aligns with the viewport center in all three supplied Work variants.
- Chose cyclic one-item navigation so the source's always-available Previous/Next controls do not require an unsupported Disabled state.
- Explicitly prohibited autoplay because neither the design evidence nor owner direction establishes timed rotation.
- Finalized image alternatives from rendered asset inspection rather than generic filenames; Stage 5 later identified and owner-resolved the scoped slot-05 source inconsistency.
- Resolved `AUD-003` and `AUD-004` with the existing dark primary text role while preserving the source accent backgrounds.
- Added a progressive-enhancement recovery path so the static Astro page never loses Work content solely because carousel JavaScript fails.

### Stage 4 Review Pass 2 — Consistency, traceability, source integrity, risks, and uncertainty

- [x] All material `SPEC-*` entries trace to approved `REQ-*`, `DES-*`, `EVD-*`, `AUD-*`, or the Stage 4 Figma re-verification.
- [x] Source-observed facts remain distinct from Stage 4 decisions: item 03 centering and control-state inventory are observed; cyclic wrapping and exact compliant text mapping are specification decisions.
- [x] `AUD-001` through `AUD-004` owner resolutions are preserved without rewriting them as Figma-observed behavior.
- [x] Accessibility behavior uses native link/button semantics and a standard manually controlled carousel model rather than adding custom keyboard conventions.
- [x] The specification does not prescribe repository file architecture, arbitrary breakpoint numbers, a backend, or unsupported routing.
- [x] The project remains Lite-eligible: Stage 4 adds only bounded client interaction behavior to the existing single static page.
- [x] `SRC-DS-001` remains explicitly time-bound and must be reverified before downstream material work.

### Stage 4 readiness

**Approved through `GATE-005`.** The Stage 4 specification passed its gate and the workflow advanced to Stage 5. Stage 5 subsequently found `AUD-009`; the project owner resolved that source inconsistency by selecting standalone `Asset/Work/05` (`6:380`) for logical position 05.

## 5. Repository Context

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
| `frontend/src/components/ConsultationLink.astro` | Create | No | Repeated native `href="#"` consultation action with Dark/Accent visual roles. |
| `frontend/src/scripts/work-carousel.ts` | Create | No | Dependency-free progressive enhancement for cyclic one-step Work navigation and live feedback. |
| `frontend/src/styles/global.css` | Create | No | Base/reset rules, source token mappings, typography, page surface, shared focus/layout primitives. |
| `frontend/src/styles/page.css` | Create | No | Static section and service-card layout/responsive rules. |
| `frontend/src/styles/work-carousel.css` | Create | No | No-JS gallery, enhanced track geometry, controls, transitions, and reduced-motion rules. |
| `frontend/src/assets/portfolio/` | Create | No | Exported source assets; exact filenames/formats follow inspected Figma exports. Logical Work slot 05 uses standalone `Asset/Work/05` (`6:380`). |

### Implementation constraints from the repository

- Keep all static content Astro-rendered. Add client JavaScript only for the Work enhancement; do not introduce a framework island or third-party carousel package for this bounded interaction.
- Keep styles in external CSS files rather than inline style attributes.
- Treat 375px, 768px, and 1440px as visual validation anchors. Select actual media-query thresholds from layout failure conditions, not device-name defaults or copied exemplar widths.
- Do not add routes, APIs, persistence, authentication, project-detail links, autoplay, or consultation behavior beyond the approved `href="#"` placeholder.
- Export source assets without changing Figma. Preserve the owner-approved `AUD-009` Work 05 correction.
- Plus Jakarta Sans delivery must be resolved from a permitted source before typography is considered complete; do not silently add an unreviewed runtime service or dependency.
- Existing Astro/Vercel delivery remains the deployment model; this plan adds no deployment-topology or production-promotion change.

## 6. Implementation Plan

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
  - Render every source-observed consultation action as a native link with literal `href="#"`, preserving Dark/Accent visual roles and visible `:focus-visible` treatment.
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

## 7. Architecture Decision

- Separate architecture needed: **No — Not required**.
- CLI decision: `architecture decide not-required`.
- Profile impact: Remain **Lite**; no profile upgrade is required.
- Reason: The approved product is one static Astro page. It adds no routes, shared application state, persistence, backend/API integration, authentication, data migration, security/privacy-sensitive workflow, or cross-service reliability/observability concern. Existing Astro/Vercel build and deployment behavior remains unchanged. The only client-side state is the bounded Work carousel, already specified as isolated progressive enhancement with a non-JavaScript fallback.
- Consequence: Do not create `ARCHITECTURE.md`. Component boundaries, file placement, carousel implementation details, and validation order belong to Stage 7 planning and later task decomposition rather than a separate architecture layer.

### Stage 6 review pass 1 — Architecture-driver scan

- [x] Routing: no additional route, dynamic route, middleware, or navigation architecture is introduced.
- [x] Shared state/data flow: no page-wide application state, cross-component store, persistence, server state, or synchronization concern is required.
- [x] APIs/integrations/auth: no backend, external API, authentication, authorization, payments, analytics integration, or user-data workflow is in scope.
- [x] Build/deployment/migration: the existing static Astro + Vercel delivery model remains sufficient; no deployment topology, runtime, storage, or migration change is required.
- [x] Security/privacy/reliability/observability: the approved scope introduces no architecture-level concern in these areas beyond normal frontend implementation quality.
- [x] Interactive behavior: the Work carousel is local, bounded client-side UI state with specified keyboard/accessibility behavior and progressive enhancement; it does not justify a separate architecture artifact.

### Stage 6 review pass 2 — Consistency and over-engineering challenge

- [x] The Not-required decision is consistent with the approved requirements, design intent, specification, Stage 5 document review, and current repository structure.
- [x] No hidden requirement was found that would force routing, persistence, shared state, framework islands, third-party services, or a server runtime.
- [x] Deferring component/file decomposition to Stage 7 preserves the workflow boundary: implementation structure is a planning decision, not evidence of architecture complexity by itself.
- [x] Remaining Lite avoids an unnecessary profile upgrade while retaining explicit traceability for the only interactive subsystem, the Work carousel.
- [x] If later scope adds routing, shared state, persistence, APIs, authentication, deployment topology changes, or other architecture drivers, this decision must be reopened rather than silently stretched.

## 8. Source-change Handling

- Snapshot verification required before task execution: Yes, including re-verification of time-bound `SRC-DS-001` and the applicable repository task-start snapshot.
- Material changes that invalidate this brief: Changes to scoped page structure, content, responsive compositions, component behavior, Work assets/interactions, consultation behavior, or approved accessibility direction.
- Earliest workflow section or stage to revisit: The earliest ownership stage affected by the changed evidence; create new `SRC-*` records and perform impact assessment rather than silently reusing `SRC-DS-001`.

## 9. Risks, Assumptions, and Questions

### Blocking

- None. Stage 6 is approved through `GATE-007`, `AUD-009` is owner-resolved, and the inspected repository has no structural blocker to Stage 7 planning.

### Non-blocking

- `SRC-DS-001` remains mutable/time-bound and must be reverified before implementation task execution.
- Portfolio image/vector exports and a permitted Plus Jakarta Sans delivery source are not present in the repository. They are implementation asset inputs, not reasons to invent a dependency or runtime service during planning.
- Exact media-query values are intentionally not fixed by the 375px/768px/1440px exemplars. Implementation selects transition points from rendered failure conditions and validates both anchors and intermediate widths.
- The repository currently exposes only the production build as an automated frontend check. Browser-based visual, keyboard, focus, contrast, zoom/reflow, reduced-motion, no-JavaScript, and assistive-structure validation remain explicit evidence requirements.
- The optional visual-clone technique in `PLAN-003` is limited to cyclic edge animation and must remain assistive-hidden/non-interactive; prefer a simpler equivalent implementation if it satisfies the specified geometry and behavior.
- No task IDs exist yet. Stage 9 will decompose the approved plan after the separate Stage 8 adversarial review.

## 10. Traceability

Stage 4 specification entries carry direct requirement and design references. The consolidated checkpoint mapping is:

| Specification area | Upstream requirements | Design intent | Acceptance |
|---|---|---|---|
| `SPEC-BEH-001`–`004` | `REQ-FR-001`, `REQ-FR-002`, `REQ-FR-004`, `REQ-FR-006`, `REQ-AR-004`–`006`, `REQ-NFR-001`–`002` | `DES-001`, `DES-004`, `DES-006`–`009`, `DES-RWD-*` | `AC-001`, `AC-002`, `AC-007`, `AC-012`, `AC-014`, `AC-015` |
| `SPEC-INT-001` | `REQ-FR-003`, `REQ-AR-002` | `DES-INT-001` | `AC-003`, `AC-008` |
| `SPEC-INT-002`–`005` | `REQ-FR-004`, `REQ-FR-005`, `REQ-AR-002`, `REQ-AR-003`, `REQ-AR-007`, `REQ-NFR-002` | `DES-006`, `DES-RWD-004`, `DES-INT-002`–`004` | `AC-004`–`009`, `AC-013` |
| `SPEC-ACC-001`–`006` | `REQ-AR-001`–`007`, `REQ-NFR-002` | `DES-003`, `DES-005`, `DES-006`, `DES-008`, `DES-009`, `DES-RWD-*`, `DES-INT-*` | `AC-008`–`013`, `AC-015` |
| `SPEC-DATA-001` | `REQ-FR-004`, `REQ-FR-005`, `REQ-AR-004` | `DES-006`, `DES-009` | `AC-004`–`006`, `AC-010` |
| `SPEC-VAL-001`–`003` | All approved current-scope requirements | All Stage 3 design-intent areas | `AC-001`–`016` |
| `AUD-009` propagation | `REQ-FR-004`, `REQ-AR-004`, `REQ-NFR-002` | `DES-006`, `DES-009`, `DES-RWD-004` | `SPEC-DATA-001`, `SPEC-ACC-004`, `AC-006`, `AC-010`, `AC-015` |

Stage 7 adds repository-aware `PLAN-*` ownership while task IDs remain deferred to Stage 9.

| Plan item | Primary specification coverage | Acceptance coverage |
|---|---|---|
| `PLAN-001` | `SPEC-BEH-001`, `SPEC-BEH-003`, `SPEC-ACC-001`, `SPEC-ACC-005`, `SPEC-ACC-006`, `SPEC-VAL-001`, `SPEC-VAL-003` | `AC-001`, `AC-011`, `AC-012`, `AC-015`, `AC-016` |
| `PLAN-002` | `SPEC-BEH-001`–`003`, `SPEC-INT-001`, `SPEC-ACC-001`, `SPEC-ACC-002`, `SPEC-ACC-004`–`006`, `SPEC-VAL-001`, `SPEC-VAL-003` | `AC-001`–`003`, `AC-008`, `AC-010`–`013`, `AC-015`, `AC-016` |
| `PLAN-003` | `SPEC-BEH-003`, `SPEC-BEH-004`, `SPEC-INT-002`–`005`, `SPEC-ACC-002`–`004`, `SPEC-ACC-006`, `SPEC-DATA-001`, `SPEC-VAL-001`–`003` | `AC-004`–`010`, `AC-012`–`015` |
| `PLAN-004` | All approved current-scope specification areas as integrated verification | `AC-001`–`AC-016` |

`PLAN-001`–`PLAN-004` are the Stage 7 decomposition boundary. Stage 9 will create task IDs that reference these approved plan items rather than re-planning the implementation.

## 11. Review Pass 1 — Feasibility and Completeness

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
- [x] The plan preserves `AUD-001` (`href="#"`), `AUD-002` (standard carousel), `AUD-003`/`AUD-004` (contrast corrections), and `AUD-009` (standalone Work 05 at logical slot 05).
- [x] The carousel plan preserves item 03 start, cyclic one-step navigation, no autoplay, native buttons, focus retention, live position feedback, reduced motion, and non-JavaScript reachability.
- [x] No arbitrary browser matrix, performance budget, breakpoint, dependency, test command, or deployment topology is invented.
- [x] Remaining uncertainty is visible and non-blocking: exact exported asset filenames/formats, permitted font delivery, and final failure-driven media-query values are resolved during implementation from source and rendered evidence.
- [x] The plan remains small enough for the Lite brief; no profile upgrade is warranted.

## 14. Readiness

**Stage 7 content complete; ready for canonical Stage 7 preflight and project-owner approval.** Repository inspection, `PLAN-001` through `PLAN-004`, two required review passes, risks, ordering, and validation are documented. The consolidated brief should remain `Reviewed` for the Stage 7 gate.

The Stage 7 gate is intentionally **not** recorded as passed by this change. Stage 8 — adversarial plan review — must not start until explicit project-owner approval is recorded and the workflow advances.
