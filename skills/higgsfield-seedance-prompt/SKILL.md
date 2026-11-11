---
name: "higgsfield-seedance-prompt"
description: "Seedance 2.5 prompt-writing system (also valid for 2.0). Use whenever the user wants to write a Seedance prompt, build a cinematic shot or scene, turn an idea or script beat into a prompt, set up references/assets, or asks about Seedance prompting technique. Trigger on phrases like \"prompt for Seedance\", \"write a Seedance prompt\", \"make a scene where...\", \"build a shot\", \"how to write a Seedance prompt\". Output is a single standalone prompt. Always consult this skill before writing any Seedance prompt."
---

# Seedance 2.5 Prompt Writer

Turn scripts, scenes, and ideas into Seedance 2.5 prompts. Block, light, and pace each shot like a film.

**Output: always a single standalone prompt in a code block.** If the shot has visible water or other sound that will be cut in the edit (see AUDIO — SOUND DESIGN ONLY), add one short post-production note below the code block.

**Style is a variable, not a canon.** Every project picks its own look: live-action cinema and photoreal, painting, 2D and anime, 3D, anything else. Every rule here is written to work for any style; where a rule depends on the style, it says so.

**Library:** the public director's console https://a-revazyan.github.io/rezhisserskiy-pult/ (data in `data.json`) collects templates, camera moves, lighting schemes and rules from real generations. If you keep your own library of rules and camera moves, read it before the first prompt of a session and add new lessons there: text · category · project · why.

---

## MODEL CAPABILITIES

- **Duration: 4 to 30 seconds per generation.** Always state the total duration in the prompt (`DURATION: 12s`). Every timecode must fit inside it. Pick the length from the dramatic shape of the shot, not by default: a single beat is 4–6s, a scene with a turn is 8–15s, a multi-cut sequence can run up to 30s.
- **Strong English typography.** Seedance renders on-screen text in English cleanly. Titles, captions, signage, packaging, product names and end cards can be generated in-shot. Write the exact text in quotes, in English, and describe font character (serif / sans / condensed, weight, case), color, size relative to frame, position, and how it appears (fades in, types on, is printed on the object). Text in other scripts (Cyrillic etc.) is added in post, so keep it out of the prompt.
- **Omni reference.** Images, short videos and audio can all be attached and named with @tags. An image can set identity, a first frame or a composition; a short video can carry camera movement and pacing; audio can drive lip-sync. Every reference takes an element slot (in practice the user works with up to 7).

---

## CORE PRINCIPLE: WRITE THE VISIBLE

The model reacts to what can be **seen and measured**, not to mood words.

Translate every abstraction into something observable.
- ❌ "tense scene" → ✅ "man freezes, slowly clenches his fist, light only from the side, half his face in shadow"
- ❌ "cool cinematic shot of a car, epic, fast" → ✅ "low tracking shot alongside the car as it powers through a wet curve, headlights glowing, spray off the tyres, hard buffeting camera shake"

Write in plain, clear, instruction-style language. Fewer precise words beat many vague ones.

Before generating, mentally "watch" the prompt as a viewer: is everything unambiguous, is the first frame non-empty, is it clear where the subject is and where it looks, where is the light coming from.

---

## WORKFLOW

0. **Intake from imagery — the preferred mode.** The user usually comes with images, moods, a book, a feeling or a few vivid phrases, not a script. You are the screenwriter and director. Before writing:
   - research the world on the web: history, costume, everyday objects, places, genre references; turn findings into concrete on-screen details;
   - settle the style with the user: if none is named, offer 1–2 looks that grow out of the imagery and run one short test generation before the whole piece;
   - build the structure yourself: for a series, bible → script and timeline → style → character/location/prop sheets → voice-over → breakdown into generations → prompts; for a single scene, beats → shots → prompt;
   - keep the user's own image-phrases as the spine of the scene: each one becomes a key shot;
   - list everything you invented under "Invented by me" (in the user's language) so the user can veto it.
1. **Ask about Cinematic Random.** Before the first prompt of every new scene, ask whether to use it (see CINEMATIC RANDOM). Never switch it on by yourself.
2. **Read as a director.** Find the dramatic shape: where the scene turns, lands, breathes.
3. **Define continuity anchors.** Who is in frame, how they look, what they carry across cuts.
4. **Write the prompt** using the block structure below.
5. **Tag assets.** Tagging rules below.

Close gaps yourself with the strongest, most specific choice — blocking, angle, light, timing, character behavior, what is in the first frame, how it ends — and say what you invented. The model fills any gap you leave on its own, usually not the way intended. Ask only about things that change the whole piece: format, length, style, a key plot turn.

---

## ASSET TAGGING

Reference image (`@tag`) sets **appearance and identity**. Text sets **what happens** and locks critical details. Both are required.

**Tag naming:**
- If the user specifies tags as `@tag_name`, use those.
- If no tags are specified, name them by load order of the supplied assets: `@image1 @image2 ...` for images, `@video1 @video2 ...` for videos, `@audio1 @audio2 ...` for audio.
- Otherwise follow the user's explicit instruction.

**Reference + text rule:** keep the character description minimal — long appearance text conflicts with the image and degrades it.

```
@TAG: age + role/build + current state + unique visible features + action-critical details + voice (only if it has a line). 100% matches the reference.
```

State critical details (small text, logos, color) in words even if they appear on the reference — the model can drop them.

Never place an `@tag` in a shot where that object is not present; the model will try to force it into frame.

Before launch, remind the user to check that every `@tag` in Higgsfield is picked from the @ list and carries its element ID. A tag left as plain text means the element is not attached; a generation failing in its last seconds is more often this than the filter.

---

## REFERENCE FRAMES AND THE ANGLE LIBRARY

The user may send "top frames" they want in the scene: stills from films, paintings, music videos, or short clips of a camera move. For each one choose a path and say which:

**A. Attach it as a Seedance reference.**
- A still → first frame or composition: `@image3 sets the first-frame composition and camera angle only; characters and style come from their own references.`
- A 3–5s clip → camera move: `@video1 is a camera reference only: replicate its camera movement and pacing.`
- Always state the job of the reference, because a still drags its own style and content along. Never contradict a camera clip in text (writing "static" over a push-in clip makes the render wobble). Set the generation length close to the clip length. Count the slot.

**B. Translate it into text** (default when the frame's style differs from the project or slots are full): camera position and height, FOV from the anchor table, the move and its speed in km/h, what sits in foreground / midground / background, and the frame the move ends on.

**Angle library.** Before writing the CAMERA block, check your angle library for a move that fits (the console's «Движения камеры» section is one: each card gives the move, a prompt phrase with scene-specific parts in [brackets], FOV, speed, and in which style it was proven). A move proven in one style is a candidate in any style: reuse the move, re-word only its style-bound camera words (see DYNAMICS). When a move works in a generation, add it to your library: name · what the viewer sees · bracketed prompt phrase · FOV · speed · style · notes.

---

## CONTEXT ISOLATION

Each generation is a blank slate — **no memory of previous shots.** A prompt is a sealed single-shot document.

Do not carry in: scene numbers, script headings, summaries of prior scenes, unused tags/characters, "as above / continues" phrasing, or people and props from a previous line that are not needed in this shot.

---

## STYLE — DISTRIBUTED, NOT A PREFIX

There is **no separate style-prefix block at the top of the prompt.** Style is not one thing in one place — it is a set of aspects, and each aspect lives in the block that already governs it, where it is most effective and unambiguous. State the target look, never what to avoid; adapt every line to this specific scene.

Cover these aspects, each in its home block:

| Aspect | Lives in | What to write |
|--------|----------|---------------|
| Lighting | **LIGHTING** | source, direction, exposure, key/fill, haze for THIS scene |
| Color / grade | **COLOR GRADE** (own block if grade is strong, e.g. teal-cyan desaturated) or folded into **LOCATION** + **LIGHTING** for a naturalistic look | palette as material + light beam + role, never a flat list |
| Lens / optical character | **OPTICS** | FOV°, rectilinear/anamorphic, prime-lens character, motion-blur |
| Camera body / tonal character | **CAMERA** | tonal latitude, highlight roll-off, color science — as a look, not a model name |
| Skin / micro-realism | **PERFORMANCE** (or inside **ACTION**) | pore-level realism, capillary flush, living eyes, catch-lights, visible breath |
| Acting | **PERFORMANCE** (or inside **ACTION**) | micro-pauses, precise eye-line, restraint, muscle-level emotion |
| Physics realism | **PHYSICS** | gravity, inertia, mass, contact shadows, fluids, particles |
| Composition / blocking | **FIRST FRAME / BLOCKING** | framing rule for THIS scene; everyone moving from frame one |
| Continuity | **POSITIVE LOCKS** | characters, props, environment identical across cuts |
| Wardrobe | **WARDROBE** (own block when costume matters) | material + condition, scene-logical |
| Format / resolution / grain / fps / bitrate | **STYLE** + **OUTPUT SETTINGS** at the **end**, just before LOCKS | 8K, photoreal, anamorphic, fine grain, real-time vs slow-mo per segment |

**Placement principle:** descriptive style (light, color, optics, physics, acting) sits *inside the content block it describes*, in the body of the prompt. Technical/format style (resolution, grain, fps, bitrate, overall look reference) sits as a **suffix stack at the end** (`STYLE`, `OUTPUT SETTINGS`), right before `POSITIVE LOCKS`. Nothing style-related goes at the very top — the prompt still opens on `SCENE CONTEXT` and `ACTIVE REFERENCES`.

Use only the aspects the shot needs. A naturalistic single take may have no `COLOR GRADE`, `WARDROBE`, or `OUTPUT SETTINGS` block at all and fold those notes into LIGHTING and POSITIVE LOCKS. A graded, multi-segment piece earns the full suffix stack.

If the user supplies their own prefix or block text, use it verbatim.

---

## PROMPT STRUCTURE

Write blocks in this order. Logic: context and references first, then space and timing, then action and physics, then the descriptive-style blocks in their home positions, and a technical-style suffix at the end. Use only the blocks the shot needs; drop the rest.

```
SCENE CONTEXT
[1–2 sentences: what happens, where, when. Geo-positions of characters.]

ACTIVE REFERENCES
[@tag + minimal anchor of critical details + "100% matches the reference"]

LOCATION MAP
[Foreground / midground / background, where the camera is, where light comes from, movement paths. Naturalistic color can live here.]

FIRST FRAME / BLOCKING
[Who is where in the first frame: positions, orientation, gaze. Composition rule for this scene.]

FORMAT MODE
[DURATION: Ns (4–30s). Then choose the level of control the shot needs:
 - Single continuous shot — "one continuous shot, the camera does not cut on its own."
 - Sequence of cuts, no timecodes — "CUT 1 … CUT 2 … CUT 3", described in order.
 - Timed multishot — explicit HARD CUTs at stated seconds.]

OPTICS
[Shot size + FOV per segment + lens/optical character. For multishot add "no drift mid-segment".]

CAMERA
[Operator behavior: height, distance, movement, focus. Camera-body tonal character as a look.]

ACTION
[Events at the precision the shot needs. Camera motion and subject motion stated separately.]

PERFORMANCE        (when acting matters)
[Acting + skin/micro-realism: muscle-level emotion, eye-line, catch-lights, breath, pore-level detail.]

PHYSICS
[Mass, inertia, contact, fluids, particles.]

LIGHTING
[Source, direction, exposure — priority block.]

COLOR GRADE        (when the grade is strong / stylized)
[Palette as material + light + role; grade character. Omit for naturalistic looks — fold color into LOCATION/LIGHTING.]

WARDROBE           (when costume matters)
[Material + condition, scene-logical.]

ON-SCREEN TEXT     (when there is typography)
[Exact English text in quotes + font character, color, size, position, how it appears.]

AUDIO
[Sound design only — diegetic effects, foley, room tone, the needed line. No music score. See AUDIO — SOUND DESIGN ONLY.]

STYLE              (technical-style suffix)
[Overall look in words, photoreal, format, grain — no director or equipment names.]

OUTPUT SETTINGS    (when format must be pinned)
[Resolution, anamorphic, real-time vs slow-mo per segment.]

POSITIVE LOCKS
[Short fixers against likely failures, in positive form, restating critical info once. Continuity lives here.]
```

The descriptive-style blocks (PERFORMANCE, PHYSICS, LIGHTING, COLOR GRADE, WARDROBE) sit in the body next to what they govern. The technical-style blocks (STYLE, OUTPUT SETTINGS) form a short suffix stack just before POSITIVE LOCKS. Nothing style-related opens the prompt.

A **lock** is a short hard fixer placed next to what it protects, e.g. `"headlights stay glowing in every shot"`. Write densely where control matters, sparsely where it does not. Say each important thing once, clearly.

---

## CUTS AND TIMING

Pick the precision the shot actually needs — these are points on a scale, not a binary:

- **Single shot (oner)** → "one continuous shot, the camera does not cut on its own."
- **Sequential cuts, no timecodes** → describe shots in order as `CUT 1 … CUT 2 … CUT 3`. Use when you want specific cuts but exact timing does not matter.
- **Timed multishot** → explicit HARD CUTs at stated seconds. Use when beats must land on a clock.
- **Freestyle b-roll** → do not lock cuts; let the model find angles.

When you specify cuts (timed or not), lock that the camera does not add its own: *"cuts only at the specified points, the camera does not cut on its own."*

Total length is 4–30s; all timecodes fit inside the stated DURATION.

**Timecode format** (only when timing matters):
```
0.0s to 1.0s — [description]
1.0s HARD CUT
1.0s to 3.0s — [description]
```

**Sequential format** (cuts without timecodes):
```
CUT 1 — [description]
CUT 2 — [description]
```

**Cut types:** `HARD CUT`, `SMASH CUT`, `MATCH CUT`, `INSERT CUT`, `REVERSE CUT`, `WHIP CUT`. Fades / crossfades only if explicitly requested.

Across internal cuts hold: same character set, same geometry, screen direction, gaze, light, wardrobe, prop state.

---

## DIRECTING

**Blocking.** State where each character stands, sits, moves; what their hands do; what sits between them. "She sits across from him at the diner booth, knees touching under the table" beats "they sit and talk."

**Pace.** Read the dramatic structure. Confession scene → air, held shots, beats of silence. Action → compression, short cuts. A reveal lands on one held close-up.

**Acting.** Translate emotion into concrete on-shot direction:
- ❌ "she looks sad" → ✅ "her eyes drop to the table, jaw tightens, she swallows once before answering"
- ❌ "he is angry" → ✅ "knuckles whiten on the glass, breath shortens, eyes never leave hers"

Restraint by default — a whisper out-acts a shout most of the time.

**Continuity** (hold in mind, do not write as a block): state carried forward (wet/dry/bloodied), appearance not drifting, emotional carry from the previous scene, one time-of-day and weather unless the location changes.

**Camera language.** Be concrete: FOV°, height, movement, motivation. Motivate every camera move.
- "Low-angle 18° dolly-in, slow push from waist to chest as she realizes."
- "Static 47° two-shot, eye-level, locked off — lets the silence sit."
- "Handheld 63°, follow from behind — camera lags half a beat."

---

## DYNAMICS — DEFAULT ENERGY

This skill defaults to dynamic, complex shots, in every style. High energy is the default; calm, held shots are the exception the user asks for.

- **The camera visibly moves in every shot**: arc, crane, track, fly-over, push into a detail, passage through foreground layers. Never write "static" or "slow push-in 5%" on its own.
- **Compound moves are welcome**: push through a crowd → crane up over helmets → reveal; fast push from a medium group shot into an extreme close-up of an eye; low fly-over between objects with a lift over an edge at the end.
- **Everyone acts**: the moment between movements, busy hands, each extra with a small action of their own. The background lives: birds, petals, crowd, glints, ripples.
- **Shots of 3–6s**, frequent cuts. An important action gets its own shot, size and timecode; a small detail inside a wide shot gets dropped.
- **Composition**: diagonal lines, foreground layers, nothing square-on and symmetrical.
- **Energy-killing words** — avoid unless calm is the point: slow and weighty, held compositions, lazy, half-closed eyes, without blinking, steady, motionless.
- **Massive objects in motion** (a raft, a ship, a train): show the motion through the background sliding past the characters, not through a wide exterior shot — those glitch.

**Camera language follows the style.** The move itself (arc, crane, push-in) is style-neutral; the words that describe it carry a style. Before every prompt check that the camera words do not pull toward another look:
- **Live-action, photoreal:** living camera is welcome — handheld, slight shake, foreground blur rushing past the lens, focus pulls, motion blur — plus the REALISM rules below.
- **Painting, illustration:** fast but smooth moves; deep focus, everything sharp as on a canvas; light described the way a painter models it. Handheld, shake and bokeh flip the image to live-action film.
- **2D, anime:** animation language — shot-size changes on the beat, sharp angles, parallax of background layers; characters exactly as on their sheets. Avoid words the model turns into a blow (sparks, hit, impact, crash) unless a blow is wanted.
- **A new style:** make the first generation a short test, decide from it which camera words the style holds, and record that in the project's rules.

---

## CINEMATIC RANDOM — ONLY WITH CONSENT

A mode in which the camera decisions are rolled at random from fixed pools instead of chosen by taste: every pool item is already cinematic, and different rolls give different signatures. Adapted from the open-source cinedance-lite skill (Higgsfield Academy, course 01, lesson 6; MIT licence, see NOTICE.md) to the rules of this skill.

**Ask every time, never switch it on yourself.** Before the first prompt of every new scene ask one short question, in Russian, with AskUserQuestion when available: «Cinematic Random для этой сцены?» — options «Нет», «Только камера», «Полный». Offer «Полный» only when the input is a mood or a genre with no script, characters or references. Revisions of a prompt keep the answer given for that scene. When the user is not there to answer, write the scene without it and say so.

**Two variants.**
- **Только камера** (project scenes). Roll AXES 2–6 only. Format, STYLE, COLOR GRADE, characters, @tags, script and every rule of this skill stay as the project has them. Put the rolls into FORMAT MODE, OPTICS, CAMERA and FIRST FRAME of the normal block structure.
- **Полный** (mood or genre only). Roll all ten axes, leave the content to the model and write the FULL-RANDOM FRAME below instead of the block structure.

**How to roll.** Roll with code (for example Python's `random`), not in the head, and never pick by taste. For the look axes (7–9 and 10) first check the user's line for vibe words in either language; a match narrows the pool, no match rolls the whole pool. Do not narrate the rolls inside the prompt; list them in the Russian breakdown so the user sees what fell.

**AXIS 1 · FORMAT** (Полный only; set the same aspect in Higgsfield, 21:9 when offered, otherwise the nearest one with the look described in STYLE)
2.39:1 widescreen with an anamorphic look (oval highlights, horizontal flares) · 1.43:1 large-format look with huge resolving detail · 1.85:1 classic theatrical widescreen · 4:3 with coarse visible film grain · 2.76:1 ultra-wide epic frame · 1:1 square with a still-film look · 9:16 vertical with an anamorphic look · 1.66:1 European widescreen with fine grain. All at 24 fps with natural motion blur.

**AXIS 2 · FIELD OF VIEW** (steps from the FOV anchor table)
107° ultra-wide · 84° wide · 63° observational · 47° neutral · 29° portrait compression · 18° compressed portrait · 12° tele-detail · 180° fisheye · a probe 84° wide lens a few centimetres from a small surface · a tilt-shift miniature look.

**AXIS 3 · HEIGHT AND RIG**
a few centimetres off the ground · low, looking up · eye level, with the level broken by composition · high, looking down · straight top-down · a crane sweeping across the space · a dive from high above · rigged to the subject, which stays fixed in frame while the world swings behind it · a perfectly smooth floating glide · handheld with a living shake.

**AXIS 4 · MOVEMENT** (no locked-off camera: dynamic is the default)
slow push forward at 1 km/h · fast push forward at 7 km/h · orbit around the subject at 3 km/h · crane rise · crane fall · a whip-pan chain across three subjects · snap zoom in · dolly-zoom (the background stretches while the subject holds its size) · diving descent · lateral arc · sprinting alongside at 15 km/h · pushing through a foreground object into the scene.

**AXIS 5 · COMPOSITION BREAK** (roll two; one if the scene is a single shot)
subject at 5% of the frame · subject overflowing the frame edges · pushed to the left third · pushed to the right third · pushed to the top edge · pushed to the bottom edge · dutch tilt 15° · dutch tilt 30° · radical centered symmetry · radical asymmetry off the edge · framed through an aperture (window, gap, doorway) · seen only in a reflection · a rack-focus reveal from the foreground to the subject.

**AXIS 6 · SHOT COUNT**
1 · 2 · 3 · 4 · 5 · 6 · 8 shots.

**AXIS 7 · GRADE** (Полный only; Только камера keeps the project's grade)
neon-noir · storm-desaturated · ember-night · cool daylight · warm tungsten · pastel drift · flat log · bleach bypass · teal-orange · monochrome black and white · saturated primaries · desaturated except one colour · day-for-night · gold-hour amber.
Vibe bias: noir, dark, lowkey / нуар, тёмный → neon-noir, ember-night, monochrome · colorful, vibrant / яркий, сочный → saturated primaries, teal-orange, gold-hour amber · neon / неон → neon-noir · pastel, dreamy / пастель, мечтательный → pastel drift, flat log · bleak, gritty / суровый, грязный → storm-desaturated, bleach bypass · warm, sunset / тёплый, закат → warm tungsten, gold-hour amber · cold, clinical / холодный, стерильный → cool daylight, flat log.

**AXIS 8 · CONTRAST** (Полный only)
pushed high with crushed blacks · flat log · soft lifted blacks · high-key bright · low-key deep shadow · silhouette-heavy.
Vibe bias: lowkey, noir, silhouette / нуар, силуэт → low-key, silhouette-heavy · bright / светлый → high-key · muted, washed / приглушённый → soft lifted blacks · punchy, contrasty / контрастный → pushed high.

**AXIS 9 · ATMOSPHERE** (Полный only)
dust · smoke · steam · rain · snow · sand · spores · volumetric god-rays · fog · underwater · a clear vacuum · flat clear air.
Vibe bias: underwater / под водой → underwater · space, void / космос → clear vacuum · desert / пустыня → dust, sand · rain, storm / дождь, шторм → rain · snow, arctic / снег → snow · fog, mist / туман → fog, steam · smoke / дым → smoke · magic, ethereal / магия → god-rays, spores · noir / нуар → smoke, fog, rain.

**AXIS 10 · ESCALATION** (Полный only)
quiet → loud · loud → quiet · plateau · circular · descending · fragmented montage.
Vibe bias: chase, fight, battle / погоня, бой → quiet → loud, montage · contemplative, still / созерцание → plateau, descending · journey, travel / путешествие → montage, quiet → loud · climax, finale / кульминация, финал → quiet → loud · aftermath / после, развязка → loud → quiet, descending.

**Coherence (fix after rolling, re-roll only the newer element):**
- Shot count above DURATION ÷ 3 → re-roll the count (shots stay 3–6 s).
- Painting, illustration or 2D project → re-roll handheld shake, tilt-shift, rack-focus reveal and anamorphic flares: they flip the image to live-action (see Camera language follows the style).
- Top-down height → that shot has no foreground layer, or re-roll the height.
- Underwater with dust, sand or smoke, or a clear vacuum with rain or snow → the vibe-driven value wins, otherwise re-roll the atmosphere.
- Rain or underwater → AUDIO names no water sounds; add the post note.

**Human-anchor scrub (Полный only).** The model invents who and what is in the world, so outside the user's own line the prompt names no body: no protagonist, character, hero, body, face, hand, fingers, arm, leg, foot, head, eye, breath, skin, hair, mouth, voice, walking, running, punch, grab. Use agnostic words instead: whatever is or isn't in it, close detail, something contacting / releasing / settling / arriving / breaking / opening / folding, surfaces, motion, atmosphere.

**FULL-RANDOM FRAME** (Полный; fill the placeholders, first line is the user's line verbatim, in English)
```
<USER LINE>

Invent the world, whatever is or isn't in it, and what happens: something no one has shot before. Hold whatever you invent from the first frame to the last: one world, one grade, one screen direction, one continuous <ESCALATION NOUN>.

<SHOT COUNT>, hard cuts on movement inside one continuous world. Let the scene <ESCALATION VERB>: it starts somewhere quiet and ends somewhere the first frame could not predict.

The frame is <FORMAT>. Primary field of view: <FOV>. The camera lives <HEIGHT>, never level with what it looks at; the frame is off-centre unless the composition calls for radical symmetry.

Composition breaks at least once per shot: <BREAKS>. Negative space runs 90/10 or 10/90. Any horizon line is tilted. On at least half the shots a foreground layer sits 5–40 cm from the lens: a shard, a leaf, dust, a fragment, whatever the invented world contains. Three depth layers at all times.

Camera moves are physical and motivated. Primary movement: <MOVEMENT>. Every cut and every camera event is tied to a visible physical event in frame: something contacting, releasing, settling, arriving, breaking, opening, folding, a shift in light, a surface giving way. One unexpected choice per shot: a lens, an angle, a move, a foreground object.

Atmosphere does real work: <ATMOSPHERE> carries every beam of light. Wet surfaces reflect the practical lights; halation blooms where light burns through the air. One motivated key light per shot and one grade for the whole scene: <GRADE>. Contrast: <CONTRAST>. One bright specular point the eye lands on.

Physics is heavy and real: mass, momentum, inertia, follow-through. Whatever moves is pushed by something visible and settles somewhere visible; every change of state is continuous. Cloth, membrane or foliage whips in the wind; particles hang in the air after something disturbs them; fragments arc and come to rest where physics puts them.

The soundtrack is diegetic sound only: an environmental bed and five to eight named sound effects tied to physical events in frame: surfaces, motion, atmosphere, distant echo, wind, metal, or their non-earthly equivalents.

Inside this frame, go wild: one world, one grade, one screen direction, one continuous <ESCALATION NOUN>.
```
Escalation words: quiet → loud = escalation / escalate · loud → quiet = subsiding / subside · plateau = plateau / hold · circular = circle / return to where it began · descending = descent / descend · fragmented montage = montage / fragment and jump. Shot count: «A single continuous shot», «Two shots», «<N> shots».

**Run protocol.** Duration 15 s for drafts unless the user set one. Leave the seed empty. Three cheap drafts at the lowest resolution offered, the user picks one; for the final, reuse that draft's seed if Higgsfield shows it, otherwise upscale the chosen draft instead of rolling again (credits). The negative field, when there is one, lists only render artifacts: morphing, warping, flicker, duplicated subject, extra limbs, distorted face, subtitles, watermark.

---

## REALISM: LIGHT, ANGLE, POSE

Scope: live-action and photoreal looks. For painted, animated or other stylized looks, take only the pose rules (section 3); skip the hard side key, the handheld "operator miss" and lens compression, and describe light in the style's own terms.

By default the model makes three choices that read as "AI": flat frontal light, a centered eye-level camera, and posed bodies with no weight. Override all three in every shot with people, unless the user asks for a stylized look.

**1. Light — one hard source from the side.**
- The model's default is frontal fill light, which makes skin look plastic. Write a single hard key from the side, remove the extra sources.
- Check three points on the face: **cheekbone, tip of the nose, lower lip** — the key catches exactly these, the rest falls into shadow.
- **The nose shadow falls to the side and down**, asymmetric across the face.
- Write it into LIGHTING: `"single hard key light from camera-left at 70°, above eye level; highlights land on the cheekbone, the tip of the nose and the lower lip; the nose casts a shadow sideways and downward across the cheek; the far side of the face falls into deep shadow; skin shows real texture and pores."`

**2. Angle — off-axis, off-center, compressed.**
- The model's default is camera at eye level, dead center. Shift the camera 15–20° to the side of the subject's axis and slightly off eye level.
- Use portrait compression (29° FOV, the 85mm look) so the background compresses and separates.
- **Keep the face off-center in the frame** — on a third, with air on the side of the gaze. A real operator never lands the subject perfectly in the center; that slight "miss" reads as real.
- Write it into CAMERA / OPTICS / FIRST FRAME: `"camera 15–20° off the subject's axis to the right, slightly below eye level, 29° FOV, background compressed; face placed on the left third of the frame, framing slightly imperfect as if caught by a handheld operator."`

**3. Pose — the moment between movements.**
- Never ask the model to "strike a pose". Ask for **the moment between two movements**.
- **Weight shifted onto one hip / one leg**, the other leg relaxed.
- **Hands are busy**: fixing hair, holding a glass, adjusting a sleeve, touching a strap.
- **The body is heavy**: feet press into the floor, fabric and flesh respond to gravity. AI models look weightless, as if glued to the floor — write the weight in.
- Write it into ACTION / PERFORMANCE / PHYSICS: `"caught mid-transition: weight shifting onto her left hip, right knee softening; her right hand tucks a strand of hair behind her ear while the left holds a half-full glass; heels press into the floor, her body settles with real weight."`

---

## PROMPTING RULES

- **Positive only.** Describe what should happen, not what to avoid. ❌ "does not fall backward" → ✅ "stays upright, feet planted."
- **Speeds in km/h.** ❌ "fast/slow" → ✅ "moves at 40 km/h", "camera pans at 5 km/h."
- **Atmosphere in percent / meters.** ❌ "light fog" → ✅ "fog density 40%", "haze visible at 15 meters depth."
- **Atmosphere builds in steps across shots.** Shot 1: fog 20% → Shot 2: 40% → Shot 3: 60%.
- **Giant scale via human-height comparison.** ❌ "huge", "three meters tall" → ✅ "stands as tall as four humans stacked head to toe."
- **Left/right is from the camera.** "Subject moves left" = left from the camera's view.
- **Environment interaction stated physically.** Snow melts on skin, rain runs down hair, wind moves fabric.
- **Emotion through muscle movement, not labels.**

---

## OPTICS — SHOT SIZE, LENS, FOV

Two levers define "how it is shot": **shot size** and **focal length**.

### Shot sizes
| Abbr | Meaning | In frame |
|------|---------|----------|
| ECU | Extreme Close-Up | a detail: eyes, button, headlight, hand |
| CU | Close-Up | full face / one element large |
| MCU | Medium Close-Up | head and shoulders |
| MS | Medium Shot | roughly to the waist |
| WS | Wide Shot | full figure + surroundings |
| EWS | Extreme Wide | scale, location |

### Focal length (mm — for describing size while writing, not for the prompt text)
| Lens | Effect | Use for |
|------|--------|---------|
| 24–35mm wide | space, slight perspective distortion | action, immersion, wides |
| 50mm normal | natural perspective, "as the eye sees" | realism, neutral shots |
| 85mm portrait | soft bokeh, subject separated from background | portrait, emotion |
| 135mm+ tele | strong compression, "watching from afar" | observation, distance, sport |

In the prompt text use **FOV in degrees** from the table below, not millimeters.

### FOV anchor table (degrees for the prompt)
| FOV | mm equiv | Purpose | When |
|-----|----------|---------|------|
| 180° | Fisheye | spherical distortion | POV, dream-state |
| 107° | 14–16mm | architectural ultra-wide | huge interiors, epic establish |
| 84° | 20–24mm | wide | establish, group blocking |
| 63° | 28–35mm | observational | wide observation, reportage |
| 47° | 40–50mm | neutral human perspective | universal establish, medium |
| 29° | 75–85mm | portrait compression | medium-isolate, dialogue bust |
| 18° | 100–135mm | natural portrait | close-portrait, identity-preserving |
| 12° | 180–200mm | tele-detail | hands, objects, detail-on-wide |
| 8° | 300–400mm | extreme compression | observation, broadcast |

Use only the discrete steps from the table. Not "23°" — use 18° or 29°. In a multishot, set FOV per segment and add `"no drift mid-segment"`.

### Camera placement in the prompt
Place the CAMERA block in the **3rd position** of the prompt's core layers (subject → action → camera → style → constraints). Moved to the end, FOV gets ignored; moved to the front, it conflicts with identity.

---

## OPTICAL TECHNIQUES

**Observation pattern (hidden-camera effect)** — all three ingredients at once:
1. Foreground occlusion — out-of-focus obstruction over 20–30% of frame (wall, pillar, branch, arch).
2. Atmospheric haze — fog/dust/shimmer between camera and subject.
3. Distance vantage — super-tele 8°–12°, operator anchored far away.
Change the occlusion type between beats; keep the vantage single.

**Sports broadcast:** `8° super-tele + handheld 1–2cm tremor + "anchored at distance, finding the action"`.

**Detail-on-wide (snake cam):** `84° wide FOV + low-angle right up against a small object` — foreground object exaggerated, background recedes into depth.

**Intimate wide:** `63–84° wide FOV on a close face` — face centered, surroundings readable without blur.

**Tele compressed air column** at 8°–12°: `"dust suspended in the long compressed air column between camera and subject"`, `"heat shimmer compressed into a wall of haze in front of the figure"`.

---

## SPECIAL PROTOCOLS

**4-mechanism multishot consistency stack (extreme FOV: 8°, 107°):**
1. Sequence-wide identity lock — single location reference across all beats.
2. LENS LOCK opener — explicit FOV phrase at the start of each beat.
3. LENS CHECK closer — confirm FOV at the end of the beat.
4. Color via material + light, not as a list.
All four are required, or extreme-FOV multishots break down after 2–3 beats.

**Whip-pan timing:**
```
0.3s — Subject A settled
0.8s — WHIP motion-blur transition
1.4s — Subject B settled
```
A whip under 0.8s renders as a hard cut without blur.

**Mixed time-speed (real-time + slow-mo):** hard cuts only between speed modes. Each shot is one speed start to finish.

**Cracks/breaks without impact (anti-impact lock):**
- "crowd PRESSES, not strikes"
- "fracture originates from edge stress, not center impact"
- "no impact point — pressure-based crack"
- sequential timing edge-to-center, not radial from a point.

---

## AUDIO — SOUND DESIGN ONLY

**We always make videos WITHOUT MUSIC.** Music is never written into the prompt. The AUDIO block holds only sound design: diegetic effects, foley, ambience, room tone, and dialogue when there is a line.

- Write every sound as a concrete, timed event tied to a visible action: `"1.2s — crisp click of the lighter lid; 1.5s — soft whoosh of the flame catching; constant low hum of the fridge in the background."`
- State the acoustic space: small tiled kitchen with a short echo, carpeted room with dead sound, open street with distant traffic.
- Lock it positively: `"the soundtrack is purely diegetic sound effects and room tone."`

**Water — always cut.** Seedance renders water sounds (pouring, splashing, rain, running tap, waves, drops) as synthetic, harsh, ear-cutting noise. These sounds are always cut from the video in the edit.
- Never describe water sounds in the AUDIO block, even when water is in frame. Describe only the other sounds of the shot.
- When water is visible or audible by logic of the scene, add a short note below the prompt: `"Post: cut / replace water audio in the edit."`

**Eating — write each bite.** By default Seedance plays one generic bite sound regardless of the food, and it sounds off. Always detail eating audio:
- **Number of bites and their timing**: `"first bite at 2.0s, second at 4.5s"`.
- **Sound specific to the food's texture**: crisp crunch of a fresh apple, flaky crackle of a croissant crust, soft muffled squish of cake, snap of chocolate, crackle of chips, chewy tear of bread.
- **The full sequence per bite**: teeth meeting the food → the break/tear → chewing (its rhythm and texture, mouth closed/soft) → swallowing where it is visible.
- Match sound loudness to the shot size: close-up — detailed and close; wide — quieter and blended into the room.

---

## CAMERA / LIGHT / COLOR

**White balance** in Kelvin, set to the scene mood, fixed within a scene (3200K / 4000K / 5600K / 8500K).

**Equipment:** describe the look, not gear. No camera/film/lens model names — they get ignored or break complex moves.

**Color rule:** tie color to **material + light beam + compositional role**, never a flat list.
- ❌ "the woman wears red, the man wears blue"
- ✅ "crimson silk scarf catching the cold tungsten spill from the corridor"

**Background in layers:** state foreground / midground / background separately.

**Camera on the shadow side**, with a stated operator axis.

---

## MODERATION — AVOID FALSE BLOCKS

Seedance runs two checks: one reads the prompt text and catches words; the other looks at finished frames and catches sexualized presentation.

- **Keep the framing non-sexual**: wide and medium shots; no low angles on short clothing, no close crops on the body; no tight contact (a man and a woman pressed together on one couch, food going into a mouth in close-up); wind only in hair and scarves.
- **If a generation fails in its last seconds**, first check that every `@tag` carries its element ID, then think about the filter.
- **Limits**: adults only, with ages written explicitly ("a woman of about 25", never "girl"); no sexual content; no real people.

---

## CHECKLIST (before each prompt)

- Came in as imagery? World researched, style settled with the user, structure built, invented details listed?
- New scene: asked about Cinematic Random? If used: rolled with code, coherence fixed, rolls listed in the Russian breakdown?
- Angle library checked for a fitting move? Top frames routed as reference (A) or text (B), each reference's job stated?
- Every shot has a visible camera move and everyone in it acts; shots 3–6s; key action has its own shot?
- Camera words match the project's style; no energy-killing words?
- Duration stated, within 4–30s, and all timecodes fit it?
- On-screen text (if any) in English, exact text in quotes, font / position / appearance described?
- Photoreal people in frame: one hard side key (cheekbone, nose tip, lower lip), nose shadow sideways and down?
- Photoreal: camera 15–20° off axis, 29° portrait compression, face off-center?
- Pose is a moment between movements: weight on one hip, busy hands, a heavy body?
- AUDIO is sound design only — no music?
- No water sounds in AUDIO; post note added if water is present?
- Eating: each bite timed, texture-specific sound, bite → chew → swallow?
- Moderation: non-sexual framing, every person an explicitly aged adult, no real people?
- All blocks in order: context and references first, then space/timing, then action/physics, then style in its home blocks, technical-style suffix last?
- Tags named per the tagging rule (`@tag_name`, or load-order `@image1`/`@video1`/`@audio1`, or user instruction)?
- `@tag` only in shots where the object is present?
- No style-prefix block at the top — prompt opens on SCENE CONTEXT / ACTIVE REFERENCES?
- Each style aspect placed in its home block (light→LIGHTING, color→COLOR GRADE or LOCATION, acting/skin→PERFORMANCE, format/grain→STYLE+OUTPUT SETTINGS suffix)?
- Style adapted to this scene (not generic)?
- Everything positive (no "does not X")?
- Speeds in km/h, atmosphere in %/meters, giants vs human height?
- Emotion through muscle movement, not labels?
- Left/right from the camera?
- FOV in degrees from the anchor table (not mm, not arbitrary)?
- CAMERA block in 3rd position?
- WB in Kelvin for the scene mood?
- Color via material + light + role, not a list?
- Camera on the shadow side, operator axis stated?
- Background in foreground/midground/background layers?
- Multishot: FOV per segment + "no drift mid-segment"; extreme FOV → all 4 consistency mechanisms?

---

## FINAL RULES

- **English prompts only.**
- **No music, ever** — sound design only.
- **Duration 4–30s**, always stated.
- **Positive phrasing only** — state the target, never the prohibition.
- **No director names, no signature-work references, no equipment names.**
- **Dynamic by default** — the camera moves and everyone acts in every shot.
- **Style is a variable** — rules are universal, camera words follow the project's style.
- **Invent boldly, mark what you invented.**
- **Cinematic Random only with consent** — ask at every new scene, never switch it on yourself.