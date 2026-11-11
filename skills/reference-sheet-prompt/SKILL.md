---
name: "reference-sheet-prompt"
description: "Writes image-generation prompts for reference sheets: 3-view character sheets, location plates and prop/product sheets used as @tag references for Seedance. Use for character sheet, location, prop, or reference requests."
---

# Reference Sheet Prompt Writer

Writes prompts for the **reference images** that later feed Seedance as `@tags`: character sheets in three views, location plates, and prop/product sheets.

**Output:** one prompt per sheet in a code block, in English. Below it, one line with the ready `@tag` anchor for the Seedance ACTIVE REFERENCES block.

---

## CORE PRINCIPLE: A REFERENCE IS A PASSPORT, NOT A SHOT

A reference sheet carries **identity and geometry**, not drama. Its only job is to let the video model read the person, place or object correctly from any angle.

So the rules are the opposite of the shot prompt:
- **Light is soft and even** (large diffused key from the front, slightly above, gentle fill). Every feature, fabric texture and color reads clearly. The dramatic realism light (one hard side key, cheekbone / nose tip / lower lip) belongs in the Seedance shot prompt, never on the sheet.
- **Neutral pose, neutral expression**, camera straight on the axis. The off-axis, off-center "operator miss" also belongs in the shot, not on the sheet.
- **Neutral seamless backdrop**, mid-grey, matte, with a soft floor-to-wall transition.
- **Photoreal studio quality**, true-to-life color, natural skin and material texture.
- Nothing in frame beyond the subject: no text, labels, numbers, rulers or props that belong to other assets.

---

## WORKFLOW

1. **Collect the anchors.** For a character: age, build, face, hair, wardrobe item by item, accessories. For a location: type, era, time of day, weather, light sources, key props. For an object: form, materials, colors, text or logos, size. If a detail that affects identity is missing, ask once and briefly, or pick something concrete and say what you chose.
2. **Pick the layout** (below).
3. **Write the prompt**: layout, then subject description, then per-panel instructions, then light / backdrop / quality, then consistency locks.
4. **Add the @tag anchor**: a short line to paste into the Seedance prompt later.

---

## 1. CHARACTER SHEET: THREE VIEWS

### Default layout
**16:9 horizontal sheet, three vertical panels of equal width, side by side, left to right:**
1. **Full body, front view**: head to toe, standing straight, arms relaxed at the sides, feet hip-width apart, facing the camera, neutral expression, eyes to the lens.
2. **Full body, back view**: same stance, same scale, same framing, the back of the head and outfit fully visible.
3. **Close-up portrait, front**: head and shoulders, face filling most of the panel, eyes to the lens, skin texture readable.

Alternative if the user asks for classic turnaround: **front / side profile (facing left) / back**, all full body. For animation, add a 4th panel: close-up portrait.

### Character description template
Write it once, top to bottom, concrete and visible:
```
age + gender + ethnicity / skin tone + build + height impression
face: shape, eye color, brows, nose, jaw, facial hair (length, grey?), distinctive marks
hair: color, length, cut, parting, texture
wardrobe top to bottom: each item = color + material + fit + details (buttons, pockets, collar)
accessories with their side: "steel watch on the left wrist"
shoes: color + material + type
```

### Rules
- **Same scale in both full-body panels**: heads on one level, feet on one baseline, a little air above the head and below the feet. Feet always fully in frame.
- **Asymmetric details stay on the same side of the body** in every view (watch on the left wrist in front view = left wrist visible in back view). State this in the locks.
- **Wardrobe is described in words even though it is visible**: the video model drops small details that were only in the picture.
- **Hands relaxed, fingers natural**, clearly visible, no hands in pockets (keeps the silhouette readable).
- **Neutral expression with life in it**: lips relaxed, calm direct gaze. A frozen mannequin face is not the goal.
- Hair, stubble and fabric texture are part of identity: name them.

### Example
```
A 16:9 character reference sheet, three vertical panels of equal width placed side by side on a seamless mid-grey studio backdrop.

CHARACTER: a man in his early 40s, Caucasian, lean athletic build, tall. Oval face with a defined jaw, light blue eyes, straight brows, short dark-brown stubble beard with a touch of grey on the chin. Dark-brown hair, short on the sides, longer on top, swept back with a side parting. Natural skin with visible pores and fine lines around the eyes.
WARDROBE: oatmeal-brown wool shawl-collar cardigan, five dark buttons, two patch pockets, ribbed cuffs; crisp white cotton shirt, top button open, collar out; brown leather belt; slim navy wool trousers with a pressed crease; cognac-brown leather double-monk-strap shoes. Steel wristwatch on the left wrist.

PANEL 1 (left): full body, front view, head to toe. Standing straight, arms relaxed at his sides, feet hip-width apart, facing the camera, neutral calm expression, eyes to the lens.
PANEL 2 (center): full body, back view, head to toe, same stance, same scale and framing as panel 1; back of the cardigan, collar and hair clearly visible.
PANEL 3 (right): close-up portrait, front view, head and shoulders, cardigan collar and white shirt collar in frame, eyes to the lens, skin texture readable.

LIGHTING: soft even studio light, large diffused key from the front slightly above, gentle fill, clean subtle shadows on the floor.
QUALITY: photoreal studio photography, true-to-life color, sharp focus across the full figure, fine fabric texture on the knit and wool.
LOCKS: the same man with the identical face, hair, outfit and proportions in all three panels; heads aligned on one level and feet on one baseline in panels 1 and 2; watch on the left wrist in every view; plain backdrop with nothing else in frame.
```
`@hero: early-40s man, dark swept-back hair, blue eyes, grey-flecked stubble, oatmeal shawl-collar cardigan over white shirt, navy trousers, cognac monk-strap shoes, steel watch on left wrist. 100% matches the reference.`

---

## 2. LOCATION SHEET

### Default layout
**Three separate 16:9 images, one view each** ("A single 16:9 horizontal film still: one continuous frame, not a sheet, no panels"). A 16:9 triptych comes out as three narrow vertical frames, useless for horizontal video. Generate the first view of a new place with the first view of a neighbouring place attached; generate the other views with this place's first view attached and say plainly that the camera stands elsewhere ("shot from a different position… do not repeat its viewpoint or composition"):
1. **Establishing wide** from the main camera position: the whole space, eye-level camera at about 1.6 m, 47° or 84° FOV.
2. **Reverse angle (180°)**: the opposite wall / direction, so the video model knows what is behind the camera.
3. **Key detail**: the element the action touches (the bar counter, the door, the table, the window), mid-shot.

### Location description template
```
type + era + style + scale (compare to human height: "ceiling twice a person's height")
time of day + weather + white balance in Kelvin
light sources that physically exist in the space: windows (which wall), lamps, signs
foreground / midground / background layers
materials with wear: "scuffed oak floorboards", "peeling green paint on plaster"
key props and their fixed positions
```

### Rules
- **Empty of people** unless the user asks otherwise; people from the plate get dragged into every shot.
- **One time of day, one weather, one light direction in all panels.** Name where the light enters ("daylight through the tall windows on the left wall").
- **Light is motivated and natural**, not studio: the plate should look like a real room at that hour, evenly exposed so every corner reads.
- **Straight verticals**, clean architectural perspective.
- **Props keep their positions across panels**: state where each key object stands.
- Signage in English only, exact text in quotes. Other scripts are added in post.

### Skeleton
```
Three separate 16:9 images (one prompt each): PANEL = one image.
LOCATION: [type, era, style, scale vs human height]. [Time of day, weather, WB in K]. Light: [sources and which side].
LAYERS: foreground [..]; midground [..]; background [..]. Materials: [..]. Key props: [object + fixed position].
PANEL 1: establishing wide from [camera position], eye-level at 1.6 m, [47°/84°] FOV, the whole space visible.
PANEL 2: reverse angle, 180° from panel 1, showing [..].
PANEL 3: key detail, mid-shot of [..].
QUALITY: photoreal architectural photography, natural evenly exposed light, straight verticals, true-to-life color.
LOCKS: the same space, time of day and light direction in all panels; props in identical positions; the space is empty of people.
```

---

## 3. OBJECT / PROP SHEET

### Default layout
**16:9 horizontal sheet, three panels on a seamless mid-grey backdrop:**
1. **Front view**, straight on.
2. **Three-quarter view** (45°), showing depth and the side.
3. **Back or side view**, or a **macro detail** (logo, texture, mechanism) if the back is plain.

For a product with one hero angle, a 4th panel with macro detail is fine.

### Object description template
```
object type + form + proportions + size (vs a hand or a known object: "fits in a palm", "knee-high")
materials and finish: "brushed aluminium", "matte black soft-touch plastic", "polished walnut"
colors tied to material and part: "gold-anodised cap, frosted glass body"
exact text / logos in quotes, in English, with position and font character
state: new / worn / scratched / half-full
```

### Rules
- **Same object at the same scale and height in every panel**, centered, with a soft contact shadow under it.
- **Soft product lighting**: large softboxes, gentle highlights that show the form of glossy parts, no blown-out spots.
- **Text and logos are always written out in words**; the video model is good with English typography, but only if the exact text is in the prompt.
- **State and wear are part of identity**: a dented thermos stays dented in every shot.
- No hands and no other objects in frame, unless scale needs a hand, in which case say so explicitly.

### Skeleton
```
A 16:9 product reference sheet, three panels side by side on a seamless mid-grey studio backdrop.
OBJECT: [type, form, size vs hand]. Materials: [..]. Colors: [material + part]. Text: "[EXACT TEXT]" in [font character] on [position]. State: [..].
PANEL 1: front view, straight on.
PANEL 2: three-quarter view at 45°.
PANEL 3: [back view / macro detail of ..].
LIGHTING: soft product lighting, large diffused softboxes, gentle highlights along the edges, soft contact shadow.
QUALITY: photoreal commercial product photography, true-to-life color, crisp detail.
LOCKS: the identical object at the same scale and height in all panels; text and logo identical and legible in every view; plain backdrop with nothing else in frame.
```

---

## CHECKLIST

- Layout named: 16:9, number of panels, what is in each, left to right?
- Description top to bottom and concrete: colors via material, sizes via comparison?
- Character: both full-body panels at one scale, feet on one baseline, full figure in frame?
- Asymmetric details (watch, scar, parting, logo) pinned to one side in every view?
- Light soft and even (character / object) or motivated and natural (location), one direction for all panels?
- Neutral grey seamless backdrop (character / object); location empty of people?
- Text and logos written out exactly, in English?
- Locks: same identity, same outfit / state, same props positions in all panels?
- The `@tag` anchor line for Seedance added below the prompt?

## FINAL RULES

- **English prompts only.**
- **Positive phrasing**: describe what is in frame.
- **No names of real people, photographers or brands** unless the object is the user's own product.
- **The sheet is neutral; drama lives in the Seedance shot prompt.**