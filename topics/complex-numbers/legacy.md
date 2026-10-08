# What complex numbers led to

Complex numbers began as a trick for solving cubic equations, and for about 250 years many mathematicians distrusted them. Then, in the 19th century, they turned out to be one of the most productive ideas in mathematics. Trying to understand them, extend them or rescue them led directly to quaternions, vector analysis, ideals and ring theory, Riemann surfaces and topology, and the modern study of prime numbers. They also changed what mathematicians think it means for something to *exist*.

This note goes through those lines one at a time. For each one it covers what happened, a small concrete example, and how direct the link to complex numbers really is.

**Prerequisites:** the companion note [Complex numbers: six definitions of one thing](representations.md), especially the plane picture (Section 2) and Hamilton's ordered pairs (Section 4). Some sections mention ideas from abstract algebra (rings, ideals) and explain them as they come up.

## The map

| # | Field | The link | Key figures | How direct |
|---|---|---|---|---|
| 1 | Abstract algebra | quaternions: dropping a law on purpose | Hamilton 1843, Graves, Cayley | direct |
| 2 | Vector analysis | dot and cross products split off from quaternions | Maxwell, Gibbs, Heaviside 1880s | direct |
| 3 | Ring theory | Gaussian integers → Kummer's ideal numbers → ideals | Gauss 1832, Kummer 1840s, Dedekind 1871 | direct |
| 4 | Galois theory | all roots live in $\mathbb{C}$; roots of unity | Gauss 1796–99, Abel, Galois | strong |
| 5 | Topology | Riemann surfaces for multi-valued functions | Riemann 1851 | direct |
| 6 | Analytic number theory | the zeta function of a complex variable | Riemann 1859, Hadamard, de la Vallée Poussin 1896 | direct |
| 7 | Physics and engineering | phasors, Fourier analysis, quantum amplitudes | Steinmetz 1893, Schrödinger 1926 | use rather than birth |
| 8 | Foundations | to exist is to be consistently constructible | Hamilton 1833 onwards | indirect but deep |

---

## 1. Abstract algebra: laws become choices

### What happened

Hamilton showed in 1833 that complex numbers could be defined as pairs of reals (see [representations.md, Section 4](representations.md#4-ordered-pairs-of-reals-hamilton)). The obvious next question was whether *triples* could be multiplied in the same way, giving a number system for 3D space. He tried for ten years and failed. It can't be done, as Frobenius proved in 1877.

On 16 October 1843 he saw the way out: use *quadruples*, and give up the commutative law $ab = ba$. The **quaternions** have three imaginary units with

$$i^2 = j^2 = k^2 = ijk = -1,$$

and from these it follows that $ij = k$ but $ji = -k$.

Within weeks his friend John Graves found an 8-dimensional system, the **octonions**, which also gives up associativity, $(ab)c = a(bc)$. Cayley rediscovered and published it in 1845.

### Why it mattered

Until 1843 the laws of arithmetic (commutative, associative, distributive) were taken as truths about number. Hamilton dropped one *deliberately* and still got a consistent, useful system. That opened the door to treating the laws as **choices**: pick the laws, and study the structure that results. That way of thinking is the core of abstract algebra: groups, rings, fields and algebras are all defined by which laws they obey.

### How direct

Direct. Quaternions were invented explicitly as the next step after complex numbers.

---

## 2. Vector analysis: the dot and cross products

### What happened

Write a quaternion as a real part plus a 3D vector part, $q = (s, \mathbf{u})$. Multiply two *pure* quaternions (real part zero) and you get

$$(0, \mathbf{u})(0, \mathbf{v}) = (-\,\mathbf{u} \cdot \mathbf{v},\ \mathbf{u} \times \mathbf{v}).$$

So a single quaternion product contains **both** the dot product and the cross product.

Maxwell wrote parts of his *Treatise on Electricity and Magnetism* (1873) using quaternion notation. Physicists found quaternions awkward for everyday work, though. For example, the square of a vector came out negative. In the 1880s Josiah Willard Gibbs and Oliver Heaviside independently separated the two parts into the operations engineers use today: $\mathbf{u} \cdot \mathbf{v}$, $\mathbf{u} \times \mathbf{v}$, and the operators div, grad and curl. A bitter debate between "quaternionists" and "vectorists" followed in the 1890s, and the vectorists won.

### Payoff

The vector calculus in every electromagnetics and fluid-mechanics course is a cut-down quaternion algebra. Quaternions themselves came back in the 20th century as the standard way to represent 3D rotations in graphics, robotics and spacecraft attitude control. They avoid the "gimbal lock" problem of Euler angles.

### How direct

Direct. Gibbs and Heaviside started from the quaternion product.

---

## 3. Number theory and ring theory: ideals

### Gaussian integers

Gauss, studying which primes can be written as a sum of two squares, worked with the **Gaussian integers**

$$\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}.$$

These behave much like ordinary integers. In particular, they have unique factorization into primes. But some ordinary primes stop being prime:

$$5 = (2 + i)(2 - i), \qquad 13 = (3 + 2i)(3 - 2i), \qquad 2 = (1 + i)(1 - i),$$

while $3$, $7$ and $11$ stay prime. The pattern is exactly Fermat's two-squares theorem. An odd prime $p$ splits in $\mathbb{Z}[i]$ if and only if $p = a^2 + b^2 = (a + bi)(a - bi)$, which happens if and only if $p \equiv 1 \pmod 4$. A fact about ordinary integers becomes a fact about factoring complex integers.

### When unique factorization fails

Encouraged by this, mathematicians tried similar number systems to attack Fermat's Last Theorem. In 1847 Lamé announced a proof that relied on unique factorization in rings built from the complex roots of unity $e^{2\pi i/p}$. Kummer had already shown, in 1844, that unique factorization can **fail** in those rings.

The simplest example of the failure uses a slightly different ring, $\mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5}\}$:

$$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}).$$

None of these four factors can be broken down further, so 6 has two genuinely different factorizations. (Proof sketch: the "norm" $N(a + b\sqrt{-5}) = a^2 + 5b^2$ is multiplicative. The four factors have norms $4, 9, 6, 6$. A proper factor would need norm 2 or 3, and $a^2 + 5b^2$ never equals 2 or 3.)

### Ideal numbers, then ideals

Kummer rescued unique factorization by inventing **ideal numbers**: extra "phantom" factors that the ring itself lacks, chosen so that factorization becomes unique again. In 1871 Dedekind made this rigorous. He replaced each ideal number by a set of ordinary elements, which he called an **ideal**. Ideals are now the basic tool of ring theory. In particular, the construction $\mathbb{R}[x]/(x^2 + 1)$ in [representations.md, Section 6](representations.md#6-polynomials-modulo-x2--1) is a quotient by an ideal.

### How direct

Direct. The whole line runs Gaussian integers → rings of complex roots of unity → Kummer → Dedekind.

---

## 4. Polynomials and Galois theory

### What happened

The **fundamental theorem of algebra** says that every polynomial of degree $n$ with complex coefficients has exactly $n$ roots in $\mathbb{C}$, counted with multiplicity. Gauss gave the first substantial proof in 1799, though it had a gap by modern standards. Argand gave a cleaner one in 1806.

That settled *where* roots live. It shifted attention to the question of whether roots can be written with a formula built from $+, -, \times, \div$ and $n$th roots, as the quadratic and cubic formulas are. Abel proved in 1824 that there is no such general formula for degree 5. Galois, before his death in 1832, explained exactly which equations can be solved this way, using what we now call group theory.

### Roots of unity

The roots of $x^n = 1$ are the $n$ complex numbers $e^{2\pi i k/n}$, equally spaced around the unit circle. They are central to Galois theory, and to one of its best-known precursors. In 1796, aged 18, Gauss showed that a regular 17-sided polygon can be constructed with ruler and compass. His argument studied the 17th roots of unity algebraically. It was the first new constructible regular polygon found since the Greeks.

### How direct

Strong, but shared. The question of solving equations by formulas is older than complex numbers, but complex numbers (the cubic formula, roots of unity, the fundamental theorem) shaped how it was posed and answered.

---

## 5. Topology: Riemann surfaces

### What happened

Some functions of a complex variable are **multi-valued**. Take $\sqrt{z}$ and follow it once around the unit circle, $z = e^{i\theta}$ with $\theta$ going from $0$ to $2\pi$:

$$\sqrt{z} = e^{i\theta/2} \quad \text{goes from} \quad e^{0} = 1 \quad \text{to} \quad e^{i\pi} = -1.$$

You return to the same $z$ but a different value of $\sqrt{z}$. Go round again and you get back to $+1$. The function $\log z$ is worse: each loop adds $2\pi i$, forever.

In his 1851 doctoral thesis Riemann proposed a way out. Instead of the plane, put the function on a **surface** made of several copies (sheets) of the plane, glued together so that going round the origin moves you to the next sheet. On this **Riemann surface** the function is single-valued again.

### Why it mattered

This made the *shape* of the surface the important thing. Riemann found that the key quantity is the number of "holes" (the **genus**): a sphere has none, a torus has one. Bending or stretching the surface doesn't change it. Properties that survive any continuous deformation are exactly the subject of **topology**. Poincaré systematized topology in the 1890s, and Riemann's surfaces were also a model for the general idea of a **manifold**, the basic object of modern geometry and of general relativity.

### How direct

Direct for Riemann surfaces. Topology also had other sources, such as Euler's bridges of Königsberg and his polyhedron formula, but complex analysis was one of the main ones.

---

## 6. Analytic number theory: primes via complex analysis

### What happened

Euler had already linked the primes to the sum $\sum 1/n^s$ through his product formula

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}.$$

In 1859 Riemann's only paper on number theory treated $s$ as a **complex** variable. He showed that the distribution of the primes is controlled by where $\zeta(s)$ equals zero in the complex plane. He conjectured that all the interesting zeros lie on the line $\operatorname{Re}(s) = \tfrac{1}{2}$. That is the **Riemann hypothesis**, still unproved and probably the most famous open problem in mathematics.

In 1896 Hadamard and de la Vallée Poussin used Riemann's approach to prove the **prime number theorem**: the number of primes up to $x$ is approximately $x / \ln x$.

### The surprise

A question about whole numbers (how are the primes spread out?) was answered using the calculus of complex functions, which seems completely unrelated. That surprise is the founding idea of analytic number theory. Complex analysis turned out not to be strictly necessary: Erdős and Selberg found an "elementary" proof in 1949. But it was complex analysis that cracked the problem first, and it remains the main tool.

### How direct

Direct.

---

## 7. Physics and engineering

These fields didn't grow out of complex numbers, but complex numbers changed how they work.

- **AC circuits.** In 1893 Charles Steinmetz showed that a sinusoidal voltage $V\cos(\omega t + \phi)$ can be handled as the complex number $Ve^{i\phi}$ (a **phasor**). Then the differential equations of a circuit become algebra. Electrical engineers write $j$ for $i$, because $i$ is current.
- **Fourier analysis and signal processing.** The functions $e^{i\omega t}$ are the natural building blocks for signals, and the discrete Fourier transform is evaluation at roots of unity. Control theory reads stability off from where the poles of a transfer function lie in the complex plane.
- **Quantum mechanics.** Schrödinger's equation (1926) has an $i$ in it, and quantum amplitudes are complex numbers. This is more than convenience. Experiments reported in 2022 support the claim that quantum theory written with real numbers only makes predictions that differ from what is observed. That is the strongest evidence so far that complex numbers are built into physics itself, not just into our methods.

### How direct

Use rather than birth. But in quantum mechanics, complex numbers may be essential to the theory itself.

---

## 8. Foundations: existence means consistency

### What happened

For 250 years, the question about $\sqrt{-1}$ was "does it exist?". Hamilton's answer in 1833 was to construct it from things already trusted (pairs of reals) and check that the construction is consistent. Then it exists as much as the reals do (see [representations.md, Foundation versus intuition](representations.md#foundation-versus-intuition)).

That answer became the general standard. A mathematical object exists if it can be consistently constructed, or, later, if axioms describing it are consistent. The same move was applied all the way down: Dedekind and Cantor constructed the reals from the rationals in 1872, and eventually everything was built from set theory. The same standard made it acceptable to study objects nobody could picture: non-Euclidean geometries, infinite-dimensional spaces, abstract groups.

### How direct

Indirect, because complex numbers were one case among several, with non-Euclidean geometry and the rigorous foundations of calculus also pushing in this direction. But it is deep, because complex numbers were the first and most persistent case of an object that wasn't a quantity yet clearly worked.

---

## The common thread

Almost every item above follows one pattern. Complex numbers taught mathematicians to accept objects defined by **how they combine** rather than by **what they are**. A complex number isn't a length or a count. It's anything that obeys the rules. Once that step was accepted:

- the rules themselves could be changed (quaternions, abstract algebra);
- new systems with the same rules could be built and studied (Gaussian integers, ideals);
- the shape of the space where the objects live could become the subject (Riemann surfaces, topology).

A caveat on the history: big shifts rarely have a single cause. Galois theory, topology and the modern view of foundations had other roots too. Of the eight lines above, "complex numbers paved the way" is literally true for 1, 2, 3, 5 and 6, and partly true for the rest.

## Further reading

- John Stillwell, *Mathematics and Its History*. Covers nearly every item here, with the mathematics included.
- Michael J. Crowe, *A History of Vector Analysis* (1967). The full quaternions-to-vectors story, including the 1890s debate.
- John Derbyshire, *Prime Obsession* (2003). The Riemann hypothesis for non-specialists, alternating history with mathematics.
- Tristan Needham, *Visual Complex Analysis* (1997). Riemann surfaces and multi-valued functions, with pictures.
- Paul J. Nahin, *An Imaginary Tale: The Story of $\sqrt{-1}$* (1998). Includes much of the engineering side.
