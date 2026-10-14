# Open question: is AI a "concrete" waiting for its theory?

**Status:** rough note and open question. Mostly speculation, apart from the historical precedents. Come back to it when starting on ML.

## The question

Tobias Dantzig: "The concrete has ever preceded the abstract." Working practice tends to come before the theory that explains it. See [Positional notation and zero, Section 7](../topics/numeration/positional-notation-and-zero.md#7-how-well-does-dantzigs-principle-hold-up) for how far that holds and where Dantzig overstated it.

Are deep learning and LLMs a concrete practice of this kind, one that will force a new branch of mathematics or science?

## Precedents: the device came before the theory

| Device that worked without being understood | Theory it eventually forced |
|---|---|
| steam engine (Newcomen 1712, Watt 1770s) | thermodynamics (Carnot 1824, Clausius, entropy) |
| telegraph and telephone engineering | information theory (Shannon 1948): bits, channel capacity |
| Heaviside's operational calculus and impulse function (1880s–90s) | theory of distributions (Schwartz, 1940s) |

There's a common saying that science owes more to the steam engine than the steam engine owes to science.

**Counterexamples, where theory came first:** Maxwell's equations led to radio (Hertz). Turing's 1936 machine came before real computers. So the pattern is common, not guaranteed.

## Why deep learning looks pre-theoretical

These things are observed reliably but not well explained:

- **Generalization.** Networks with far more parameters than training examples don't overfit the way classical statistics predicts. "Double descent" contradicts the textbook bias–variance curve.
- **Scaling laws.** Loss falls as a smooth power law in compute, data and parameters, over many orders of magnitude. They are empirical, not derived, a bit like Kepler's laws before Newton.
- **Emergent abilities.** In-context learning, "grokking" (generalization arriving suddenly, long after the training data is fitted), and abilities that weren't explicitly trained.
- **Optimization.** Gradient descent on a huge non-convex loss landscape reliably finds good solutions.

## Candidate theories (partial, none has won)

- **Neural tangent kernel:** in the infinite-width limit, training behaves like kernel regression.
- **Mean-field and statistical mechanics of learning:** treat training like a physical system with many interacting parts.
- **Singular learning theory** (Watanabe): algebraic geometry for models whose parameters aren't identifiable, which describes neural networks.
- **Mechanistic interpretability:** reverse-engineer trained networks circuit by circuit. This is closer to natural history or biology than to physics.

## Things to keep in mind

- **The theory may be about something broader than the device.** Thermodynamics turned out to be about energy and probability in general, not about engines. A theory prompted by LLMs might be about learning, compression or high-dimensional probability, with neural networks as just the first example.
- **It may be old maths combined in a new way** (statistics, dynamical systems, information theory) rather than a brand-new branch.
- **A second way it could play out: AI as an instrument.** The telescope and microscope led to new science by showing things nobody had seen. AI used as a tool for mathematics (proof assistants like Lean plus models, conjecture search) might play that role. Then AI would be *producing* new abstractions, not *needing* one.

## Open questions for later

- What would count as the "Carnot moment" for deep learning, the question whose answer forces the theory? (Possibly: why do scaling laws have the exponents they do?)
- Is there a quantity that plays the role entropy played for engines?
- Which existing foundations will matter most? My guess: linear algebra, probability, optimization, information theory. Those are the tools every candidate above is built from.

## Prerequisites to learn first

Linear algebra (done abstractly), probability and statistics, optimization, information theory (Shannon). Later: kernel methods, a little statistical mechanics.
