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

- **2026-09-24** — `2026-09-24-shared-weather.html`: a fiftieth technique,
  and the first chaotic system that is dissipative rather than conservative
  — one where phase space itself contracts. Nights 5 and 26 were chaotic
  too: the three-body waltz's mutual gravity and common-descent's double
  pendulum are both Hamiltonian, so by Liouville's theorem the volume a
  cloud of nearby starting conditions occupies is exactly preserved forever,
  only stretched and folded, and common-descent's own added drag was
  strong enough to kill the chaos outright, settling every pendulum back
  toward a calm, ordinary, non-chaotic rhythm at the bottom of its swing.
  This is the Lorenz system: dx/dt = σ(y−x), dy/dt = x(ρ−z)−y,
  dz/dt = xy−βz, the three equations Edward Lorenz kept in 1963 after
  radically truncating Barry Saltzman's Fourier model of atmospheric
  convection down to its three most energetic terms — x the intensity of
  a convective roll, y the temperature difference between its rising and
  falling currents, z how far the vertical temperature profile bows away
  from a straight line. Its divergence, σ+1+β combined, is a constant
  negative number everywhere in the state space, so unlike nights 5 and
  26 this system is always, unconditionally, shrinking every volume it
  contains toward zero — and yet it is exactly as chaotic as they are,
  nearby trajectories still separating exponentially with the same
  positive Lyapunov exponent that made those nights' bundles unravel.
  Both are true at once because contraction and separation happen along
  different directions: trajectories are squeezed flat onto a
  two-lobed, self-similar surface with no thickness and a fractal
  dimension near 2.06, then spread apart exponentially only within that
  surface, matting it into an object Ruelle and Takens named a "strange
  attractor" in 1971. Every one of the forty threads on screen starts
  from a different, often wildly different, point in space, seeded
  nowhere near each other or the attractor itself, yet all of them, in a
  few seconds, get reeled onto the identical double-lobed shape and
  begin the same unpredictable back-and-forth between wings — the
  opposite emphasis from common-descent's identical starting bundle
  tearing apart, and the truer origin of "the butterfly effect," a
  phrase Lorenz didn't coin until a 1972 talk but had already lived
  through in 1961, when he re-ran a forecast from a printout rounded to
  three decimals instead of the six his program actually carried and
  watched the weather it produced diverge completely within an
  in-machine month. Runge-Kutta integrates all forty streams at once,
  each colored along a blue-to-gold gradient by which wing it currently
  occupies, so a color change on screen is a trajectory changing its
  mind about which lobe to circle next — itself a chaotic, symbolic
  sequence with no pattern a human eye has ever found in it. Drag to
  orbit the attractor and see the two lobes from any angle; scroll to
  dolly in and out; click anywhere to drop a fresh storm from whatever
  point you chose, and watch it forget its origin and join the shared
  shape within moments. Left alone, the view keeps slowly turning on its
  own. Open the file directly in a browser.

- **2026-09-23** — `2026-09-23-undecided-ground.html`: a forty-ninth
  technique, and the first fractal boundary drawn by convergence rather
  than escape. Night 43's Julia set asked every pixel a private
  yes-or-no question about z² + c — does this point's orbit run to
  infinity, or stay bound forever — and painted the boundary between
  those two fates. This asks a different question of the same shape:
  under Newton's method applied to a polynomial with six complex roots,
  which root does this starting point eventually fall into? There is no
  escape here, no third fate — every point in the plane is drawn, sooner
  or later, into one of six wells — so instead of one bounded region set
  against one unbounded one, the plane splits into six basins of
  attraction, and the fractal is what happens wherever three or more of
  them meet. Arthur Cayley posed exactly this in 1879, the
  "Newton–Fourier imaginary problem," and solved the two-root case by
  hand in an afternoon: the boundary is a single straight line, the
  perpendicular bisector between the roots, because either root's pull
  only ever wins outright. He tried three roots next and got nowhere; it
  took Fatou and Julia's own turn-of-the-century work on iterated
  rational maps to explain why, and nobody actually saw the shape of the
  answer until computer graphics could render it, a century later. Six
  roots sit on screen here, not three, each one a complex number treated
  as a physical thing rather than a fixed constant: a small, restless
  particle system nudges every well with a weak pull back toward the
  center, a soft mutual repulsion so no two ever quite collide, and a
  little noise, so the map keeps drifting even untouched. The iteration
  itself never computes the polynomial or its derivative directly — for
  a polynomial given as a product of its roots, Newton's update
  algebraically collapses to z' = z − 1 / Σᵢ 1/(z − rᵢ), summing one
  reciprocal per root and inverting once, which is both cheaper per
  pixel and the reason moving a single root reshapes the whole boundary
  at once rather than demanding a full polynomial refit. Color carries
  two answers at once: which well a pixel eventually settles into sets
  its hue, how many iterations that took sets its brightness, so each
  basin reads as a smooth field near its own well and frays into thin
  concentric filigree approaching the boundary, self-similar at every
  scale it's viewed — the same lacework Night 48's caustic net folded
  into cusps, arrived at here by counting the steps of an algorithm
  instead of crossing rays. Drag a well to relocate it and watch the map
  answer instantly, every basin it touches reshaping live; drag open
  ground to pan; scroll to zoom into the boundary's own detail, which
  never resolves into a smooth curve no matter how far in you go. Left
  alone, the wells keep drifting on their own, so no arrangement of the
  boundary lasts long enough to call finished. Open the file directly in
  a browser.

- **2026-09-22** — `2026-09-22-drowned-light.html`: a forty-eighth technique,
  and the first governed by geometric optics -- what light does when it bends
  -- rather than a field, a swarm, an agent, or a discretized solver update
  shaded directly onto the screen. Every earlier night that touched water
  rendered its surface: night 4's glass-tide lit a wave height field with
  Blinn-Phong reflection, one bounce, stopping at the same pixel it left.
  Tonight the surface itself never appears on screen at all. A shallow sea is
  built the ordinary way, as a sum of eight plane-wave trains at different
  wavelengths, directions, and speeds, plus a handful of short-lived radial
  ripple packets seeded by the cursor, each a damped sinusoid expanding
  outward from where it was dropped. But instead of shading that field, every
  point on it is treated only as a lens: its local slope gives a surface
  normal, Snell's law bends a bundle of parallel sun rays through it at the
  ratio between air and water (1 : 1.33), and each ray is carried on in a
  straight line until it crosses a floor some distance below. Nothing about
  any single ray is interesting -- what matters is where a great many of them
  land together. A flat patch of sea sends its rays down in a neat,
  undistorted grid; a patch curved like a lens focuses its rays into a small,
  bright knot, and a patch curved the other way spreads them thin into a dark
  gap. The bright, tangled net that results -- the same one on the floor of
  every sunlit swimming pool, and under the base of any wine glass -- is not
  drawn, it is counted: one ray landing per bin of an accumulation buffer, the
  method Nishita and Nakamae described for rendering underwater light in 1994.
  The reason it resolves into sharp cusps and folds rather than a smooth
  gradient is exactly the mathematics Michael Berry and Colin Upstill worked
  out for caustics in 1980 as instances of Thom's catastrophe theory: the map
  from a ray's starting point to its landing point stops being one-to-one
  wherever neighboring rays cross, and light piles up precisely on that fold.
  None of that is solved for symbolically here -- it falls out on its own from
  tens of thousands of straight lines and one refraction each, recomputed from
  scratch every frame as the sea moves. The sun's own angle drifts slowly and
  without pattern, sliding the whole net sideways over the course of minutes
  the way real sunlight does over a longer day. Move the cursor to trouble the
  surface, trailing a wake of small ripples that bend the net beneath it;
  click to drop a single stone and watch one ripple ring pass under the
  caustics, forking and refocusing them as it crosses. Open the file directly
  in a browser.

- **2026-09-21** — `2026-09-21-rim-of-mirrors.html`: a forty-seventh
  technique, and the first where the plane itself is not flat. Every night
  before this one — fields, swarms, force laws, automata, grammars,
  tessellations, even the pentagrid two nights ago — took place on
  ordinary Euclidean paper; the only thing that ever changed was the rule
  laid on top of it. Tonight the rule is the simplest one there is — a
  mirror, reflected in a mirror, reflected in a mirror — and the only
  thing that changes is the geometry it's reflected in. This is a {7,3}
  tiling of the hyperbolic plane, regular heptagons meeting three to a
  vertex, drawn in the Poincaré disk model: a faithful map of the whole
  infinite hyperbolic plane compressed into a finite circle, where
  straight lines (geodesics) become arcs that always cross the boundary
  at right angles, and every heptagon on screen is exactly congruent to
  every other in the only distance that actually matters here, however
  small it's been squeezed by the time it reaches the rim. The
  construction is a kaleidoscope, not a simulation: start with one
  heptagon sized so its interior angle is exactly a third of a circle
  (solved from a single hyperbolic right-triangle identity, cosh R =
  cot(π/7)·cot(π/3)), then reflect it across each of its seven edges to
  get seven neighbors, reflect each of those across their own edges, and
  keep going — breadth-first, mirror after mirror, discarding any copy
  that lands where one has already landed — until the copies are packed
  too close to the rim to matter. Every reflection is computed the way a
  billiard reflects off a curved cushion: use the disk's own symmetry to
  slide the mirror line through the origin, reflect across that diameter
  by ordinary conjugation, slide back. No copy is ever drawn twice, and
  none is approximated — the seven-sided outline is the true geodesic
  polygon, its edges sampled along that same origin-trick whenever a tile
  is large enough on screen for the bend to show. Night 19's power
  diagram and night 46's pentagrid both tiled a flat plane by a rule
  about distance or position; this tiles by a rule about mirrors, and the
  reason it can do with regular heptagons what no flat tiling ever could
  — three meeting at a vertex with room to spare — is that the surface is
  curved to make room for them. This is the same picture Donald Coxeter
  handed M.C. Escher at a conference in Amsterdam in 1954, a diagram of a
  hyperbolic tessellation that Escher, who had no training in the
  mathematics, spent the next four years teaching himself to reconstruct
  by hand; it became the four "Circle Limit" woodcuts, and the vanishing
  fish and angels and devils in them are not really shrinking toward the
  rim, any more than these heptagons are — every one is the same size,
  out where the metric lives, and it's only the flat page, or the flat
  screen, straining to hold an infinite curved world that makes the ones
  near the edge look like they're running out of room. Color drifts from
  a warm amber spark at the center through rose and magenta to a cooling
  violet as the reflections stack up, each ring of copies a little darker
  than the one it was born from, a fine dark seam traced at every shared
  mirror line. Nothing here moves on its own except a slow unforced
  drift, the whole disk wandering along a lazy, irrational circuit around
  wherever it currently sits; drag to grab the tiling directly and pull
  any part of the infinite pattern into the middle — the disk never runs
  dry, because a hyperbolic isometry maps the whole thing onto itself, so
  wherever you drag from is exactly as full as where you started. Click
  without dragging to let go and drift back to center. Open the file
  directly in a browser.

- **2026-09-19** — `2026-09-19-fivefold-hush.html`: a forty-sixth technique,
  and the first built from no field, no lattice, no swarm, no force law,
  and no forward-in-time process at all — every tile placed by a single
  piece of closed-form algebra rather than a rule stepped forward one
  frame at a time. This is de Bruijn's pentagrid construction (1981): five
  families of parallel lines, spaced one unit apart and 72° apart from
  each other so their five directions land exactly on a pentagon, each
  family free to slide by its own real-numbered offset. Every point in
  the plane sits on one side or the other of every line in all five
  families at once, and that one five-digit reading — which strip of
  family 0, which strip of family 1, and so on — is unique to the little
  region it's standing in; running the same five numbers back through the
  five directions that produced them lands on a single vertex, and the
  four regions that meet at any one crossing of two lines land on the
  four corners of a rhombus. Ten unordered pairs of the five families, ten
  rhombus orientations, and only two shapes among them — a 72° fat rhombus
  where the crossing families sit one apart in the pentagon's order, a
  36° thin one where they sit two apart — tiling the entire plane without
  ever repeating and settling, as it grows, toward the golden ratio's own
  value for how many fat rhombi there are for every thin one. It's the
  same two-tile aperiodic set Roger Penrose found by hand in 1974; de
  Bruijn's contribution was showing that every valid arrangement of them
  is just a flat slice through this multigrid, which is itself the shadow
  a five-dimensional cubic lattice casts when it's cut at the right angle.
  Night 43's Julia set also answered a private yes-or-no question at every
  point independently, but by iterating a map to see whether it escapes;
  nothing here ever iterates — five numbers, five directions, one lookup,
  done. Night 19's power diagram also tiled the plane from a handful of
  seed parameters, but by nearest-seed distance, a purely local and
  metric rule; a pentagrid cell's identity depends on its position against
  five infinite lines, not on distance to anything. The five offsets are
  the only moving part, and moving one doesn't drag a region of the
  picture the way a parameter drags Night 42's attractor — it only flips
  the sparse, scattered rhombi sitting close enough to one of that
  family's lines from fat to thin or back, the rest of the tiling not
  even noticing, which is the actual mechanism — a "phason flip" —
  physicists reach for to explain how a real quasicrystal can quietly
  rearrange itself without ever breaking its long-range order. That order
  is not a metaphor here: this is the same five-fold symmetry Dan
  Shechtman found in an electron-diffraction pattern in 1982, dismissed
  for two years because a crystal repeating in five-fold symmetry was
  supposed to be mathematically impossible, and awarded the Nobel Prize
  in Chemistry in 2011 once it was accepted that quasicrystals were real.
  Two families of orientation carry two palettes — five shades of ember
  gold for the fat rhombi, five of deep indigo for the thin, one hue per
  pair of line families, with a fine dark seam traced at every shared
  edge. The five offsets drift on their own slow, mutually irrational
  clocks, so the pattern is never quite still; move the cursor to bend
  two of them directly and watch the flips ripple through in scattered
  unison rather than a wave; click to cut an entirely new slice through
  the same five-dimensional lattice and let the whole rose window
  reassemble itself from a flash of white. Open the file directly in a
  browser.

- **2026-09-18** — `2026-09-18-unwritten-treaties.html`: a forty-fifth
  technique, and the first where every agent's only knowledge of the world
  is which of a handful of kinds every other agent belongs to. This is
  Particle Life — the pairwise force law popularized as "Clusters" by
  Jeffrey Ventrella and later as a real-time demo by Tom Mohr — reduced to
  a single rule: every pair of particles within reach feels a signed force
  read off a fixed species-by-species matrix, strongly repulsive at
  contact, then either attracting or repelling through a wider ring
  depending on that one number, and nothing at all beyond it. Night 8's
  boids blended three separate steering rules — separation, alignment,
  cohesion — computed and summed every frame; there is exactly one rule
  here, and it carries no notion of heading at all, yet flocks, chases, and
  stable rings still emerge from six kinds of particle relating to each
  other through a matrix that isn't even symmetric — species A can be drawn
  to B while B is repelled by A, which is what turns some clusters into
  slow-orbiting binaries and others into one kind endlessly fleeing another
  around the torus. Night 41's hard disks resolved exact pairwise
  collisions the instant two circles touched; nothing here ever resolves,
  contact is just the steepest part of a continuous force curve, softened
  enough that colonies interpenetrate and separate again rather than
  bouncing. Night 39's predator and prey lived only as two numbers pushed
  through a shared rate equation, no individuals, no positions; here the
  chase is the same shape wearing every particle's own coordinates, an
  aggregate behavior nobody wrote down watching itself happen from eight
  hundred independent bodies. Night 16's Ising spins and night 12's
  Kuramoto phases both coupled through fixed, symmetric neighborhoods; here
  the neighborhood is whoever is currently close enough, which keeps
  changing as everyone moves, and the coupling strength itself depends on
  which two kinds happen to have drifted into range. Positions wrap on a
  torus, neighbors found each frame through a uniform spatial grid, so no
  boundary wall ever interrupts a chase. Each of the six kinds keeps its
  own hue, brightening toward white the faster it moves, drawn with
  additive light so a dense cluster's core glows hot where members
  overlap, and a slow trailing fade behind every frame leaves a comet's
  tail on anything moving fast enough to outrun its own afterglow. The
  overall force strength breathes over about seventy seconds between a calm
  regime where clusters settle into slow stable orbits and an energetic one
  where the whole board churns and re-sorts. Move the cursor through the
  field to startle everything nearby away from it, like a hand through an
  ant farm; click anywhere to tear up the entire relationship matrix and
  hand the same eight hundred particles an entirely new, unwritten set of
  treaties to live under. Open the file directly in a browser.

- **2026-09-17** — `2026-09-17-phantom-convoy.html`: a forty-fourth
  technique, and the first governed by a follow-the-leader rule carrying
  its own built-in overreaction rather than a field, a swarm behavior, a
  force law, a spin flip, or exact collision mechanics. This is the
  Nagel-Schreckenberg model (1992), the cellular automaton traffic physics
  was built on: cars live on a ring of discrete cells, hold nothing but an
  integer velocity, and every tick apply four rules in lockstep — speed up
  by one if nothing's close, slow down to whatever gap actually remains
  ahead, then, with some fixed probability, brake one notch below even
  that for no reason at all, and finally move. Night 16's Ising lattice
  also flips by a coin weighed against a rule, but that coin weighs an
  energy cost against a temperature; this coin weighs nothing — it fires
  the same regardless of what's ahead, a driver's plain inattention rather
  than any physics minimizing anything. Night 41's hard disks actually
  touch, exact elastic collisions solved pairwise; nothing here ever
  collides, a car's own speed is capped below its gap every tick so
  contact is structurally impossible, yet gridlock still happens, which is
  the entire point being demonstrated. That one extra unforced
  deceleration is the whole mechanism behind the phantom traffic jam — a
  dense-enough road left alone, no accident, no lane closure, no reason
  visible to anyone in it, spontaneously knots into stop-and-go clusters
  that crawl backward against the flow of traffic, each car braking a beat
  later and a beat harder than the one ahead of it until the wave outruns
  its own cause. It isn't a metaphor for the phenomenon; it is small
  enough to be the actual mechanism, the same one a 2008 ring-road
  experiment filmed forming from nothing in real cars on a real track.
  Four lanes share the loop, cars weighing a blocked lane against a
  clearer neighboring one and a safe gap behind before committing to a
  change, so jams that start in one lane spill sideways into the others
  exactly the way real congestion does. Color reads velocity directly,
  brake red at a dead stop climbing through ember and gold to a near-white
  cruise at top speed, with a sharp red flash on any car whose speed just
  dropped, so a jam's shockwave shows as a pulse of brake light visibly
  running upstream through a river of gold. Total traffic breathes slowly
  over about a minute between light and heavy, crossing the model's own
  critical density from the free-flow side to the jammed side and back.
  Move the cursor near the loop to lean on the nearest stretch of road
  like a rubbernecking zone, capping speed locally and watching a jam
  nucleate exactly there; click anywhere to stall a car in place near the
  loop for a few seconds and force everyone behind it to find a way
  around. Open the file directly in a browser.

- **2026-09-16** — `2026-09-16-wandering-threshold.html`: a forty-third
  technique, and the first where nothing is drawn as a particle, a lattice
  cell, or a histogram bin at all — every pixel asks its own private
  yes-or-no question, answered by iterating one complex map, z' = z² + c,
  starting from that pixel's own coordinate. Night 42's Clifford attractor
  ran a few thousand points through a fixed map and let their accumulated
  landings paint a shape; night 22's fractal flame ran a chaos game, a
  different randomly-chosen affine map at every step, into a persistent
  histogram. Both point-sample a plane and build an image out of where
  points end up. This inverts that: the plane itself, one pixel at a time,
  is the thing being tested — does this starting point's orbit stay
  bounded forever under z² + c, or does it eventually run to infinity?
  Bounded points render as void, the same near-black as the page itself;
  escaping points are colored by how fast they escaped, a smooth,
  continuous count blending the log-log of the escape radius into the
  integer iteration count, which is what keeps the color bands from
  showing their seams. The knife-edge between those two answers — close
  enough to bounded that an orbit wanders for a long time before finally
  running off, or never runs off at all — is the Julia set, and it is
  fractal for a specific reason: it is the closure of every repelling
  periodic orbit of the map, and z² + c folds space onto itself just
  enough at every scale that the boundary between staying and leaving can
  never simplify into a smooth curve. Night 40's amber suspension found a
  boundary too, but that one was a level set of a finite sum of soft
  falloffs, entirely local and computable from nearby sources; this
  boundary is a global, infinite-horizon question about a single point's
  whole future, only ever approximated by capping how many iterations a
  pixel is allowed before it is called bounded by default. c is never
  fixed. A short list of the constant's historically named landmarks — a
  dendrite, the San Marco spiral, a Siegel disk, Douady's rabbit, the
  airplane, a scattering of dust — is visited in a slow, eased loop,
  lingering near each named shape and hurrying through the featureless
  country between them, the same lean-toward-a-drifting-baseline
  structure night 42 used on the Clifford map's own coefficients, but
  leaning a single complex number instead of two of four reals. Move the
  cursor to pull the constant away from that baseline, warping whatever
  shape is currently showing without resetting its identity; click to
  pick a point on screen and fall toward it, the view easing into a steep
  zoom centered exactly there and back out again, so the same fractal
  boundary that built the wide shape reveals another copy of comparable
  detail however far in you go. Iteration depth and internal render
  resolution both adapt each frame to whatever the machine can sustain,
  so the image softens under load rather than the animation stalling.
  Open the file directly in a browser.

- **2026-09-15** — `2026-09-15-folded-horizon.html`: a forty-second
  technique, and the first with no field, no lattice, no agents, and no
  evolving population at all — a single fixed nonlinear map, iterated
  forever. The Clifford attractor: x' = sin(a·y) + c·cos(a·x),
  y' = sin(b·x) + d·cos(b·y). Four numbers and two trig sums are the
  entire rule; there is no diffusion term, no neighbor lookup, no
  collision, no birth or death. Night 17's harmonograph came closest — a
  handful of continuous oscillator terms summed into one pen's position —
  but that pen draws a single unbroken thread and the shape is whatever
  curve it traces over time. Here a few thousand points, seeded at
  random, are each run through the same map independently and forever;
  no point remembers the last one, none interacts with any other, and
  the fractal wings that appear are not drawn by anyone — they are
  simply the only place left for a point to land once the map has folded
  the plane over itself enough times, the same folding-and-stretching
  that makes any chaotic map's attractor a fixed shape even though no
  individual orbit ever repeats. Night 10's lightning grew by thousands
  of blind random walks freezing on contact; this has no randomness
  anywhere in its dynamics, only in where each point happens to start —
  everything that looks organic here is pure determinism, folded until
  it looks improvised. Because sine and cosine are bounded by one, the
  entire attractor is provably confined to a box of half-width 1+|c| and
  half-height 1+|d|, so the frame is scaled straight off the live
  parameters rather than measured from the points themselves. Color
  carries no physical quantity — no speed, no temperature, no age — only
  which of the map's four sign-quadrants (the sign of cos(a·x) crossed
  with the sign of cos(b·y)) a point currently occupies, since it is
  exactly the folding between those quadrants that builds the wings;
  brightness alone answers to how far a point just jumped, so the
  fast-folding seams of the attractor glow and the slow-dwelling regions
  stay a dim ember. The four parameters drift on their own slow
  independent walks, breathing the wings from a tight rose into a loose
  scattered fan and back over a couple of minutes, close enough to keep
  one attractor's identity but never quite settling. Move the cursor to
  lean two of the four parameters toward it, warping the fold in real
  time and snapping back toward the drifting baseline when the pointer
  leaves; click to draw an entirely new set of four parameters — a
  different species of attractor — and let the plane refold itself
  around it from a flash of white. Open the file directly in a browser.

- **2026-09-14** — `2026-09-14-mean-free-hush.html`: a forty-first
  technique, and the first built on exact pairwise hard-disk collision
  rather than a field, a lattice, a swarm rule, or a continuum solver.
  Night 9's ink weather solved a real velocity field on a fixed grid;
  night 21's borrowed weight was particles too, but smeared into a
  continuous density by an SPH kernel, never actually touching; night 34's
  lattice wake ran a lattice-gas automaton, particles confined to a
  hexagonal lattice with a handful of discrete velocity directions. This is
  closer to the thing kinetic theory was built to describe in the first
  place — a few hundred hard disks with continuous position and velocity,
  each frame's overlaps found through a uniform spatial grid rebuilt from
  scratch, resolved with the same exact two-body elastic impulse a
  billiards engine would use, mass drawn from disk area so heavier bodies
  push back harder. A wall down the center splits the box in two with a
  single gap in it. Every particle that reaches the left outer wall is
  handed a fresh velocity sampled from a hot Gaussian, the
  Maxwell–Boltzmann speed distribution a thermal reservoir imposes on
  whatever touches it; every particle reaching the right wall gets the same
  treatment from a colder distribution. Nothing forces the two populations
  to mix — only the gap does that, one collision at a time — so color, read
  straight off each disk's instantaneous speed from a red hot to blue cold,
  shows the whole story: two separate temperatures on either side, a
  violet, turbulent jet where they cross, and a texture that never fully
  homogenizes because the reservoirs keep resupplying the difference
  they're fighting to erase. A few heavier golden disks ride inside the
  swarm doing nothing themselves, carrying no reservoir, no purpose but to
  be shoved — their own fading paths, drawn as a faint trailing line each
  keeps behind it, are exactly the random walk Einstein derived from unseen
  molecular bombardment in 1905 and Perrin confirmed by watching pollen
  grains through a microscope. Move the cursor near the dividing wall and
  it takes hold of the gap, sliding it to wherever the pointer sits; left
  near the wall's own oscillation, the gap drifts on a slow sine instead.
  Away from the wall, the cursor stirs — every disk nearby gets a gentle
  push outward, a private breeze. Click anywhere to strike a spark:
  everything within reach of the click is kicked to a sudden, shared high
  temperature and left to cool back into the crowd on its own. Open the
  file directly in a browser.

- **2026-09-13** — `2026-09-13-amber-suspension.html`: a fortieth technique,
  and the first to extract an explicit boundary from a field rather than
  shade a field's interior directly, walk a ray into it, or lean on a
  physics solver's own particles for shape. Every nucleus in a small pool
  contributes a "soft object" falloff (Wyvill, McPheeters & Wyvill, 1986) of
  its distance — (1 − d²/R²)³ inside its own reach, zero beyond it — and the
  frame's entire shape is nothing but the level set where the sum of every
  nucleus's falloff crosses one fixed threshold. Night 23's raymarcher
  walked a ray through a signed distance field and shaded whatever surface
  it hit; night 21's SPH fluid never had a boundary at all, only a cloud of
  kernel-weighted density read pixel by pixel. This instead runs marching
  squares, the two-dimensional sibling of Lorensen and Cline's 1987 marching
  cubes, over a coarse grid laid across the field: every cell's four corners
  are tested against the threshold, and wherever two neighboring corners
  disagree, linear interpolation along that one edge finds the exact
  crossing point, which is stitched corner-to-crossing-to-corner into that
  cell's own sliver of the boundary — the same trick medical imaging uses to
  turn a CT scan's density values into an explicit organ outline. No cell is
  colored by hand; every fill is read straight off a temperature the field
  itself carries, the weighted average of whichever nuclei are actually
  contributing there. A little over a dozen blobs of amber wax drift inside
  a glass tube, each one nothing but a position, a velocity, and a
  temperature that always relaxes toward whatever a shelf of heat at the
  tube's floor and a cool neck above are independently pulling it toward —
  hotter near the floor, cooler near the neck — but only within a thin
  boundary layer at each end; a blob coasting through the middle of the tube
  carries whatever heat it left the last boundary with, nearly unchanged,
  which is what lets it overshoot its own neutral height by a wide margin
  in either direction before the next boundary layer finally catches up
  with it. Buoyancy is a single line: a nucleus warmer than neutral rises,
  one colder sinks, no fluid ever solved for beyond that one number, and a
  gentle drag stands in for the wax's own viscosity so nothing accelerates
  forever. The entire rise-coast-cool-sink-reheat cycle real lava lamps run
  on falls out of that one lag between a blob's position and its own
  temperature, with the field doing all the visual work of merging two
  close blobs into one shape and splitting a stretched one back into two
  the instant marching squares finds the neck between them has thinned past
  the threshold. The floor's own heat breathes slowly over a couple of
  minutes, sliding the whole tube between a sluggish simmer and a vigorous
  boil. Move the cursor to draw a warm current through the glass, nudging
  nearby blobs toward the floor's own temperature and off on their own
  climb; click to drip a fresh hot droplet in at that point, retiring
  whichever blob has gone coldest if the tube is already full. Left alone,
  the whole tube empties and reseeds a fresh stack of droplets at the floor
  every couple of minutes. Open the file directly in a browser.

- **2026-09-12** — `2026-09-12-tooth-and-clover.html`: a thirty-ninth
  technique, and the first with no field, no lattice, and no fixed population
  — an agent-based predator-prey ecology, the Rosenzweig-MacArthur model (a
  logistically-capped Lotka-Volterra) run not as two coupled numbers but as a
  few hundred individuals, each born, fed, and eventually eaten or starved on
  its own private clock. Night 8's murmuration and night 18's elective
  affinities both moved swarms of a fixed size through steering rules and a
  force matrix; this swarm has no fixed size at all, since every prey and
  every predator carries its own energy budget that a birth or a death can
  only ever move by one. Pale clover-green grazers gain energy for free, at a
  rate a slow three-minute season swings between lean and abundant and that
  thins wherever too many graze the same patch at once, the logistic term
  standing in for a finite pasture; fed enough, a grazer splits in two, its
  energy halved between parent and child, the same conservation night 37's
  evolving lineage answered to for pixels instead of calories. Amber hunters
  spend energy just by existing, sense the nearest grazer within reach through
  a coarse spatial grid rebuilt every frame rather than a brute check against
  every other agent, steer toward it, and either eat on contact — energy up,
  grazer gone — or, fed enough themselves, split the same way their prey do.
  Starve to zero calories at either trophic level and that individual simply
  stops, no rule beyond bookkeeping required for what reads, from outside, as
  population booms and famines chasing each other in a ring nobody scripted. A
  vanished grazer population drags every remaining hunter down with it and
  forces a full reseeding; a vanished hunter population instead drifts back on
  its own after a lean stretch, the way a locally-hunted species recolonizes
  from elsewhere. Move the cursor to sow a patch of grass, giving nearby
  grazers a private feast; click to drop a fresh hunting pack wherever you
  point, culling whatever bloom has gotten out of hand. Left alone, the whole
  ecology resets to a fresh scatter of both kinds every few minutes
  regardless. Open the file directly in a browser.

- **2026-09-11** — `2026-09-11-kindred-foam.html`: a thirty-eighth
  technique, and the first in which every lattice site carries a
  persistent identity rather than a bare state — the Cellular Potts
  model (Graner & Glazier, 1992), the differential-adhesion picture
  biologists use to explain why a scrambled mix of two embryonic tissue
  types will, given nothing but random jostling and a preference for
  their own kind, sort itself back into clean domains, one sometimes
  wrapped entirely inside the other, the way Malcolm Steinberg's
  dissociated-and-remixed embryo cells were once filmed doing in a dish.
  Night 16's Ising lattice already ran a Metropolis acceptance rule over
  a spin field, and night 19's power diagram already grew and shrank
  territory by a coarsening law, but neither pixel had a name: an Ising
  spin is just +1 or -1 with no memory of which domain it belongs to,
  and a power-diagram cell has a weight but no interior pixels to
  reassign one at a time. Here several hundred cell IDs each own a patch
  of the lattice, and the only move is a land grab: a random site looks
  at a random neighbor and, weighing the change in total contact energy
  against a penalty for straying from its own preferred size, either
  lets that neighbor's identity creep one pixel further or refuses —
  sometimes anyway, at a rate set by a temperature nudged upward
  wherever the cursor lingers, so the tissue nearest your attention
  turns loose and molten while the rest keeps its shape. Contact energy
  is not one number here but a table of three: rose, verdigris, and
  amber lineages each pay a different cost for touching their own kind
  versus a stranger, tuned into a hierarchy of self-adhesion, so the
  foam does not merely coarsen into arbitrary blobs the way spins do —
  it sorts, and gradually nests, the stickiest lineage drawing itself
  into clusters, the next-stickiest working around it, and the least
  self-loving type left threading the gaps between them, echoing the
  layered engulfment differential adhesion predicts for real tissue.
  Click to graft a fresh, randomly-typed cell wherever you point, a
  foreign implant the sorting has to work around. When the boundary
  energy stops falling, or a few minutes pass, the foam dissolves and a
  new scramble of a few hundred cells is poured out to sort itself from
  scratch. Open the file directly in a browser.

- **2026-09-08** — `2026-09-08-selective-memory.html`: a thirty-seventh
  technique, and the first governed by selection against a measured error
  rather than a rule, a field, a swarm, a grammar, or a hand-tuned
  interactive parameter — a (1+1) evolutionary strategy, the mechanism
  behind Roger Alsing's famous experiment reconstructing the Mona Lisa out
  of fifty semi-transparent polygons. Every other night here runs a
  process forward and looks at what it becomes; this one runs a single
  lineage of one candidate picture, mutates a clone of it at random —
  nudge a vertex, tint a color, add or remove a shape, swap two layers'
  draw order — renders that clone at a tiny scale no bigger than a
  postage stamp, and compares it pixel by pixel against a hidden target
  scene nobody ever shows the viewer directly. If the mutation's error is
  lower, the clone replaces the original outright; if not, it is simply
  thrown away and never influences anything again. There is no
  population, no crossover, no fitness proportional to anything except a
  single number getting smaller — the closest relative in this project's
  own history is night 22's fractal-flame chaos game, which also renders
  through iteration, but that iteration searches nothing and answers to
  no target; every accepted change here has to have earned its place by
  literally looking more like the thing it is blindly trying to
  remember. Early on the mutation step is enormous — whole polygons
  lurch across a third of the canvas, colors swing wildly — so the
  picture finds its coarse composition, sky from hill, light from dark,
  in seconds; that step anneals down over the following minutes the way
  simulated annealing cools, so what starts as blocking in shapes ends
  as nudging a single vertex by a hair's width, chasing diminishing
  error into fine detail no one mutation could have found on its own.
  The hidden target itself is a small generated nightscape — gradient
  sky, a soft-glowing moon, a scatter of stars, two or three silhouetted
  hill ridges — regenerated from scratch every few minutes, different
  each time, so the lineage is always chasing a dream it has never
  actually seen and can only approach by trial, error, and the
  occasional lucky mutation that survives. Move the cursor to spend the
  mutation budget near it instead of scattering it uniformly across the
  whole canvas, so whatever region holds your attention sharpens first
  while the rest stays rough; click to cheat, once, exactly there —
  sampling the true hidden color at that point and planting a patch of
  it directly into the lineage without waiting for chance to find it,
  the one moment this blind process is allowed to peek. When the error
  stops falling, or a few minutes have passed, the reconstruction holds
  still, the true scene fades up underneath it so you can see exactly
  how close a few dozen polygons got, and then the whole canvas
  dissolves to black and a fresh dream begins from nothing but a single
  flat guess at the average color of what it hasn't met yet. Open the
  file directly in a browser.

- **2026-09-07** — `2026-09-07-soft-orbium.html`: a thirty-sixth technique,
  and the first governed by a smooth, integrator dynamic rather than a
  discrete replacement rule — Lenia (Bert Chan, 2018), the continuous
  generalization of Conway's Game of Life that treats a cell's
  neighborhood, its fate, and its very state as real numbers rather than a
  fixed set of counts. Night 11's SmoothLife already softened Life's hard
  birth/survival thresholds into two radii and a sigmoid, but it still
  replaced each cell's state outright every step, the way the discrete
  rule it descends from always has. Lenia doesn't replace anything: every
  cell holds a density between 0 and 1, and each step nudges that density
  by a small increment — never resets it — toward wherever a growth
  function wants it to go, so a cell's history is baked into everything
  that happens to it next rather than erased every tick. The neighborhood
  itself is a single soft ring, a bell curve peaked at half the kernel's
  radius rather than SmoothLife's two flat, hard-edged disks, so there is
  no boundary anywhere in the whole calculation, only gradients — the
  growth function judging that ring's weighted average is itself a bell
  curve too, positive near a preferred density and negative everywhere
  else, so a cell held too sparse or too crowded decays while one sitting
  in the narrow sweet spot between grows, ever so slightly, frame after
  frame. Set loose from nothing but scattered noise this dissolves to flat
  gray nothing almost immediately; it is only from a deliberately
  asymmetric seed — a teardrop of mass heavier on one side than the
  other — that the rule sometimes discovers what its inventor's community
  spent years cataloguing: a self-stabilizing blob that neither grows
  without bound nor decays to nothing, and that a mere asymmetry is enough
  to send gliding steadily across the grid, one of Lenia's many named
  species, orbium chief among them, an organism nobody wrote down and
  everybody found by search. Most seeds here die formless or bloom into a
  static mat instead, and that failure rate is the honest picture —
  nothing here guarantees a species, only searches for one. Color reads
  the growth signal itself rather than the density it acts on: a cell
  presently gaining ground glows warm amber, one presently losing it cools
  toward violet, and one sitting exactly at equilibrium settles to a
  still, pale jade — so a gliding blob's leading edge and trailing edge
  paint themselves in opposite temperatures without either ever being
  drawn on purpose, the mechanism that moves it made visible as the two
  colors chasing each other around its rim. The growth function's own
  center and width both breathe slowly over minutes, sliding the whole
  field's chemistry between a narrow, choosy tolerance that only a few
  seeds survive and a broad, forgiving one that lets almost any blob
  persist. Move the cursor to trickle a faint feed of density into the
  field, the gentlest possible seed; click to plant a full asymmetric blob
  outright, oriented in a random direction, and see what it becomes. The
  whole grid wraps at its edges, a torus with nowhere for a gliding blob
  to run off to, and roughly every three minutes — sooner if the field has
  gone fully dark or fully saturated on its own — it fades out and
  reseeds itself from a fresh scatter of teardrops. Open the file directly
  in a browser.

- **2026-09-06** — `2026-09-06-shard-lineage.html`: a thirty-fifth
  technique, and the first whose entire structure is decided by collision
  rather than by wandering, seeking, reading, or propagating a
  constraint — Jared Tarbell's Substrate (2003), the generative-art
  algorithm behind a whole decade of shattered-glass and circuit-board
  wallpapers. A crack is nothing but a point and an angle: it walks
  forward in a dead straight line, one short step at a time, until the
  cell directly ahead of it is already occupied by another crack or by
  the edge of the screen, at which instant it simply stops and is never
  touched again. Night 10's lightning also froze in place at the moment
  of contact, but every one of its walkers wandered blindly first; a
  crack here never wanders — its only freedom is the single angle it is
  born with. Most cracks are not born free at all: four in five spawn
  directly off an already-frozen line, at that line's own angle plus or
  minus a right angle and a few degrees of scatter, so a crack's
  direction is quite literally inherited from whichever wall it broke
  away from, the way a real fracture in glass or rock propagates along
  and off the planes already laid down rather than starting fresh. The
  other one in five starts from a bare, unclaimed point with no ancestry
  at all, an occasional new fault line that owes nothing to anything
  already drawn — which is why one canvas quietly ends up several
  visually distinct territories, each descended from its own founding
  crack, meeting at whatever angle their unrelated lineages happened to
  collide at. Nothing is stroked as a line: every step scatters a small
  handful of translucent grains across the crack's width, offset from
  center by their own soft falloff, so a wall of a few hundred short
  segments reads as one continuous sanded stroke rather than a row of
  dashes — Tarbell's own name for the technique, the sand painter.
  Grains lean lighter on the side facing a fixed low sun and darker on
  the side away from it, one dot at a time, so every shard reads as
  gently beveled the instant it exists, without a single explicit
  highlight ever being drawn. Grain hue drifts on its own slow clock,
  sliding the whole territory between warm cream-gold and cool ash-slate
  over several minutes, independent of the cracking underneath it. The
  canvas keeps growing until a little over half of it is claimed, at
  which point new cracks stop spawning, the surviving few finish out
  their own lines, and after a short held pause with nothing moving, the
  entire pane fades to black and a fresh scattering of founding cracks
  starts the fracture over from nothing. Move the cursor to bend nearby
  growing cracks gently toward it, a warm draft nudging a fault as it
  forms; click to plant a fresh founding crack at that exact point, in a
  random direction, no ancestry required. Open the file directly in a
  browser.

- **2026-09-05** — `2026-09-05-lattice-wake.html`: a thirty-fourth
  technique, and the third fluid in this project's history, and the first
  built from a lattice-gas kinetic model rather than a continuum equation
  solved on a grid or a swarm of particles carrying the fluid's mass with
  them. This is the lattice Boltzmann method, D2Q9 flavor: every cell
  holds not a velocity but nine numbers, one for each of the compass
  directions plus rest, each representing how much of that cell's fluid is
  presently moving that way. Two steps, repeated forever: collision, where
  each cell's nine numbers relax a fraction of the way toward the
  Maxwell-Boltzmann equilibrium implied by its own locally-summed density
  and momentum; and streaming, where each of the nine numbers simply
  slides one cell over in its own direction. Density and velocity are
  never solved for directly, the way night 9's stable-fluids solver
  explicitly built and inverted a pressure Laplacian to force the field
  divergence-free, or night 21's SPH summed a kernel over neighbors to
  estimate a smooth field at a moving point — here macroscopic flow is
  just a statistic, the zeroth and first moment of a distribution nobody
  ever asked to be smooth or incompressible, and it comes out that way
  anyway, an emergent consequence of collide-and-stream. A solid cell
  needs no boundary condition solved for it at all: streaming toward a
  wall or a planted obstacle is simply redirected back the way it came,
  one bounce-back rule standing in for what a continuum solver would spend
  a whole no-slip constraint on. Left running, a channel of leftward-forced
  inflow around any obstacle placed in it does not sit still — past a
  critical ratio of inertia to the fluid's own relaxation time, exactly
  Reynolds' own criterion, the wake behind the obstacle tears into an
  alternating train of vortices peeling off first one side then the other,
  a Kármán vortex street nobody scripted, the flow's own instability, the
  closest thing this project's fluids have had yet to the double
  pendulum's tear into chaos at night 26. Color reads vorticity rather
  than dye or height: amber-coral where the local spin curls one way,
  indigo-cyan where it curls the other, a faint white bloom laid over both
  wherever the raw speed climbs, so a shed vortex train reads as an
  alternating necklace of warm and cool beads drifting downstream while
  untroubled inflow stays a calm, near-black hush. The relaxation time
  driving that spin breathes slowly over several minutes, sliding the same
  channel between a viscous, laminar hush around its obstacles and a
  proper turbulent shedding train without touching the geometry at all.
  Move the cursor to drag a temporary eddy-maker through the current, its
  own trailing wake following it live; click to plant a permanent pillar
  wherever it stands, up to a handful at once, each throwing its own
  street into the others' way. Left alone, the whole channel dissolves its
  pillars back to a single, freshly placed one every couple of minutes,
  reseeded with its own small asymmetry so a new street always finds its
  own side to start peeling from. Open the file directly in a browser.

- **2026-09-03** — `2026-09-03-naive-retina.html`: a thirty-third technique,
  and the first in which nothing was designed at all — no field, no
  automaton rule, no grammar, no force law, no constraint solver, not even
  the hand-placed primitives of Night 23's raymarch. This is a
  compositional pattern-producing network (Stanley, 2007): a small
  feedforward neural network, three hidden layers of sixteen tanh neurons
  apiece, with weights drawn once from a Gaussian and never trained on
  anything, ever. Every pixel independently feeds its own coordinate, its
  distance from center, a constant bias, and four shared latent numbers
  through the identical seven hundred and thirty-nine weights, and
  whatever the last layer outputs becomes that pixel's color — the entire
  image is one matrix multiplication chain evaluated fresh per pixel per
  frame, on the GPU, with no memory of the pixel beside it and no history
  from the frame before. Nobody chose the shapes that result; tanh's own
  smoothness and the network's own depth choose them, the way a handful of
  random sine waves chose Night 17's rosettes without anyone drawing a
  rosette on purpose. Two hyperparameters rolled fresh with every new mind
  push the image to extremes: the input layer's own weight scale, which
  runs from a little over one to three and a half — near one and whole
  valleys of color turn over slowly, camera-close; near four and the same
  network reads as fine, lace-thin static — and a coin flip on whether x
  arrives raw or through an absolute value, which is the entire difference
  between a lopsided creature and one with an exact mirror seam down the
  middle. Color comes from the three raw outputs run through independently
  tuned sine waves, each with its own frequency, phase, and slow drift, so
  the palette keeps cycling on its own clock even on the frames when the
  network itself is unchanging. Every other night's cursor reached into
  the picture at the point where it stood — pushing ground, scattering
  pheromone, nudging a bob. This one reaches somewhere no picture exists
  at all: two of the eight shared input numbers, identical for every pixel
  on the screen, so moving the cursor a finger's width doesn't disturb a
  neighborhood, it reshapes the entire image at once, the same instant,
  everywhere — a walk through the network's input space rather than a
  touch on its output. Left to itself the network still drifts: two more
  latent inputs wheel forward on their own slow sines, and the whole set
  of seven hundred thirty-nine weights eases from the mind it was born
  with toward a freshly drawn one every twenty-some seconds, arriving with
  nothing sharper than the ease curve itself, so the picture is never the
  same for two seconds running and never once cuts. Click to abandon the
  crossfade outright and wake a brand new, uncorrelated mind on the
  spot — no relation to the one standing before it. Open the file directly
  in a browser.

- **2026-09-01** — `2026-09-01-drift-and-deluge.html`: a thirty-second
  technique, and the first built from stochastic subdivision rather than a
  field, a swarm, an automaton, a grammar, or a force law between bodies —
  and the first to run two independent generative processes on the same
  structure in sequence, one recursive and instantaneous, one physical and
  never finished. The land is grown once by diamond-square midpoint
  displacement (Fournier, Fussell & Carpenter, 1982): four random corners,
  then every square's center set to the average of its corners plus a
  random offset, every diamond's center to the average of its diamond
  neighbors plus the same, halving the grid and the offset's scale by 2^-H
  each pass, where H is the Hurst exponent — near 0 and each halving keeps
  almost as much noise as the last, jagged country; near 1 and each pass
  damps hard, rolling hills. The whole heightfield exists after eight
  halvings, before a single frame is drawn — night 1's flow field advected
  particles through Perlin's continuous, closed-form noise sampled point by
  point; this instead builds its roughness by literally subdividing a grid,
  fractal structure as a residue of the recursion rather than a formula
  evaluated fresh each time. What happens next isn't that recursion again
  but an unrelated law laid on top: particle-based hydraulic erosion (after
  Hans Theobald Beyer's 2015 thesis), thousands of individual raindrops
  rolling downhill from random high points along the local gradient with a
  little inertia, picking up sediment where the ground steepens beneath
  them and dropping it where the ground levels out, evaporating a little
  every step until there's none left to carry. No single drop reshapes
  anything visibly; a few dozen a frame, forever, is what carves ridges
  into valleys and rounds a jagged birth into something that reads as a
  real, weathered country — mass transport of rock standing in for the
  momentum transport night 9's fluid solver ran on water. Lit by a low sun
  whose azimuth wheels slowly around the whole country and whose elevation
  breathes between noon and long shadow, height and slope together read as
  water, wet sand, moss, bare rock, and snow, rock pushing through the
  snow line wherever a slope is too steep to hold it, faint contour bands
  threaded through the land the way a survey map would draw them, and a
  scattered, twinkling glint combing every shoreline the sun sits high
  enough to catch. Move the cursor to raise the ground gently beneath it, a
  slow tectonic push; click to drop a strike outright, a crater punched
  down with its own rim thrown up around the edge of impact — deep enough,
  it fills as a fresh lake on the spot — which the rain then spends the
  next stretch quietly smoothing back into the country. Left alone, the
  rain never stops falling, and roughly every couple of minutes the whole
  country dissolves into a freshly grown one with its own Hurst exponent
  and its own coastlines, absorbed into view over a few seconds rather than
  cut to. Open the file directly in a browser.

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
