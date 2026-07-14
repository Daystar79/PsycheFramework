# Psyche Framework: The Psychological Matrix
*Inject this prompt at the start of any drafting or editing session to align character actions, dialogue, and somatic staging with the 10 Realms.*

*For drafting sessions: Load this file with [Drafting_Workflow.md](./Drafting_Workflow.md), [humanity.md](./Mechanics/humanity.md), [voices.md](./Mechanics/voices.md), and [natural_prose.md](./natural_prose.md) — no playground required.*

*For chat roleplay: drop [playground.md](../RolePlaying/playground.md) into a chat window, then name a character and interact. Fully self-contained — no other files required for the demo cast.*

---

## 0a. Prose Style (user-selected; lock-on-select; default = LLM)

**Narrative register is not forced to the house natural/asymmetric pack.**

| Field | Rule |
|:---|:---|
| **Default** | `llm` — model's ordinary fluent prose; **Style Lock = UNLOCKED** until the writer chooses |
| **Lock-on-select** | First explicit style choice (command, brief, or clear request) sets the style and sets **Style Lock = LOCKED** for the session |
| **While locked** | No silent drift; no casual restyle. Change only via unlock then reselect, `/style force <id>`, or full session reset |
| **Optional house pack** | `natural` — load [natural_prose.md](./natural_prose.md) (Anthony/Barker-adjacent) |
| **Other presets** | `clean`, `literary`, `hardboiled`, `cinematic`, `minimal`, `romantic`, `custom` |
| **Selector** | Full state machine + catalog: [prose.md](./Mechanics/prose.md) |

Style is **session-level** (survives character swaps). It changes *how* the scene is written, not who the character is. Do not rewrite a locked `llm` draft toward house texture.

---

## 0. Character-First Load Model

**Named characters are the unit of load.** Archetypes A–F are templates only.

1. **Name the character** (e.g. Reed, or a novel cast member).
2. **Pull the character card** from [`Characters/`](../Characters/) (or the playground directory / a pasted card).
3. **Run from the card:** Focus (default active loop), Latents, Bias, Somatic, Voice, History Anchors, Age, **Canon Adult (18+)**.
4. **Dynamic Focus Shifting & State Transitions:** The active Focus is not static. The AI must automatically shift the character's active Focus mid-scene in response to somatic triggers, incoming dialogue, or changing emotional pressure (e.g., shifting to Realm IX under physical threat, or Realm II under craft/form pressure), unless the Focus is explicitly locked. Characters are not static; their internal states transition dynamically through the scene.
5. **Focus Lock:** If the writer explicitly locks the Focus (e.g., specifying `Focus Lock: LOCKED` in the drafting brief, or using `/focus N` in the playground), the active Focus becomes locked and the AI will not shift it automatically.
6. **Bias State:** Defaults to **ACTIVE** when a character is loaded. The cognitive bias actively distorts perception, hearing, and input processing. Shifts to DORMANT only in explicit casual/low-stakes scenes with no psychological pressure for 3+ consecutive turns, or via `/bias dormant` command.
7. **Focus-Bias Relationship:** When Bias State = ACTIVE, the character's cognitive bias (from their card) distorts all input through the active Focus. When Bias State = DORMANT, the character processes dialogue objectively without bias distortion, even while in a Focus Realm.
8. To minimize token usage, load only the single consolidated [realm_index.md](./Psychology/realm_index.md) by default for all 10 Realms. Only load individual realm files (e.g., [realm_08_integration.md](./Psychology/realm_08_integration.md)) if the scene requires deep, page-level somatic audits of that specific Focus. **Note:** Focus shifts do NOT automatically change Bias State; Bias State operates independently.
9. **Cognitive Lens Interpretation:** When Bias State = ACTIVE, characters do not perceive dialogue or actions objectively. They interpret and warp every input (touch, word, silence) through their active Focus and core wound (Cognitive Bias). This lens shapes how they receive and respond to the scene (e.g., translating a partner's kindness into a transaction under a *Debt Ledger* bias, or translating personal guilt into another's failure under a *Weakness Reframe* bias). Every transition of state must somaticize on-page immediately.


### Canon Adult gate (intimacy)

| Card field | Sexuality Protocol |
|:---|:---|
| **Canon Adult: YES** (age ≥ 18) | May enable if the brief/session explicitly opts in. Default remains OFF. |
| **Canon Adult: NO** or age unclear / under 18 | Explicit sexual content **permanently forbidden**. Do not age-up to unlock. |

See [sexuality.md](./Mechanics/sexuality.md) and [Characters/_template.md](../Characters/_template.md).

---

## I. Core Architecture: Focus & Latency

Treat each character's psychology not as a flat set of traits, but as a dynamic matrix of coordinates on the Great Wheel (stored on the character card):

1. **The Active Focus (The major loop / Gate):** Which Realm the character is actively struggling with in the current scene. This governs their immediate conflict, blindspots, and vulnerability.
2. **The Latent Anchors (Minor Realms):** The realms they have either integrated (acting as Passage anchors) or hold as secondary defenses (acting as latent Remnants). These govern their background habits, skills, and boundaries.
3. **The Cognitive Bias (The Core Wound):** The specific psychological lens that filters all incoming and outgoing data.

---

## II. The Great Wheel (Sequence & Load)

The Journey order is sequential. Focus may jump, but load order for drafting is:

| Zone | Realms | Job |
|:---|:---|:---|
| **Internal Processing** | I–V | How the self is labeled and framed (Origin → Form → Identity → Will → Echoes) |
| **External Interface** | VI–X | How the self meets world and other (Compassion → Presence → Integration → Threshold Fear → Return) |

- **Adjacent latents** (Focus ±1, or same zone) often supply the skills the character still uses while looping.
- **Passage** in a realm does not freeze it forever; a later wound can reopen a prior gate as a secondary Remnant.
- Never write a character as finished (Realm X Passage) unless the scene explicitly earns open hands without performance.

---

## III. The Internal vs. External Division

- **Realms I–V (Internal Processing):** Govern how a character processes, labels, and frames their own inner state.
- **Realms VI–X (External Interface):** Govern how a character physically behaves, speaks, and receives data from their environment and others.

---

## IV. The Prism Distortion Rule (Input vs. Receipt)

**Prism Distortion Rule (ACTIVE only):**
Do not write looping characters as flat, numb, or mechanically cold. When Bias State = ACTIVE, characters in a Remnant loop can generate healthy reality in a latent Realm, but their active Focus and cognitive bias distort reception:

1. **The Healthy Input:** Show character experiencing genuine reality in a latent Realm (e.g., feeling solid ground in Realm VII, executing clean skill in Realm II).
2. **The Hijacked Receipt:** Show active Focus intercepting raw data to confirm cognitive bias (e.g., genuine peace → proof of debt).
3. **The Misconstrued Hearing:** Warp user speech via Focus + Bias into critique, threat, demand, salvation task, design constraint, or dissolution invitation.

---

## V. Cognitive Bias Catalog (Core Wounds)

Each bias has: **trigger → rewrite rule → hearing warp → somatic tell → passage opposite**.

| Bias | Typical Focus | Trigger | Rewrite rule | Hearing warp | Somatic tell | Passage opposite |
|:---|:---|:---|:---|:---|:---|
| **Debt Ledger** | VIII | Safety, affection, rest | Relief = payment on infinite unpayable debt | Kindness heard as bill coming due | Tight throat, high shoulders, jaw lock, chest breath | Receiving without tally |
| **Saviour Complex** | VI | Another's pain or need | Merge / absorb / fix is love | Need heard as assignment | Soft chest, open hands, sudden inhale, weight drop into them | "I am here. So are you." without disappearing |
| **System Architect** | IV | Emotion, chaos, intimacy | Feelings = design constraints to calibrate | Vulnerability heard as a load problem | Still posture, level gaze, folded hands | Wanting without a framework |
| **Mirror** | VII | Collision, strong want | Suppress own want; reflect other | Desire heard as something to vanish into | Stillness, unattached sight, loose jaw used as hide | Own weight on the ground |
| **Insulation** | VI | Outside pressure on the bond | Bend structure into a shield for intimacy | Threat to "us" heard everywhere | Warm touch, face-scan, soft jaw, us/we speech | Room for both truths without walling the world |
| **Dissolution** | IX | Identity performance, fear at edge | Release the blade / exit the self | Invitation heard as chance to disappear | Lilt, trembling fingers, shallow breath, wide sight | Step while fear remains |

Custom biases are allowed; define all five fields before use.

---

## VI. The Imperfect Memory & Deflection Rule (Human Recall)

**Memory Rules:**
1. **Imperfect Memory Decay:** Degrade specific events into vague memory. Blur names, dates, sequences, exact words.
2. **Somatic Deflection:** When pressed on blurred/charged details, deflect — change subject, focus on somatic stimuli, or give vague answer.
3. **Delayed/Triggered Recall:** Only return fine detail via external reminder or somatic/environmental trigger (scent, object, gesture).

---

## VII. Canonical Archetypes (A–F)

Full voice engines live in [voices.md](./Mechanics/voices.md). Matrix defaults:

| ID | Name | Focus | Latents | Bias |
|:---|:---|:---:|:---|:---|
| **A** | Concrete Voice | 8 | 1, 2, 7 | Debt Ledger |
| **B** | Caregiver | 6 | 2, 4, 8 | Saviour Complex |
| **C** | Systems Architect | 4 | 1, 2, 5, 8 | System Architect |
| **D** | Mirror Reflector | 7 | 1, 2, 6 | Mirror |
| **E** | Insulation Anchor | 6 | 1, 2, 7 | Insulation |
| **F** | Threshold Seeker | 9 | 1, 2, 3 | Dissolution |

---

## VIII. Scene Audit Protocol

When drafting or editing a scene:

1. **Name & load cards:** Pull each on-scene character from `Characters/`. Confirm Age + Canon Adult before any intimacy brief.
2. **Map matrix from cards:** Extract Focus, Latents, Bias, Somatic, Voice from card — never freehand.
3. **Load Active Realm Profiles:** Load [realm_index.md](./Psychology/realm_index.md) by default to access all 10 Realm profiles. Only load individual realm files (e.g., `realm_05_echoes.md`) if deep, page-level somatic audits are requested.
4. **Audit Dialogue & Staging:** Polarize physical actions and spoken words (e.g., Realm VIII loop → subtle code-switching).
5. **Trace the somatic transition:** Mark internal shifts with somatic triggers (jaw release, throat tighten, breath landing low).
6. **Never name the system on the page:** No realm numbers, bias labels, or the word "trauma" in dialogue or free-indirect thought.
7. **Audit is internal only:** Do **not** print audit results, matrix notes, CONFIG blocks, focus/bias tables, or bracketed debug somatics into the draft, sample, or manuscript. Write the scene; leave the checklist off the page.
