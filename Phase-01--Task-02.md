---
artifact: TASK
id: P01-T02
status: Draft
baseline:
  design:
    - SRC-DS-001
  repository:
    - SRC-REPO-002
  runtime:
    - SRC-RUN-001
  documentation:
    - ART-IMPLEMENTATION-REVIEW
  assets: []
created: 2026-08-18
updated: 2026-08-18
project: Single-page design portfolio
profile: Lite
execution_mode: Gated
---

# Phase 01 — Task 02: Correct Work carousel list semantics

## 1. Objective

Correct the Stage 11 accessibility finding `IMPL-001` without changing the approved design or carousel behavior. The Work track must remain a semantic list whose direct children retain native list-item semantics, while each logical Work item still exposes the approved slide/group position context to assistive technology.

This correction must produce a new implementation-output snapshot derived from `SRC-REPO-002` and must be fully retested before the workflow returns to final implementation review.

## 2. Source References

- Design input: `SRC-DS-001` — current Stage 11 verification `VER-011` is Unchanged.
- Repository baseline: `SRC-REPO-002` at commit `edd76540e89eb4e82c82ab567c183eb1b9abf0f4`.
- Validation runtime: `SRC-RUN-001` — READY Vercel preview for the previous implementation output.
- Finding: `IMPL-001` — Stage 11 axe-core detected a serious WCAG 1.3.1 list-structure violation at 375px, 768px, and 1440px.
- Plan references: `PLAN-003`, `PLAN-004`.
- Specification references: `SPEC-ACC-003`, `SPEC-VAL-002`, `SPEC-VAL-003`.
- Acceptance references: `AC-005`, `AC-007`, `AC-008`, `AC-009`, `AC-012`, `AC-013`, `AC-014`, `AC-015`.
- Related task: `P01-T01` — complete; output `SRC-REPO-002`.

## 3. Finding and Failure Evidence

Fresh Stage 11 validation used `@axe-core/playwright` against the unchanged `SRC-REPO-002` frontend. At all three supplied design widths, axe-core reported rule `list` with **serious** impact and WCAG 1.3.1 tagging.

Observed cause:

- `#work-carousel-track` is a `<ul>`.
- Its direct children are `<li>` elements with explicit `role="group"`.
- The explicit role overrides each child’s native `listitem` role.
- The `<ul>` therefore no longer has direct children exposed as list items, violating list structure.

The same validation confirmed the production build still succeeds and the separate keyboard/live-announcement check passes. The correction is therefore scoped to semantic structure, with regression protection for the already-approved interaction and visual behavior.

## 4. Snapshot Verification

Immediately before implementation:

- Reverify `SRC-DS-001`; stop if the scoped Figma design has materially changed.
- Confirm task-start `HEAD` descends from `SRC-REPO-002` and that unrelated frontend changes have not entered the branch.
- Classify workflow/review-only commits after `SRC-REPO-002` as expected workflow output.
- No design rebaseline is expected for this correction.

## 5. Prerequisites

- Stage 11 finding `IMPL-001` remains unresolved.
- `P01-T01` remains complete and `SRC-REPO-002` remains the previous implementation output.
- The correction is approved through the new Stage 9 gate before code edits begin.
- Root and frontend `AGENTS.md` remain controlling repository instructions.
- Existing source assets, content, carousel dataset, and responsive geometry must remain unchanged.

## 6. Scope

### Included

- Correct the Work carousel DOM/ARIA structure so the `<ul>` directly owns native list items.
- Preserve an accessible per-slide grouping/position description without overriding the list-item role; an inner semantic group is the preferred minimal approach if needed.
- Preserve `aria-current`, the labelled carousel region, Previous/Next accessible names, polite live feedback, and all five meaningful image alternatives.
- Re-run build, axe-core, carousel regression, responsive/visual regression, and Vercel-preview validation.
- Update `IMPLEMENTATION-REVIEW.md` with the finding, correction, and retest evidence when returning to Stage 11.

### Excluded

- Visual redesign or spacing changes.
- Carousel motion, ordering, timing, or navigation changes.
- New dependencies in the committed frontend.
- Additional routes, backend behavior, APIs, persistence, authentication, autoplay, modal behavior, or project-detail links.
- Unrelated guideline polish discovered during final review unless it is required to resolve a failing acceptance criterion.

## 7. Repository Context

The affected implementation is isolated to the Work carousel:

- `frontend/src/components/Work.astro` owns the semantic Work markup and slide labels.
- `frontend/src/scripts/work-carousel.ts` owns cyclic state, `aria-current`, live feedback, and input serialization.
- `frontend/src/styles/work-carousel.css` owns slide geometry and enhancement layout.

The current failure is caused by markup semantics in `Work.astro`; no evidence currently requires changes to carousel state logic or responsive geometry.

## 8. Files and Modules

| Path | Action | Responsibility |
|---|---|---|
| `frontend/src/components/Work.astro` | Modify | Restore valid list/list-item semantics while retaining slide/group position context. |
| `frontend/src/styles/work-carousel.css` | Modify only if required | Keep any added semantic wrapper layout-neutral. |
| `frontend/src/scripts/work-carousel.ts` | Modify only if required | Preserve current state/announcement behavior if semantic ownership of `aria-current` needs adjustment. |
| `IMPLEMENTATION-REVIEW.md` | Update after retest | Record `IMPL-001`, correction evidence, and final review status. |

No other product files are expected to change.

## 9. Dependencies and Interfaces

- The five-item ordered dataset and item-03 initial state remain unchanged.
- The direct `<ul>` → `<li>` semantic relationship is mandatory after correction.
- Per-slide position context must remain equivalent to “1 of 5” through “5 of 5”.
- The carousel region remains labelled by “My Work”.
- No-JavaScript fallback must remain a horizontally reachable five-item list without dead controls.

## 10. Ordered Implementation Steps

1. Reverify task-start design and repository inputs.
2. Inspect `Work.astro`, carousel CSS, and carousel script against `IMPL-001`.
3. Apply the smallest markup-semantic correction that preserves native list-item ownership and the approved slide/group position context.
4. Build the production site.
5. Run axe-core at 375px, 768px, and 1440px and verify no critical or serious violations remain.
6. Re-run keyboard, focus, live-region, cyclic navigation, rapid-input, touch, reduced-motion, and no-JavaScript regression checks.
7. Confirm 320px reflow and supplied Figma exemplars have no visual/layout regression.
8. Verify a corrected Vercel preview.
9. Record all five task checks as Passed only with executed evidence.
10. Complete `P01-T02`, creating a new Implementation-output snapshot derived from `SRC-REPO-002`.

## 11. Accessibility and Responsive Requirements

### Accessibility

- `<ul>`/`<li>` native structure must remain valid in the accessibility tree.
- Explicit slide/group semantics must not replace the native `listitem` role on the `<li>`.
- Position context remains exposed for each logical Work item.
- Previous/Next buttons remain native buttons with visible focus.
- Enter and Space activation retain focus on the activated control.
- Manual changes continue to announce “Project N of 5” politely.
- Meaningful image alternatives remain unchanged.

### Responsive and motion

- No layout change at 375px, 768px, or 1440px.
- No implementation-caused page-level horizontal overflow at 320px.
- Reduced-motion behavior and carousel outcomes remain identical to `SRC-REPO-002`.

## 12. Validation

The canonical task defines five required checks:

1. **Build** — `pnpm build` succeeds from `frontend/`.
2. **Accessibility semantics** — axe-core reports no critical/serious violations at 375/768/1440; list semantics and carousel accessibility remain correct.
3. **Carousel regression** — item 03 start, cyclic one-step movement, keyboard/touch, focus retention, rapid-input serialization, reduced motion, and no-JS fallback pass.
4. **Responsive and visual regression** — no layout/fidelity regression at the three Figma anchors or 320px reflow.
5. **Vercel preview** — corrected branch preview is READY and exposes corrected carousel semantics before final review.

## 13. Acceptance Criteria

- [ ] `IMPL-001` is corrected: the Work `<ul>` directly contains list items that preserve their native role.
- [ ] Axe-core reports no critical or serious violations at 375px, 768px, and 1440px.
- [ ] `AC-005`, `AC-007`, `AC-008`, `AC-009`, `AC-013`, and `AC-014` remain unchanged and pass regression checks.
- [ ] `AC-012` remains valid at 320px reflow.
- [ ] `AC-015` visual fidelity remains unchanged at all supplied exemplars.
- [ ] The corrected Vercel preview is verified.
- [ ] A new Implementation-output snapshot is recorded with parent lineage from `SRC-REPO-002`.

## 14. Risks and Considerations

| Risk | Impact | Mitigation |
|---|---|---|
| Fixing ARIA by replacing list semantics with generic containers | Could trade one semantic problem for another | Preserve native `<ul>/<li>` first; add group semantics inside rather than overriding the list item. |
| Added wrapper changes slide dimensions | Could regress exact carousel geometry | Keep wrapper layout-neutral and compare all three exemplar widths. |
| Moving ARIA state breaks announcements | Could regress screen-reader behavior | Re-run focus/live-region and accessible-tree checks. |
| Correction is visually invisible | Could be missed by visual-only review | Axe-core/WCAG structure test is a required completion check. |

## 15. Implementation Discoveries

| Discovery | Impact | Owning artifact | Required update |
|---|---|---|---|
| `IMPL-001`: explicit `role="group"` on Work `<li>` breaks list structure | Serious WCAG 1.3.1 failure at all supplied viewports | `IMPLEMENTATION-REVIEW.md` | Record finding, correction, and retest before final acceptance. |

## 16. Deviations

None planned. The correction is required to satisfy the already-approved accessibility specification; it does not change product behavior or visual intent.

## 17. Definition of Done

- [ ] The semantic defect is corrected within scope.
- [ ] All five required task validations pass with evidence.
- [ ] No visual or interaction regression is introduced.
- [ ] `P01-T02` produces a new implementation-output snapshot derived from `SRC-REPO-002`.
- [ ] Stage 10 can be re-approved with the corrected output.
- [ ] Stage 11 final review can resume with `IMPL-001` marked corrected and retested.
