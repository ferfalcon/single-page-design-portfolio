---
artifact: TASK
id: P01-T01
status: Not started
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

# Phase 01 — Task 01: Implement and validate the single-page portfolio

## 1. Objective

Replace the existing Astro starter with the complete approved Single-page design portfolio Home page and deliver it as one coherent, independently verifiable result: source-faithful static sections, accessible responsive behavior, the progressively enhanced five-item Work carousel, and the final integrated regression/preview gate described by `PLAN-001` through `PLAN-004`.

The task must remain within the approved single-page scope. It must not add routes, backend behavior, authentication, persistence, external APIs, Work-detail navigation, autoplay, a modal, or an invented consultation destination.

## 2. Source References

- Source baseline: `SOURCE-BASELINE.md`
- Design input: `SRC-DS-001`
- Repository implementation baseline: `SRC-REPO-001`
- Current workflow-only repository state inspected for decomposition: `main` at `9940af6c0cd6875708a7845b5d37614fda961ac4`
- Supporting runtime inputs: None
- Documentation inputs: `DESIGN-AUDIT.md`, `IMPLEMENTATION-BRIEF.md`, `PROJECT-CONTEXT.md`, `WORKFLOW-STATE.md`
- Asset inputs: Figma-scoped source assets from `SRC-DS-001`; exported filenames/formats are intentionally unresolved until implementation inspection
- Plan references: `PLAN-001`, `PLAN-002`, `PLAN-003`, `PLAN-004`
- Requirement references: `REQ-FR-001`–`REQ-FR-006`, `REQ-AR-001`–`REQ-AR-007`, `REQ-NFR-001`, `REQ-NFR-002`
- Specification references: all approved current-scope `SPEC-BEH-*`, `SPEC-INT-*`, `SPEC-ACC-*`, `SPEC-DATA-001`, and `SPEC-VAL-*` entries in `IMPLEMENTATION-BRIEF.md`
- Acceptance references: `AC-001`–`AC-016`
- Design/audit decisions: `AUD-001`, `AUD-002`, `AUD-003`, `AUD-004`, `AUD-009`
- Architecture: Stage 6 decision is **Not required**; no architecture artifact applies
- Related tasks: None

## 3. Snapshot Verification

Complete again immediately before Stage 10 implementation begins.

- Design verification requirement: recheck the scoped `🤖 Workflow` page and the mobile/tablet/desktop Home exemplars because `SRC-DS-001` is time-bound.
- Repository verification requirement: confirm the implementation-relevant frontend still matches `SRC-REPO-001` except for expected workflow/documentation output, and confirm the task-start branch descends from current approved `main`.
- Current decomposition observation: `main` at `9940af6c0cd6875708a7845b5d37614fda961ac4` is the approved Stage 8 merge. Current `frontend/` inspection still shows the Astro starter: `Welcome.astro`, one `index.astro`, one `Layout.astro`, and starter `astro.svg`/`background.svg` assets.
- Difference classification at decomposition: Expected workflow output only; no frontend implementation change observed.
- Upstream rebaseline required now: No.
- Blocking condition: if the Figma scope or implementation-relevant frontend changes materially before task start, stop and classify/rebaseline before coding.

## 4. Prerequisites

- Stage 8 plan review remains approved and `GATE-009` remains Passed.
- Stage 9 task decomposition is approved before entering Stage 10.
- The task is registered in canonical workflow state and marked Ready only after required references, validation definitions, and trace coverage are complete.
- `SRC-DS-001` and the task-start repository state are freshly verified before implementation.
- Before HTML, CSS, or client-side JavaScript work, follow `.agents/skills/modern-web-guidance/SKILL.md` as required by root `AGENTS.md`.
- Use Context7 for version-specific Astro/web-platform guidance when needed.
- Resolve real Figma exports and a permitted Plus Jakarta Sans delivery source from authoritative evidence; do not fabricate asset filenames, dependencies, licenses, or runtime services.

## 5. Scope

### Included

- Replace starter page content with the complete source-observed single-page portfolio.
- Implement Header/Hero/services, About, Work, Contact, and Footer in the approved reading order.
- Implement all six service categories and source artwork.
- Render source-observed “Free Consultation” actions as native links with literal `href="#"`.
- Implement semantic structure, heading hierarchy, meaningful/decorative image treatment, keyboard behavior, visible focus, contrast corrections, resilient reflow/zoom, reduced-motion behavior, and failure-driven responsive transitions as part of the relevant implementation work.
- Implement Work as a dependency-free, progressively enhanced five-item cyclic previous/next carousel with logical item 03 as the enhanced initial active item, item 05 mapped to standalone `Asset/Work/05`, native controls, accessible naming/position feedback, focus retention, rapid-input safety, no autoplay, reduced-motion handling, and a usable no-JavaScript fallback exposing all five originals without dead controls.
- Run the integrated production-build, browser, accessibility, responsive, visual-comparison, no-JavaScript, and Vercel-preview verification required by `PLAN-004`.
- Correct implementation defects discovered by those checks without expanding product scope.

### Excluded

- Additional routes or pages.
- Backend, API, authentication, persistence, database, or external integration work.
- Work-item detail navigation or project links.
- Carousel autoplay.
- Consultation booking behavior beyond the approved `href="#"` placeholder.
- Structural or visual Figma edits.
- Unrelated refactors, framework changes, state libraries, carousel packages, or new deployment topology.

## 6. Repository Context

Task decomposition is based on current approved `main` commit `9940af6c0cd6875708a7845b5d37614fda961ac4`.

Observed current frontend state:

- Framework: Astro with TypeScript/module output.
- `frontend/package.json` declares Astro `^7.2.2`, Node `>=22.12.0`, and only `dev`, `build`, `preview`, and `astro` scripts.
- `frontend/src/pages/index.astro` exists as the only page.
- `frontend/src/layouts/Layout.astro` exists as the current layout.
- `frontend/src/components/Welcome.astro` is the only current component and is starter-only.
- `frontend/src/assets/astro.svg` and `frontend/src/assets/background.svg` are starter assets.
- No repository-confirmed lint, unit, component, E2E, or automated accessibility command exists today. `pnpm build` is the only confirmed automated frontend validation command.
- `frontend/AGENTS.md` requires Astro dev-server background mode when a server is started.

## 7. Files and Modules

| Path | Action | Existing or proposed | Responsibility |
|---|---|---|---|
| `frontend/src/pages/index.astro` | Modify | Existing | Compose the approved single-page section order and page-level semantics. |
| `frontend/src/layouts/Layout.astro` | Modify | Existing | Document shell, metadata, global stylesheet/font integration. |
| `frontend/src/components/Welcome.astro` | Delete when unused | Existing | Remove starter-only UI. |
| `frontend/src/components/Header.astro` | Create | Proposed | Brand/header and consultation action. |
| `frontend/src/components/Hero.astro` | Create | Proposed | Intro and six-service presentation. |
| `frontend/src/components/About.astro` | Create | Proposed | About content and profile portrait. |
| `frontend/src/components/Work.astro` | Create | Proposed | Semantic Work section and progressive-enhancement hooks. |
| `frontend/src/components/Contact.astro` | Create | Proposed | Contact call-to-action section. |
| `frontend/src/components/Footer.astro` | Create | Proposed | Footer composition. |
| `frontend/src/components/ConsultationLink.astro` | Create | Proposed | Repeated native consultation-link behavior and visual variants. |
| `frontend/src/styles/global.css` | Create | Proposed | Reset/base rules, reusable source-token mappings, typography, color/contrast primitives, focus/reflow foundations. |
| `frontend/src/styles/page.css` | Create | Proposed | Page/section layout and responsive behavior. |
| `frontend/src/styles/work-carousel.css` | Create | Proposed | Work geometry, responsive presentation, control states, and motion/reduced-motion behavior. |
| `frontend/src/scripts/work-carousel.ts` | Create | Proposed | Dependency-free Work enhancement, cyclic navigation, state, live feedback, and failure-safe control exposure. |
| `frontend/src/assets/portfolio/` | Create/populate | Proposed | Approved exported portfolio artwork, portrait, and Work assets. |
| `frontend/src/assets/astro.svg` | Delete when unused | Existing | Remove starter-only asset. |
| `frontend/src/assets/background.svg` | Delete when unused | Existing | Remove starter-only asset. |

Exact portfolio export filenames/formats remain implementation evidence and must not be invented during decomposition.

## 8. Dependencies and Interfaces

- `PLAN-001` foundation work precedes section/carousel integration because shared shell, styles, assets, and token mappings are prerequisites.
- Static sections and Work may be implemented in separate internal slices, but this Stage 9 task remains one implementation result and one final task completion event.
- `index.astro`, shared styles, and portfolio assets are coordination points; avoid concurrent conflicting edits if work is split internally.
- Work enhancement must preserve useful initial HTML when JavaScript is unavailable or fails.
- Any visual clones used only for cyclic edge animation must be implementation-only, assistive-hidden, and non-focusable; prefer a simpler equivalent if rendered testing shows clones are unnecessary.
- No public API, backend contract, migration, or shared application-state interface is introduced.

## 9. Ordered Implementation Steps

1. Re-read root and `frontend/` `AGENTS.md`, then run canonical workflow context/checks before coding.
2. Freshly verify the active Figma scope and task-start repository state; stop on unexpected material change.
3. Inspect the mandatory modern-web guidance and current Astro documentation needed for the implementation.
4. Export/resolve the approved portfolio assets, including standalone Work 05, and resolve a permitted Plus Jakarta Sans delivery approach without inventing an unsupported dependency/service.
5. Implement `PLAN-001`: replace the starter foundation, establish semantic page shell, external CSS structure, reusable source-token mappings, contrast-remediation primitives, resilient page sizing/reflow rules, and portfolio asset organization.
6. Implement `PLAN-002`: build Header, Hero/services, About, Contact, Footer, and repeated ConsultationLink behavior with accessibility and responsive behavior integrated rather than deferred.
7. Implement `PLAN-003`: build the semantic five-item Work section and dependency-free progressive enhancement with approved cyclic interaction, item-03 enhanced start, item-05 correction, keyboard/pointer behavior, focus retention, live position feedback, rapid-input handling, reduced motion, and no-JavaScript reachability.
8. Integrate all sections, resolve shared-style/file conflicts, and keep client JavaScript limited to the Work interaction.
9. Run the repository-confirmed production build and the manual validation matrix below; correct defects within approved scope.
10. Create and inspect the Vercel preview for the branch. Compare the rendered result with Figma at the supplied exemplars and intermediate/reflow conditions.
11. Re-run affected validation after corrections. Do not claim any check Passed without execution evidence.
12. Commit the completed implementation, record Implementation-output lineage through the workflow CLI, update task validation/task status, and proceed only to the next workflow gate permitted by canonical state.

## 10. State, Responsive, and Accessibility Requirements

### States and failure behavior

- Static content: no loading state is expected because there is no data fetch.
- Consultation links: default, hover, focus-visible, and activation must remain native-link behavior; destination remains `#`.
- Work enhancement unavailable/failed: all five original Work items remain reachable/readable through a non-scripted presentation and dead Previous/Next controls are not exposed.
- Work enhancement active: item 03 begins as the logical active item; each activation moves exactly one item; 01↔05 wraps cyclically; focus stays on the activated control; rapid inputs cannot leave state between items.
- Work items are not links and do not invent detail destinations.

### Responsive behavior

- Validate source fidelity at 375px, 768px, and 1440px viewport widths.
- Select actual CSS transition points from content/layout failure rather than copying device labels as arbitrary breakpoints.
- Validate intermediate widths, especially around service-grid, About image/text, Work-neighbor, Contact, and footer transitions.
- Validate 320 CSS px reflow and 200% zoom without implementation-caused page-level horizontal scrolling, clipped essential text, or unreachable controls.
- Allow content blocks to grow under wrapping/zoom; avoid fixed-height text containers that truncate required copy.

### Accessibility

- Use semantic landmarks/sections and a coherent heading hierarchy independent of responsive visual font size.
- Keep service artwork decorative to assistive technology; provide meaningful alternatives for the profile portrait and each actual Work image.
- Consultation links and carousel buttons must be native keyboard-operable controls with clearly visible focus.
- Previous/Next accessible names must communicate “Previous project” and “Next project”.
- The Work region must be labelled from “My Work”; semantic slides expose position context 1-of-5 through 5-of-5; manual navigation announces an equivalent of “Project N of 5” politely without moving focus.
- Apply the approved dark-text contrast correction to the Accent CTA and UI/UX, Apps, and Photography labels so implemented text meets applicable WCAG AA contrast for rendered size/weight.
- Preserve required hover/focus distinction under `prefers-reduced-motion: reduce`; suppress non-essential interpolation without changing carousel outcome.

## 11. Validation

### Automated validation

- Build: run `pnpm build` from `frontend/`; expected result is a successful Astro production build with no required build errors.
- Unit tests: Not repository-confirmed; do not claim or invent a command.
- Component/integration tests: Not repository-confirmed.
- End-to-end tests: Not repository-confirmed.
- Type checking/linting: no standalone repository-confirmed command; only checks actually provided/executed by the current project may be reported.

### Manual/browser validation

- Confirm document landmarks, heading order, and source-observed section sequence.
- Confirm all six service categories and their matching approved artwork.
- Confirm every consultation action is a link with literal `href="#"`, keyboard activation, and visible focus.
- Confirm meaningful/decorative image alternatives, including standalone Work 05 at logical position 05.
- Measure/check the known remediated text contrast pairings in implemented default/interactive states.
- Confirm unenhanced/failed-enhancement Work fallback exposes all five originals and no dead carousel controls.
- Confirm enhanced initial item 03, Previous/Next names, Enter/Space activation, pointer/touch operation, one-step movement, both cyclic edges, focus retention, rapid-input serialization, slide position context, and live status updates.
- Confirm reduced-motion behavior preserves the same logical carousel result without non-essential motion.
- Compare rendered output with `SRC-DS-001` at 375px, 768px, and 1440px, plus intermediate widths.
- Check 320 CSS px reflow and 200% zoom for readability, reachability, and absence of implementation-caused page horizontal overflow.
- Verify no unsupported route, modal, API, backend, auth, persistence, Work-detail link, autoplay, or invented consultation destination entered scope.
- Verify the branch Vercel preview before merge and capture enough evidence to support the workflow validation/result claims.

## 12. Acceptance Criteria

- [ ] `AC-001`–`AC-003`: complete page content, six services, and approved consultation-link behavior are observable and correct.
- [ ] `AC-004`–`AC-010`: Work fallback/enhancement, five logical positions, Work 05 correction, cyclic navigation, naming/feedback, interaction, and image meaning are verified.
- [ ] `AC-011`–`AC-015`: semantic structure, focus/keyboard behavior, contrast, responsive/reflow behavior, reduced motion, and source fidelity are verified.
- [ ] `AC-016`: implementation remains lightweight/static Astro with client JavaScript limited to justified Work behavior.
- [ ] The three supplied design exemplars and intermediate widths pass visual/responsive inspection within approved accessibility deviations.
- [ ] `pnpm build` passes on the completed task output.
- [ ] Required manual validation and Vercel preview verification are completed with evidence.
- [ ] Fresh input/task-start snapshot verification is complete and no unresolved material source drift remains.
- [ ] The committed result is recorded as an Implementation-output repository snapshot with parent lineage.
- [ ] Task validation and canonical task status are updated through the workflow CLI.

## 13. Risks and Considerations

| Risk or assumption | Impact | Mitigation or validation |
|---|---|---|
| `SRC-DS-001` is mutable/time-bound. | Implementation could silently target newer design content. | Freshly verify scoped Figma nodes before Stage 10; stop/rebaseline on material drift. |
| Portfolio exports are not present in the starter repo. | Wrong asset/filename/content could reduce fidelity. | Export from authoritative scoped Figma source during implementation; do not invent filenames during decomposition. |
| Plus Jakarta Sans delivery is unresolved. | Typography fidelity or licensing/delivery could be mishandled. | Resolve a permitted authoritative delivery source before claiming typography completion; avoid unreviewed packages/runtime services. |
| Exact breakpoints are intentionally unspecified. | Blind device breakpoints could fail at intermediate widths. | Select transitions from rendered failure conditions and test anchors plus intermediate widths. |
| Carousel cyclic animation may tempt duplicate semantic content. | Screen-reader duplication/focus bugs. | Prefer originals-only technique; if visual clones are required, keep them assistive-hidden/non-focusable and snap state back to originals. |
| Repository has no automated a11y/E2E suite. | Manual regressions are easier to miss. | Use explicit evidence-backed browser matrix plus production build and preview verification; add tooling only if narrowly justified and plan remains consistent. |
| Root Node guidance text and package engine differ. | Agents could assert an unsupported exact Node requirement. | Treat `frontend/package.json` (`>=22.12.0`) as implementation engine evidence unless repository/runtime is explicitly changed. |

## 14. Implementation Discoveries

Record discoveries here during Stage 10. Do not silently work around an upstream documentation/source error.

| Discovery | Impact | Owning artifact | Required update |
|---|---|---|---|
| None at decomposition. | None. | N/A | N/A |

## 15. Deviations

None at decomposition. Record any approved implementation deviation with evidence before task completion.

## 16. Definition of Done

- [ ] The complete approved single-page portfolio is implemented within `P01-T01` scope.
- [ ] All task acceptance criteria pass.
- [ ] Required build and manual/browser/preview validation executed successfully.
- [ ] No required validation remains failing or unverified.
- [ ] Input and task-start repository verification remain valid or an approved rebaseline was completed.
- [ ] The implementation output snapshot and parent lineage are recorded canonically.
- [ ] Accessibility, responsive behavior, states, fallback behavior, and reduced motion are implemented with the behavior they verify, not deferred to cleanup.
- [ ] Discoveries/deviations/remaining risks are recorded.
- [ ] Relevant workflow documentation and task status are updated.
- [ ] The result is ready for the Stage 11 final implementation review only after canonical Stage 10 completion requirements are satisfied.

## 17. Completion Report

Complete after implementation, not during Stage 9.

- Files created, modified, or deleted:
- Input snapshot IDs used:
- Task-start repository snapshot:
- Implementation-output repository snapshot:
- Source verification performed:
- Behavior implemented:
- Validation executed:
- Validation results:
- Deviations:
- Remaining risks:
- Documentation updated:
- Next permitted workflow action:
