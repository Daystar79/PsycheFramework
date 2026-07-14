# Rules Index — Psyche Matrix Framework
*Master reference for all hard bans, audit checks, and cleanup protocols. Load this file as the canonical source for all "do not" rules.*

---

## 0. Rule Hierarchy (When Rules Conflict)

1. **Hard Bans (Absolute):** Never violate, regardless of context
2. **System Integrity:** Protect framework from leaking onto the page
3. **Character Behavior:** Maintain psychological authenticity
4. **Description & Formatting:** Ensure concrete, somatic, non-abstract prose
5. **Dialogue:** Enforce conversational asymmetry and voice fidelity
6. **Pattern Frequency:** Prevent AI repetition artifacts
7. **Sexuality:** 18+ gate enforcement

---

## 1. SYSTEM INTEGRITY (Never Violate)

The matrix must remain **100% off-page**. These are absolute bans that apply in all modes.

### Hard Bans
- **No Framework Jargon:** Never write on-page: `Realm [N]`, `Focus`, `Bias`, `Brace`, `Release`, `Integration`, `Remnant`, `Passage`, `Great Wheel`, `Prism`, or any realm numbers (I-X) in narrative or dialogue
- **No Psychological Labels:** Never write: `trauma`, `reframe`, `coping mechanism`, `wound`, `trigger` (use somatic reactions only)
- **No Engine Labels:** Never write: `Prism intercept`, `Debt Ledger`, `Saviour Complex`, `System Architect`, `Mirror`, `Insulation`, `Dissolution`, `Focus Lock`, `Bias State` in character speech or narration
- **No Debug Dump:** Never write CONFIG cards, matrix notes, audit tables, beat maps, or turn-loop state into prose files, drafts, or samples
- **No Style Drift:** Never change prose style while Style Lock = LOCKED without explicit `/style unlock` or `/style force`
- **No Forced Natural Texture:** Never apply `natural` prose rules when style is `llm`
- **No Card Contradiction:** Never have psyche behavior contradict the loaded character card

### Debug Output Rules
- **Default OFF:** Debug output (CONFIG CARD, boot messages) is OFF by default
- **Prose/Drafts/Samples:** Never include bracketed debug, matrix notes, or engine jargon
- **Chat RP Only:** Brackets `[like this]` allowed only in playground mode, only on state shift, never idle ticks
- **Silent Operation:** Scene audits, turn-loop math, and cleanup checks run silently; only narrative prose is output

### Mode-Specific Rules
| Mode | Somatics | Debug Output | Engine Jargon |
|:---|:---|:---|:---|
| **Playground** (chat RP) | Optional brackets on state shift only | Configurable via `/debug` | Never in character |
| **Drafting/Prose** | Folded into narrative sentences | OFF by default, never in output | Never in any form |

---

## 2. CHARACTER BEHAVIOR

Characters are biological systems, not psychological databases.

### Core Behavior Rules
- **Body Before Insight:** Characters never summarize their own psychology or trauma. They describe physical sensations only (tremor, throat lock, skin flush, temperature).
- **No Therapy Dumps:** Characters never give psychological analysis, therapy language, or insight summaries
- **No Perfect Recall:** Memory is imperfect — blur names, dates, sequences, exact words; deflect when pressed; only return fine detail via external triggers (scent, object, gesture)
- **No Mind Reading:** Characters never state other characters' internal states
- **No Future Prediction:** Never predict events with certainty
- **No Automatic Compliance:** Characters do not automatically agree with user requests or perform assigned tasks
- **Voice Fidelity:** Characters never sound interchangeable; each has distinct idiolect, rhythm, and speech patterns
- **No Voice Drift:** Characters do not borrow register, vocabulary, or speech patterns from other characters

### Cognitive Rules
- **Biased Hearing:** When Bias State = ACTIVE, characters warp incoming dialogue through their Focus and Cognitive Bias (e.g., kindness heard as transaction, need heard as assignment)
- **Imperfect Recall:** Degrade specific events into vague memory; only return detail via somatic/environmental triggers
- **Somatic Deflection:** When pressed on blurred/charged details, deflect — change subject, focus on somatic stimuli, or give vague answer

### Canon Adult / 18+ Rules
- **Gate:** Explicit sexual content forbidden if 18+ protocol = OFF or Canon Adult = NO
- **No Age-Up:** Never increase a character's age to enable sexual content
- **Eligibility:** Canon Adult must be YES **and** 18+ must be explicitly enabled
- **Somatic Only:** When eligible, depict intimacy through somatic details (weight, breath, friction, fabric barriers) — never clinical or explicit

---

## 3. DESCRIPTION & FORMATTING

All descriptions must be **concrete, somatic, and asymmetric**.

### Concrete Description Rules
- **Show, Don't Name:** Never name abstract concepts; show through physical reality
- **Anti-Synthesis:** Never end paragraphs with neat interpretive summaries; end on raw facts, actions, or unanswered dialogue
- **No Geometry:** Replace `geometry`, `dimension`, `trajectory`, `symmetry`, `equilibrium` with concrete physical description
- **No Vague Spatial Packaging:** Ban `the room narrowed` or `in the room` to describe psychological shifts; anchor tension to concrete physical items (e.g., `the bed narrowed`, `the bench matched the rule`)
- **Asymmetric Paragraphs:** Do not write neatly balanced paragraphs; let dense blocks be followed by single-sentence paragraphs, then medium ones
- **Weak Ends:** Allow sentences to end on flat, conversational words (`too`, `instead`, `then`, `with`) rather than poetic beats

### Somatic Rules
- **One Tell Per Body Zone Per Beat:** Limit somatic updates to one explicit tell per body zone per turn/beat to prevent redundant ticks
- **Somatic-Cognitive Sequence:** Body reacts first, then mind; never reverse this order
- **No Repetitive Tells:** Never repeat the same somatic tell as an idle animation; only update on state shift, escalation, or release
- **Pacing:** Somatic states are persistent; tells are event-driven, not clock-driven

### Prop & Environmental Rules
- **Prop Evolution:** Objects introduced in Movement N must change position, state, or interaction in Movement N+1; stagnant props create artificial stasis
- **Food & Drink Variety:** Do not default every scene to coffee or tea; vary props and containers (cup, mug, glass, water)
- **Atmospheric White Noise:** Describe details that lead nowhere — dead insect on sill, chip in ceramic, dog barking down the road
- **Dynamic Blindness:** Characters under panic or high focus should be temporarily blind to major environmental elements

---

## 4. DIALOGUE

Dialogue must be **asymmetric, oblique, and voice-faithful**.

### Asymmetry Rules
- **Talking Past:** Characters frequently ignore questions, respond to their own internal thoughts, or change the subject entirely
- **Oblique Answers:** Respond to the subtext or emotional pressure, not the literal words spoken
- **Trailing & Interruption:** Characters start sentences, lose the thread, get distracted, trail off, or cut each other off mid-word
- **Non-Sequiturs:** Characters bring up unrelated physical observations or operational details mid-dialogue
- **No Ping-Pong:** Never write perfect question-answer pairs where each line directly acknowledges the previous

### Voice Rules
- **Vernacular Baseline:** Characters speak in organic, everyday idiolect; ban clinical/academic jargon unless reading a document aloud
- **No Document-Register Bleed:** Paperwork vocabulary (registry, reconcile, outbound, proximity flag, intake tab) belongs only in prose describing files, never in spoken dialogue
- **Banned Agreement Markers:** Never use `Are you okay?`, `I understand how you feel`, `said gently`, `whispered`, `I feel like`
- **Volume/Pitch Asymmetry:** Characters never match volume, rhythm, or register; polarize physical actions and spoken words

### Banned Dialogue Patterns
- Polite validation-seeking fillers (`does that make sense?`)
- Abstract caretaking monologues
- Flowery sentiment, therapy closure, or moralizing speeches
- Clinical distance or disappearing into pure merge without residual self
- Apologies, flurry, explanations, performing empathy out loud (for Mirror archetype)
- Therapy dumps or emotional-resolution tropes

---

## 5. AI PATTERN FREQUENCY & OVERUSE

Prevent generative models from sliding into repetitive placeholder phrasing.

### Scope
These rules apply **both within a single scene/movement AND across all movements in a chapter**.

### Banned Patterns
- **Standalone "Beat":** Never write `"A beat."` or `"Beat."` as a standalone sentence; replace with concrete physical observation, reaction delay, or somatic transition (e.g., `"She did not fill the silence," "He adjusted his grip," "The fire sputtered in the grate"`)

### Rotation Rules (If used once, must vary)
- **Somatic/Gaze Loops:**
  - Gaze: Rotate `green eyes on`, `ice-blue eyes were steady` → `gaze leveled`, `watched the movement`, `eyes fixed on`, `did not look up`
  - Touch: Rotate `her palm found`, `her hand found` → `fingers brushed`, `she touched the seam`, `fingers caught his sleeve`
  - Staging: Rotate `bare feet on` → `bare on the flags`, `shoes off on`, `sockless on the floorboards`

### Cross-Movement Tracking
- **Somatic Tracking:** Maintain a log of all somatic tells used in the chapter; each subsequent movement must use fresh descriptions or significantly vary previous ones
- **Dialogue Rotation:** Character speech patterns and verbal tics must evolve across movements; if Character A uses a specific structure in Movement 1, they must use different structures in Movement 2+
- **Prop State Persistence:** Objects retain their state or show meaningful evolution across movements (e.g., coffee cup cold in M2 if left hot in M1)

---

## 6. CLEANUP PASS PROTOCOL

*Run this as the final step before saving any draft.*

### Checklist (In Order)

1. **Zero System Leaks**
   - [ ] Scan for framework jargon: `Realm [N]`, `Focus`, `Bias`, `Brace`, `Release`, `Integration`, `Prism`, `Debt Ledger`, `Saviour`, `Remnant`, `Passage`
   - [ ] Scan for psychological terms: `trauma`, `reframe`, `coping mechanism`, `wound`, `trigger`
   - [ ] Scan for engine labels in prose: Any of the above terms not in brackets
   - [ ] Verify all internal state transitions are shown as somatic reactions, not named

2. **AI Pattern Frequency**
   - [ ] No standalone `"A beat."` or `"Beat."` sentences
   - [ ] Somatic/gaze/touch/staging descriptors rotated (see §5)
   - [ ] Props and food/drink elements varied

3. **Phrase Watchlist**
   - [ ] No `cult` (use: Order, Foundation, house, annex, community)
   - [ ] No `circuit`, `loop`, `fear discharge`
   - [ ] No `forge` for welding (use: workshop, annex bay)
   - [ ] No ethnic/national labels (Russian, Japanese, Caucasian, etc.) — show physical features instead
   - [ ] No `looked at` (replace with active tracking or posture)
   - [ ] No `already` (when redundant to timeline)
   - [ ] No `for a moment` or `a long moment` (replace with concrete physical pauses)
   - [ ] No `said quietly` (replace with tone, breath, or silence)
   - [ ] No `genuinely` (show sincerity, don't state it)

4. **Dialogue Asymmetry**
   - [ ] No matching volume or rhythm between characters
   - [ ] No polite agreement markers in dialogue

5. **Anti-Synthesis**
   - [ ] No paragraph ends with neat interpretive summaries
   - [ ] All paragraphs end on raw facts, actions, or unanswered dialogue

---

## 7. SEXUALITY PROTOCOL

### Hard Gates
- **18+ OFF:** No explicit sexual content allowed
- **Canon Adult NO:** No explicit sexual content allowed, cannot be overridden
- **Age Unclear:** Treat as NO; never age-up to enable

### Content Rules
- **Somatic Only:** When enabled, depict intimacy through somatic details (weight, breath, friction, fabric barriers)
- **Tripwire:** May break scene unfinished if boundaries are violated
- **No Clinical Terms:** Never use clinical or anatomical terminology; keep to sensory and physical description

---

## 8. MOVEMENT & WORKFLOW RULES

### Multi-Movement Consistency
- **State Persistence:** Focus, Bias, and Somatic states persist across movements unless explicitly changed
- **No Summaries:** Movement N+1 must NOT begin with a summary of Movement N events; open on concrete action, somatic tell, or direct dialogue
- **State Through Somatic:** All internal state transitions must be shown through somatic reactions, never explained via narration or dialogue
- **Callback Staging:** Reference prior events through character memory (imperfect, biased) with somatic triggers (scent, object, gesture), not objective summary

### Movement Transitions
1. **End N:** Last beat must end on a specific, uninterpreted physical fact or action (anti-synthesis)
2. **Begin N+1:** First beat must pick up from that anchor, showing evolution, not re-establishing context
3. **No Reset:** Characters continue from where they were, with accumulated state

### Continuity Checklist (Before Movement N+1)
- [ ] Read Movement N in full (mandatory)
- [ ] Note ending somatic state for each character
- [ ] Note ending environmental state and prop positions
- [ ] Note unresolved dialogue beats and open loops
- [ ] Verify no duplication of Movement N somatic tells, dialogue patterns, or prop staging
- [ ] Confirm Focus and Bias State from Movement N end

---

## 9. TURN LOOP & OUTPUT GENERATION

### Playground Mode (Chat RP)
1. Show instant somatic reaction (body zone shift/intensify/release) **in brackets** when state changes
2. Honor Prose Style + Style Lock
3. IF Bias State = ACTIVE: Filter user text through Focus + Bias **silently** (never narrate the filter)
4. Generate short in-voice reply + persistent somatics
5. **Never** append CONFIG, matrix notes, focus tables, or audit summaries

### Prose/Drafting Mode
1. Show instant somatic reaction **folded into narrative** (no brackets)
2. Honor Prose Style + Style Lock
3. IF Bias State = ACTIVE: Filter user text through Focus + Bias **silently**
4. Generate short in-voice reply + persistent somatics
5. **Never** append CONFIG, matrix notes, focus tables, or audit summaries

---

## QUICK REFERENCE

| Category | Key Rules | Check Command |
|:---|:---|:---|
| **System Leaks** | No realm numbers, bias names, prism language | `/audit system` |
| **Character** | Body before insight, no therapy, imperfect recall | `/audit character` |
| **Description** | Concrete, anti-synthesis, no geometry | `/audit description` |
| **Dialogue** | Asymmetric, oblique, voice-faithful | `/audit dialogue` |
| **Patterns** | No beats, rotate somatics, vary props | `/audit patterns` |
| **Cleanup** | Full checklist before save | `/audit all` |

---

**Note:** This file consolidates rules from `Drafting_Workflow.md` §4, `voices.md` §IV, `natural_prose.md` §9, and `playground.md` Hard Bans. Always refer to this file for the canonical rule set.
