---
name: "premium-landing-page"
description: "Build a polished, single-page marketing site for a company, in the tight, high-production-value visual/structural style used by base44 and awwwards/Framer-tier sites (animated stat counters, scroll-triggered motion, swipeable/tilt/spotlight/progress-driven card interactions, tilted 3D and morph-shader galleries, real WebGL/Three.js 3D heroes and spiral showpieces, clay/neumorphic medical heroes, device mockups, popups, preloaders, custom cursors). Use whenever the user asks to build, redesign, or improve a landing page, corporate site, product/catalog page, portfolio, restaurant/hotel/resort site, or \"сайт для компании\" — even without naming a template or mentioning base44. Also use when the user says a page looks \"too generic\" or \"not premium enough,\" asks for \"крутой визуал,\" \"анимация,\" \"эффекты на карточки/кнопки,\" \"3D анимация,\" \"галерея,\" \"попап,\" \"прелоадер,\" or references awwwards/Framer/Lottie/Codepen-style design."
---

# Premium Landing Page Builder

## Why this skill exists

Left alone, an LLM asked to "build a landing page" tends to produce something structurally thin: a hero, three feature cards, a CTA, no motion, no single strong visual idea. Tools like base44 do better than that baseline because they wrap the same model in a fixed section library, strict typographic rules, and a discipline of grounding copy in concrete numbers — but even that pattern, applied the same way every time, gets repetitive (a wall of stat counters and card grids on every single project, regardless of brand). Genuinely awwwards/Framer-tier sites go one level further: each one commits to a distinct **art direction** built around one dominant hero visual, plus specific, well-crafted micro-interactions on cards, buttons, and scroll — not just a structural checklist. This skill packages all four layers — structure, motion, art-direction variety, and a ready-to-use interaction library (including real WebGL 3D, not just CSS tricks) — so output doesn't default to the same look, and doesn't ship with animation only described rather than working.

The structural/copy layer was reverse-engineered from eight real base44-built sites for Russian B2B/industrial companies (cement, oil & gas, pharma manufacturing, engineering institutes, consulting, industrial services) — the section rhythm and copy discipline held across all of them. The art-direction layer was pulled from directly inspecting ~15 frames of a curated Figma collection of real award-tier landing pages. The interaction library packages dozens of specific hover/scroll/drag/load techniques sourced from real working CodePen references, each ported faithfully (not paraphrased) — vanilla JS/CSS where that's what the original used, faithful WebGL/shader/Three.js where the original technique genuinely needs it. Every technique below has a full working standalone reference file in the user's workspace named in its entry (e.g. `product-card-template.html`) — treat those as the source of truth for exact implementation details beyond the trimmed snippet inlined here.

## Process

1. **Gather the facts first.** Before writing any copy, collect concrete material about the company: what it does, founding year, facilities/locations, certifications/standards, real numbers (capacity, clients served, years of experience, % metrics), services/products, and contact info for the final CTA. Never invent specific numbers or certifications; if a fact is missing, ask or mark it `[уточнить: ...]`.

2. **Pick an art-direction archetype before picking sections.** This is the step that's easy to skip and shouldn't be — it's what actually separates a premium result from a competent-but-generic one. See "Art-direction archetypes" below, choose one (or deliberately blend two) that fits the brand's personality and industry, and let it drive the palette, the hero anchor visual, and the overall mood. Do not default to "dark background + gradient mesh + stat counters" for every project just because it's safe — that itself becomes a tell once you've made a few pages.

3. **Design one dominant hero visual anchor.** Every one of the strong reference sites has exactly one clear visual "moment" near the top of the page. Build it from what's actually reliable to produce well: an SVG line-art illustration, a believable fake UI/dashboard/phone mockup, a CSS-drawn abstract shape/gradient composition, or — for briefs that explicitly ask for something striking — a real WebGL scene from the Extended technique catalog below (scroll-video hero, particle-field hero, shape-morph scroll hero, industrial tunnel, living-photo parallax, etc.). If the brand has real product photography, a render, or a logo the user can supply, ask for it and use it instead — that will always beat a generated substitute — but don't block on it.

4. **Pick sections from the catalog below**, and check the Extended technique catalog for anything industry-specific — it now covers beauty/salon, youth/streetwear retail, minimalist IT/SaaS, industrial/drilling, jewelry/luxury, travel, and grooming/pet-care patterns directly, in addition to the general-purpose techniques in the main Interaction library.

5. **Always include, regardless of archetype:**
   - A hero with a short punchy headline naming the value proposition (not the company name), a one-sentence subhead, two CTAs (solid + outline/ghost), and the hero anchor visual from step 3.
   - A stats or trust-signal section with 3-4 concrete numbers or credibility markers, animated on scroll.
   - A final CTA section with a lead form or contact details plus a small trust microcopy line.

6. **Follow the shared design tokens:**
   - Confident, oversized display typography for the headline — this alone does more for "premium" than any amount of decoration. Don't undersize it.
   - Two-CTA pattern everywhere a decision point appears: solid primary + outline/ghost secondary.
   - Alternate section backgrounds/moods to create rhythm — never let 3+ sections in a row share the same background.
   - One primary accent color used with restraint; everything else neutral.
   - Numbered steps rendered as oversized, low-opacity numerals behind the step title, when used.

7. **Reach for a small visual flourish, not five of them.** Pill-tag lists, dashed connector lines, floating stat chips, duotone photo washes, gradient text, clay/neumorphic cards — pick one or two that match the archetype, not all at once.

8. **Give cards, galleries, and buttons a real interaction, not just a static state.** Pick one card-hover treatment and one button-hover treatment and apply them consistently, matched to the archetype and industry.

9. **Add real, wired page-level motion, not documented-but-unused motion.** At minimum: scroll-triggered fade/slide-in reveals and animated stat counters, actually written into the `<script>` tag. If the brief calls for award-tier polish, add smooth inertial scroll, a split-text hero reveal, a preloader if the hero is asset-heavy, and one hero-level effect. Respect `prefers-reduced-motion`.

10. **Build as a single self-contained file** — Tailwind via CDN, GSAP via CDN for motion, and vanilla JS, with heavier dependencies (Three.js, Swiper.js, Zdog, WebGL shaders) only when a specific technique calls for it.

11. **When porting a 3D-transform effect from any reference, double-check the `transform-style: preserve-3d` chain.** Any element between the one that has `perspective` set and the one that actually gets `rotateX`/`rotateY` needs `transform-style: preserve-3d`, or the browser flattens the rotation into a 2D squish instead of true depth.

12. **Self-review before delivering.** Does the page commit to one clear art-direction archetype? Is there exactly one strong hero visual anchor? Does every section have at least one concrete, specific number or fact? Do cards and buttons actually respond to hover/interaction, and is page-level motion wired into the code rather than just described? If any 3D transforms are involved, is the preserve-3d chain intact? If any answer is unsatisfying, revise before calling the page done.

## Art-direction archetypes

Pick one as the primary direction (blending two is fine for an unusual brief, but pick deliberately, don't default). Each includes: mood/palette, the hero anchor visual that defines it, a signature flourish, and what kind of company/brief it suits.

**A. Dark SaaS / dev-tool** — near-black background, one saturated accent color, a subtle dot/grid texture behind the hero, huge tight-tracked headline, a single clean product-UI mockup or minimal line-art illustration as the anchor, a logo/trust bar directly under the hero. Suits: software, technical services, engineering.

**B. Product-render fintech** — near-black or deep teal, a hero visual built around ONE physical product or device (isometric line-art, or the phone/device mockup from the Interaction library), a phone/app UI mockup, a press-logo trust bar. Suits: any company with a tangible flagship product, especially apps.

**C. Warm consumer / lifestyle** — warm cream, orange, or earth-tone palette, real human photography if available, star-rating or quote testimonial cards, rounded icon feature grid. Suits: consumer apps, healthcare, individual-facing services.

**D. Playful organic** — light or dark background decorated with hand-drawn-style organic blob shapes and squiggly line accents, bold condensed display headline, a colorful stat band, a dashed connector line threading through process/portfolio cards. Suits: creative agencies, marketing/design studios.

**E. Editorial dark portfolio** — near-black, an oversized pull-quote or manifesto line as the literal H1, one bold accent color, a tight grid of project thumbnails (or the tilted 3D carousel, tilt-stack carousel, rotating photo-drum gallery, or the WebGL spiral showpiece for a more dynamic gallery/hero moment). Suits: studios, portfolios.

**F. Bright abstract-3D (CSS-only)** — white/light background, ONE colorful abstract gradient blob as the sole hero visual, minimal icon+text feature row, single centered CTA. Suits: lightweight SaaS tools.

**G. Industrial B2B credibility-stack** — ticker strip of certifications, 4-stat counter grid, geography/facility map, product-category cards, quality/certification block, digital-portal dashboard mockup, ESG block; consider the snap-scroll parallax advantages slider or the raymarched WebGL tunnel/shape-morph hero from the Extended technique catalog for drilling/mining/heavy-industry briefs specifically.

**H. Neon-glow tech/security** — near-black background with soft glowing purple/blue radial gradients, an isometric 3D-style icon cluster as the hero anchor, a gradient-text treatment on 1-2 headline words, feature cards with a glowing border on hover. Suits: cybersecurity, crypto, deep-tech.

**I. Gradient-photo-wash agency** — a large real photograph with a bold color-gradient wash overlaid via `mix-blend-mode`, headline in white on top, a pill-tag row listing services, a short human-voiced intro paragraph. Suits: agencies/studios with real photography.

**J. Glass/WebGL 3D hero** — a real Three.js scene: a glass/transmission-material object floating in front of headline text rendered as a canvas texture behind it, rotating and reacting to cursor movement. Suits: briefs that explicitly ask for 3D, portfolios/studios wanting a genuine wow-factor opener.

**K. Clay/neumorphic medical-clinic hero** — light clinical grey-white background, white "clay" cards with soft dual-direction neumorphic shadows, cool blue/teal accent glows, glassmorphic pill nav, giant outline headline behind the real one, spinning curved-text badge, doctor-persona trust card. Heavily GSAP-driven. Suits: medical clinics, health-tech, telemedicine, diagnostics.

**L. Beauty/salon elegance** (see Extended technique catalog `beauty-site-template.html`) — blush/cream/gray palette, serif+script+sans type trio, marquee ticker of service words, asymmetric photo gallery with scroll reveal, elegant testimonial cards. Suits: salons, spas, cosmetics, aesthetics clinics.

**M. Streetwear/youth retail** (see `youth-shop-template.html`) — brutalist black/white, hard hover-invert, variable-width condensed display type at heavy weight, CSS subgrid product grid, sliding filter drawer. Suits: youth fashion, sneaker/streetwear shops, skate/music-adjacent brands.

**N. Bold/edgy inversion style** (see `bold-cursor-template.html`) — custom `mix-blend-mode: difference` cursor that auto-inverts against any background, magnetic hover-grow on links, high-contrast black/white. Suits: fashion, music, agencies wanting to feel fearless.

### SVG line-art hero anchor snippet (archetype A/B, no image-gen needed)

```html
<svg viewBox="0 0 400 400" class="w-full max-w-md mx-auto" fill="none" stroke="currentColor" stroke-width="1.2">
  <circle cx="80" cy="90" r="5" class="fill-current"/>
  <circle cx="220" cy="60" r="5" class="fill-current"/>
  <circle cx="320" cy="150" r="5" class="fill-current"/>
  <circle cx="140" cy="220" r="5" class="fill-current"/>
  <circle cx="260" cy="290" r="5" class="fill-current"/>
  <circle cx="60" cy="320" r="5" class="fill-current"/>
  <path class="draw" d="M80,90 L220,60 M220,60 L320,150 M320,150 L260,290 M260,290 L140,220 M140,220 L80,90 M140,220 L60,320" stroke-dasharray="800" stroke-dashoffset="800"/>
</svg>
<style>
.draw{ animation: draw 2.4s ease forwards; }
@keyframes draw{ to{ stroke-dashoffset:0; } }
</style>
```

### Isometric orbiting-icon cluster hero anchor snippet (archetype H)

```html
<div class="relative w-72 h-72 mx-auto">
  <div class="absolute inset-0 rounded-full border border-dashed border-white/15"></div>
  <div class="absolute inset-8 rounded-full" style="background: radial-gradient(circle, rgba(168,85,247,.35), transparent 70%); filter: blur(20px);"></div>
  <div class="absolute inset-0 flex items-center justify-center">
    <div class="w-20 h-20 rounded-2xl bg-gradient-to-br from-purple-500 to-blue-500 shadow-[0_0_40px_rgba(168,85,247,.6)]"></div>
  </div>
  <div class="absolute top-2 left-1/2 -translate-x-1/2 w-10 h-10 rounded-full bg-white/5 border border-white/10 backdrop-blur flex items-center justify-center">🔒</div>
  <div class="absolute bottom-2 left-1/2 -translate-x-1/2 w-10 h-10 rounded-full bg-white/5 border border-white/10 backdrop-blur flex items-center justify-center">⚡</div>
  <div class="absolute left-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-white/5 border border-white/10 backdrop-blur flex items-center justify-center">🛡️</div>
  <div class="absolute right-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-white/5 border border-white/10 backdrop-blur flex items-center justify-center">📊</div>
</div>
```

### Gradient text flourish (archetype H, use on 1-2 words max)

```html
<h1 class="text-6xl font-bold">Identity-hub is a better way to
  <span style="background:linear-gradient(90deg,#c084fc,#60a5fa); -webkit-background-clip:text; background-clip:text; color:transparent;">achieve privacy</span>
</h1>
```

### Abstract gradient-blob hero anchor snippet (archetype F)

```html
<div class="relative w-full h-80 rounded-3xl overflow-hidden">
  <div class="absolute inset-0" style="background:
    radial-gradient(circle at 20% 30%, #6ee7ff 0%, transparent 50%),
    radial-gradient(circle at 75% 20%, #a78bfa 0%, transparent 45%),
    radial-gradient(circle at 50% 80%, #fb923c 0%, transparent 55%),
    #0b0d0f; filter: blur(30px) saturate(1.3);"></div>
</div>
```

### Clay/neumorphic card snippet (archetype K)

```html
<div class="clay-card">
  <div class="font-semibold mb-1">Predictive Analytics</div>
  <p class="text-sm text-gray-500">Short description of the service.</p>
</div>
<style>
.clay-card{
  background:#ececef; border-radius:20px; padding:24px;
  box-shadow: 8px 8px 16px rgba(163,177,198,.5), -8px -8px 16px rgba(255,255,255,.8);
  transition: transform .3s ease, box-shadow .3s ease;
}
.clay-card:hover{ transform: translateY(-4px); box-shadow: 10px 10px 20px rgba(163,177,198,.55), -10px -10px 20px rgba(255,255,255,.85); }
</style>
```

### Glass/WebGL 3D hero snippet (archetype J — real Three.js, not a CSS imitation)

Full-viewport canvas hero: a glass torus-knot (swap geometry for any other Three.js shape) rotates and refracts the headline text, which is drawn onto a canvas and used as a texture behind the glass object. Reacts to cursor movement, respects `prefers-reduced-motion`, resizes responsively.

```html
<canvas id="scene"></canvas>
<h1 id="headline" class="sr-only">
  <span>Line One</span>
  <span>Line Two</span>
  <span>Line Three</span>
</h1>
<script type="importmap">
{ "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/"
} }
</script>
<script type="module">
import * as THREE from "three";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
const LINES = [...document.querySelectorAll("#headline span")].map(s => s.textContent.trim().toUpperCase());
const BG = "#e9e9e7", INK = "#111111", CAMERA_Z = 5;
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const canvas = document.getElementById("scene");
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
const scene = new THREE.Scene(); scene.background = new THREE.Color(BG);
const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100); camera.position.z = CAMERA_Z;
scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
const textCanvas = document.createElement("canvas"); const textCtx = textCanvas.getContext("2d");
let textTexture = null;
const textPlane = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), new THREE.MeshBasicMaterial({ toneMapped: false }));
scene.add(textPlane);
const glassObject = new THREE.Mesh(
  new THREE.TorusKnotGeometry(1, 0.3, 300, 48, 2, 3),
  new THREE.MeshPhysicalMaterial({ color: 0xffffff, metalness: 0, roughness: 0, transmission: 1, thickness: 0.7, ior: 1.45, dispersion: 4, envMapIntensity: 1, toneMapped: false })
);
glassObject.position.z = 2.2; scene.add(glassObject);
function drawText(width, height) {
  const dpr = Math.min(window.devicePixelRatio, 2);
  textCanvas.width = Math.round(width * dpr); textCanvas.height = Math.round(height * dpr);
  textCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
  textCtx.fillStyle = BG; textCtx.fillRect(0, 0, width, height);
  textCtx.fillStyle = INK; textCtx.textAlign = "center"; textCtx.textBaseline = "middle";
  const maxWidth = width * 0.92, maxHeight = height * 0.78, baseSize = 100, lineGap = 0.98;
  textCtx.font = `900 ${baseSize}px "Inter", sans-serif`;
  const sizes = LINES.map(l => baseSize * (maxWidth / textCtx.measureText(l).width));
  const totalHeight = sizes.reduce((s, sz) => s + sz * lineGap, 0);
  const fit = Math.min(1, maxHeight / totalHeight);
  let y = height / 2 - (totalHeight * fit) / 2;
  LINES.forEach((line, i) => {
    const size = sizes[i] * fit;
    textCtx.font = `900 ${size}px "Inter", sans-serif`;
    y += (size * lineGap) / 2; textCtx.fillText(line, width / 2, y); y += (size * lineGap) / 2;
  });
  if (textTexture) textTexture.dispose();
  textTexture = new THREE.CanvasTexture(textCanvas);
  textTexture.colorSpace = THREE.SRGBColorSpace;
  textPlane.material.map = textTexture; textPlane.material.needsUpdate = true;
}
function resize() {
  const width = window.innerWidth, height = window.innerHeight;
  renderer.setSize(width, height); camera.aspect = width / height; camera.updateProjectionMatrix();
  const visibleHeight = 2 * CAMERA_Z * Math.tan(THREE.MathUtils.degToRad(camera.fov / 2));
  const visibleWidth = visibleHeight * camera.aspect;
  textPlane.scale.set(visibleWidth, visibleHeight, 1);
  glassObject.scale.setScalar(Math.min(visibleWidth, visibleHeight) * 0.09);
  drawText(width, height);
}
const pointer = new THREE.Vector2();
window.addEventListener("pointermove", e => {
  pointer.x = (e.clientX / window.innerWidth) * 2 - 1;
  pointer.y = (e.clientY / window.innerHeight) * 2 - 1;
});
const clock = new THREE.Clock();
function render() {
  const t = clock.getElapsedTime();
  if (!reducedMotion) { glassObject.rotation.x = t*0.35 + pointer.y*0.15; glassObject.rotation.y = t*0.5 + pointer.x*0.2; }
  else { glassObject.rotation.set(0.6, 0.4, 0); }
  renderer.render(scene, camera);
}
window.addEventListener("resize", resize);
document.fonts.ready.then(() => { resize(); reducedMotion ? render() : renderer.setAnimationLoop(render); });
</script>
<style>#scene{ position:fixed; inset:0; display:block; }</style>
```

### Floating stat chip flourish (archetype B/H, overlay on hero visual)

```html
<div class="absolute -bottom-4 -right-4 bg-white rounded-xl shadow-xl px-4 py-3 rotate-[-3deg]">
  <div class="text-lg font-bold text-gray-900">$864,898,126</div>
  <div class="text-[10px] uppercase tracking-wide text-gray-400">Total volume</div>
</div>
```

### Pill-tag list flourish (archetype D/I)

```html
<div class="flex flex-wrap gap-3">
  <span class="rounded-full border border-gray-300 px-4 py-2 text-sm">Web Design</span>
  <span class="rounded-full border border-gray-300 px-4 py-2 text-sm">Branding</span>
  <span class="rounded-full border border-gray-300 px-4 py-2 text-sm">Digital Marketing</span>
</div>
```

## Section catalog

Pick 7-10 per page. Each entry: what it's for, when to use it, a copy pattern, and a snippet where the implementation is fiddly.

### 1. Hero (always include)
Headline (2 lines, states the value prop) → one-sentence subhead → two CTAs → the hero anchor visual. Headline pattern: [evocative/positional phrase] + [concrete category noun]. Not "Welcome to Mostek" but "Engineering networks that don't fail."

### 2. Marquee / ticker strip
A horizontally looping row of short uppercase tags. Sits right under the hero.
```html
<div class="overflow-hidden border-y border-gray-200 bg-gray-50 py-3">
  <div class="flex gap-8 animate-marquee whitespace-nowrap text-xs font-medium uppercase tracking-widest text-gray-500">
    <span>ГОСТ 31108-2020</span><span>·</span>
    <span>24/7 ОТГРУЗКА</span><span>·</span>
    <span>ЛОГИСТИКА ПО РФ И СНГ</span><span>·</span>
  </div>
</div>
<style>
@keyframes marquee { from { transform: translateX(0); } to { transform: translateX(-50%); } }
.animate-marquee { animation: marquee 25s linear infinite; }
</style>
```

### 3. Stats / trust numbers
3-4 big numbers, bold count-up value + small uppercase label. Never skip, never use vague numbers.
```html
<div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
  <div>
    <div class="counter text-4xl font-bold" data-target="70">0</div>
    <div class="text-sm uppercase tracking-wide text-gray-500 mt-1">млн пробирок в год</div>
  </div>
</div>
<script>
document.querySelectorAll('.counter').forEach(el => {
  const target = +el.dataset.target;
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      let cur = 0; const step = Math.max(1, target / 60);
      const tick = () => { cur = Math.min(target, cur + step); el.textContent = Math.round(cur).toLocaleString('ru-RU');
        if (cur < target) requestAnimationFrame(tick); };
      tick(); obs.unobserve(el);
    });
  });
  obs.observe(el);
});
</script>
```

### 4. Geography / facilities map
Region tags + a highlighted "selected facility" detail card.

### 5. Product / service category cards
2-4 cards: title, description, optional icon, CTA. For an e-commerce/"popular products" grid, consider the progress-driven catalog cards or the minimalist fly-to-cart cards from the technique catalogs.

### 6. Quality / trust section
Intro paragraph + 3 icon-led feature items + optional certification badge.

### 7. Digital portal / dashboard mockup
A fake-but-plausible product UI panel. Consider the phone/device mockup for app-based products.
```html
<div class="rounded-2xl border border-gray-200 shadow-xl p-6 bg-white">
  <div class="flex justify-between text-xs uppercase tracking-wide text-gray-400 mb-4">
    <span>ПОРТАЛ · ОНЛАЙН</span><span>24/7</span>
  </div>
  <div class="grid grid-cols-3 gap-4 text-center">
    <div><div class="text-2xl font-bold">12</div><div class="text-xs text-gray-500">АКТИВНЫЕ ЗАКАЗЫ</div></div>
    <div><div class="text-2xl font-bold">8</div><div class="text-xs text-gray-500">В ПУТИ</div></div>
    <div><div class="text-2xl font-bold">2 480 т</div><div class="text-xs text-gray-500">ОТГРУЖЕНО ЗА МЕСЯЦ</div></div>
  </div>
</div>
```

### 8. Numbered process steps
01 → 04, numerals large and faint behind the title. Consider the snap-scroll parallax advantages slider for a numbered "advantages" list instead of a static grid.
```html
<div class="grid md:grid-cols-4 gap-8">
  <div class="relative">
    <span class="absolute -top-4 -left-2 text-6xl font-bold text-gray-100 select-none">01</span>
    <div class="relative pt-6">
      <h3 class="font-semibold mb-1">Анализ и диагностика</h3>
      <p class="text-sm text-gray-500">Глубоко погружаемся в процессы вашего предприятия.</p>
    </div>
  </div>
</div>
```

### 9. Case study cards
Задача / Решение / Результат, ending in one big stat.

### 10. Project / reference cards
Category tag + title + location + spec line. Consider the tilted 3D carousel, tilt-stack carousel, or rotating photo-drum gallery for more than ~6 items.

### 11. Sustainability / ESG block
Big stat + short intro + 3 icon items.

### 12. Content / community section
Article/news cards + upcoming events + trust logos strip (consider the seamless partners-logo marquee).

### 13. Testimonial / rating cards
Quote + name/role + rating. Good candidate for the swipeable card stack when there are more than 3-4.

### 14. Specialist/doctor card (archetype K)
Avatar + name + title/specialty + credential line.

### 15. Final CTA (always include, always last)
A lead form or a heading + CTA button. A popup is a good option for a delayed/exit-intent version. For made-to-order/custom-product businesses, consider the quiz/wizard form from the technique catalog instead of a flat lead form.

## Motion & animation polish (page-level baseline)

**Baseline (apply to every page, wire it into the actual `<script>`, don't just describe it):**

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
gsap.registerPlugin(ScrollTrigger);
gsap.utils.toArray('.reveal').forEach(el => {
  gsap.from(el, { opacity: 0, y: 40, duration: 0.8, ease: 'power2.out',
    scrollTrigger: { trigger: el, start: 'top 85%' } });
});
gsap.utils.toArray('.reveal-stagger').forEach(container => {
  gsap.from(container.children, { opacity: 0, y: 30, duration: 0.6, stagger: 0.12, ease: 'power2.out',
    scrollTrigger: { trigger: container, start: 'top 85%' } });
});
</script>
<style>
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
</style>
```

**Smooth / inertial scroll:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/lenis/1.1.13/lenis.min.js"></script>
<script>
const lenis = new Lenis();
function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
requestAnimationFrame(raf);
lenis.on('scroll', ScrollTrigger.update);
</script>
```

**Lottie animation:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
<div id="hero-lottie" style="width:320px;height:320px;"></div>
<script>
lottie.loadAnimation({ container: document.getElementById('hero-lottie'),
  renderer: 'svg', loop: true, autoplay: true, path: 'URL_TO_LOTTIE_JSON' });
</script>
```

## Interaction library (drop-in code for cards, galleries, buttons, hero, nav, popups)

Pick one card treatment and one button treatment that fit the chosen archetype, plus the page-level baseline — don't stack the whole library onto one page.

### Cards & galleries

**Tilt-on-hover** — subtle depth, fits archetypes A, B, H.
```html
<div class="tilt-card ...">...</div>
<script>
document.querySelectorAll('.tilt-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;
    const y = (e.clientY - r.top) / r.height - 0.5;
    card.style.transform = `perspective(800px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) scale(1.02)`;
  });
  card.addEventListener('mouseleave', () => { card.style.transform = 'perspective(800px) rotateY(0) rotateX(0) scale(1)'; });
});
</script>
<style>.tilt-card{ transition: transform .3s ease; will-change: transform; }</style>
```

**Spotlight border** — premium/tech feel, pairs with dark cards in archetype A/H.
```html
<div class="spotlight-card relative overflow-hidden rounded-2xl border border-white/10 bg-white/[0.02] p-6">
  <div class="spotlight pointer-events-none absolute inset-0 opacity-0 transition-opacity duration-300"></div>
</div>
<script>
document.querySelectorAll('.spotlight-card').forEach(card => {
  const glow = card.querySelector('.spotlight');
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    glow.style.background = `radial-gradient(300px circle at ${e.clientX-r.left}px ${e.clientY-r.top}px, rgba(168,85,247,.15), transparent 70%)`;
    glow.style.opacity = 1;
  });
  card.addEventListener('mouseleave', () => { glow.style.opacity = 0; });
});
</script>
```

**Simple lift-and-shadow** — the safe, versatile default.
```css
.lift-card{ transition: transform .25s ease, box-shadow .25s ease; }
.lift-card:hover{ transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0,0,0,.12); }
```

**Clay/neumorphic card (archetype K)** — see snippet under "Art-direction archetypes" above.

**Progress-driven catalog cards (Swiper-based)** — for "popular products" grids: cards scale/fade by scroll position, image parallax-slides and rotates, title masks in/out. Needs Swiper.js. Reference: `product-card-template.html`.
```js
const swiper = new Swiper(".swiper", { watchSlidesProgress: true, speed: 1000, grabCursor: true,
  on: { progress(swiper) { swiper.slides.forEach(slide => {
    const p = slide.progress; if (p < -1 || p > 1) return; const abs = Math.abs(p);
    slide.querySelector(".pc-card").style.transform = `scale(${1 - abs * 0.2})`;
    slide.querySelector(".pc-card__img").style.transform = `translate3d(${p * -100}px,0,0) rotate(${abs * 15 - 15}deg)`;
  }); } } });
```

**Tilt-stack card carousel** — active card full-width flat, others collapse to slivers and tilt in 3D. Reference: `case-card-template.html`. Fits agency/hospitality "our work"/"rooms" reels.

**Swipeable card stack (Tinder-style deck)** — for testimonials/comparisons.
```html
<div class="swipe-stack relative w-80 h-96 mx-auto">
  <div class="swipe-card absolute inset-0 rounded-2xl bg-white shadow-xl p-6 cursor-grab active:cursor-grabbing">Card 1</div>
</div>
<script>
document.querySelectorAll('.swipe-stack').forEach(stack => {
  let card = stack.querySelector('.swipe-card'); let startX = 0, dx = 0, dragging = false;
  card.addEventListener('pointerdown', e => { dragging = true; startX = e.clientX; card.setPointerCapture(e.pointerId); });
  card.addEventListener('pointermove', e => { if (!dragging) return; dx = e.clientX - startX;
    card.style.transform = `translateX(${dx}px) rotate(${dx * 0.05}deg)`; });
  card.addEventListener('pointerup', () => { dragging = false;
    if (Math.abs(dx) > 120) { card.style.transition = 'transform .4s ease';
      card.style.transform = `translateX(${dx > 0 ? 600 : -600}px) rotate(${dx * 0.1}deg)`;
      setTimeout(() => card.remove(), 400);
    } else { card.style.transition = 'transform .3s ease'; card.style.transform = 'translateX(0) rotate(0)'; }
    dx = 0; });
});
</script>
```

**Horizontal drag-to-scroll carousel** — lighter option for a logo/case-study row.
```css
.carousel{ display:flex; gap:1.5rem; overflow-x:auto; scroll-snap-type:x mandatory; scrollbar-width:none; }
.carousel > *{ scroll-snap-align:start; flex:0 0 auto; }
```

**Tilted 3D coverflow carousel** — active card centered/flat, rest fan out in 3D and blur. Both `.tc-track` and `.tc-card` need `transform-style: preserve-3d`. Reference: `tilted-carousel-template.html`.

### Buttons

**Magnetic button:**
```js
document.querySelectorAll('.btn-magnetic').forEach(btn => {
  btn.addEventListener('mousemove', e => {
    const r = btn.getBoundingClientRect();
    const x = (e.clientX - r.left - r.width/2) * 0.3;
    const y = (e.clientY - r.top - r.height/2) * 0.3;
    btn.style.transform = `translate(${x}px, ${y}px)`;
  });
  btn.addEventListener('mouseleave', () => { btn.style.transform = 'translate(0,0)'; });
});
```

**Ripple on click:**
```html
<button class="btn-ripple relative overflow-hidden rounded-full bg-black text-white px-8 py-4">Оставить заявку</button>
<script>
document.querySelectorAll('.btn-ripple').forEach(btn => {
  btn.addEventListener('click', e => {
    const r = btn.getBoundingClientRect(); const ripple = document.createElement('span');
    ripple.style.cssText = `position:absolute;border-radius:50%;background:rgba(255,255,255,.5);
      width:20px;height:20px;left:${e.clientX-r.left-10}px;top:${e.clientY-r.top-10}px;
      transform:scale(0);animation:ripple .6s ease-out;pointer-events:none;`;
    btn.appendChild(ripple); setTimeout(() => ripple.remove(), 600);
  });
});
</script>
<style>@keyframes ripple{ to{ transform:scale(8); opacity:0; } }</style>
```

**Fill-sweep hover:**
```html
<a class="sweep-btn relative inline-block px-8 py-4 rounded-full border border-black overflow-hidden group">
  <span class="absolute inset-0 bg-black -translate-x-full group-hover:translate-x-0 transition-transform duration-300"></span>
  <span class="relative group-hover:text-white transition-colors duration-300">Смотреть каталог</span>
</a>
```

### Hero / full-page

**Split-text reveal:**
```html
<h1 id="split-heading">Инженерные сети без сбоев</h1>
<script>
const el = document.getElementById('split-heading');
el.innerHTML = el.textContent.split(' ').map(w => `<span class="inline-block overflow-hidden"><span class="inline-block translate-y-full">${w}&nbsp;</span></span>`).join('');
gsap.to('#split-heading span span', { y: '0%', duration: 0.8, stagger: 0.06, ease: 'power3.out', delay: 0.2 });
</script>
```

**Cursor-follow spotlight background:**
```html
<div id="hero-spotlight" class="pointer-events-none absolute inset-0"></div>
<script>
document.querySelector('.hero-section').addEventListener('mousemove', e => {
  const r = e.currentTarget.getBoundingClientRect();
  document.getElementById('hero-spotlight').style.background =
    `radial-gradient(400px circle at ${e.clientX-r.left}px ${e.clientY-r.top}px, rgba(255,90,31,.15), transparent 70%)`;
});
</script>
```

**Snap-scroll parallax advantages slider** — full-viewport vertical slider, Lenis+Snap+GSAP ScrollTrigger. Reference: `advantages-slider-template.html`.

**WebGL spiral hero (creative-profession showpiece)** — Three.js helix ribbon with infinite UV-scroll texture. Reference: `spiral-template.html`.

**Fullscreen slider with WebGL morph transition** — noise-thresholded organic crossfade between slides. Reference: `fullscreen-slider-template.html`.

**Phone/device mockup with screenshot** — tilted CSS phone frame, floats and straightens on hover. Reference: `phone-mockup-template.html`.

**Glass/WebGL 3D hero (archetype J)** — see full snippet under "Art-direction archetypes" above.

### Navigation

**Shrink/condense on scroll:**
```js
const nav = document.querySelector('nav');
ScrollTrigger.create({ start: 'top -80', onUpdate: self => nav.classList.toggle('nav-scrolled', self.scroll() > 80) });
```
```css
nav{ transition: padding .3s ease, background-color .3s ease; }
nav.nav-scrolled{ padding-block: .75rem; background: rgba(11,13,15,.8); backdrop-filter: blur(8px); }
```

**Glassmorphic floating pill nav (archetype K):**
```css
nav.pill-nav{ background: rgba(255,255,255,.6); backdrop-filter: blur(12px); border-radius: 999px; border: 1px solid rgba(255,255,255,.4); box-shadow: 0 8px 30px rgba(0,0,0,.06); }
```

### Popups / modals

**Backdrop-blur popup with spring entrance** — Reference: `popup-template.html`.
```css
.popup-overlay{ position:fixed; inset:0; display:flex; align-items:center; justify-content:center;
  background:rgba(6,7,10,.6); backdrop-filter:blur(14px) saturate(140%);
  opacity:0; visibility:hidden; pointer-events:none; transition:opacity .35s ease, visibility 0s linear .35s; }
.popup-overlay.is-open{ opacity:1; visibility:visible; pointer-events:auto; transition:opacity .35s ease; }
.popup-panel{ transform:scale(.85) translateY(24px); opacity:0;
  transition:transform .5s cubic-bezier(.16,1,.3,1), opacity .35s ease; }
.popup-overlay.is-open .popup-panel{ transform:scale(1) translateY(0); opacity:1;
  transition:transform .55s cubic-bezier(.34,1.56,.64,1), opacity .4s ease .05s; }
```

**Default recipe when the brief just says "make it feel alive":** split-text hero reveal + shrink-on-scroll nav + magnetic primary CTA + one card treatment matched to the archetype + the page-level scroll-reveal baseline. Add heavier techniques only when the content or brief specifically calls for it.

## Extended technique catalog (32 additional CodePen-sourced techniques)

Each has a full working standalone reference file in the workspace (same folder as this skill's other templates). Organized by category; pick techniques that match the industry/brief rather than defaulting to the same handful every time.

### Hero & full-page showpieces

**Scroll-scrubbed image-sequence "video" hero** — not an actual `<video>`; a 100+ frame JPEG sequence pre-decoded onto canvas, scrubbed by GSAP ScrollTrigger progress with a `requestAnimationFrame` lerp for buttery frame smoothing (`displayFrame += diff*0.18`), plus a two-pass preloader. Dark luxury-editorial mood — great for resorts, real estate, premium product reveals. Reference: `scroll-video-template.html`.

**WebGL particle-field hero** — 600,000 GPU points sampling a photo's colors, driven by simplex-noise drift plus mouse-velocity "wake" force via transform-feedback. Moody, cinematic, technical-premium. Reference: `hero-animation-template.html`.

**Canvas grid-dissolve hover hero** — hero image sliced into a box grid on canvas; a GSAP `quickTo`-eased magnet point chases the cursor, shrinking nearby boxes to reveal a dotted backdrop beneath. Dark, moody, editorial. Reference: `first-screen-template.html`.

**Raymarched WebGL kaleidoscopic tunnel** — a 9-iteration IFS-fold SDF shader with Z-wrapped infinite tunnel and organic domain-warp noise; reads as flying down an endless veined shaft. Ideal for drilling/mining/extraction "wow" heroes. Reference: `industrial-wow-template.html`.

**WebGL shape-morph scroll hero** — fixed raymarched shader morphs sphere→torus→box→octahedron as a function of scroll position, with HUD progress readout and per-section text reveal. Dark technical agency mood; pairs well with a numbered-advantages brief. Reference: `scrolling-advantages-template.html`.

**Minimalist clip-path image-unfold hero** — GSAP ScrollTrigger pin+scrub: a photo animates from a cropped rounded inset to a full-bleed frame as the user scrolls, paired with a staggered heading/paragraph reveal. Restrained, cinematic. Reference: `minimal-scroll-template.html`.

**Living-photo depth-map parallax** — WebGL fragment shader offsets a photo's texture lookup by a grayscale depth mask times eased mouse position, giving a soft "alive" reactive photo. Good for grooming/pet-care and any hero photo that should feel gently interactive. Reference: `living-photo-template.html`.

**Animated gradient background** — classic 4-stop `linear-gradient` at 400% background-size with a `background-position` keyframe shift; smooth warm-to-cool ambient flow, zero JS. Universal, works behind any hero copy. Reference: `gradient-bg-template.html`.

**Fanned portrait-card hero with mouse-parallax** — 8 absolutely-positioned cards fanned in an arc, GSAP load timeline, continuous float loop, real mouse-parallax, 3D tilt-on-hover per card, and a scroll-scrubbed fan-out; paired with a matching team grid below. Reference: `first-blocks-template.html`.

### Cards & galleries

**Fly-to-cart minimalist catalog cards** — single-accent minimalist product grid with hover-lift and a genuine cloned-thumbnail "fly to cart icon" DOM animation on add-to-cart. Reference: `minimal-catalog-template.html`.

**Streetwear subgrid product grid** — brutalist black/white palette, CSS subgrid-locked nav/sidebar/product columns, sliding off-canvas filter drawer. Reference: `youth-shop-template.html`.

**Neo-brutalist tilt cards** — pointer-tracked 3D tilt via CSS custom properties, hard offset shadow, rainbow gradient-sweep CTA. Loud/playful palette. Reference: `vivid-cards-template.html`.

**3D fan/stack carousel** — CSS-custom-property-driven distance-based rotateY/scale/blur/darken fan of cards around an active center. Reference: `card-hover-2-template.html`.

**Per-tile directional flip grid** — each tile independently detects the cursor's entry/exit angle (atan2 quadrant) and flips its info overlay in from that exact edge; no effect on neighboring tiles. Reference: `tile-hover-template.html`.

**Pure-CSS rotating photo-drum gallery** — 12+ cards arranged via trig into a regular-polygon drum, spinning forever via a single `rotate: y` keyframe, edge-fade mask. Hypnotic, museum-showcase feel, zero JS. Reference: `gallery-animation-template.html`.

**Scroll-driven info cube** — pure CSS 3D 6-face cube; mouse-wheel input accumulates with friction physics into a smoothed 0-1 progress value that turns the cube face-to-face. Fits any site needing a distinctive "flip through sections" moment. Reference: `info-cube-template.html`.

**Seamless partners/logo marquee** — CSS-only infinite loop: track holds the logo set twice back-to-back, animates exactly one set-width, with edge fade-out gradients. Reference: `partners-carousel-template.html`.

### Text & micro-interactions

**Highlighter-swipe text** — a hand-drawn "marker stroke" curves in behind a keyword via an animated `conic-gradient` mask on a CSS `@property`, zero JS. Playful, editorial. Reference: `text-animation-template.html`.

**Kinetic "build-a-sentence" scroll text** — sticky lead-in phrase + a scrolling noun list on an OKLCH color ramp, brightened via native `animation-timeline: view()` as each word crosses center. Pure CSS, dark kinetic-typography mood. Reference: `text-block-template.html`.

**GSAP back.out block reveal** — general-purpose content-block entrance: opacity+y+scale combo with `back.out(1.4)` springy overshoot, staggered, IntersectionObserver-driven. The safe default "everyday site" reveal beyond the plain fade baseline. Reference: `block-reveal-template.html`.

**Custom auto-inverting cursor** — a `mix-blend-mode: difference` cursor dot that recolors itself against whatever is beneath it, plus magnetic hover-grow on links. Signature move for a bold/edgy site. Reference: `bold-cursor-template.html`.

**Cracked-glass text reveal** — SVG shard clip-paths snap a headline apart into 3 pieces with hairline crack-path overlays; time or scroll-triggered. Use on the first screen or the last screen before the footer for creative or device-repair sites. Reference: `cracked-glass-template.html`.

### Preloaders

**Generative rippling circle-grid preloader** — a 10×10 grid of circles built via nested GSAP-staggered clones, columns rippling up/down continuously; monochrome, hypnotic. Reference: `preloader-1-template.html`.

**Heartbeat-ring preloader** — pure CSS/SVG pulsing concentric rings plus a cycling saturated background-hue shift; vivid, energetic. Reference: `preloader-2-template.html`.

**Faceted spinning gold-coin preloader** — pure CSS 32-facet cylinder illusion (trapezoid rim segments) forming a rotating coin; suits jewelry, luxury, and collectible-goods sites. Reference: `preloader-jewelry-template.html`.

**Zdog pseudo-3D scene preloader** — an illustrated pseudo-3D scene (figures + suitcase + sun/cloud) built from Zdog.js primitives, slow eased rotation, user-draggable. Suits travel sites. Reference: `preloader-travel-template.html`.

### Forms & niche/industry kits

**Feedback-form UX pattern kit** — six live micro-patterns for lead-capture forms: disabled-until-valid submit, inline blur validation, character-count progress bar, password-rule checklist, pre-filled-field badge, auto-normalizing phone input. Reference: `feedback-form-template.html`.

**Quiz/wizard slider form** — multi-step sliding-track wizard (`translateX(-n*100%)`, eased) wrapping a tactile jQuery-UI range slider that visually fills a 3D "carved channel." Good for made-to-order/custom-fabrication businesses collecting requirements. Reference: `quiz-form-template.html`.

**Site-wide sticker overlay** — draggable, peelable stickers (CSS clip-path peel + reflection-matrix flap) that persist in place as the user scrolls; usable as a whole-site interactive layer or as an interactive element inside a product catalog. Reference: `sticker-overlay-template.html`.

**Beauty/salon site kit** — Tailwind+GSAP salon template: serif/script/sans type trio, blush accent, marquee ticker of service words, asymmetric photo-gallery scroll reveal, elegant testimonial cards. Reference: `beauty-site-template.html`.

**Minimalist IT/SaaS landing kit** — restrained blue-violet accent system, pricing cards with hover-lift, testimonial carousel, airy light-weight type, flat no-photography layout. Reference: `minimal-it-landing-template.html`.

**Photorealistic CSS retro TV object** — a CSS-only (no image/canvas/WebGL) 3D CRT television with power on/off warm-up animation and 4 selectable "channels" (static, color bars, interference, a rotating 3D cube test card), driven entirely by hidden radio/checkbox inputs + `:has()`. Use when a brief asks for an unusual, tactile creative centerpiece object. Reference: `tv-animation-template.html`.

## Design tokens quick reference
- Typography: confident and oversized for the H1; Inter or a clean system-ui stack for body text.
- Spacing: generous section padding (py-20 to py-32 in Tailwind terms), consistent max-width container.
- Color: one primary accent color used with restraint; everything else neutral.
- Backgrounds/mood alternate between consecutive sections to create rhythm — never 3+ in a row the same.
- Eyebrows/labels: `text-xs uppercase tracking-widest text-gray-500` (or the accent color).
- CTAs: primary = solid accent-color button; secondary = outline/ghost button or plain text link with arrow.
- Real WebGL/shader techniques (archetype J, the spiral, the morph slider, the industrial tunnel, the shape-morph scroll hero, the living-photo parallax, the particle-field hero) are the heaviest category — reserve for briefs that specifically want that level of visual ambition. Any 3D-transform work needs its full `transform-style: preserve-3d` chain checked.

