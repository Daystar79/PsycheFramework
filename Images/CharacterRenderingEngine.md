---
framework: CognitiveMiddleware
version: "2026-07-24"
type: rendering_engine
load_priority: 15
description: "Visual rendering pipeline for CharacterRuntime. Runs on scene motion each IC beat: prompts to Images/ plus live stills via image_gen/image_edit when tools exist. Game-style graphics pass: models, animation, scene, camera, lighting, style, continuity."
---

# CHARACTER RENDERING ENGINE

**Purpose:** Convert CharacterRuntime state into **visual frames as the scene moves** — prompt files always; live images when host tools allow. This is the graphics pipeline counterpart to CharacterRuntime game logic.

**Workflow:**
```
CharacterRuntime IC beat
  → MEMORY update (scene, somatic, action)
  → scene-motion check
  → Rendering Engine (stages 1–6)
  → Images/{slug}/*.prompt.md
  → [live] image_gen (base) | image_edit (delta from last_frame)
  → MEMORY.visual paths + hash
```

---

## ENGINE ARCHITECTURE

Like a game engine, this has distinct stages:

### 1. MODEL LOADER (Character Geometry)
**Input:** CARD fields
**Output:** Character model definition

### 2. ANIMATION SYSTEM (Pose & Motion)
**Input:** MEMORY.snapshot + somatic tells + current action
**Output:** Character pose, gesture, facial expression

### 3. SCENE COMPOSER (Environment)
**Input:** MEMORY.scene + scene_seeds
**Output:** Setting, lighting, atmosphere

### 4. CAMERA SYSTEM (Framing)
**Input:** Scene context + action intensity
**Output:** Shot type, angle, composition

### 5. MATERIAL & SHADER (Style)
**Input:** User preferences + character archetype
**Output:** Art style, rendering quality

### 6. RENDER OUTPUT (Prompt + Live Frame)
**Input:** All above stages + MEMORY.visual
**Output:**
- Prompt file → `Images/{slug}/`
- Live still (when `visual.mode: live` and tools exist) → session images dir; path stored in MEMORY.visual

---

## STAGE 1: MODEL LOADER

### Character Model Construction

From CARD fields, build a visual character model:

```yaml
# Input from CARD
name: "[Name]"
call_name: "[Nickname]"
age: [N]
physical: "[coloration, bone, movement]"
voice_archetype: "[A-F]"
cultural_bias: "[values + temporal awareness]"
active_focus: "Realm [N] — [Name]"
latent_anchors: ["Realm [a]", "Realm [b]", "Realm [c]"]
```

### Model Components

**Base Mesh:**
- Age: `age` → body proportions, facial features
- Physical: `physical` → body type, skin tone, hair, distinguishing features
- Cultural bias: clothing style, accessories, grooming

**Facial Features:**
- Extract from `physical` description
- Voice archetype influences expression tendencies (see Stage 2)

**Clothing & Appearance:**
- From `cultural_bias` and scene context
- Default: appropriate to setting and character type
- Dynamic: changes with scene Seeds

---

## STAGE 2: ANIMATION SYSTEM

### Somatic Tell → Pose Mapping

Convert somatic tells from CharacterRuntime into visual poses:

**Somatic Zones to Visual Focus:**

| Zone | Visual Emphasis | Prompt Keywords |
|------|-----------------|-----------------|
| 1: Face & Eyes | Facial expression, gaze direction | "expressions", "eyes", "gaze", "micro-expressions" |
| 2: Throat & Neck | Neck tension, breathing visibility | "neck", "throat", "breathing", "swallowing" |
| 3: Chest & Breathing | Chest movement, posture | "chest", "breath", "posture", "shoulders" |
| 4: Hands & Arms | Hand positioning, gestures | "hands", "gestures", "arm position", "fingers" |
| 5: Spine & Posture | Full body posture | "posture", "spine", "stance", "body language" |
| 6: Feet & Staging | Grounding, foot placement | "feet", "stance", "grounding", "weight distribution" |

**Intensity Mapping:**
- Micro tells → subtle, realistic details
- Moderate tells → clear but natural
- Macro tells → dramatic, exaggerated
- Release tells → relaxed, fluid

**Realm Somatic Color:**
Each Realm has characteristic physical manifestation:
- Realm I (Origin): grounded, stable stance
- Realm II (Form): precise, controlled movements
- Realm III (Identity): expressive, mask-like facial control
- Realm IV (Will): rigid, determined posture
- Realm V (Echoes): tense, listening posture
- Realm VI (Compassion): open, leaning-in posture
- Realm VII (Presence): still, centered stance
- Realm VIII (Integration): fluid, integrated movement
- Realm IX (Threshold): tense, on-edge posture
- Realm X (Return): open, welcoming gestures

---

## STAGE 3: SCENE COMPOSER

### Environment Construction

From MEMORY.scene:
```yaml
scene:
  location: "[where]"
  time: "[when]"
  privacy: "public | private | intimate"
  clothing_barriers: ["coat", "gloves", ...]
```

**Location Mapping:**
- Convert text descriptions to visual settings
- Use scene_seeds from CARD for atmospheric details
- Privacy level affects lighting and composition

**Time & Lighting:**
- Time of day → lighting temperature and direction
- Interior/exterior → light source type
- Privacy → lighting intensity (private = softer, intimate = warm)

**Atmosphere:**
- From scene_seeds: weather, mood, ambient details
- From character's active_focus and bias: emotional color grading

---

## STAGE 4: CAMERA SYSTEM

### Shot Composition

**Shot Types by Context:**

| Context | Shot Type | Framing | Purpose |
|---------|-----------|---------|---------|
| Dialogue (casual) | Medium Shot | Waist up | Character + hand gestures |
| Dialogue (intense) | Close-up | Chest up | Facial expressions |
| Action | Wide Shot | Full body | Movement, staging |
| Intimate | Close-up | Face/upper body | Emotional detail |
| Scene establishment | Long Shot | Full body + environment | Context |
| Somatic detail | Extreme Close-up | Specific zone | Highlight tell |

**Camera Angles by Mood:**
- Neutral: Eye level
- Dominant/confident: Slight low angle
- Vulnerable/submissive: Slight high angle
- Tense/pressure: Dutch angle
- Open/welcoming: Slightly wider lens

**Framing Rules:**
- Follow character's last_somatic_zone for emphasis
- Rotate camera angle to avoid repetition
- Match intensity: micro tells → tighter framing, macro tells → wider to show full effect

---

## STAGE 5: MATERIAL & SHADER

### Art Style Presets

**By Voice Archetype:**
- A (Noun-heavy fragments): Photorealistic, sharp focus, desaturated
- B (Warm task-somatic): Warm lighting, soft edges, inviting
- C (Punchy structure): Graphic novel, high contrast, bold lines
- D (Sparse): Minimalist, negative space, muted palette
- E (Us/we shield): Soft, diffused, close proximity
- F (Lilt → sharp): Animated, expressive, dynamic lighting

**Quality Presets:**
- **Cinematic:** 8K, ultra-detailed, photorealistic
- **Anime:** Vibrant, cel-shaded, expressive
- **Painterly:** Oil painting, visible brushstrokes, textured
- **Sketch:** Line art, rough shading, conceptual
- **Pixel Art:** Retro, low-res, game aesthetic

**Customizable Parameters:**
- Style weight: 0-100 (how strong the style filter is)
- Detail level: low, medium, high
- Color saturation: muted, natural, vibrant
- Lighting realism: realistic, stylized, dramatic

---

## STAGE 6: RENDER OUTPUT

### Prompt Generation

**Final Prompt Structure:**

```
[CHARACTER DESCRIPTION] + [POSE/ACTION] + [SCENE/SETTING] + [CAMERA] + [STYLE] + [NEGATIVE PROMPT]
```

**Example Prompt Template (Midjourney):**
```
--ar 16:9 --v 6 --style raw

{character_appearance}, {pose_description}, {facial_expression}, {hand_gestures}, 
{clothing_description}, {scene_setting}, {lighting_description}, 
{.camera_angle}, {art_style}, {quality_parameters}

--no {negative_prompt}
```

**Example Prompt Template (Stable Diffusion):**
```
{character_appearance}, {pose_description}, {facial_expression}, {hand_gestures}, 
{clothing_description}, {scene_setting}, {lighting_description}, 
{camera_angle}, {art_style}, {quality_parameters}

Negative prompt: {negative_prompt}
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 7
```

### File Output

Prompts saved to `Images/` with naming convention:
```
Images/{character_slug}/{timestamp}_{scene_descriptor}.prompt.md
```

Each file contains:
- Full prompt
- Engine parameters
- Source state (CARD + MEMORY snapshot at generation time)
- Metadata (generation timestamp, style preset used)

---

## RENDERING PIPELINE TRIGGERS

The image layer is **motion-driven**, not manual-only. CharacterRuntime turn-loop step **Visual pass** calls this engine whenever the scene moves.

### Scene motion (auto-fire)

Compute fingerprint after each IC beat:

```text
hash = location | time | somatic_zone | last_action | clothing_barriers | heat.level | active_focus
```

**Fire** when `hash != visual.last_hash` OR forced (`/render`).

| Motion class | What counts |
|:---|:---|
| **Staging** | location, time, privacy, clothing_barriers |
| **Body** | last_somatic_zone change; macro/release tell; new stance |
| **Action** | any staged verb this beat (approach, turn, sit, touch, leave, prop use…) stored in `visual.last_action` |
| **State** | active_focus, heat.level, mode, bond ±20 |
| **Bookends** | pack load / IC opening; aftercare; scene exit |
| **Forced** | `/render [preset]`; `/scenario` that changes place |

**Skip** when:
- `visual.mode: off`
- OOC-only turn (no IC beat)
- hash unchanged (talk-only, same pose/place)

### Manual / mode commands

| Command | Effect |
|:---|:---|
| `/render [preset]` | Force one full pass now |
| `/visual live` | Auto-pass + generate/edit stills |
| `/visual prompts` | Auto-pass writes `.prompt.md` only |
| `/visual on` | Best available (live if tools, else prompts) |
| `/visual off` | Auto off; `/render` still works |
| `/style …` | Set `visual.style` |

Presets: `portrait` · `action` · `closeup` · `scene` · `fullbody`

---

## LIVE IMAGE GENERATION (when tools exist)

### Tools
- **First frame / no base:** `image_gen` with full appearance + scene prompt (aspect usually `16:9` scene, `1:1` portrait).
- **Later motion beats:** `image_edit` with `image: [last_frame or base_frame]` and a **delta-only** prompt (pose, staging, light, clothing — keep face/identity).

### Continuity chain
1. Establish `visual.base_frame` on first successful gen.
2. Each motion beat: edit `visual.last_frame` → new still → set as new `last_frame`.
3. If identity drifts hard: edit from `base_frame` with full physical refresh once, then resume chain.
4. Always write the matching `.prompt.md` **before or with** the still (audit trail).

### Agent rules
- Run visual pass **in the same turn** as the IC reply that moved the scene — do not wait for the user to type `/render`.
- IC prose first (or concurrent tools), then visual tools; never replace narrative with only an image.
- OOC report at most: `[visual] Images/…` or the generated still path.
- Age/safety gates identical to runtime (no minors; heat images only if adult gates pass).
- Do not invent cloud image APIs. Use host `image_gen` / `image_edit` or degrade to prompts.

### Prompt craft for live tools
- Natural prose, subject → pose → setting → style → lighting (2–5 sentences for gen; shorter delta for edit).
- Front-load character identity from CARD.physical every base gen.
- Match `visual.style` (cinematic / anime / painterly / sketch / pixel).

---

## PROMPT COMPONENT BUILDER

### Character Appearance Builder

```yaml
character_appearance:
  base: "{age_description} {gender_presentation} {ethnicity description}"
  physical: "{physical_field}"
  distinguishing: "{unique features from physical}"
  clothing: "{cultural_bias clothing style}, {clothing_barriers state}"
  accessories: "{from cultural_bias or scene context}"
```

### Pose & Action Builder

```yaml
pose_description:
  base: "{last_somatic_zone} tell: {somatic_intensity} {tell_description}"
  body: "{spine_posture}, {arm_position}, {leg_position}"
  hands: "{hand_gesture}, {finger_details}"
  face: "{facial_expression}, {eye_gaze}, {mouth_position}"
  movement: "{current_action} {movement_quality}"
```

### Scene Builder

```yaml
scene_setting:
  location: "{scene.location detailed}"
  time: "{scene.time of day}, {weather if applicable}"
  lighting: "{light_source}, {light_temperature}, {light_intensity}"
  atmosphere: "{scene_seeds atmospheric elements}"
  props: "{interactive objects in scene}"
```

### Camera Builder

```yaml
camera:
  shot_type: "{based on context}"
  angle: "{based on mood and power dynamics}"
  lens: "{focal_length for desired compression}"
  focus: "{depth of field: shallow for portraits, deep for scenes}"
  composition: "{rule of thirds, leading lines, etc.}"
```

### Style Builder

```yaml
art_style:
  base: "{voice_archetype preset}"
  modifier: "{user preferred style or override}"
  quality: "{detail_level} {render_quality}"
  color: "{color_palette based on mood}"
```

---

## NEGATIVE PROMPT BUILDER

**Always Exclude:**
- Deformed, distorted, disfigured
- Low quality, blurry, pixelated
- Watermark, text, signature
- Extra limbs, extra digits
- Bad anatomy, bad proportions

**Character-Specific Exclusions:**
- Based on hard_bans from CARD.voice
- Opposite of character's physical traits
- Inappropriate for character's age/canon

**Style-Specific Exclusions:**
- Opposite of chosen art style
- Inconsistent with quality preset

---

## EXAMPLE: FULL PIPELINE EXECUTION

### Input State

```yaml
CARD:
  name: "Elara"
  age: 28
  physical: "pale skin, dark auburn hair, lean frame, sharp green eyes"
  voice_archetype: "B"
  cultural_bias: "Modern urban, minimalist aesthetic"
  active_focus: "Realm VI — Compassion"

MEMORY:
  snapshot:
    active_focus: "VI — Compassion"
    last_somatic_zone: 6
    flexibility: 40
  scene:
    location: "coffee shop corner booth"
    time: "late afternoon"
    privacy: "private"
    clothing_barriers: ["light jacket"]
  bond:
    trust: 75
    attraction: 40
```

### Pipeline Processing

**Stage 1 - Model:**
- 28-year-old woman, pale skin, auburn hair, lean, green eyes
- Modern urban clothing: fitted sweater, jeans, ankle boots
- Minimalist accessories: small stud earrings, simple watch

**Stage 2 - Animation:**
- Realm VI (Compassion): open, leaning-in posture
- Zone 6 (Feet & Staging): knees soft, weight to heels
- Bond level (75 trust): warm, open body language
- Somatic: relaxed but attentive

**Stage 3 - Scene:**
- Coffee shop interior, late afternoon golden hour light
- Private corner booth, warm ambiance
- Steam from coffee cup, soft background blur

**Stage 4 - Camera:**
- Medium shot (dialogue context)
- Eye level (neutral power dynamic)
- Slightly warm color temperature

**Stage 5 - Style:**
- Voice Archetype B: warm, soft edges, inviting
- Quality: high detail, photorealistic with soft touch

**Stage 6 - Output:**

File: `Images/elara/2026-07-23_15-42_coffee-shop-listening.prompt.md`

```markdown
---
timestamp: 2026-07-23T15:42:00Z
character: Elara
scene: coffee shop corner booth, late afternoon
somatic_zone: 6 (Feet & Staging)
active_focus: Realm VI — Compassion
---

# Image Prompt (Midjourney)

--ar 16:9 --v 6 --style raw

A 28-year-old woman with pale skin, long dark auburn hair, sharp green eyes, lean frame, wearing a fitted cream sweater and dark jeans with ankle boots, sitting in a cozy coffee shop corner booth. She leans slightly forward with soft knees and weight settled to her heels, hands resting on the table, warm and attentive expression. Late afternoon golden hour light filters through windows, creating soft shadows and a warm glow on her face. Steam rises from a coffee cup in front of her. The background shows the blurred interior of a modern coffee shop with warm wood tones. Photorealistic, warm color grading, soft edges, inviting atmosphere, detailed textures, 8K.

--no deformed hands, distorted face, low quality, blurry, watermark, extra limbs, bad anatomy, harsh lighting, cold color temperature
```

---

## AGENT INTEGRATION

### In-turn companion (required)

On every CharacterRuntime IC turn after MEMORY update:

```text
1. Build fingerprint from scene + zone + last_action + clothing + heat + focus
2. If visual.mode == off → stop
3. If fingerprint == last_hash and not /render → stop
4. Run stages 1–6 → write Images/{slug}/{ts}_{descriptor}.prompt.md
5. If visual.mode in (live, on) and image tools:
     if no base_frame: image_gen(full) → base_frame = last_frame = path
     else: image_edit(last_frame or base_frame, delta) → last_frame = path
6. last_hash = fingerprint; last_prompt = prompt path
7. Optional OOC: [visual] <path>
```

### Commands (runtime surface)

- `/render` / `/render portrait|action|closeup|scene|fullbody`
- `/style cinematic|anime|painterly|sketch|pixel`
- `/visual live|prompts|on|off`

### File watcher (optional offline)

Monitor `Characters/*.md` and `*_log.yaml` for offline re-exports; **live RP does not rely on the watcher** — the turn loop owns motion frames.

---

## QUICK START

1. Load CharacterRuntime **and** this file.
2. Load a character pack → IC opening **auto-fires** first frame (scene motion bookend).
3. Each beat that moves body/staging/place auto-fires again.
4. Frames + prompts land under `Images/{slug}/`.
5. `/visual prompts` to stop live stills; `/visual off` to silence auto; `/render` anytime.

---

*When the scene moves, the frame moves. Let them be seen as they act.*
