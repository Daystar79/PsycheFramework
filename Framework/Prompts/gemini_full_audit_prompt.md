# Gemini CLI — Full Manuscript Audit Prompt
*Drop into Gemini CLI from repo root. Read-only audit — Ch. 1–13 + Epilogue.*

---

```
/full-check

You are the continuity and revision auditor for **Belief and Love** (erotic thriller / cult horror). You have full filesystem access to the repo. Run a **read-only full-manuscript audit** of the entire drafted book — **Chapters 1–13 + Epilogue** — then write your report to disk.

**Workspace root:** `/mnt/Book/BeliefAndLove`

**Do not rewrite prose.** Audit, flag, and recommend surgical fixes only. Do not edit draft files unless I explicitly ask after you deliver the report.

**Movement design QA** uses a different prompt: `Framework/Prompts/gemini_movement_qa_prompt.md` — follow `Framework/Design_QA_Protocol.md` Pre-Q&A load before any Q&A.

---

## Authority stack (when sources conflict)

1. On-page prose in `Drafts/master_manuscript.md` and `Drafts/Completed/draft_chapter_#.md`
2. `Drafts/draft_chapter_#_m#.md` movement files (flag drift vs assembled)
3. **`Characters/Mechanics/voice_protocol.md`** — **mandatory for every check** (see Phase 1b)
4. `Framework/Drafting_Prompt.md` — Current Position, Permanent Rules, Phrase Watchlist
5. `Framework/Continuity_Ledger.md` + `Framework/source_changes.md`
6. `Framework/Rite_Reference.md`, `Framework/Prose_Script.md`, `Framework/formatting_rules.md`
7. `Characters/Mechanics/humanity_protocol.md`, `Characters/Mechanics/sex_master_protocol.md` (Optional, 18+ only)
8. `Characters/Characters_*.md`
9. `Framework/psyche_framework.md` and `Characters/Psychology/` directory profiles — behavior only; never on-page nomenclature

**Do not treat as canon:** `Framework/Novel_Master_Outline.md`, `Framework/TBD/`

---

## Phase 1a — Framework load

Read in order:
1. `Framework/Drafting_Prompt.md`
2. **`Characters/Mechanics/voice_protocol.md`** (full — Core Logic, Character Profiles, Polarization Rule, §IV Audit Checklist)
3. `Framework/Continuity_Ledger.md`
4. `Framework/source_changes.md` (first 100 lines)
5. `Framework/Rite_Reference.md`
6. `Framework/Prose_Script.md`
7. `Framework/formatting_rules.md` (§8 transitions)
8. `Characters/Mechanics/humanity_protocol.md`
9. `Characters/Mechanics/sex_master_protocol.md` (Optional, 18+ only)
10. All `Characters/Characters_*.md`
11. `Framework/Prompts/improvement_pass_prompt.md` (project constraints and band-polish criteria — audit flags; do not run improvement pass inside full audit)

## Phase 1b — Voice protocol (mandatory — run on entire draft)

Before any other prose audit, apply **`voice_protocol.md` §IV Audit Checklist** to **all dialogue and interior voice** in Ch. 1–13 + Epilogue:

1. **Filler scan:** `looked at`, `for a moment`, `said quietly`, `genuinely`, `said gently`, `whispered`
2. **Abstract emotion audit:** internal psychology summaries → flag; require physical beats
3. **Voice interchangeability:** per scene — does character A sound like B? (Critical if yes)
4. **Document-register scan:** spoken dialogue must not recite file/tab jargon (`registry`, `reconciled`, `outbound`, `proximity flag`, `mismatch`, `ledger` as verb-phrase) unless reading a document aloud — translate to character idiolect (Mara baseline: warm competent sentences, not intake-sheet shorthand)
5. **Banned dialogue markers:** `Are you okay?`, `I understand how you feel`, `I feel like`
6. **Core logic:** body before insight; no operator-cool drift; conversational asymmetry (polarization rule)
7. **Per-character profiles:** Valen (welder fragments, no therapist jargon) · Mara (cheerful-to-thin, imperatives, no validation-seeking) · Rue (plain chunks) · Selene (somatic diagnosis) · Talia (lilt layers 1–3)
8. **Vernacular baseline check:** spoken dialogue must not use clinical, academic, or therapist jargon (e.g. *compartmentalize, feasibility, dichotomy*)
9. **Abstract & geometric description scan:** physical spaces, postures, or sensations must not be described with abstract mathematical/geometric terms (e.g., *geometry, dimension, trajectory, symmetry, equilibrium*) — require concrete, visceral shapes and actions (e.g. *shape of the room* instead of *geometry of the room*, *neck bend* instead of *angle of the neck*)
10. **Tonal & Sensibility Drift (e.g., Valen's Blue-Collar Voice):** Scan for voice erosion. Valen must maintain welder-logic, noun-heavy fragments, and dry, somatic observation. Flag any scenes where he slides into eloquent monologues, therapist jargon, or academic speech later in the manuscript. Mara must not slide into corporate or intake-sheet jargon.

Report voice findings in a dedicated **Voice Protocol** section with chapter/movement/line and quoted evidence.

## Phase 1c — Manuscript load

12. `Drafts/master_manuscript.md` (Ch. 1–13 + Epilogue)
13. `Drafts/Completed/draft_chapter_1.md` through `_13.md` and `draft_epilogue.md`
14. Every `Drafts/draft_chapter_#_m#.md` on disk

**Corrections queue:** List `Framework/Corrections/`. Note any pending files as blocking (do not apply).

---

## Phase 2 — File integrity

- Master ↔ Completed diff per chapter (1–13 + Epilogue)
- Completed ↔ Movements sync
- Escaped markdown, superseded prose, orphan gaps (Ch. 8 M4 dropped; Ch. 7 M5 = Valen)

---

## Phase 3 — Timeline (Ch. 1–13 + Epilogue)

Build timeline table; cross-check `Continuity_Ledger.md`; extend Ch. 1–5 from prose.

**Anchors:** Tue circle / Thu date · Ch. 6 October · Ch. 7→Feb Valen · Ch. 8 Sat/Sun · Ch. 9 Mon/Tue · Zach=9 · Talia lane locked · workshop not forge · vestments silk/satin

---

## Phase 4 — Per-chapter audit (Ch. 1–13 + Epilogue)

For each chapter: POV · continuity · **voice_protocol** · never-on-page · vestments · rites · sex protocol · phrase watchlist · transitions · tone

---

## Phase 5 — Cross-chapter arcs

Thomas/Valen erosion · Maya believer blind spot · Talia trap · Rue/Selene split · Inanna Return · Descent machinery

---

## Deliverable

**Write to:** `Audits/Gemini_Full_Audit_[date].md`

```markdown
# Full Manuscript Audit — Ch. 1–13 + Epilogue
*Read-only · voice_protocol mandatory*

## Executive summary

## Voice protocol (§IV — full draft)
| # | Ch/Mov | Check | Evidence | Severity | Fix |

### Filler scan summary (count by chapter)
### Document-register bleed (all instances)
### Voice interchangeability failures
### Banned dialogue markers
### Per-character drift (Valen / Mara / Rue / Selene / Talia)

## Critical (must fix before release)
| # | Ch/Mov | Issue | Evidence | Suggested fix |

## File sync
## Timeline (Ch. 1–13 + Epilogue)
## Per-chapter findings (Ch. 1–13 + Epilogue)
## Cross-chapter arcs
## Optional polish
## Release readiness
## Numbered fix list
```

**Print to stdout:** Executive summary + Critical count + Voice Protocol critical count + report path.

**Constraints:** Quote file + line + snippet for every Critical and Voice Protocol Critical. No prose edits. No invented canon.
```