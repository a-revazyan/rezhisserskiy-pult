---
name: "higgsfield-image-prompt"
description: "Writes image prompts by the Higgsfield Image & Prompt Library method (Soul Cinema, Seedream, GPT Image Sunburst, Nano Banana): stills, location plates, exact text, infographics, storyboards."
---

# Image Prompt Writer (Higgsfield Image & Prompt Library method)

Distilled from Higgsfield Academy (https://higgsfield.ai/academy), Course 01 / Lesson 04, "Image & Prompt Library": 27 prompts across Soul Cinema, Seedream 5.0 Pro, GPT 2.5 Sunburst and Nano Banana Pro, each shown with the image it produced. The method is retold here in our own words.

Use this skill for any single still image: a cinematic frame, an empty location plate, a source image that will later feed video or new camera angles, a prop with exact text, an editorial layout, an infographic, a storyboard or previs sheet.

Related skills:
- Multi-view reference sheets (character in three views, prop sheet) -> `reference-sheet-prompt`.
- Ad posters, banners, promo creatives -> load `anti-slop-design-director` first, then apply this skill's text rules to the exact copy.
- Video prompts -> `higgsfield-seedance-prompt`. A plate made here can become a Seedance @tag.

**Output:** one prompt in English, in a code block. Above it, one line: recommended model + aspect ratio. Below it, at most one line on anything you assumed. Talk to the user in their language; the prompt itself stays in English (exact on-image text can be in any language, in quotes).

---

## CORE IDEA: DESCRIBE THE SHOT, NOT THE VIBE

Every prompt in the library reads like notes from a cinematographer, a set dresser and a script supervisor at once. It fixes:
- **what the camera is** (height in metres, position, aim, lens, field of view, focus);
- **where every object sits** (foreground / midground / background, frame left / centre / right);
- **where light comes from, and where it is not allowed to go**;
- **which colours are true** (each material keeps its own colour, no global tint);
- **what must not appear**, and **exact counts** of the things that must.

Vague praise words ("beautiful, epic, ultra detailed, 8k, masterpiece") never appear. They are replaced by measurable facts: metres, millimetres, degrees, counts, frame positions, named materials.

---

## STEP 1. COLLECT THE ANCHORS

Before writing, know:
1. **Purpose:** final hero still, location plate for later video, source image for angles or 3D, prop insert, graphic/layout, storyboard.
2. **Subject and place:** era, region, materials, key objects.
3. **Time and light:** time of day, weather, light sources.
4. **Text:** must there be readable text? If yes, the exact words.
5. **Format:** aspect ratio (16:9, 2.39:1, 4:3, 3:4, 1:1...).
6. **People:** in frame or an empty plate? (Plates are empty by default.)

If something that changes the image is missing, ask once and briefly, or pick something concrete and say what you chose.

## STEP 2. PICK THE MODEL

| Model | What the library uses it for | Prompt style that worked |
|---|---|---|
| **Soul Cinema** | Cinematic stills, environments, moody interiors, location plates without text | From a short imperative paragraph up to a full 250-word cinematic description |
| **Seedream 5.0 Pro** | Large-scale and invented worlds: orbital habitats, desert megacities, sci-fi labs, plain streets | The compact formula (60-110 words), always the same block order |
| **GPT 2.5 Sunburst** (GPT Image) | Anything that must be exact: readable text (including Japanese), licence plates, book spreads, typography, infographics with real numbers, storyboard grids, grey-mesh previs, style transfer from a reference, products with many markings, long source-image specs | Long, structured, literal prompts with quoted text and explicit "not X" |
| **Nano Banana Pro** | Photoreal location plates | Works with both the compact formula and the full cinematic version |

Rule of thumb: **readable text, numbers, grids or exact counts -> GPT 2.5 Sunburst.** Atmosphere and cinematic look -> Soul Cinema. Big worlds in few words -> Seedream. The library runs the same prompt through several models, so the structure below is model-agnostic; only density changes.

When generating through Higgsfield tools, confirm the current model id with `models_explore` and also set the aspect ratio in the generation settings, not only in the text.

## STEP 3. PICK THE LENGTH

| Tier | Length | When |
|---|---|---|
| Imperative sketch | 30-60 words | Quick exploration where layout matters more than look. Plain commands: "Create an empty... Place X on the right... Add... Frame the shot from the doorway." |
| Compact formula | 60-110 words | Default for location plates and world-building |
| Full cinematic | 150-300 words | Hero stills, mood pieces, complex light |
| Source-image spec | 600-1000 words | The image will feed video, angle generation or a 3D scene, so every object must stay where you put it |

---

## THE ANATOMY: NINE BLOCKS, IN THIS ORDER

### 1. Opening line: medium + subject + condition
State what kind of image it is before anything else.
- "A cinematic still of..." / "A cinematic night still of..."
- "An empty photographic view of..." (the plate formula; "empty" = no people)
- "Wide cinematic interior still of..."
- "Photorealistic cinematic prop photograph of..."
- "Design a ... magazine spread as one flat landscape 4:3 graphic."
- "A ROUGH WORKING ANIMATION STORYBOARD, not finished animation art."

Add a "not X" right in the opening when a model tends to drift ("not a flat digital mockup", "not finished animated-film stills"). Capitals are used sparingly, for the one word that defines the genre.

### 2. Format
Aspect ratio in the text: "Cinematic still, 2.39:1.", "horizontal 16:9", "portrait 3:4", "landscape 4:3". For layouts: "edge-to-edge flat artwork, no paper perspective, no shadows". For photographed objects: "entire plate visible with its edges".

### 3. Camera
Write it like a camera report:
- **Position:** where the camera physically stands. "across the dirt road from the property", "under the covered walkway on the opposite side of the street", "from a pedestrian footbridge above the centreline", "in the near corner, three-quarter angle across the hall", "from an upper balcony".
- **Height in metres:** 0.8 m (low, ground plate), 1.2-1.6 m (eye or shoulder), 5 m (footbridge), balcony "~30° down".
- **Aim and tilt:** "level", "looking across and slightly down the row", "only a gentle downward tilt", "looking down the cylinder axis".
- **Lens:** focal length as full-frame equivalent + "spherical" (not anamorphic) + horizontal field of view + "distortion off". For architecture add "verticals straight", "clean rectilinear rendering".
- **Focus:** "deep focus", "focus on the far facade", "shallow depth on the foreground lantern", "the house in sharp focus beyond".

Horizontal field of view on full frame (use these numbers, they are what the library uses):

| Lens | 14 | 18 | 24 | 28 | 32 | 35 | 40 | 50 | 85 | 135 |
|---|---|---|---|---|---|---|---|---|---|---|
| HFOV | ~104° | ~90° | ~74° | ~65° | ~59° | ~54° | ~48° | ~40° | ~24° | ~15° |

Typical choices: 24 mm for a whole room or a vast interior; 28-35 mm for streets and plates; 40-50 mm for a classic cinematic frame of a building or street; 85 mm+ for compressed, isolated subjects.

### 4. Layout: place everything
- **Depth layers:** near foreground, midground, background, horizon/sky. Give each layer its content.
- **Frame positions:** "on frame left in the mid-distance", "just right of centre in the midground", "slightly left of centre", "at frame right".
- **A foreground framing element** makes a frame feel shot rather than rendered: out-of-focus crop leaves along the lower edge, a paper lantern close to the lens, a blurred balcony railing along the bottom and left edges, a dark post in near-black silhouette.
- **Proportions:** "clouds fill two thirds of the frame", "the faceplate fills most of the frame".
- **Interiors:** walk the room in reading order: "Read the frame from the left." Describe the left wall, then the back wall, then the right wall, then the middle. Give room size in metres and ceiling height.
- **Prevent lazy placement:** "standing free of every wall", "well clear of the sideboard behind it", "clear floor surrounds the rug on all sides".

### 5. Light logic
Name every source, its direction and quality, what it touches, and where it must stop.
- Source + direction + quality: "direct late-afternoon sun from the right, long single shadows", "soft directionless daylight flattening the shadows", "hard midday desert sun from upper left, deep shadows under the canopies".
- **Hidden sources:** say the source is never visible and describe light only by what it does to surfaces ("the source and the opening itself never visible ... only the downward direction of the light read through the surfaces").
- **Practicals-only scenes:** list them and close the list: "five practical sources and nothing else", then "each keeps its own pool with generous falloff".
- **Containment:** "warm lantern light stays contained to the facades; the machine's cold glow spills only onto the pavement directly before it." This is how mixed colour temperatures stay clean.
- **Effect on surfaces:** which edges catch highlights, which way shadows fall, how walls grade from bright to mid-tone.
- **Exposure:** "exposed comfortably, nothing sinks to black", or "the sky still carries the exposure while the street already lives on its lamps".
- A strong single line helps: "Sunlight is the scene's engine."

### 6. Colour foundation
- Default phrase: **"Maintain a neutral photographic foundation"**, then say that each material keeps its local colour ("cream siding, gray sky, straw-yellow grass and saturated green corn each keeping their local color").
- **Governing pair:** name the two colours that define the room ("light orange walls and pale blue floor as the room's governing pair").
- **Ban the global wash:** "warm only where the sun physically falls", "no global amber wash", "no global orange tint over the blue floor".
- Graphics: a closed palette of 3-5 named colours ("warm ivory, carbon black, electric acid lime and one muted lilac accent").

### 7. Capture and texture
Pick one capture character and stick to it:
- Clean: "clean modern digital-cinema capture, no film grain, no halation, no haze".
- Analog: "mild / gentle analog grain".
- Period: "soft vintage film texture with fine grain and slightly faded blacks, like a quiet frame from a 1990s Japanese drama".

Then two or three **tactile** material details: "tactile salt crust ridges and thin water film", "cable bundles and panel seams", "gritty stucco, sand ripples and flaking paint", "condensation on glass".

### 8. Mood key (one line)
A genre or register, not adjectives: "quiet nostalgic Americana in a restrained prestige-drama key", "nostalgic domestic-drama grade", "intimate domestic realism: curated but credible, lightly lived-in, presently empty".

### 9. Guards (always last)
- **Negatives, including where people hide:** "No people, silhouettes, faces or figures behind the lattices, in window glass, mirrors or reflections."
- **Text policy:** either "no readable text, signage, logos or licence plates" (and for decorative script: "calligraphy reads only as soft abstract brush forms"), or exact quoted text (see TEXT below).
- **Count locks:** "Keep exactly one vending machine and one waste bin." List every hero object with its count.
- **Avoid list of likely failures for this scene:** "Avoid visible lamps or skylights, god rays, spotlight circles, dark corners, clutter"; "avoid the sofa pushed against a wall, a second armchair, a television, warped perspective".
- Optional **purpose line:** "A movie set prop example demonstrating precise text, not a flat vector design." Telling the model what the image is for helps it choose.

---

## COMPACT FORMULA (copy, fill, send)

```
An empty photographic view of [PLACE]: [3-5 KEY ELEMENTS with materials and positions]. [ONE NEAR-FOREGROUND ELEMENT]. Camera at [H]m [WHERE IT STANDS] looking [TOWARD WHAT], [F]mm spherical lens. [LIGHT: time, source, direction, quality], [ATMOSPHERE: haze, mist, dust]. [CAPTURE: gentle analog grain / fine digital detail], tactile [2-3 MATERIAL DETAILS]. No people, [vehicles / animals], readable text or logos.
```

For a plate that will be used for camera moves, say so: "vast open ground allowing a full 360-degree camera orbit", or "composition built for a very wide frame".

## SOURCE-IMAGE SPEC (for images that feed video, angles or 3D)

Write in separate paragraphs, in this order:
1. **Overview:** genre, room/place, time, the view and what must be in frame ("the left wall, the back wall and the right wall with its window all in frame").
2. **Camera:** height, exact standing point ("inside the near end just left of the centreline, aimed toward the far-right corner"), tilt, lens + HFOV, distortion off, verticals straight, deep focus.
3. **Space and materials:** dimensions in metres, ceiling, wall finish, floor finish, trims.
4. **Inventory in reading order:** left wall -> back wall -> corners -> middle group -> right wall. Every object with material, colour, size and what sits on it.
5. **Light logic:** sources, direction, pools, shadows, what stays readable in shade, which lamps are off.
6. **Colour foundation:** neutral base, governing pair, local colours, no global wash.
7. **Capture character.**
8. **Mood line.**
9. **Guards:** no people anywhere including reflections; no readable text on spines, prints, objects; "Keep exactly one X, one Y..."; avoid list.

---

## TEXT, NUMBERS AND LAYOUTS (GPT 2.5 Sunburst)

- Put every string in quotes with **"exactly"**: `reading EXACTLY "7HGF204"`. State position, size, colour and style for each string ("red cursive ... centered at the top", "tiny centered bottom text").
- Close the set: **"Carefully reproduce all requested text and its location; no additional letters or numbers."** For layouts: "No additional copy beyond the supplied words and numbers."
- Keep main lettering large enough to read: "main lettering and prices must stay large enough to read amid the abundance of drawn objects".
- Non-Latin scripts work when quoted exactly (the library renders Japanese signage). Test Cyrillic with a short string first.
- Real-world objects with text: give correct proportions and construction ("correct 2:1 proportions", "raised embossed characters", "two screws at the upper mounting holes").
- Photographed print vs flat graphic, choose one: "convincing real ink on paper, not a flat digital mockup" OR "edge-to-edge flat artwork, no paper perspective, no shadows".
- Layouts: name the grid ("rigorous twelve-column baseline grid under a daring asymmetric composition"), type by category (condensed grotesk display, high-contrast italic serif, monospaced annotations), then list every block with its exact copy, top to bottom, left to right.
- **Data:** give the exact values and make them consistent across table and chart; demand honesty: "plot all positions honestly relative to axes", "ensure every final point matches the table". If the data is invented, say so on the image ("fictional dataset for a design demonstration").

## STORYBOARDS AND PREVIS (GPT 2.5 Sunburst)

- Grid first: "exactly six equal rectangular panels in a strict 3 columns by 2 rows grid", gutters, borders.
- Medium: "loose graphite and dark-blue pencil on white paper" OR "untextured neutral grey polygon mesh, flat shading, as if captured from a 3D viewport before materials and lighting".
- One character, described as simple primitives so it stays identical in every panel ("circle head with two dot eyes and one bent antenna, box torso, stick-like jointed arms"). Add "maintain exact recognisable silhouette".
- Shot list per panel: number, shot size, action. Then exact labels: `"01 / WIDE", "02 / INSERT" ...`.
- Long list of what it is NOT (no colour, no texture, no cinematic lighting, no polished cartoon, no UI or software chrome) and a final purpose line: "must unmistakably read as an unfinished blocking stage".

## USING A REFERENCE IMAGE

- Say exactly which qualities to take: "Use the attached reference specifically for its DRAWING STYLE, COMPOSITION DENSITY and ...".
- "Create a new original scene, not a copy." "Ignore all screenshot buttons, arrows and UI overlays."
- Make density measurable: "around forty small figures", "at least four depth layers", "individually distinct faces and poses instead of repeated clones", "no empty sky, no large empty areas".

## PRODUCT WITH A PERSONALITY LAYER

Two layers in one prompt:
1. **Technical base:** materials, every marking with exact text and position, exact counts of knobs/switches with their labels and order, a readable screen.
2. **Personality layer:** stickers, hand tags, tape notes, wear, each with exact text, plus limits: "visually rich but not randomly dirty", "real patina of handling, no destruction", "leave the logo visible", "without crowding the serial plate". End with the intent: "one specific person's treasured device, not a pristine catalogue product".

---

## WHEN A GENERATION FAILS: FIX THE PROMPT, NOT THE LUCK

| Problem in the image | Add to the prompt |
|---|---|
| Extra or duplicated objects | Count lock: "Keep exactly one X, one Y" + name the likely duplicate in the avoid list |
| People appear | "No people, silhouettes, faces, figures" + "in windows, mirrors or reflections" |
| Random gibberish text | "No readable text, signage or logos"; decorative script -> "reads only as abstract brush forms" |
| Whole image tinted orange/teal | Neutral photographic foundation + local colours + contain each light source + "no global wash" |
| Visible lamp, skylight, god rays | "The source never visible; no fixtures, no visible beam or haze"; light described through surfaces |
| Muddy black corners | "Exposed comfortably, nothing sinks to black; shadows stay open" |
| Bent verticals, fisheye look | Exact focal length + HFOV + "distortion off, verticals straight, rectilinear" |
| Furniture pushed to the walls | "standing free of every wall", "clear floor on all sides" |
| Too clean, too neat, postcard | Numbers: figures, layers, props; "no empty areas"; "imperfect" |
| Style drift (storyboard looks finished) | "not X" in the opening + list of banned rendering traits + purpose line |
| Wrong or extra letters | Quote with "exactly", give position, close with "no additional letters or numbers"; switch to GPT 2.5 Sunburst |

Change one thing at a time and keep the rest of the prompt identical, so you can see what the change did.

## FINAL CHECKLIST

- [ ] Opening line names the medium and subject.
- [ ] Aspect ratio stated.
- [ ] Camera: position, height in m, aim, lens mm + HFOV, distortion, focus.
- [ ] Every important object has a layer and a frame position.
- [ ] Every light source named, with direction and where it stops.
- [ ] Neutral colour foundation or a closed palette.
- [ ] One capture character + tactile details.
- [ ] One mood line, no empty praise words.
- [ ] Guards: no people (incl. reflections), text policy, count locks, avoid list.
- [ ] Exact text quoted with "exactly" and closed with "no additional".
- [ ] Model matches the job (text and numbers -> GPT 2.5 Sunburst).

---

## WORKED EXAMPLES

**Compact plate** (Seedream 5.0 Pro or Nano Banana Pro, 16:9):

```
An empty photographic view of a wealthy Roman domus atrium in the first century AD: a square impluvium pool of still rainwater at the centre, red-and-ochre frescoed walls with painted columns, a black-and-white mosaic floor, a bronze brazier and two terracotta urns by the far doorway. A dark wool curtain edge hangs out of focus at frame left. Camera at 1.5m in the entrance passage looking straight down the axis toward the tablinum, 28mm spherical lens. Soft overcast daylight falling through the open roof square onto the pool, corners in cool open shade. Gentle analog grain, tactile fresco cracks, worn mosaic tesserae and wet stone. No people, human statues, readable inscriptions or modern objects.
```

**Exact text on a prop** (GPT 2.5 Sunburst, 4:3):

```
Photorealistic product photograph of one vintage amber glass apothecary bottle standing on a dark oak shelf, horizontal 4:3, bottle centred and filling two thirds of the frame height, the entire label visible and in focus. Cork stopper sealed with dark red wax. A cream paper label with a thin black double border, slightly yellowed, one corner gently lifting. On the label, top to bottom: small caps "No. 47"; large black serif "TINCTURA LUNAE"; a thin rule; italic "Night Tonic"; small text "Take three drops at dusk". Carefully reproduce all requested text in exactly this order and position; no additional letters, numbers or logos. Warm window light from the left, soft controlled reflections on the glass, the shelf behind falling into soft blur. Restrained photographic look, real paper and glass, not a flat vector mockup.
```