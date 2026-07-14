# Characters Directory

Named fictional people are the **unit of load**. Archetypes A–F are voice/matrix templates only.

## Flow

1. Author (or playground user) **names a character**.
2. System **pulls that character's card** (`Characters/[slug].md` or the directory inside `playground.md`).
3. Live config is filled from the card: Focus, Latents, Bias, Somatic, Voice, **Canon Adult**.
4. Roleplay / drafting runs from that data — not from a bare archetype letter.

## Canon Adult (18+) gate

| Card field | Effect |
|:---|:---|
| **Canon Adult: YES** | User may enable Sexuality Protocol (`/18+ on`) for explicit content. Still OFF by default. |
| **Canon Adult: NO** | Explicit sexual content is **permanently locked**. `/18+ on` is refused. Do not age-up to unlock. |

Age on the card is canon. If age is under 18, **Canon Adult must be NO**.

## Files

- [`_template.md`](./_template.md) — copy for new characters
- Sample cards: `reed.md`, `helen.md`, `cass.md`, `wren.md`, `nora.md`, `lior.md` (generic demos for the playground)

## Adding a novel character

1. Copy `_template.md` → `Characters/[slug].md`
2. Fill Identity (especially **Age** + **Canon Adult**)
3. Fill Psyche Matrix from the Great Wheel + bias catalog
4. Optionally map **Voice archetype base** to A–F for engine defaults, then override with idiolect
5. For chat demos: drop [`playground.md`](../Web/playground.md) (or root `playground.md`) into the chat, then paste your card and name them — or add them to the playground Character Directory
