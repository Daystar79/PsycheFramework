# Cognitive Middleware

**An invisible cognitive matrix for character-driven fiction drafting and somatic roleplay.**  
Body-first psychology, bias distortion, and realm-aware somatics — running silently off-page.

---

## What It Is

**CognitiveMiddleware** is a sophisticated runtime engine developed for character-driven long-form fiction. It enables consistent, psychologically rich characters through:

- **Body Before Insight** — Physical reactions and somatic tells always precede psychological explanation.
- **Character-First** — Named characters from card files are the single source of truth.
- **Tripartite Filtering** — Worldview filters split into background world-filters (Cultural Bias & Occupation) and a dynamic situational filter (Cognitive Bias / Wound) that remains dormant at rest.
- **100% Off-Page** — The entire matrix stays invisible in the final prose. No realm numbers, bias names, or system terms appear on the page.
- **Great Wheel Integration** — Somatic and bracing/release profiles for all 10 Realms.
- **Transformation Engine** — Dynamic evolution or regression of character attributes based on narrative pressure and somatic tells.

The framework is designed to fight common AI writing problems: therapy-speak, perfect recall, symmetric dialogue, pattern repetition, and on-page system leakage.

---

## Core Philosophy

- The matrix is a **tool for the writer**, not content for the reader.
- Characters are not therapists, narrators, or helpful assistants.
- Memory is imperfect and biased. Recall is triggered somatically, not on command.
- Style, focus, and bias state are controllable but never visible in the output.
- Adult/sexual content is strictly gated and never enabled by default.

---

## Quick Start

1. Clone or copy this framework into your book project folder.
2. Deploy scaffolds (optional but recommended) — **pick by OS** (or use the auto launcher):
   ```bash
   # Preferred (auto-detects Windows vs Unix):
   python3 scripts/run.py deploy

   # Unix / macOS / WSL:
   scripts/unix/deploy.sh

   # Windows PowerShell:
   # powershell -NoProfile -ExecutionPolicy Bypass -File scripts/windows/deploy.ps1
   ```
3. For every drafting session, load:
   - `Framework/Main.md`
   - `Framework/Rules_Index.md`
   - `Framework/Psychology/realm_data.yaml`
   - On-scene character cards + `Characters/[slug]_log.yaml` (runtime matrix)
   - `Framework/Continuity_Ledger.md` (scene timeline / close)
4. Write movements/scenes using the brief + cards. The matrix runs silently.
5. On approved movements: dual commit — Continuity_Ledger **and** character logs (not the cards).
6. Run the linter (again: auto launcher or OS-specific wrapper):
   ```bash
   python3 scripts/run.py lint Drafts/
   # Unix:    scripts/unix/lint.sh Drafts/
   # Windows: scripts/windows/lint.ps1 Drafts\
   ```

---

## Key Files

| File | Purpose | Usage / Load |
|------|---------|--------------|
| `Framework/Main.md` | Core engine, workflow, commands, and principles | **Always load** |
| `Framework/Rules_Index.md` | Hard bans, cleanup protocol, dialogue rules | **Always load** |
| `Framework/Psychology/realm_data.yaml` | Somatic profiles for all 10 Realms | **Always load** |
| `Framework/linter.py` | Automated prose linter (core) | Via `scripts/run.py lint` |
| `scripts/run.py` | OS-aware launcher (deploy / lint / migrate) | **Agents: use this** |
| `scripts/unix/*.sh` | Unix shell wrappers | Linux / macOS / WSL |
| `scripts/windows/*` | Windows PowerShell / CMD wrappers | Windows |
| `Characters/_template.md` | Public card scaffold (identity + build defaults only) | Copy for new characters |
| `Characters/_log_template.yaml` | Public runtime log schema (snapshot + history) | Copy → `[slug]_log.yaml` |
| `Framework/Continuity_Ledger.md` | Scene timeline / somatic close | Always load when drafting |
| `Framework/Character_Change_Log.md` | Consolidated matrix snapshot (human-readable) | Optional / post-commit sync |
| `Characters/` (named cards, `Relations.md`) | **Author-local only** — demo cast; not open-licensed; not deployed | Local testing |
| `Framework/Mechanics/` | Prose styles, sexuality rules, voice templates, humanity details | Load as needed |
| `Framework/Prompts/` | Interactive character builder and improvement prompts | Reference only |
| `Simulator/CharacterRuntime.md` | **Drop-in** RP engine: storage boot, Character Pack load/save, modes TEST/COMPANION/HEAT | Paste whole file into chat |

---

## Character Simulator (drop-in)

**No git required.** Paste `Simulator/CharacterRuntime.md` into any chat to activate.

1. Runtime runs **Storage Boot** (detects Drive/local/paste capability).
2. You **load**, **create**, or **paste** a **Character Pack** (card + memory in one portable file).
3. Play in `/mode test` (fidelity), `companion` (relationship), or `heat` (adult, gated).
4. `/save` writes change-state back to cloud (if tools exist) or dumps a pack for re-paste.

Pack = CARD (identity) + MEMORY (snapshot, bond, pins, heat). Same idea as `Characters/[slug].md` + `_log.yaml` for repo users.

Key simulator commands: `/load` `/new` `/save` `/pack` `/storage` `/mode` `/user` `/18+` `/pin` — full list inside the runtime file.

## Author Commands (Drafting & RP)

| Command | Effect |
|---------|--------|
| Load character card | Silent state load (name + card) |
| `/create …` | Build minimal new card |
| `/focus N` | Lock active Focus to Realm N |
| `/focus unlock` | Allow dynamic Focus shifts |
| `/bias active` / `dormant` | Force bias state (Active distorts perception, Dormant acts normally) |
| `/style <id>` | Lock prose style |
| `/style unlock` | Allow style change |
| `/18+ on` / `off` | Enable/disable heat (only if Canon Adult = YES) |
| `/transform event: <desc> strength: <level>` | Force a transformation pressure calculation |
| `/reset` | Clear session state |

---

## Tripartite Filter System

1. **Cultural Bias (Background):** Metaphysical frame, ethical defaults, and **temporal awareness** (how they track time/destiny, e.g., cyclic liturgy vs. linear progress).
2. **Occupation (Background):** Technical lexicon, prop/tool familiarity, and immediate staging focus.
3. **Cognitive Bias (Triggered):** Wound-based perception warp. Stays **DORMANT** during casual beats, intercepting inputs only when emotional pressure activates it.

---

## Transformation & Evolution

- **Cards** hold build-default `transformation_weights` (active focus, latent anchors, bias strength, somatic flexibility).
- **Runtime evolution** lives in `Characters/[slug]_log.yaml` (snapshot + history) and is mirrored in `Framework/Character_Change_Log.md`.
- **Scene close** (day/time, temporary body state, plot beats) lives in `Framework/Continuity_Ledger.md`.
- Do not append movement history to character cards.

---

## Historical & Safety Gates (Roleplaying)

- **Safety Gating:** Strict prohibition of Lolicon/Shotacon tropes. Canon verification is required for 18+ Anime/Hentai imports.
- **Historical Figures:** Lifespan/active era must be specified. Character cards prioritize their **own writings/primary documentation**, falling back to the cultural and temporal bias of their era only when documentation is lacking. Modern or post-era concepts are strictly banned from their awareness. Under no circumstances may the AI engine break character or use external search/lookup tools to resolve historical gaps during active roleplay.

---

## Automated Prose Linter (`linter.py`)

Run via the OS-aware launcher (or platform wrappers under `scripts/`):

```bash
python3 scripts/run.py lint Drafts/
```

Scans drafts for:
- **System Leaks:** On-page mentions of Realms, biases, and matrix weights.
- **Therapy-Speak:** Jargon like *wound*, *trauma*, *trigger*, or *reframe*.
- **Dialogue Tags/Fillers:** Banned markers like *whispered*, *Are you okay*, and *said quietly*.
- **Formatting Breaks:** Excessive horizontal rules (`---`) separating real-time actions.

See [scripts/README.md](scripts/README.md) for Windows vs Unix command tables (for humans and AI agents).

## Scripts (Windows & Unix)

| Tool | Auto (any OS) | Unix | Windows |
|:---|:---|:---|:---|
| Deploy | `python3 scripts/run.py deploy [target]` | `scripts/unix/deploy.sh` | `scripts/windows/deploy.ps1` |
| Lint | `python3 scripts/run.py lint <path>` | `scripts/unix/lint.sh` | `scripts/windows/lint.ps1` |
| Migrate | `python3 scripts/run.py migrate` | `scripts/unix/migrate.sh` | `scripts/windows/migrate.ps1` |

**AI agents:** detect the host OS, then either call `scripts/run.py` (preferred) or the matching `scripts/unix/` / `scripts/windows/` wrapper. Do not run `.sh` on native Windows or `.ps1` on Unix unless a compatible shell is confirmed.

---

## License

Cognitive Middleware uses a hybrid open-source license model:

* Software components (such as `Framework/linter.py` and `deploy_framework.py`) are licensed under the **MIT License**.
* Creative content, manuals, the public character **template**, prompts, YAML schemas under `Framework/`, and **`Simulator/`** (Roleplay / CharacterRuntime) are licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.
* **Author-local materials are not open-sourced:** named cards under `Characters/` (except `_template.md` / `README.md`) and `Characters/Relations.md`. All rights reserved; not distributed by `deploy_framework.py`.

Copyright (c) 2026 Cian Didymos. See [LICENSE.md](LICENSE.md) for full license details.

---

*Install once. Load for every session. Let the matrix run silently. Write clean prose.*
