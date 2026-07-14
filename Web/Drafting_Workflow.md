# Drafting Workflow — Psyche Matrix Framework
*Workflow and process rules for design, drafting, and checking.*

---

## 1. Session Types (Do Not Combine)

| Type | Goal | Output |
|------|------|--------|
| **Design** | Recursive Q&A — lock canon, fill brief | Updated Movement Brief + `chapter_N_mM_design.md` + bible/card deltas in `source_changes.md` |
| **Draft** | One movement, one pass | `draft_chapter_#_m#.md` — no new canon mid-draft |

*   **Speed Rule:** Design session ends with a **complete** Movement Brief. Draft session uses only the Brief + read lists. Approval = small revision pass, then merge.
*   **Voice Protocol:** [voices.md](./Mechanics/voices.md) is mandatory for every draft and check. Run the Audit Checklist before save/sign-off.

---

## 2. Design Pass Protocol

Performed before every drafting session. No prose is generated during this step.

### Pre-Q&A Load (Mandatory)
Before starting Q&A, load:
1.  All framework protocols ([humanity.md](./Mechanics/humanity.md), [voices.md](./Mechanics/voices.md)).
2.  Active character cards in the scene.
3.  The entire preceding chapter and all prior movements in the current chapter on disk.

### Character Lens
Character Q&A must lock **do / think / believe** per on-scene character using cards, protocols, and guide behaviors (not plot summary).

### Design Brief Template
Fill and place in `Drafting_Prompt.md` at the end of the Design Pass:
```
Chapter band: [M1 title / M2 title / ... - chapter scope]
Chapter:      [N - M# next]
Movement:     [Title]
POV:          [who]
Opens on:     [exact image / room / line]
Must-land:    [ordered beats 1-6 - draft spine]
Must-not:     [hard stops - scope creep + bore traps]
Close:        [last image; who goes where]
Dual arc:     [Thomas lane / Maya lane this movement]
Reader knows: [dramatic irony to preserve]
Checklist:    ☐ rites/drugs  ☐ vestments  ☐ shop rhythm  ☐ dual arc  ☐ close image
Reference:    [Rite_Reference.md section; Guide Realm chapter for POV]
```

---

## 3. Draft Session Protocol

### Preceding Movement Read Rule (Mandatory)
Before writing, read to ensure no callback staging drift:
*   **For Ch. N, M1:** Read the **last movement** of Ch. N−1 in full.
*   **For Ch. N, M2+:** Read **every prior movement** in Ch. N.

### Drafting Action Steps
1.  **Read the Manifest:**
    *   Active `Movement Brief` in `Drafting_Prompt.md`.
    *   Preceding movement(s) (per table above).
    *   `Rite_Reference.md` (if ritual elements are on scene).
    *   Active character cards.
    *   [humanity.md](./Mechanics/humanity.md) and [voices.md](./Mechanics/voices.md).
2.  **Generate Prose:**
    *   Write exactly one movement.
    *   Match the voice on the page. What is written supersedes all outlines.
    *   Do not skip ahead without design sign-off.
3.  **Perform Cleanup Pass:**
    *   Execute the **Cleanup Pass Protocol** (Section 4) before submitting or saving.
4.  **Assemble & Merge:**
    *   When all movements are approved, assemble to `draft_chapter_N.md`.
    *   Log changes in `source_changes.md`.
    *   Merge into master manuscript only on user approval.

---

## 3a. Multi-Movement Consistency Protocol

When generating multiple movements for the same chapter, enforce strict cross-movement consistency to prevent duplication and ensure state persistence.

### State Persistence Rules
*   **Focus State:** Active Focus persists across movements unless explicitly changed via `/focus N` in the Movement Brief or design notes.
*   **Bias State:** Defaults to ACTIVE; persists across movements unless explicitly set to DORMANT via `/bias dormant`.
*   **Somatic State:** Ending somatic tells from Movement N must be the starting point for Movement N+1. State evolves, not resets.

### Cross-Movement Anti-Duplication
*   **Somatic Rotation:** Somatic tells used in Movement N cannot be reused in Movement N+1 without significant variation in phrasing, body zone, or intensity.
*   **Dialogue Pattern Rotation:** Character speech patterns (question structures, verbal tics, rhythm) must rotate across movements. If a character starts sentences with a specific pattern in Movement 1, they must use different patterns in subsequent movements.
*   **Prop Evolution:** Objects and environmental details introduced in Movement N must change position, state, or interaction in Movement N+1. Stagnant props create artificial stasis.

### Continuity Checklist (Before Starting Movement N+1)
*   ☐ Read Movement N in full (mandatory)
*   ☐ Note ending somatic state for each character
*   ☐ Note ending environmental state and prop positions
*   ☐ Note unresolved dialogue beats and open loops
*   ☐ Verify no duplication of Movement N somatic tells, dialogue patterns, or prop staging
*   ☐ Confirm Focus and Bias State from Movement N end

### Showing vs. Explaining Enforcement (Cross-Movement)
*   **Never Summarize:** Movement N+1 must NOT begin with a summary of Movement N events. Open on concrete action, somatic tell, or direct dialogue.
*   **State Through Somatic:** All internal state transitions between movements must be shown through somatic reactions, never explained via narration or dialogue.
*   **Callback Staging:** When referencing events from prior movements, stage them through character memory (imperfect, biased) not objective summary. Use somatic triggers (scent, object, gesture) for recall, not exposition.

### Movement Transition Protocol
When ending Movement N and beginning Movement N+1:
1. **End N with Concrete Anchor:** Last beat of Movement N must end on a specific, uninterpreted physical fact or action (anti-synthesis).
2. **Begin N+1 with Continuation:** First beat of Movement N+1 must pick up from that anchor, showing evolution, not re-establishing context.
3. **No Reset:** Characters do not "re-enter" the scene; they continue from where they were, with accumulated state.

---

## 4. The Cleanup Pass Protocol (The Final Loop)

The final step in the drafting session is the **Cleanup Pass**. This is a dedicated editing pass designed to scrub out generative AI artifacts, pattern stickiness, and framework leaks. Do not skip this pass or run it concurrently with initial drafting.

### The Cleanup Checklist:

1. **Zero System Leaks (Hard Ban):**
   * Scan the manuscript text for any framework jargon: `Realm [N]`, `Focus`, `Bias`, `Brace`, `Release`, `Integration` (when used as system titles), and any psychological terms (e.g. `reframe`, `coping mechanism`).
   * Translate all internal state transitions into somatic reactions and third-limited indirect thoughts. Keep the matrix 100% off-page.
   * **No debug dump in drafts or samples (hard ban):** Never write any of the following into `Drafts/`, `samples/`, or other manuscript files:
       - Bracketed somatic lines (`[Shoulders high…]`, `[Prism intercept…]`) — **prose/draft mode only**; fold body tells into narrative sentences
       - Live CONFIG cards, session state blocks, or `/card` reprints
       - Post-scene appendices: "Matrix notes", focus/bias audit tables, beat maps, off-page analysis
       - Engine labels inside prose even without brackets: `Prism`, `Debt Ledger`, `Saviour`, `Remnant`, `Passage`, realm numbers, `Bias State`, `Focus Lock`
   * Scene Audit, turn-loop state math, and cleanup checklists run **silently**. Only narrative prose is saved.
   * Sample files may keep a **short pre-scene header** (title, cast, seed, adult gate) above a `---` rule. Everything after that rule is pure scene prose — no matrix footer.
2. **AI Pattern Frequency Check:**
   * **Banish Standalone "Beats":** Delete any instances of `"A beat."` or `"Beat."` as standalone sentences. Replace them with specific physical pauses or reactions.
   * **Rotate Somatic/Gaze Loops:** If a sensory detail (e.g., `green eyes on`, `ice-blue eyes were steady`, `palm found`, `bare feet on`) is used once, subsequent descriptions in the scene must be rotated to fresh, concrete phrasing.
   * **Diversify Props:** Ensure food and drink elements (coffee/tea/water) and spatial packaging (`in the room`) are varied and anchored to concrete items.
3. **Phrase Watchlist & Filler Scan:**
   * Run a search for banned terms (`cult`, `circuit`, `loop`, `forge` for Thomas's welding, ethnic/national labels).
   * Search for and prune overused fillers: `looked at`, `already` (when redundant), `for a moment`, `said quietly`, and `genuinely`.
4. **Dialogue Asymmetry Check:**
   * Verify that characters do not match volume or rhythm.
   * Banish polite agreement markers (e.g. `Are you okay?`, `I understand how you feel`, `said gently`, `whispered`).
5. **No Narrative Closure / Anti-Synthesis Check:**
   * Check paragraph endings. Confirm they end on raw, concrete facts, actions, or unanswered dialogue rather than neat interpretive summary sentences (e.g. *"It was a silent pact..."*).
