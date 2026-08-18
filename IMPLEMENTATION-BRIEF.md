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
- Current workflow checkpoint: Stage 3 — Design Intent
- Requirements are approved through `GATE-003`. Design intent is the active checkpoint; specification, repository-aware planning, architecture decision, and final Lite review are intentionally not started.

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

**Approved through `GATE-003`.** Stage 3 — Design Intent is the active gated checkpoint.

## 3. Design Intent

### Stage 3 source check

- `SRC-DS-001` remains time-bound. A fresh metadata inspection on 2026-08-18 again confirmed the scoped `🤖 Workflow` page (`2141:862`), the 375px, 768px, and 1440px Home exemplars, responsive Header/Footer/Hero/About/Work/Contact component sets, Default/Hover/Focus control variants, the profile portrait, and all five Work assets.
- The supplied widths remain design exemplars rather than implementation breakpoint instructions. Stage 3 describes intended transformations and failure conditions; Stage 4 and planning may make them testable and select concrete implementation values where necessary.
- The immutable implementation baseline remains `SRC-REPO-001`. Stage 3 does not prescribe repository architecture or implementation paths.

### Design principles

- Preserve the source’s friendly portfolio character: warm neutral page surface, bold Plus Jakarta Sans typography, colorful service cards, large imagery, rounded controls, generous whitespace, and a dark closing call-to-action.
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
- Intent: The hero remains the dominant page heading. About, Work, and Contact remain section-level headings. Service labels remain subordinate to the hero introduction. Mobile may use the source’s compact large heading treatment while larger layouts use larger heading styles, but visual size changes must not change document meaning or reading hierarchy.
- Snapshot and evidence: `SRC-DS-001`; `EVD-002` through `EVD-006`; Figma Typography usage guidance.
- Requirement references: `REQ-AR-001`, `REQ-AR-006`, `REQ-NFR-002`.
- Content edge intent: Heading and paragraph containers may grow vertically when text wraps; typography must not depend on fixed heights that clip required content.

### DES-004 — Keep the six service cards individually recognizable and visually grouped

- Classification: Observed
- Confidence: High
- Intent: Preserve all six service categories as distinct colored cards with their paired decorative illustrations. The cards remain a deliberately varied visual group rather than six generic identical list rows. Graphic Design remains a prominent anchor while the other categories retain the source’s grouped mosaic character as available width changes.
- Snapshot and evidence: `SRC-DS-001`; `EVD-003`, `EVD-008`, `EVD-013`, `EVD-015`.
- Requirement references: `REQ-FR-002`, `REQ-FR-006`, `REQ-AR-004`, `REQ-AR-005`, `REQ-NFR-002`.
- Accessibility intent: Service illustrations remain decorative; label readability takes priority over retaining a known failing text/background combination.

### DES-005 — Keep About portrait-led and relationship-focused

- Classification: Observed
- Confidence: High
- Intent: Preserve the strong relationship between Amy’s portrait and the About copy. At narrower supplied layouts the portrait precedes the text; at the wide composition the portrait and copy form a side-by-side relationship. The portrait remains meaningful content rather than decorative texture.
- Snapshot and evidence: `SRC-DS-001`; `EVD-004`, `EVD-008`, `EVD-010`, `EVD-015`.
- Requirement references: `REQ-FR-001`, `REQ-FR-006`, `REQ-AR-004`, `REQ-NFR-002`.
- Content edge intent: If copy expansion creates collision or excessive compression, preserve readable text and portrait recognition by allowing the layout to stay or return to the stacked relationship sooner.

### DES-006 — Make Work imagery the dominant portfolio evidence

- Classification: Confirmed
- Confidence: High
- Intent: Keep Work visually image-first: large project imagery carries the section, with previous/next controls visibly associated with the gallery but not competing with it. Work images remain presentation content, not project-detail links, in the current scope.
- Snapshot and evidence: `SRC-DS-001`; `EVD-005`, `EVD-010`, `EVD-015`; `AUD-002` owner resolution.
- Requirement references: `REQ-FR-004`, `REQ-FR-005`, `REQ-AR-003`, `REQ-AR-004`, `REQ-NFR-002`.
- Design boundary: Stage 3 does not define the initial slide, wrap/loop rule, boundary state, or exact transition algorithm.

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
- Intent: Correct the Accent CTA text pairing and the UI/UX, Apps, and Photography service-label pairings while preserving the source’s recognizable palette roles, hierarchy, and state distinction as closely as practical. A compliant pairing is more important than pixel-identical reproduction of a known accessibility failure.
- Snapshot and evidence: `SRC-DS-001`; `EVD-012`, `EVD-013`; `AUD-003`, `AUD-004` and their owner resolutions.
- Requirement references: `REQ-AR-005`, `REQ-NFR-002`.
- Deferred detail: Stage 4/planning will make the compliant treatment testable and select concrete values or token mappings; Stage 3 does not invent replacement colors without implementation-context validation.

### DES-009 — Preserve image meaning and decorative boundaries

- Classification: Confirmed
- Confidence: High
- Intent: Service artwork remains visual ornament attached to already visible service labels. The profile portrait and Work imagery remain meaningful visual content. Alternative text should communicate meaningful images’ role without duplicating nearby text or turning decorative service artwork into screen-reader noise.
- Snapshot and evidence: `SRC-DS-001`; `EVD-010`, `EVD-015`.
- Requirement references: `REQ-AR-004`, `REQ-NFR-002`.
- Deferred detail: Final alternative-text wording belongs to Stage 4/implementation once visible context and asset treatment are fixed.

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

#### DES-RWD-004 — Preserve the Work carousel’s intentional neighboring-image visibility

- Classification: Observed
- Confidence: High
- Intent: The Work viewport should communicate that more projects exist beyond the currently emphasized imagery. The narrow composition shows a cropped/partial horizontal gallery, the middle composition emphasizes a large central image with neighboring imagery visible at the edges, and the wide composition exposes three large items across. Preserve that “more content exists” cue rather than collapsing the section into a single isolated image at every width.
- Snapshot and evidence: `SRC-DS-001`; `EVD-005`, `EVD-008`, `EVD-015`; `Section/Work` responsive variants.
- Requirement references: `REQ-FR-004`, `REQ-FR-006`, `REQ-NFR-002`.
- Deferred detail: Stage 4 defines observable slide positioning, clipping, reachability, boundary behavior, and transition mechanics.

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
- Intent: Preserve the source’s Dark and Accent action roles and their Default/Hover/Focus visual distinction while implementing consultation controls as links. Dark actions remain appropriate in header/footer contexts; Accent actions remain appropriate in About/Contact contexts, subject to the approved contrast correction.
- Snapshot and evidence: `SRC-DS-001`; `EVD-009`, `EVD-012`, `EVD-016`; `AUD-001` owner resolution.
- Requirement references: `REQ-FR-003`, `REQ-AR-002`, `REQ-AR-005`, `REQ-AR-007`.
- Design boundary: The placeholder `href="#"` is a product requirement, not a new destination or interaction flow.

#### DES-INT-002 — Treat Work controls as a conventional paired previous/next carousel control

- Classification: Confirmed
- Confidence: High
- Intent: Keep the 64×64 circular previous/next controls visually paired with the Work gallery, with distinct Default/Hover/Focus presentations and directional iconography. Their accessible meaning remains equivalent to “Previous project” and “Next project”.
- Snapshot and evidence: `SRC-DS-001`; `EVD-005`, `EVD-009`, `EVD-010`, `EVD-011`; `AUD-002` owner resolution.
- Requirement references: `REQ-FR-004`, `REQ-AR-002`, `REQ-AR-003`.
- Deferred detail: Stage 4 owns exact activation results, start state, wrap/boundary behavior, and disabled-state decisions if any.

#### DES-INT-003 — Keep interaction feedback restrained and reduced-motion-safe

- Classification: Recommended from observed source behavior
- Confidence: Medium
- Intent: Preserve the source’s quick dissolve-style feedback as a restrained visual cue where useful, but reduce or suppress non-essential interpolation for users who prefer reduced motion. Visual distinction between states must remain perceivable even when motion is absent.
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
- Work images remain non-interactive presentation content. Carousel controls are the current scope’s Work interaction.
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
| Work imagery | Five 540×360 source assets | Preserve image-first gallery and neighboring-item cue | No project-link behavior added |

### Deferred Stage 4 decisions

The following are intentionally **not** resolved as precise behavior in Stage 3:

- Numeric implementation breakpoints and exact interpolation thresholds.
- Carousel initial item/position, step size, wrap/loop or boundary behavior, disabled states if any, and exact transition mechanics.
- Exact compliant foreground/background token or color values for `AUD-003` and `AUD-004`.
- Final alternative-text wording for the profile portrait and five Work images.
- Exact focus-ring CSS, keyboard event implementation, or announcement behavior.
- Browser-support targets or performance thresholds not established by an authoritative project source.

None of these items blocks the design-intent checkpoint because their outcomes or ownership boundaries are explicit.

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
- [x] The fresh Stage 3 Figma metadata check is consistent with `VER-003` and does not silently redefine the time-bound `SRC-DS-001` snapshot.
- [x] Approved owner resolutions for `AUD-001` through `AUD-004` remain intact and are not reframed as Figma-observed behavior.
- [x] The project remains Lite-eligible: Stage 3 introduces no routing, persistence, authentication, integration, or cross-cutting state architecture.

### Stage 3 readiness

**Ready for gated Stage 3 approval.** Stage 4 — Specification has not been started.

## 4. Specification

Not started. Reserved for Stage 4 after the preceding gated approval.

## 5. Repository Context

Detailed repository inspection for planning has not started. Current project constraints remain governed by `SRC-REPO-001`, `PROJECT-CONTEXT.md`, root `AGENTS.md`, and the nearest scoped instructions.

## 6. Implementation Plan

Not started. Reserved for the Lite planning checkpoint after requirements, design intent, specification, and documentation review are approved.

## 7. Architecture Decision

- Separate architecture needed: Not evaluated yet.
- Reason: Architecture handling remains reserved for its workflow checkpoint; approved requirements and Stage 3 design intent introduce no new architecture-driving concern.

## 8. Source-change Handling

- Snapshot verification required before task execution: Yes, including re-verification of time-bound `SRC-DS-001` and the applicable repository task-start snapshot.
- Material changes that invalidate this brief: Changes to scoped page structure, content, responsive compositions, component behavior, Work assets/interactions, consultation behavior, or approved accessibility direction.
- Earliest workflow section or stage to revisit: The earliest ownership stage affected by the changed evidence; create new `SRC-*` records and perform impact assessment rather than silently reusing `SRC-DS-001`.

## 9. Risks, Assumptions, and Questions

### Blocking

- None for the Stage 3 design-intent checkpoint.

### Non-blocking

- `SRC-DS-001` remains mutable and time-bound.
- Exact carousel mechanics, breakpoint placement, compliant contrast treatment, and final image-alt wording remain intentionally unresolved until their owning later stages.
- `GATE-003` records the approved Stage 2 requirements. Stage 3 preflight/gate has not been recorded; Stage 4 remains blocked pending explicit Stage 3 approval.

## 10. Traceability

Stage 2 requirements and Stage 3 design decisions carry direct upstream references in their owning entries. The consolidated cross-section traceability table will be completed after Stage 4 and planning identifiers exist.

## 11. Review Pass 1 — Completeness and Correctness

Overall Lite review not started. Stage-specific review passes are recorded in the Requirements and Design Intent sections.

## 12. Corrections from Pass 1

Overall Lite review corrections not started.

## 13. Review Pass 2 — Consistency, Traceability, Source Integrity, Risks, and Uncertainty

Overall Lite review not started. Stage-specific consistency reviews are recorded in the Requirements and Design Intent sections.

## 14. Readiness

Not evaluated for task decomposition. The current gated checkpoint is **Stage 3 design intent ready for approval**; Stage 4 has not started.
