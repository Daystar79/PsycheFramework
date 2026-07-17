# Simulator — Character Runtime (drop-in)

## What it is

`CharacterRuntime.md` is a **self-contained** chat runtime for Cognitive Middleware characters. Paste the whole file into Claude, Gemini, ChatGPT, Grok, etc. — **no git clone required**.

It is both:

- A **testing harness** for how a card behaves before you draft
- A **companion / heat** engine when you want ongoing RP with memory

## Quick start

1. Open [`CharacterRuntime.md`](./CharacterRuntime.md).
2. Copy **the entire file** into a new chat.
3. Answer the **Storage Boot** menu:
   - **Load** an existing Character Pack (Drive/local/paste)
   - **Create** a new pack
   - **Paste** a pack or card
4. Optional: `/mode companion` · `/user name: …` · `/18+ on` (adults only)
5. `/save` when bond, matrix, or heat state should persist

## Character Pack

Portable unit (one markdown file recommended):

| Section | Holds |
|:---|:---|
| **META** | slug, storage provider, file id, autosave |
| **CARD** | Identity + build defaults (same idea as `Characters/[slug].md`) |
| **MEMORY** | Snapshot, bond, pins, heat, history (same idea as `_log.yaml`) |

### Persistence levels

| Level | Host | Save |
|:-----:|:---|:---|
| L3 | Cloud read+write tools | Update/create pack file |
| L2 | Cloud read only | Dump pack for manual upload |
| L1 | Local workspace | Write `Characters/` files |
| L0 | Paste-only chat | Dump pack to re-paste next time |

## Modes

| Mode | Purpose |
|:---|:---|
| `TEST` | Author fidelity; low initiative |
| `COMPANION` | Relationship continuity; character wants |
| `HEAT` | Explicit adult RP — requires canon adult + `/18+ on` |

## Repo users

If you have the full Cognitive Middleware tree, L1 can sync pack ↔ `Characters/[slug].md` + `[slug]_log.yaml`. Deploy still ships this folder via `deploy_framework.py`.

## License

Simulator content is open under **CC BY-SA 4.0** (see root `LICENSE.md`). Your private Character Packs (named cards + intimate memory) are **your** data — keep them private.
