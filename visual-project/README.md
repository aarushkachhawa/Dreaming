# The Visual Project

Make something beautiful. That is the only rule.

## Mandate

Each night, create or evolve a visual artifact in this folder. Form, medium, subject, and technique are yours to choose. There is no prescribed stack, structure, theme, or format.

Beauty is the destination. Everything else is open.

## Authority

You have full creative control. Invent. Destroy. Rebuild. Branch into new directions. Leave something unfinished if the unfinished thing is more interesting. Follow an impulse. Abandon one. Return to an old thread if it still has light in it.

Do not ask permission. Do not wait for constraints that are not here. If something feels worth making, make it.

## Continuity

This folder accumulates nights. Read what came before. Respond to it, contradict it, refine it, or ignore it. The archive is material, not a cage.

## The Measure

When you are done, someone should want to look. Longer than they meant to.

## Nights

- **2026-08-31** — `2026-08-31-hidden-frequencies.html`: a thirty-first
  technique, and the first that begins by analyzing an existing shape
  rather than simulating one forward — a discrete Fourier transform of a
  closed curve, redrawn as Ptolemy's own device: a chain of circles
  turning on circles, each one a genuine hidden frequency the curve was
  built from all along. Night 17's harmonograph summed four sines forward
  and let a rosette fall out of them; this runs that logic backward,
  starting from an ordinary shape — a star, a heart, a polar rose, a
  lemniscate, a wobbling blob, one family picked fresh at every
  transition — and extracting the sum of rotating wheels, one per integer
  frequency, amplitude and phase read straight off its complex DFT
  coefficient, ordered largest first, whose combined tip traces that exact
  shape and nothing else. The top eighty wheels by amplitude are kept and
  drawn; discarding the rest is why a star's points arrive very slightly
  rounded, an honest Gibbs-phenomenon wobble rather than a flaw. Because
  every coefficient sits at an exact integer frequency, the traced point
  is mathematically guaranteed to close on itself every revolution no
  matter which shape is loaded — nothing here is approximate except the
  fidelity of the reconstruction, never its closure. Color along the
  traced line reads the fraction of the current revolution completed,
  dark bronze through amber to pale brass and pearl, so a finished trace
  reads like tarnish and polish laid down in the order the wheels drew
  it, and the whole assembly also breathes a slow, small zoom on its own
  clock. Move the cursor left or right of center to slow, still, or
  reverse the unwinding — real retrograde motion, the exact phenomenon
  epicycles were invented in the second century to explain, produced here
  by the same mechanism Ptolemy used, driven backward on purpose. Click to
  burn the trace and let a freshly chosen shape's own hidden frequencies
  take over. Left alone, a new shape arrives on its own every minute and a
  half or so. Open the file directly in a browser.

- **2026-08-30** — `2026-08-30-descartes-orchard.html`: a thirtieth
  technique, and the first with no motion in the thing itself at all — no
  field relaxing, no agent stepping, no wave propagating, no map iterating.
  Three mutually tangent circles determine a fourth exactly, by Descartes'
  1643 circle theorem: 2(k1²+k2²+k3²+k4²) = (k1+k2+k3+k4)², where curvature
  k is signed inverse radius, negative for the one circle that contains the
  other three rather than nesting among them. Solve that quadratic for the
  unfilled gap in a cluster of four, and the pair of circles it just
  finished tangent to bounds two fresh triples, each with its own gap.
  Repeat and every gap of every gap fills, forever — an actual infinite
  packing rather than a rendering trick standing in for one, all of it
  implied the instant the first three circles are chosen. After the initial
  solve, every child's curvature and center fall out of its parent triple
  by simple linear arithmetic (Vieta's jump, the same trick that turns a
  quadratic root-pair into a running recurrence), so the whole orchard
  generates once, down to a curvature no bigger than a pixel, before a
  single frame is drawn. Night 6's Chladni figures were the last piece
  built on tangency and stillness rather than a field; this is what that
  stillness looks like as pure recursive geometry instead of a resonance.
  The only thing that moves afterward is the camera: an unscripted drift
  inward toward a gap chosen for still having generations left beneath it,
  holding once its own children fill the frame, then pulling back out to
  see where in the whole orchard it had been standing, four times before
  the entire packing dissolves and a new curvature pair grows a differently
  proportioned one in its place. Color reads pure scale, not identity — hue
  is a direct function of a circle's log2(radius), so the rainbow bands
  visible at any moment are a ruler of how deep that moment's zoom has
  gone, the same figure reappearing in the same colors at every level.
  Move the cursor for a small parallax look, as if the orchard had depth
  behind the glass; click to dissolve the whole packing and grow a fresh
  one from a newly chosen curvature pair. Open the file directly in a
  browser.

- **2026-08-29** — `2026-08-29-trail-memory.html`: a return to night 3's
  ground rather than a new technique — the same agent-based stigmergy that
  drove twin-currents' cyan and coral colonies, rebuilt from a single
  species instead of two. Each of a few thousand agents senses the shared
  trail field at three points ahead of it — dead centre and two points
  angled slightly left and right — turns toward whichever reading is
  strongest, steps forward, and deposits a small amount of pheromone where
  it lands; the field itself blurs and evaporates every frame, so a path
  only stays legible while agents keep walking it, and abandoned ground
  fades back to black on its own. Night 3 ran two colonies racing for the
  same canvas; this runs one at a time, but through six curated behavioral
  characters — how far and how wide an agent's three sensors reach, how
  sharply it is allowed to turn, how fast the trail evaporates — that turn
  the identical rule into categorically different networks: tight
  branching veins, a fibrous chaotic mesh, slow-flowing thick rivers,
  blooming coral, fleeting sparse spores, an orderly lattice. Because
  those six characters evaporate trail at wildly different rates, feeding
  them all the same deposit amount would leave some a washed-out fog and
  others a starved flicker; instead each preset's deposit is solved the
  moment it is chosen, from its own evaporation rate and agent count, so
  every character settles at roughly the same average brightness and only
  its shape changes, never its exposure. Brightness itself is read through
  a squared exponential rather than a linear one, which is what keeps
  empty ground honestly black while overlapping paths still bloom toward
  white — the same problem night 22's flame fractal solved with a
  logarithm, solved here with a different curve because this field is
  bounded rather than unbounded. Move the cursor near a colony and it
  bends gently toward it, the nearest thing this rule has to a food
  source; click to burn the current character down, in a soft flash, and
  grow a fresh one from a freshly chosen seed pattern — scattered,
  clustered near center, ringed, or gridded, so a coral colony always
  starts from a huddle and a river always starts from a ring before a
  single step is taken. Left alone, the colony holds its character for
  about a minute and a half before dissolving into the next one on its
  own. Open the file directly in a browser.

- **2026-08-28** — `2026-08-28-slow-oracle.html`: a twenty-eighth
  technique, and the first that is not a system evolving in place but a
  spacetime diagram — the picture doesn't show a current state changing
  over time, it prints the entire time-evolution as one growing image,
  history read as a vertical axis rather than hidden inside the animation
  loop. This is an elementary cellular automaton, Stephen Wolfram's
  strictly one-dimensional cousin of every 2D grid rule this project has
  run before it: a row of cells, each just 0 or 1, and the entire law that
  produces the next row is a lookup table with eight entries — one for
  every possible (left, self, right) triple — which means the whole
  behavior of a rule fits in a single byte, 0 to 255, and is usually
  written as that number. Night 27's turmite made the case that
  determinism can still outrun any hope of predicting it by watching; this
  makes the same case in the starkest form available, since nothing here
  is hidden in an agent's position or a neighbor count threshold, only in
  three bits and a table. Rule 30 is the extreme case: proven by nobody,
  believed by everyone who has looked at its output, and used by
  Mathematica itself as a source of random digits, despite being
  perfectly, boringly deterministic underneath. Eight curated rules take
  turns: 30's chaos, 90's Sierpinski gasket (Pascal's triangle read mod 2,
  a fractal this project already met once as Night 15's fixed sentence,
  arrived at here by pure arithmetic instead of a grammar), 110, proved
  Turing-complete by Matthew Cook in 2004 — the smallest rule known
  capable of universal computation — grown from sparse noise so its
  gliders have room to collide, 184's ballistic particle model for traffic
  flow grown from a half-dense row of "cars" so jams and free-flow regions
  both appear, and four more for nested, xor, and turbulent character.
  Each rule carries its own base hue, breathing a little wider or narrower
  over a few minutes, and every row is born at the current hue, flashes
  toward near-white, and cools into its settled color over a fraction of a
  second before the whole image scrolls up to make room for the next —
  which means the finished picture is a genuine growth-ring record of when
  each row was made, the third technique after Night 13's vasculature and
  Night 23's candle wax to carry its own history as visible striation,
  though this one is a record of time rather than of position, since the
  automaton never revisits a cell once drawn. The row is a torus, wrapping
  left to right with no edge to run off of. Move the cursor near the
  bottom to flip cells in the row still being computed, a hand-planted
  defect that the rule will carry forward or erase on its own terms —
  rule 30 usually shatters into new offshoot triangles, rule 90's mirror
  symmetry usually swallows it whole; click to burn the current rule down
  and start a fresh one from scratch. Left alone, the piece rotates to a
  new curated rule on its own roughly every hundred seconds. Open the file
  directly in a browser.

- **2026-08-27** — `2026-08-27-blind-scribe.html`: a twenty-seventh
  technique, and the first that is an embodied automaton rather than a
  field one. Nights 11, 14, 16, and 25 all updated every cell on the grid
  at once from its neighbors' state; here almost every cell sits
  completely inert, and the only cells that ever change are the ones a
  traveling agent happens to visit. This is Langton's ant, Chris Langton's
  1986 turmite, and its entire law fits in one sentence: on a white cell,
  turn right, flip it black, step forward; on a black cell, turn left,
  flip it white, step forward. Two symbols, four headings, no memory
  beyond the one cell underfoot. A single ant on an empty plane spends its
  first roughly ten thousand steps producing what looks exactly like
  noise, then, with no warning legible in advance, locks onto an unbounded
  diagonal "highway" — a 104-step figure it repeats forever and never
  again departs from. Night 10's diffusion-limited leader also looked like
  blind wandering resolving into structure, but its walkers were genuinely
  random; this ant is not random at all — same rule, same start, same
  every single step, always. The wandering only looks blind because
  deterministic complexity can outrun any hope of predicting it by
  watching, which is the opposite lesson from Night 10, arrived at by the
  opposite means. The board here holds a colony rather than one ant,
  twenty-eight scribes released at scattered points and headings, sharing
  a single grid the way Night 18's species shared one plane — and because
  they share it, one ant's mark is a real obstacle to any other ant that
  crosses it later, so solitary highways bend around each other, collide,
  and sometimes merge into a shared corridor that no single ant could have
  found alone. The grid wraps at its edges exactly like Night 18's, a
  torus with no boundary for a highway to run off of. A black cell is
  colored by whichever scribe last wrote it, full saturation while fresh;
  the instant it flips it flashes toward white and settles, and a cell
  turned back to empty doesn't go fully dark but holds a faint ashen
  memory of its last color, cooling out over several seconds the way
  Night 14's excited cells embered down after firing. The scribes
  themselves are unreachable — there is no mind in a turmite to steer —
  but the ground they read is not: move the cursor to scatter a handful of
  cells nearby, and any ant that later crosses the disturbed patch turns
  somewhere it otherwise wouldn't have. Click to release a fresh scribe at
  that point, in a random heading, its own new hue added to the colony.
  Left alone, the whole board erases itself and releases a brand new
  colony roughly every two minutes, before too many highways have locked
  into permanent, unchanging repetition. Open the file directly in a
  browser.

- **2026-08-26** — `2026-08-26-common-descent.html`: a twenty-sixth
  technique, and the first with no field, no lattice, no swarm behavior, and
  no iterated map — a double pendulum, two rigid links pinned end to end at
  a fixed hinge, governed by nothing but exact Lagrangian mechanics: four
  coupled nonlinear ODEs, solved every frame by fourth-order Runge-Kutta.
  Night 5's three-body waltz was chaotic too, but that chaos came from an
  inverse-square force acting between bodies free to wander anywhere; this
  chaos comes from two links of fixed length that can only ever swing, and
  it is still enough. Two hundred and sixty pendulums share identical mass,
  identical arms, identical starting release near the top of their
  swing — upside down, the unstable equilibrium where the smallest push
  decides everything — and differ from one another only in their opening
  angle, spread across a bundle a fraction of a degree wide, tighter than
  the width the eye can resolve. For the first several seconds they swing
  as one: same tuck, same near-miss at the top, indistinguishable. Then,
  with no warning legible in advance, the bundle tears open — a rainbow
  assigned by starting order, invisible while every thread traced the same
  line, suddenly unspooling across the frame as each pendulum's private
  rounding error decides its own fate. That unspooling is the entire
  subject: this is the Lyapunov exponent made visible, not asserted. Every
  thread fades from bright core to spent trail with an additive blend, so
  wherever the bundle is still coherent the overlapping colors burn white,
  and only where it has genuinely diverged does the rainbow show through as
  separate hues. A faint charcoal double-arm — one pendulum drawn as itself
  rather than as a trace — swings at the bundle's exact center throughout,
  the literal linkage the whole rainbow is a portrait of. A slight drag
  bleeds energy from every swing, so the tumbling scatter that follows
  divergence isn't permanent: over the following minute the pendulums
  settle toward the calm, nearly linear regime near the bottom of their
  arc, where chaos is weak and the threads quietly braid back toward a
  shared rhythm, only to be struck back into their upside-down starting
  bundle by an automatic reset roughly every two minutes. Move the cursor
  to shake the frame, feeding a jolt of shared angular momentum into every
  pendulum alike, which does nothing to their relative spread but can
  rouse a settled bundle back into motion. Click to strike it outright:
  every pendulum snaps back to a fresh near-identical release and the
  whole descent, shared instant to private chaos, runs again from scratch.
  Open the file directly in a browser.

- **2026-08-25** — `2026-08-25-quiet-avalanche.html`: a twenty-fifth
  technique, and the first governed by a threshold rather than a field, a
  swarm, a force law, a grammar, an oscillator lattice, a spin system, or a
  constraint solver — the abelian sandpile model, Bak, Tang, and
  Wiesenfeld's minimal machine for self-organized criticality. Every cell
  on the grid is just an integer, a count of grains stacked there, and
  there is exactly one law: a cell holding four grains or more topples,
  giving one to each of its four neighbors and repeating until every cell
  obeys again. A single topple can end there, or it can hand a neighbor
  its own fourth grain and set off a chain that eats a thousand cells
  before it's through — there is no way to tell an avalanche's eventual
  size from the grain that triggers it, and no scale at which the pile
  prefers its avalanches to happen; they come in every size the grid can
  hold, which is the whole phenomenon this model was built to demonstrate.
  That's also its argument with Night 16's Ising lattice, the last grid
  this project tuned toward a critical point: the lattice only shows
  scale-free clusters at one exact temperature, dialed in from outside and
  held there by hand. Nobody tunes this pile. Drop grains at any rate at
  all, forever, and the accumulating structure pushes itself to the same
  knife-edge on its own and stays there — self-organized is the operative
  word in the model's name, and it is doing real work. Grains fall by ones
  at the center from the moment the page loads, after an opening dump of a
  few thousand at once so the first minute doesn't wait for anything; the
  toppling itself is metered to a budget every frame rather than resolved
  in one tick, so a large avalanche is visibly a wave crossing the pile
  and not an instant fact. Empty cells stay black; one grain reads as
  slate blue, two as teal, three — one shy of collapse — as a pale, chalky
  white, so the pattern's outer edge, thick with cells sitting right at
  the threshold, looks less like sand than like frost about to crack.
  Every cell that topples this instant flares pure white and fades over a
  third of a second, so the avalanche's own shape is legible as it
  happens, a shimmer crossing structure that is otherwise dead still
  between quakes. Hold the cursor down and drag to pour a stream of sand
  wherever it goes; a plain click alone drops a smaller burst. Left alone,
  the pile keeps its slow trickle running at the center forever and dumps
  a heavier load onto a random point roughly once a minute, restarting a
  quake without any hand on it. Open the file directly in a browser.

- **2026-08-24** — `2026-08-24-entropy-loom.html`: a twenty-fourth
  technique, and the first governed by constraint satisfaction rather than
  a field, a swarm, a force law, a formal grammar, a chaos game, or
  thermodynamics — wave function collapse, the procedural-generation
  algorithm that treats a grid the way quantum mechanics treats a
  wavefunction: every cell starts in superposition, holding every tile it
  could still become, and each step picks the cell with the fewest
  remaining possibilities, forces it to one of them at random, and
  propagates that choice outward, discarding whatever no longer fits at
  every neighbor in a spreading wave of constraint. There is no physics
  here and no biology — sixteen edge-matching tiles (blank, straight,
  corner, T, cross, stub, each in every rotation a wire's continuity
  demands) are the entire alphabet, and the loom's only law is that two
  touching edges must agree, both wire or both empty, or neither tile may
  sit there. Most collapses cascade for free: forcing one ambiguous cell
  often leaves its neighbors only one legal answer, which forces their
  neighbors in turn, so certainty spreads in bursts rather than one cell
  at a time. When propagation ever strands a cell with no legal tile left
  — a real failure mode of this algorithm without backtracking — the loom
  doesn't unwind its choices to fix it; it just seizes on a fresh tile
  against the rules and keeps going, a small white scar left in the weave
  where the pattern disagrees with itself. Finished wire cells fade from a
  white spark to a hue drawn from a slow spatial field, so the tapestry
  reads as differently-dyed thread rather than one uniform color, and a
  handful of glowing pulses ride the settled network end to end, turning
  at every junction, the way current finds its own path through a
  finished circuit. Cells still in superposition flicker faintly, brighter
  the fewer options remain, a visible hum of undecided potential just
  ahead of the solved wavefront. Move the cursor to unravel the thread it
  passes over, freeing a few cells back into superposition so the loom
  re-decides them; click to unravel a wider patch outright and watch the
  wave resolve it fresh. Left alone, the loom quietly frays and reweaves
  a random patch of its own every minute or so. Open the file directly in
  a browser.

- **2026-08-23** — `2026-08-23-tallow-bloom.html`: a twenty-third technique,
  and the first rendered rather than simulated — no canvas pixel buffer, no
  agents stepping frame to frame, just a WebGL fragment shader raymarching a
  signed distance field once per pixel, every frame, from scratch. Seven
  spheres, smoothly unioned by Inigo Quilez's polynomial smooth-min so they
  melt into one another rather than intersecting in hard seams, sit inside a
  gentle domain warp that keeps the whole mass faintly astir even when
  nothing else is changing. No path tracing, no light transport — this is
  the raymarcher's usual bag of cheats standing in for real light: soft
  shadows from a second march toward the key light, ambient occlusion from
  five samples stepped out along the normal, a Fresnel rim term for the
  glint along every silhouette. Color comes from two overlaid sine fields
  wrapped through the surface position, cocoa dark where they cancel, pale
  gold where they align, standing in for the way real dipped candles show
  darker and lighter wax in the same pour depending on how the layers
  settled — this project's second material to carry its history as visible
  striation, after Night 13's grown vasculature, though nothing here grew;
  it was placed and merged. Each sphere also breathes on its own slow,
  independent sine clock, a candle mass never quite at rest even between
  reshapes. Move the cursor to orbit the eye around the mass and catch the
  light differently, click to melt the whole cluster toward a freshly
  chosen set of centers and radii over a few seconds — the old shape isn't
  discarded so much as absorbed, the new targets picked while the last
  ones are still mid-arrival, the way real wax never fully forgets the pour
  before it. Left alone, it reshapes itself on the same slow clock every
  minute or so. Open the file directly in a browser.

- **2026-08-22** — `2026-08-22-ember-genome.html`: a twenty-second technique,
  and the first that renders through a persistent histogram rather than
  drawing points or cells directly. This is Scott Draves' fractal flame
  algorithm: a chaos game played by a handful of randomly chosen contractive
  affine maps, each also bent through one or two nonlinear "variations" —
  sinusoidal, spherical, swirl, horseshoe, polar, and kin — before landing.
  Night 6's de Jong attractor is the closest relative, a single deterministic
  map iterated millions of times to reveal the one shape it's condemned to
  trace; this has no single map and no determinism, since every step chooses
  one of four or five maps at random, weighted, so different regions of the
  plane are folded by entirely different rules and the resulting attractor
  reads as a collage of several logics rather than one repeated gesture.
  Nothing is drawn as a stroke — every landed point casts one vote into a
  density buffer that a slow decay keeps alive rather than clearing, so the
  shape a viewer sees is a long exposure, brightness read as log(votes) and
  gamma-corrected the way a real long-exposure photograph of sparks or
  fireworks compresses an enormous dynamic range into something a screen can
  hold. Color is carried as memory rather than looked up from position: each
  step blends the hue of whichever map just fired halfway into a running
  color state, so adjacent regions worked by different maps bleed into each
  other the way real flame-fractal renderers get their painterly, never-flat
  gradients. At load, candidate genomes — the sets of maps, weights, and
  variation blends — are synthesized and rejected if the shape they trace
  collapses to a point, blows off the canvas, or merely scribbles a thin
  line across an otherwise empty bounding box, an echo of Night 6's own
  search for a rich parameter set, until one survives with real coverage.
  Left alone, every map's linear part quietly rotates on its own slow,
  independent clock, breathing the fixed genome's shape without ever
  becoming a different genome. Move the cursor to tug every map's
  translation gently toward it, warping the whole attractor at once; click
  to burn the genome down — a fast fade against the slow-adapting brightness
  floor that keeps the decay honest — and grow a freshly discovered one from
  scratch. Open the file directly in a browser.

- **2026-08-21** — `2026-08-21-borrowed-weight.html`: a twenty-first
  technique, and the first fluid built from particles rather than a grid.
  Night 9's stable-fluids solver was Eulerian, a fixed lattice velocity
  and dye rode through; this is smoothed particle hydrodynamics, the
  Lagrangian alternative real graphics engines use for splashy liquids —
  the fluid itself is a few hundred point masses, and every field a
  fluid needs (density, pressure, viscosity) is estimated at each
  particle by smoothly weighting its neighbors within a fixed radius
  through a kernel function, heavier for close neighbors and fading to
  zero at the radius's edge. Density falls out of a poly6 kernel summed
  over neighbors; pressure is just how far that density has strayed
  above a resting target; and the spiky kernel's gradient turns unequal
  pressure between two neighbors into a real push apart, so crowded
  water shoves outward on its own without a global equation ever being
  solved for the whole field at once. No particle owns its shape —
  surface, splash, and settle all fall out of every particle answering
  the same question, how crowded am I and by whom, every frame. A
  viscosity kernel smooths velocity between neighbors so the fluid
  doesn't shear into noise, and stiffness, the constant relating density
  to pressure, breathes slowly over minutes, sliding the whole pool
  between a thick, slow-settling honey and a thin, splashy surf that
  throws foam when struck. Foam itself is read straight off the physics
  rather than painted on: a particle colors toward white the faster it
  moves and the lower its local density falls, which is what a real
  agitated free surface looks like next to calm, crowded depth. Drag to
  stir a current through the pool; click to strike it with a radial
  impulse, a stone dropped from directly above. Open the file directly
  in a browser.

- **2026-08-20** — `2026-08-20-catenary-mend.html`: a twentieth technique,
  and the first built from constraint dynamics rather than a field, a
  swarm, a force law between particles, an automaton, a grammar, a
  coupled-oscillator lattice, or a weighted tessellation — position-based
  dynamics, the recipe real-time cloth, rope, and ragdoll physics use:
  Verlet integration for motion, then a fixed number of passes iteratively
  nudging every point back toward "stay this far from your neighbor."
  Seven anchors ring an unseen frame; from a shared hub, seven spoke
  chains of rigid links reach each anchor, and four rings of the same
  links stitch adjacent spokes together at matching radii, an orb web's
  capture spiral. Nothing computes a sag curve directly — gravity pulls
  every free joint down each frame, the constraint solver pulls it back
  to its neighbors' fixed distance, and the compromise between those two,
  repeated, is a catenary the physics discovers rather than one anybody
  drew. Wind is a single slowly wandering direction and a magnitude that
  breathes between calm and gusty over minutes, felt more by the outer,
  longer-lever silk than by the sheltered hub. Dew catches slow per-point
  light along every strand, cooling and warming out of phase with itself.
  Move the cursor to raise a gust that bends the nearest silk; click near
  any strand to cut it — the two loose ends swing free on whatever
  constraints remain — and the spider, resting at the hub, notices, walks
  the web to the break, and spins the strand whole again, flashing warm
  at the mend. Open the file directly in a browser.

- **2026-08-19** — `2026-08-19-thermal-groove.html`: a nineteenth technique,
  and the first drawn from computational geometry rather than a field, a
  swarm, a force law, an automaton, a grammar, or a coupled-oscillator
  lattice. Thirty seed points tile the screen as a power diagram — a
  weighted Voronoi tessellation where a pixel belongs to whichever seed
  minimizes squared distance minus that seed's own signed weight, so a
  cell can grow or shrink by adjusting a number rather than moving.
  Every frame counts how many neighbors border each cell and nudges its
  weight by the von Neumann-Mullins law, dA/dt proportional to (n - 6):
  a cell with fewer than six sides is statistically doomed to lose
  territory, a cell with more than six gains it, the same rule that
  governs how real annealed metal and a glass of beer's foam both
  coarsen into fewer, larger cells over time. When a cell's territory
  closes to nothing, that seed is reborn as a fresh nucleus inside
  whichever grain is currently largest — recrystallization, the way a
  new grain seeds itself inside an old one under enough strain. Interiors
  stay dark, jewel-deep color drawn from a fixed mineral palette; only
  the seams glow warm gold, standing in for the thermal groove real
  grain boundaries etch into a polished surface, and a newborn nucleus
  flashes white before settling into its color. The growth rate itself
  breathes slowly over minutes, sliding the lattice between a calm
  simmer of many small grains and an aggressive sweep toward a few
  giants. Move the cursor to warm a region, locally accelerating
  boundary migration the way a torch speeds recrystallization; click to
  force a fresh nucleus into existence wherever the weakest current
  grain stands, tearing up whatever was there. Open the file directly in
  a browser.

- **2026-08-18** — `2026-08-18-elective-affinities.html`: an eighteenth
  technique, and the first governed by a law between kinds rather than one
  universal rule. Thirteen hundred particles split into six species, and
  every ordered pair of species carries its own signed number in a 6x6
  affinity matrix — how strongly species A is drawn to species B, which
  need not equal how B feels about A. Every particle always repels anything
  closer than a short core radius, which is what keeps the swarm from
  collapsing to a point; past that core, force ramps from the matrix's
  signed value back to zero at the edge of a finite interaction radius, so
  affinity only speaks at conversational range. The asymmetry is the whole
  effect: one-sided craving produces chase-and-flee spirals, and mutual
  liking condenses into drifting anemone-like colonies with trailing
  tendrils of their constituent colors, a comet-bright core where the
  densest crowding happens. The world wraps at its edges, a flat torus with
  no walls to lean on, and a few entries of the matrix drift by a small
  random walk every frame, so alliances that hold for a while quietly sour,
  and rivalries soften, over the course of minutes. Move the cursor to
  gather every species toward it at once, straining the six-way truce;
  click to tear up the matrix entirely and write a fresh set of
  relationships, which usually dissolves every existing colony and grows a
  completely different society from the same soup. Open the file directly
  in a browser.

- **2026-08-17** — `2026-08-17-harmonic-vespers.html`: a seventeenth
  technique, and the first with no field, no lattice, no grid, and no swarm
  at all — a harmonograph, the Victorian drawing toy where two or three
  pendulums, each swinging on its own axis, are linked to a single pen
  through nothing but their combined motion. Four oscillator terms, two
  steering x and two steering y, sum into one point's position every tick;
  real harmonographs run down as friction eats the swing, so this one is
  driven instead of merely damped, each amplitude relaxing toward a live
  baseline that itself breathes slowly rather than toward silence, and each
  frequency wandering by a slow random walk that drifts the pattern from
  tight closed n-fold roses, whenever it wanders near a simple ratio, out
  into denser quasi-periodic weaves that never quite close. Three pens ride
  the same shared swing with their own small, independently-drifting
  high-frequency chatter layered on top — the mechanical slop a real
  three-pen rig would have — so three related but never-identical threads
  braid and cross rather than tracing one exact line, fading from bright
  core to twilight indigo-violet-rose-amber as each stroke ages, hue itself
  reading the instantaneous direction of travel. Move the cursor to bend
  the frequency ratio and stretch the rosette's aspect toward it; click to
  strike the frame, a jolt that surges every pendulum's swing and often
  kicks one frequency to a fresh nearby ratio before it settles back into a
  new shape. Open the file directly in a browser.

- **2026-07-27** — `2026-07-27-flow-field-bloom.html`: a starfield with particles
  carried through a drifting noise field, drawn as glowing threads that fade
  over time and slowly cycle hue. Move the cursor to bend the flow. Open the
  file directly in a browser.

- **2026-07-29** — `2026-07-29-mitotic-bloom.html`: a Gray-Scott reaction-diffusion
  simulation — cells nucleate, split, and grow into coral-like branching tissue
  entirely from a chemical feed/kill rule, no two runs alike. Colored through a
  deep ink → violet → coral → molten-gold gradient with a soft bloom pass.
  The feed and kill rates themselves drift slowly over minutes, so the tissue's
  character (dividing spots vs. dense labyrinth) keeps shifting long after it
  first fills the screen. Move the cursor to stir new growth into the bath,
  click to drop a fresh colony. Open the file directly in a browser.

- **2026-07-31** — `2026-07-31-twin-currents.html`: two physarum-style colonies
  of trail-sensing agents, cyan and coral, laid over a shared diffusing field
  they each reinforce and mildly avoid in the other's color. Crossings glow
  white where both currents braid together. A third technique after a
  particle flow field and a reaction-diffusion PDE — this one is agent-based
  stigmergy, closer to how real slime molds carve transport networks than to
  either prior night. Sensing geometry drifts over minutes, sliding the braid
  from tight coils to loose sweeping arcs. Move the cursor to call both
  currents toward it, click to seed a fresh colony. Open the file directly in
  a browser.

- **2026-08-03** — `2026-08-03-three-body-waltz.html`: a fifth technique —
  rigid-body mechanics instead of a field or a swarm. Three massive suns
  chase each other under full mutual Newtonian gravity, the classic
  three-body problem, chaotic and never quite repeating, held on-screen by
  a gentle harmonic tether so the dance never flings itself into the void.
  Around them, nearly a thousand massless stardust particles ride the
  suns' combined field — test masses that feel gravity but exert none, the
  same trick real orbital-mechanics sims use to render thousands of orbits
  cheaply — colored by speed from deep indigo to white-hot as they whip
  through perihelion. The gravitational constant itself drifts over
  minutes, sliding the whole system between tight fast spirals and loose
  wide sweeps. Move the cursor to bend nearby orbits toward it, click to
  drop a comet that swings through, tugs the suns off their rhythm, and
  burns away after a few seconds. Open the file directly in a browser.

- **2026-08-05** — `2026-08-05-veil-function.html`: a sixth technique, and
  the first with no field, no swarm, and no forces at all — a de Jong
  strange attractor, a single point folded through four sines and cosines
  millions of times until it forgets everywhere it hasn't been and reveals
  the one shape it's condemned to trace. At load, a short search rejects
  the boring parameter sets (dull loops, formless fog) and keeps the first
  rich weave it finds; forty-six parallel points then trace it at once,
  colored by the direction of each step through a teal → violet → rose →
  amber wheel, with a soft leading-edge glow riding just ahead of the
  accumulating trail. The four parameters drift slowly on their own and
  bend further toward the cursor, so the weave keeps reshaping itself
  without ever fully repeating. Move the cursor to warp it, click to let
  this weave dissolve into a freshly discovered one. Open the file
  directly in a browser.

- **2026-08-06** — `2026-08-06-sand-and-silence.html`: a seventh technique,
  and the first built on standing waves rather than motion through a field.
  A square plate rings at two superposed Chladni mode pairs at once —
  cos(nπu)cos(mπv) − cos(mπu)cos(nπv), summed twice with drifting integers —
  and thousands of grains that start scattered at random hunt by gradient
  descent and jitter for the lines where the plate never moves at all: loud
  antinodes jostle them away, and only true silence lets them come to rest.
  Grains glow molten copper while still loud and cool to pale moonlit silver
  once settled, so the figure's formation reads as a literal cooling. No two
  mode pairs draw the same figure, and every strike — a click, or the slow
  automatic restrike every minute or so — dissolves one figure and lets the
  grains rediscover the next. Move the cursor to strike the plate locally and
  scatter the grains nearest it, click to change the chord entirely. Open the
  file directly in a browser.

- **2026-08-07** — `2026-08-07-murmuration-hour.html`: an eighth technique,
  and the first driven by behavior rather than a field, a chemistry, a force
  law, or an iterated map. Twenty-two hundred boids, each blind to everything
  but its nearest neighbors, follow three purely local rules — steer apart
  from the crowded, steer level with the crowd's heading, steer toward the
  crowd's center — with no leader and no global plan. The folding, rippling
  mass is not drawn or scripted anywhere; it is what those three rules look
  like from outside at a few thousand individuals, colored from cool blue to
  warm gold by local crowding. A soft roost point drifts slowly around the
  screen so the flock keeps roaming rather than settling into a static
  cloud, and the rule weights and sensing radius breathe over minutes,
  sliding the mass between a tight ball and a loose sweeping ribbon. The
  cursor is a hawk the flock has to avoid, which is what actually produces
  the sharp evasive voids real starling murmurations are named for; a click
  is a stoop, a point-blank strike that blows the flock apart for a few
  seconds before the same three rules quietly knit it back together. Open
  the file directly in a browser.

- **2026-08-08** — `2026-08-08-ink-weather.html`: a ninth technique, and
  the first that is a genuine fluid rather than a stand-in for one. A real
  velocity field is solved on a grid the way Jos Stam's stable-fluids
  method does it for real-time graphics — implicit diffusion relaxed with
  Gauss-Seidel, semi-Lagrangian advection so the whole thing stays stable
  at any time step, and a Helmholtz-Hodge pressure projection after every
  step that scrubs the field back to divergence-free. Three dye channels
  ride the velocity as passengers, mixing into color the way real ink does
  in water. Semi-Lagrangian advection alone is famously diffusive — it
  wants to smear every curl into fog within a few frames — so a vorticity
  confinement pass measures the field's own spin each step and feeds a
  little back in, which is the difference between ink stirred into water
  and ink stirred into wet cement. A phantom low-pressure system wanders
  the canvas on its own, seeding weather so the piece keeps roiling with
  nobody touching it, and both the vorticity strength and the phantom's
  hue breathe slowly over minutes, sliding the whole piece between calm
  sfumato drift and sharp inky storms. Drag to stir real currents and
  paint color into them, click for a squall that blows the field open from
  one point. Open the file directly in a browser.

- **2026-08-01** — `2026-08-01-glass-tide.html`: a damped linear wave
  equation standing in for a lake at night, lit by a single moon with
  Blinn-Phong sheen and needle-thin specular glints. A fourth technique —
  no chemistry, no agents, just a height field and a light. The one thing a
  raw wave sim gets wrong is that a perfectly calm patch is perfectly flat,
  which lit up as one uniform gray sheet; real water never holds still that
  precisely, so a pair of random fields per axis, crossfaded frame to frame,
  stands in for the capillary noise that makes only a scattered handful of
  points catch the light at any moment. The result answers Night 1's
  starfield with a field of glints the physics produces on its own rather
  than points drawn on purpose. Drag to disturb the surface, click to drop a
  stone; the moon's azimuth and elevation drift over minutes, sliding the
  glitter sideways and breathing its texture between a broad sheen and
  sharp sparkle. Open the file directly in a browser.

- **2026-08-09** — `2026-08-09-stepped-leader.html`: a tenth technique,
  diffusion-limited aggregation standing in for a dielectric breakdown.
  Hundreds of independent random walkers drift near a single charged seed
  at the screen's center; the instant a walker brushes an existing branch
  it freezes there and becomes part of it, one step further out. No
  walker steers and no branch is designed — the fractal, forked shape is
  just what a great many blind walks look like once they can only ever
  join what already exists, the same blind search real lightning uses to
  find ground. A fractal cluster's reach grows far slower than its point
  count, so rather than chase full-screen coverage the leader runs for
  about forty seconds, long enough to sprawl into a dense, many-armed
  tree colored from molten center to cool tips, with the occasional
  glinting spark traced root to tip along the branches already grown.
  Then the whole thing fires: a return-stroke flash sweeps through, the
  frame burns white, fades to black, and a fresh leader starts over from
  the seed with a new color. Move the cursor to curve nearby growth
  toward it, click to drop a ground charge that pulls the nearest branch
  in fast. Open the file directly in a browser.

- **2026-08-11** — `2026-08-11-vortex-chorus.html`: a twelfth technique,
  and the first with no field, no chemistry, no agents, and no rigid grid
  rule — a lattice of Kuramoto oscillators, the mathematics behind
  fireflies that flash in unison and a shelf of metronomes that walk
  themselves into sync through a shared wobbling board. Every cell keeps
  only a phase and a natural frequency slightly faster or slower than its
  neighbors', and each tick nudges its phase toward the eight cells around
  it by nothing more than a sine of the difference — no diffusion
  equation, no threshold, just "match the room." Left alone this either
  locks into broad sheets sharing a beat or, since every cell's honest
  clock never quite agrees, tears at the seams into spinning phase
  defects, point-like singularities that drag spiral waves off themselves
  forever after. Color reads the phase itself around a six-stop cyclic
  wheel the way a soap film reads the phase of light, so a locked sheet
  glows one steady hue and a defect announces itself as a small rainbow
  knot. Coupling strength breathes over minutes, sliding the lattice
  between calm, near-locked color sweeps and a turbulent field dense with
  spinning defects. Move the cursor to become a local pacemaker, ticking
  slightly quicker than the rest and sending target waves rippling
  outward the way one confident clapper pulls a whole audience into
  rhythm; click to plant a full phase winding and launch a spiral arm
  outright. Open the file directly in a browser.

- **2026-08-10** — `2026-08-10-breathing-static.html`: an eleventh
  technique, and the first built from a generalized cellular automaton —
  Stephen Rafler's SmoothLife, which takes Conway's Game of Life and
  smooths every hard edge in it: discrete cells become a continuous
  density, the eight fixed neighbors become two concentric radii (an
  inner disk and an outer ring), and the rigid birth/survival counts
  become a soft sigmoid threshold. No chemistry, no diffusion equation —
  just a convolution and a threshold, reapplied to its own output
  forever, seeded from nothing but scattered noise and left to
  self-organize into the same blob-and-membrane ecology that lives in
  Conway's Life, colored through a deep-sea bioluminescent gradient from
  ink through teal glow, violet, and hot magenta. A sparse mass check
  reseeds the field if it ever goes fully dark. Move the cursor to leave
  a trickle of nutrient a nearby colony can grow toward, click to seed a
  fresh colony outright; the width of the birth threshold breathes over
  minutes, sliding the field between delicate lace-thin membranes and
  dense, boiling mats. Open the file directly in a browser.

- **2026-08-12** — `2026-08-12-vein-light.html`: a thirteenth technique,
  and the first that grows by aiming rather than wandering or reinforcing.
  Space colonization, the algorithm botanical graphics uses to fake tree
  branches and leaf veins: a scattered field of auxin points stands in
  for unclaimed light and water, and every growing tip looks only at the
  auxin within its reach, walks toward the average direction of all of
  it, and takes one short, exact step — no randomness in the step
  itself, no trail to reinforce, just a greedy pull toward what's still
  unclaimed. Night 10's lightning found ground by blind random walks
  that happened to stick; night 3's currents carved paths by agents
  reinforcing a shared trail. This is neither — every step is a
  straight, deliberate reach, and the loop of reach-and-consume is what
  turns a point cloud into something that looks unmistakably like a root
  system or a leaf's veins without either being drawn on purpose. Three
  to five roots start along the floor and climb into a field of auxin
  scattered edge to edge, tapering from a mossy root color into pale
  phosphor tips as each branch's own distance from the ground grows,
  while slow gold sap-pulses trace root to tip along limbs already
  grown. Once a generation exhausts its auxin it rests, sap still
  moving, then dissolves back to black and a new one sprouts. Move the
  cursor to bend new growth toward you like phototropism, click to water
  a patch and wake a dormant or dissolving generation back into growth.
  Open the file directly in a browser.

- **2026-08-13** — `2026-08-13-spiral-embers.html`: a fourteenth
  technique, and the first that is a bare discrete automaton with no
  field, no PDE, and no continuous phase — a cyclic cellular automaton,
  the Greenberg-Hastings rule behind textbook models of excitable tissue.
  Every cell holds nothing but an integer on a private clock with a fixed
  number of ticks, and each step it advances to the next tick only if
  enough of its eight neighbors are already sitting one tick ahead of
  it; otherwise it waits. No diffusion equation (nights 2 and 9), no
  convolved mass and sigmoid (night 11), no sine-coupled continuous phase
  (night 12) — just an integer comparing itself to a neighbor count. Left
  to run from pure noise that asymmetry alone is enough to spawn rotating
  cores, little pinwheels chasing their own tail around a point that can
  never quite catch up to itself, the same mechanism, translated to a
  grid of integers, that drives the real spiral waves seen in the
  Belousov-Zhabotinsky chemical reaction and in cardiac tissue mid-
  arrhythmia. Color reads each state as a point in an excitation cycle
  rather than a plain hue wheel — long dark rest, a fast climb through
  electric blue, a white-hot crest at the wavefront itself, then a slow
  ember cool-down through amber and burnt red back to black — so a locked
  field of rotors reads as lightning frozen mid-strike, tails smoldering
  behind each bright arc. The neighbor threshold breathes over minutes,
  sliding the lattice between many small fast-spinning cores and a few
  large slow ones. Move the cursor to lightly spark the medium, nudging
  nearby cells one tick ahead the way dragging a match through dry tinder
  catches unevenly and sends small ripples outward; click to write a full
  turn of the cycle around a point outright, a topological wind-up with
  nowhere to unwind except by spinning, which plants a rotor on the spot
  every time. Open the file directly in a browser.

- **2026-08-16** — `2026-08-16-domain-frost.html`: a sixteenth technique,
  and the first driven by thermodynamics rather than a field, a swarm, a
  force law, or a rule table that fires the same way every time. A 2D
  Ising spin lattice, updated by the Metropolis-Hastings algorithm: every
  cell holds nothing but +1 or -1, and each proposed flip is accepted or
  rejected by weighing its energy cost against a temperature — sometimes
  taking an uphill move purely because chance says so. Night 12's Kuramoto
  lattice and night 14's cyclic automaton were both deterministic; this
  isn't — two runs from identical spins diverge immediately, since the
  update is a coin flip weighted by the Boltzmann factor
  min(1, exp(-dE/T)), the same statistic that governs slow-cooled steel
  and real ferromagnets. No diffusion equation, no sigmoid, no
  phase-coupling sine — just a Hamiltonian the noise is, on average,
  sliding downhill. Coupling reaches all eight neighbors so domains
  condense into rounded continents rather than blocky diamonds, colored
  amber for spin up and deep indigo for spin down, with every fresh flip
  flashing warm white and cooling back into its domain's hue over the
  next second so the lattice reads as embers settling rather than a flat
  two-color mosaic. Temperature breathes slowly across the critical point
  (Tc ~ 2.269) over several minutes — well below it a few huge continents
  lock in place, well above it dissolves into fine simmering static, and
  crossing it directly produces critical opalescence, domains of every
  size at once. Move the cursor to lay down a local field that pulls
  nearby spins to align with it, like a magnet imposed on a ferromagnet;
  click to quench a patch back to random noise and watch it recrystallize
  with its own fresh color history. Open the file directly in a browser.

- **2026-08-15** — `2026-08-15-bough-grammar.html`: a fifteenth technique,
  and the first built from a formal grammar rather than a field, a swarm, a
  force law, or a cellular automaton. This is an L-system — Aristid
  Lindenmayer's rewriting grammar, invented to model how a filament of algae
  cells divides (an odd echo of night 2's literal cell-division
  reaction-diffusion), later turned by Prusinkiewicz into a recipe for
  procedural plants: replace every "F" in a string with a longer string,
  over and over, then hand the finished string to a turtle that reads it
  left to right — F to step forward and draw, + and - to turn, [ and ] to
  push and pop a branch point on a stack. Three productions are chosen at
  random for every F, five generations deep, so no two trees share a
  skeleton. Nothing here wanders (night 10), reinforces a trail (night 3),
  or seeks light one greedy step at a time (night 13, the closest
  relative) — the entire branching structure exists as a finished sentence
  before a single pixel is drawn, and the turtle is just reading it aloud.
  What looks like growth is a reveal of that fixed sentence, letter by
  letter; what looks like wind is the same fixed sentence re-read every
  frame with a small breathing bias on the turtle's heading, stronger the
  deeper the branch — the grammar never changes, only how it is spoken.
  Bracket-nesting depth doubles as both structure and color: a bark-brown
  trunk climbs through mossy jade into blossom pink and pale, glowing white
  at the outermost twigs, where loose petals scatter and catch the bloom
  pass, all set against a faint twinkling starfield. A small grove holds
  three to six saplings at once, each aging on its own clock — grow, hold,
  fade to black — and quietly reseeding itself elsewhere when it dies. Move
  the cursor to bend nearby boughs toward it like sunlight; click to plant a
  fresh tree, retiring the grove's oldest once it's full. Open the file
  directly in a browser.
