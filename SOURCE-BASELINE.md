---
artifact: SOURCE-BASELINE
project: Single-page design portfolio
profile: Lite
execution_mode: Gated
created: 2026-08-18
updated: 2026-08-18
---

# Source Baseline

## 2. Document Information

- Project: Single-page design portfolio
- Created: 2026-08-18
- Last updated: 2026-08-18
- Owner: Project owner
- Related context: `PROJECT-CONTEXT.md`
- Operational state: `WORKFLOW-STATE.md`

## 3. Design Source Evidence

### SRC-DS-001 — Figma `🤖 Workflow` baseline

- **Source type:** Figma
- **Purpose:** Authoritative design source for the single-page portfolio implementation.
- **Included scope:** Figma page `🤖 Workflow` (`2141:862`), including responsive Home frames, local section/navigation components, design-system documentation, and assets used by those frames.
- **Explicitly observed responsive frames:** `Home / Mobile` (`2141:14174`, 375×3318), `Home / Tablet` (`2141:14238`, 768×2966), and `Home / Desktop` (`2141:14302`, 1440×2642).
- **Observed reusable areas:** Navigation/Header, Navigation/Footer, Section/Hero, Section/About, Section/Work, Section/Contact, button and carousel states, portfolio/service assets, and color/spacing/radius/typography documentation.
- **Excluded scope:** Other Figma pages and any structural or visual design edits outside `🤖 Workflow`.
- **Captured or inspected at:** 2026-08-18T01:55:05Z
- **Version, revision, or checksum evidence:** The supplied Figma URL is mutable; the workflow record therefore classifies this source as `Time-bound`, not immutable.
- **Captured evidence:** Direct Figma metadata inspection of node `2141:862`.
- **Access and reproduction instructions:** Open the project Figma URL and inspect node `2141:862` on page `🤖 Workflow`.
- **Dependencies:** Local components, variables/styles, and assets referenced inside the scoped page.
- **Authority for this project:** Primary source for visual, responsive, component, and interaction intent.
- **Known limitations:** No named immutable Figma version was supplied at initialization; later verification must detect upstream changes before material work.

## 4. Repository Source Evidence

### SRC-REPO-001 — GitHub baseline

- **Repository:** `ferfalcon/single-page-design-portfolio`
- **Relevant application, package, or directory:** `frontend/`
- **Branch at capture:** `main`
- **Captured at:** 2026-08-18T01:55:05Z
- **Pinned commit:** `07635a8eafb4323909619a0b62e41a4d8144d764`
- **Lockfile/workspace evidence:** `frontend/pnpm-lock.yaml` and `frontend/pnpm-workspace.yaml` are present.
- **Uncommitted changes or patch:** Not applicable to the GitHub commit snapshot.
- **Access and reproduction instructions:** Check out the recorded commit and inspect `frontend/`.
- **Build or inspection context:** Astro + TypeScript project using pnpm; current `frontend/src/pages/index.astro` still renders the Astro starter `Welcome` component.
- **Known limitations:** This baseline records committed repository state only; local uncommitted work outside GitHub is not represented.

## 5. Runtime Source Evidence

No runtime snapshot is registered as an active Stage 0 input. The existing Vercel site may be registered later if runtime evidence is required for validation or deployment comparison.

## 6. Documentation Source Evidence

The repository contract and bundled workflow documentation were inspected from `SRC-REPO-001`. They remain repository evidence rather than separate active documentation snapshots at initialization.

## 7. Asset Source Evidence

No separate asset snapshot is registered. Figma-local assets in the scoped design and repository assets are covered by their owning input snapshots until inspection proves a separately pinned asset bundle is necessary.

## 8. Source Verification Log

| Date and time | Snapshot | Verification method | Result classification | Change detected | Action |
|---|---|---|---|---|---|
| 2026-08-18T01:55:05Z | `SRC-DS-001` | Direct Figma metadata inspection | Pending canonical verification | Unknown | Record a CLI verification before Stage 0 closure |
| 2026-08-18T01:55:05Z | `SRC-REPO-001` | GitHub branch/commit inspection | Pending canonical verification | No observed change | Record a CLI verification before Stage 0 closure |

## 9. Upstream Rebaseline and Impact Assessments

No rebaseline has been required at initialization.

## 10. Baseline Review

### Pass 1 — Completeness and correctness

- [x] Material design and repository sources have stable snapshot IDs.
- [x] Exact Figma scope and repository commit are recorded.
- [x] The mutable Figma source is not mislabeled immutable.
- [x] Repository scope identifies `frontend/` and the starter implementation state.
- [ ] Canonical `snapshot verify` records still need to be written before Stage 0 closure.

### Pass 2 — Consistency, traceability, source integrity, risks, and uncertainty

- [x] Narrative source ownership matches the workflow record.
- [x] Repository and Figma evidence use the same active snapshot IDs as generated state.
- [x] No later-stage product behavior or implementation detail is asserted here.
- [x] Figma mutability is an explicit limitation.
- [ ] Re-run generated-state and stage preflight checks after canonical verification.
