# Complex numbers: six definitions of one thing

You can define the complex numbers in several ways that look nothing alike:

1. a symbol $i$ with $i^2 = -1$,
2. points (or arrows) in the plane,
3. lengths and angles, $re^{i\theta}$,
4. pairs of real numbers with an odd-looking multiplication rule,
5. certain $2 \times 2$ real matrices,
6. polynomials "modulo $x^2 + 1$".

This note goes through each one: where it came from, what problem it solved, and what it makes easy. Then it asks in what precise sense they are all "the same thing". Some are literally the same object in different notation. Some are different objects with the same structure (*isomorphic*). And there is a theorem saying there was never any real choice.

**Prerequisites:** real numbers, high-school algebra and trigonometry, and basic matrices. Section 6 uses a little ring theory (ideals, quotients), explained as it comes up.

**Companion code:** [representations.py](representations.py) multiplies the same two numbers in every representation and checks they agree. Run it from the repository root with `uv run python topics/complex-numbers/representations.py`.

## The map

| # | Representation | An element looks like | Introduced | Best for |
|---|---|---|---|---|
| 1 | Formal symbol | $a + bi$, with $i^2 = -1$ | Cardano 1545, Bombelli 1572 | everyday algebra, solving polynomials |
| 2 | Plane | the point or arrow $(a, b)$ | Wessel 1797, Argand 1806, Gauss 1831 | geometry, rotations, pictures |
| 3 | Polar / exponential | $re^{i\theta}$ | de Moivre c. 1707, Euler 1748 | multiplication, powers, roots, oscillations |
| 4 | Ordered pairs | $(a, b)$ with a defined product | Hamilton 1833 (published 1837) | proving they exist; how computers store them |
| 5 | Matrices | $\left(\begin{smallmatrix} a & -b \\ b & a \end{smallmatrix}\right)$ | after Cayley's matrices, 1858 | linear algebra, eigenvalues, Cauchy–Riemann |
| 6 | Quotient ring | $a + bx$, computed mod $x^2 + 1$ | Cauchy 1847, Kronecker 1880s | generalizing: field extensions, finite fields |

**The short answer to "are these the same?"** Representations 1, 2 and 4 are one object in three notations. Representation 3 is the same numbers in different coordinates. Representations 5 and 6 are genuinely different objects with identical structure. And a uniqueness theorem (Section 7) says *any* reasonable construction has to give the same structure. The one exception is that nothing algebraic can tell $i$ apart from $-i$.

---

## 1. The formal symbol: $a + bi$

### History: it was the cubic, not the quadratic

The usual story says mathematicians wanted to solve $x^2 + 1 = 0$, so they invented $i$. That has the history backwards. For centuries, $x^2 + 1 = 0$ simply had no solution, and that was fine. The parabola $y = x^2 + 1$ never touches the axis, so there's no root to find, and nothing is broken.

What forced the issue was the **cubic**. In 1545 Gerolamo Cardano published, in his *Ars Magna*, a formula for a root of $x^3 = px + q$:

$$x = \sqrt[3]{\frac{q}{2} + \sqrt{\frac{q^2}{4} - \frac{p^3}{27}}} \;+\; \sqrt[3]{\frac{q}{2} - \sqrt{\frac{q^2}{4} - \frac{p^3}{27}}}.$$

Cardano did run into square roots of negative numbers. He noticed that $5 + \sqrt{-15}$ and $5 - \sqrt{-15}$ add to $10$ and multiply to $40$. He called this "as subtle as it is useless" and moved on.

Then in 1572 Rafael Bombelli, in his *L'Algebra*, looked at $x^3 = 15x + 4$. It has the obvious root $x = 4$ ($64 = 60 + 4$). Cardano's formula has $p = 15$ and $q = 4$, so $\frac{q^2}{4} - \frac{p^3}{27} = 4 - 125 = -121$, and it gives

$$x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}.$$

This time you can't shrug and say "no solution". The equation has three perfectly real roots ($4$ and $-2 \pm \sqrt{3}$). Yet the formula insists on passing through square roots of negatives. (This is the *casus irreducibilis*. It was later proved that for many cubics with three real roots, no formula using real radicals alone can avoid the detour.)

Bombelli had what he called a "wild thought". Just compute with $\sqrt{-1}$ using the ordinary rules of algebra, plus the single rule $(\sqrt{-1})^2 = -1$, and see what happens. He guessed that $\sqrt[3]{2 + \sqrt{-121}} = 2 + \sqrt{-1}$, and checked it:

$$(2 + \sqrt{-1})^3 = 8 + 12\sqrt{-1} + 6(\sqrt{-1})^2 + (\sqrt{-1})^3 = 8 + 12\sqrt{-1} - 6 - \sqrt{-1} = 2 + 11\sqrt{-1} = 2 + \sqrt{-121}.$$

Likewise $\sqrt[3]{2 - \sqrt{-121}} = 2 - \sqrt{-1}$. Add them and the imaginary parts cancel: $x = 4$. The right real answer.

**This is the key historical insight.** Imaginary numbers were not invented to give answers to problems that had none. They were the *route* to real answers of problems that clearly had them. They were a tool long before anyone believed they were objects.

The names tell the story of that reluctance. Descartes called them "imaginary" in 1637, and he meant it as an insult. Leibniz called $\sqrt{-1}$ "an amphibian between being and non-being". Euler introduced the symbol $i$ in 1777. Gauss gave us the neutral word "complex" in 1831.

### Definition

A complex number is an expression $a + bi$ with $a, b$ real. You compute with the ordinary rules of algebra and replace $i^2$ by $-1$ wherever it appears:

$$(a + bi) + (c + di) = (a + c) + (b + d)i,$$

$$(a + bi)(c + di) = ac + adi + bci + bd\,i^2 = (ac - bd) + (ad + bc)i.$$

To divide, multiply top and bottom by the **conjugate** $\overline{a + bi} = a - bi$, which makes the denominator real:

$$\frac{1}{a + bi} = \frac{a - bi}{(a + bi)(a - bi)} = \frac{a - bi}{a^2 + b^2}.$$

### What's missing

This definition *assumes* a thing called $i$ exists, and that the usual rules still hold once you add it. For about 250 years nobody could say what $i$ actually was. And the rules did sometimes break. In his *Algebra* (1770), Euler wrote $\sqrt{-2} \cdot \sqrt{-3} = \sqrt{6}$, using the familiar rule $\sqrt{a}\sqrt{b} = \sqrt{ab}$. The correct value is $i\sqrt{2} \cdot i\sqrt{3} = -\sqrt{6}$, because that rule fails for negative numbers. If even Euler could slip, the foundations needed work. Sections 4 and 6 supply them.

### Insight and payoff

The symbol view is how you calculate day to day. Its big payoff is the **Fundamental Theorem of Algebra**: every polynomial of degree $n \ge 1$ with complex coefficients has exactly $n$ complex roots, counted with multiplicity. You add a square root of *one* negative number and get roots of *every* polynomial, including ones like $x^4 + 1$ or $x^5 - x + 1$, for free. That is a strong hint that $i$ wasn't arbitrary (see Section 8).

---

## 2. Points in the plane

### History

The geometric picture took over 200 years after Bombelli to appear. (John Wallis tried in 1685 without much success.) It was found independently by people outside the mathematical establishment:

- **Caspar Wessel** (1797) was a Norwegian–Danish **surveyor**. For map-making he wanted to calculate with directed line segments. He defined addition as placing arrows head to tail, and multiplication as multiplying the lengths and adding the angles. His paper was written in Danish and ignored for a century.
- **Jean-Robert Argand** (1806) was a Paris bookkeeper and amateur. He self-published the same idea anonymously.
- **Carl Friedrich Gauss** had used the picture privately since about 1799. When he published it in 1831, people paid attention. He also wrote, roughly, that if $+1$, $-1$ and $\sqrt{-1}$ had been called *direct*, *inverse* and *lateral* units, instead of positive, negative and imaginary, the subject would never have seemed so obscure.

Notice who got there first. The first clear account came from Wessel, a surveyor with a practical problem, not from a professional mathematician. But it took Gauss's reputation to get the idea accepted.

### Definition

Identify $a + bi$ with the point $(a, b)$, or the arrow from the origin to it. Real numbers lie on the horizontal axis, and $i$ is the point $(0, 1)$, one unit *up*.

Addition is vector addition: put the arrows head to tail (the parallelogram rule).

### Key insight: multiplying by $i$ is a quarter turn

Negative numbers already give a clue. Multiplying by $-1$ flips the number line through the origin, which is a half turn. What should $i$ be? It should be something that, done twice, gives $-1$. That is, something that done twice gives a half turn. The natural answer is a **quarter turn**.

Check it: $i(a + bi) = -b + ai$, so $(a, b) \mapsto (-b, a)$. That is exactly a rotation by $90°$ counterclockwise.

More generally (proved in Sections 3 and 5): **multiplying by $w$ scales by $|w|$ and rotates by the angle of $w$.**

This dissolves the 250-year mystery. $i$ isn't a quantity hiding somewhere on the number line. It's a *direction perpendicular to* the number line. Gauss's word "lateral" is exactly right.

### The cost: no ordering

You can't put the complex numbers in a line consistent with arithmetic. In any ordered field, squares are $\ge 0$, so $1 = 1^2 > 0$ and $-1 < 0$. But $-1 = i^2$ is a square. Contradiction. Going sideways off the number line means giving up "bigger" and "smaller".

### Best for

Geometry and 2D rotations. Visualizing roots: the solutions of $z^n = 1$ are the corners of a regular $n$-gon. Conformal maps. In engineering: pole–zero plots and stability (poles in the left half-plane), Nyquist plots, and constellation diagrams in digital communications (QAM).

---

## 3. Polar and exponential form

### Definition

Describe a point by its distance from the origin and its angle:

$$z = r(\cos\theta + i\sin\theta) = re^{i\theta}, \qquad r = |z| = \sqrt{a^2 + b^2}, \quad \theta = \arg z.$$

### The product rule, and why it's just trigonometry

**Claim:** $(\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta) = \cos(\alpha + \beta) + i\sin(\alpha + \beta)$.

**Proof (full, given the trig addition formulas).** Multiply out:

$$(\cos\alpha\cos\beta - \sin\alpha\sin\beta) + i(\sin\alpha\cos\beta + \cos\alpha\sin\beta),$$

and recognize the two angle-addition formulas. $\blacksquare$

So $r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2\, e^{i(\theta_1 + \theta_2)}$: **multiply the lengths, add the angles.** Read the proof backwards and it says complex multiplication *is* the angle-addition formulas, in compact form. You never need to memorize those formulas again. Expand $e^{i(\alpha + \beta)} = e^{i\alpha} e^{i\beta}$ and read off the real and imaginary parts.

Repeating this gives **de Moivre's formula**, $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$, from which multiple-angle formulas like $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$ fall out.

### Why $e^{i\theta}$?

Two ways to see that $e^{i\theta} = \cos\theta + i\sin\theta$ (**Euler's formula**):

- **Power series (a proof, if you take these series as the definitions).** Put $i\theta$ into $e^x = \sum x^n / n!$. Since $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, the even terms give the series for $\cos\theta$ and the odd terms give $i$ times the series for $\sin\theta$. The series converge absolutely, so splitting them into even and odd parts is legitimate.
- **Motion.** Think of $e^{i\theta}$ as a moving point. This gives the most memorable explanation, set out in the next subsection.

### Euler's identity as half a turn

What makes $e^x$ special is that $f(x) = e^x$ satisfies $f' = f$ with $f(0) = 1$. It grows at a rate equal to its current size. Ask the same of $f(\theta) = e^{i\theta}$: start at $f(0) = 1$, and require $f' = if$. Multiplying by $i$ is a quarter turn (Section 2). So **the velocity is always the position turned $90°$.**

To make the motion concrete, use the matrix $J = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, which turns vectors by $90°$ counterclockwise (more on this in Section 5). Let $\mathbf{r}(\theta)$ be a point in the plane with

$$\mathbf{r}' = J\mathbf{r}, \qquad \mathbf{r}(0) = (1, 0).$$

The solution is $\mathbf{r}(\theta) = e^{\theta J}(1, 0)$, the first column of the matrix exponential $e^{\theta J} = \sum_n (\theta J)^n / n!$.

**Claim.** The point moves counterclockwise around the unit circle at unit speed.

**Proof.** The velocity $J\mathbf{r}$ is perpendicular to $\mathbf{r}$, so

$$\frac{d}{d\theta}\lvert\mathbf{r}\rvert^2 = 2\,\mathbf{r}\cdot\mathbf{r}' = 2\,\mathbf{r}\cdot J\mathbf{r} = 0.$$

So the distance from the origin never changes: it stays $\lvert\mathbf{r}(0)\rvert = 1$. The speed is $\lvert\mathbf{r}'\rvert = \lvert J\mathbf{r}\rvert = \lvert\mathbf{r}\rvert = 1$, because a rotation doesn't change length. $\blacksquare$

Unit speed means that after time $\theta$ the point has travelled arc length $\theta$. Starting from $(1, 0)$, that point is $(\cos\theta, \sin\theta)$; this is just what radians, $\cos$ and $\sin$ mean. So

$$e^{\theta J} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad \text{that is,} \qquad e^{i\theta} = \cos\theta + i\sin\theta.$$

**Rigor:** a sketch. It assumes two standard facts: the matrix exponential satisfies $\frac{d}{d\theta}e^{\theta J} = Je^{\theta J}$, and a linear ODE with a given starting point has only one solution. The second is what lets us say that "the moving point" and "$e^{\theta J}$" are the same thing.

**Now set $\theta = \pi$.** The circumference is $2\pi$, so after time $\pi$ the point is halfway round, at $(-1, 0)$:

$$e^{\pi J} = -I, \qquad \text{that is,} \qquad e^{i\pi} = -1, \quad\text{or}\quad e^{i\pi} + 1 = 0.$$

This is Euler's identity, and it's not a mystical coincidence of constants. Each constant does one job:
- $e$ means "grow at a rate equal to your size",
- $i$ means "turn that growth $90°$ sideways",
- $\pi$ is the length of half a unit circle.

In the same way, $e^{i\pi/2} = i$ (a quarter turn) and $e^{2\pi i} = 1$ (a full turn).

### History: the formulas came before the picture

Abraham de Moivre had his formula by about 1707. Roger Cotes found an equivalent of $i\theta = \ln(\cos\theta + i\sin\theta)$ in 1714. Euler published $e^{i\theta} = \cos\theta + i\sin\theta$ in his *Introductio* of 1748. All of this was found by manipulating series and formulas, **50 to 90 years before the plane picture of Section 2**. Euler was working blind, with symbols alone. The geometry came later and explained *why* it works.

### Same numbers, different coordinates

Polar form is not a new number system. It's the same numbers described in different coordinates, just like polar coordinates on the plane. And the description isn't one-to-one: $\theta$ is only defined up to multiples of $2\pi$, and $0$ has no angle at all.

Here is the precise statement. For nonzero numbers, the map $(r, \theta) \mapsto re^{i\theta}$ turns "multiply the $r$'s, add the $\theta$'s" into complex multiplication. In group-theory terms it is a surjective homomorphism from $(0, \infty) \times \mathbb{R}$ onto the nonzero complex numbers, with kernel $\lbrace (1, 2\pi k) : k \in \mathbb{Z} \rbrace$. So the multiplicative group of $\mathbb{C}$ is "positive reals times a circle": $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times S^1$.

The price is that *addition* is awkward in polar form (you need the law of cosines). The $2\pi$ ambiguity also comes back in practice. It's why the complex logarithm needs a branch cut, why `np.angle` returns values in $(-\pi, \pi]$, and why signal processing needs phase unwrapping (`np.unwrap`).

### Best for

Multiplication, division, powers and roots. The $n$th roots of unity are $e^{2\pi i k/n}$. Above all, **oscillations**:

- $\cos\omega t = \operatorname{Re} e^{i\omega t}$, and differentiating $e^{i\omega t}$ just multiplies by $i\omega$.
- **Phasors** in AC circuits. A capacitor's impedance $1/(i\omega C)$ is a scaling combined with a $-90°$ rotation, which is the "current leads voltage by $90°$" rule.
- Linear ODEs. $e^{(\sigma + i\omega)t}$ is a growing or decaying oscillation in one symbol.
- **Fourier analysis**, which builds signals out of $e^{i\omega t}$.

---

## 4. Ordered pairs of reals (Hamilton)

### Motivation

By the 1830s the geometric picture had made complex numbers respectable. But it borrowed its legitimacy from geometry. William Rowan Hamilton wanted the complex numbers to rest on the real numbers alone, with no appeal to pictures and no mysterious $\sqrt{-1}$. He pointed out that in $a + b\sqrt{-1}$, the "$+$" can't be ordinary addition, because you can't add a real number to something that isn't one. His paper "Theory of Conjugate Functions, or Algebraic Couples" was read in 1833 and published in 1837.

### Definition

$\mathbb{C}$ is the set $\mathbb{R}^2$ of ordered pairs, with

$$(a, b) + (c, d) = (a + c,\ b + d), \qquad (a, b)(c, d) = (ac - bd,\ ad + bc).$$

There is no $i$ here and no square root of anything negative, only real arithmetic. You then check the field axioms (commutativity, associativity, distributivity, and inverses, with $(a, b)^{-1} = \left(\frac{a}{a^2 + b^2}, \frac{-b}{a^2 + b^2}\right)$ for $(a, b) \neq (0, 0)$). This is tedious but routine. Because everything is built from real numbers, **the complex numbers are exactly as consistent as the real numbers.** That settles the question "does $i$ exist?" for good.

### Getting $a + bi$ back

Pairs of the form $(a, 0)$ behave exactly like real numbers: $(a, 0) + (c, 0) = (a + c, 0)$ and $(a, 0)(c, 0) = (ac, 0)$. So we agree to write $a$ for $(a, 0)$. Now *define* $i = (0, 1)$. Then

$$i^2 = (0, 1)(0, 1) = (0 \cdot 0 - 1 \cdot 1,\ 0 \cdot 1 + 1 \cdot 0) = (-1, 0) = -1,$$

$$(a, b) = (a, 0) + (b, 0)(0, 1) = a + bi.$$

So $a + bi$ is just a convenient way of writing the pair $(a, b)$. The square root of $-1$ is no longer assumed. It's *constructed*.

The quarter turn from [Section 2](#key-insight-multiplying-by-i-is-a-quarter-turn) also falls straight out of the multiplication rule:

$$(0, 1)(a, b) = (0 \cdot a - 1 \cdot b,\ 0 \cdot b + 1 \cdot a) = (-b,\ a),$$

which is the arrow $(a, b)$ turned $90°$ counterclockwise. Nothing geometric went into the definition, yet multiplying by $i$ rotates.

### Where does the strange multiplication come from?

It wasn't pulled out of a hat. It's exactly the result of multiplying out $(a + bi)(c + di)$ with $i^2 = -1$. Hamilton reverse-engineered his definition from Representation 1. That's worth saying plainly: the pair definition looks unmotivated precisely *because* its motivation is in the other representations. This is often true of "rigorous" definitions in textbooks. They are the end of a story, presented as if they were the beginning.

### Foundation versus intuition

There is an irony here. Hamilton set out to free complex numbers from geometry, and the definition he chose, pairs $(a, b)$, looks like nothing so much as points in the plane.

The irony goes away once you separate two questions:

- **What justifies the definition?** An ordered pair is just two real numbers in a fixed order. The rules above use only real arithmetic, with no distance, angle or direction anywhere. So if you trust the reals, you must trust the complex numbers. That is the *foundation*.
- **How do you understand it?** By the picture. Descartes had identified pairs of reals with points in the plane two centuries earlier, so it's hard to see $(a, b)$ and not see a point. And the multiplication rule turns out to be exactly rotate-and-scale. That is the *intuition*.

Hamilton wasn't banning the picture. He was saying that the picture shouldn't be what makes complex numbers legitimate. This has become the standard pattern in modern mathematics: define without geometry, then picture freely. The algebraic foundation and the geometric picture fit together exactly, and that's no accident. Both describe the same structure.

There is a further twist. Hamilton reduced complex numbers to real numbers, but what did *real* numbers rest on? For Hamilton, our sense of time. A rigorous answer came only in 1872. So he didn't fully solve the foundational problem. He moved it from "what is $\sqrt{-1}$?" to "what is a real number?" That is real progress: a smaller, more basic question. The [appendix](#appendix-algebra-as-the-science-of-pure-time) tells this part of the story.

### Legacy

Hamilton then spent ten years trying to multiply *triples* the same way. He failed, because it can't be done. On 16 October 1843, walking along a canal in Dublin, he realized that *quadruples* work if you give up commutativity, and carved $i^2 = j^2 = k^2 = ijk = -1$ into Brougham Bridge. These are the **quaternions**, used today for 3D rotations in graphics, robotics and spacecraft attitude control.

### Best for

Rigor and existence proofs. Also **computers**: a NumPy `complex128` is literally two `float64`s stored side by side, and the hardware multiplies them using Hamilton's formula.

---

## 5. $2 \times 2$ real matrices

### Definition

Send $a + bi$ to the matrix

$$M(a + bi) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} = aI + bJ, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$

Note that $J^2 = -I$. $J$ is the $90°$ rotation matrix, and it plays the role of $i$.

### Where it comes from: represent a number by what it does

Fix $w = a + bi$ and look at the map "multiply by $w$" on the plane: $(x, y) \mapsto (ax - by,\ bx + ay)$. This map is real-linear, so it has a matrix, and that matrix is $M(w)$. Its columns are the images of $1 = (1, 0)$ and $i = (0, 1)$. So **the matrix is the action of multiplying by $w$, written down.** This idea of representing an element by the linear map it induces is called the *regular representation*. It's the same idea behind group representations.

### The isomorphism

**Theorem.** $M(z + w) = M(z) + M(w)$, $M(zw) = M(z)M(w)$, $M(1) = I$, and $M$ is one-to-one. So the set $\lbrace aI + bJ \rbrace$ of these matrices is a field isomorphic to $\mathbb{C}$.

**Proof (full).** Additivity and injectivity are clear. For products,

$$(aI + bJ)(cI + dJ) = acI + (ad + bc)J + bdJ^2 = (ac - bd)I + (ad + bc)J,$$

using $J^2 = -I$. That's the same computation as in Section 1, because $J$ satisfies the same equation as $i$. $\blacksquare$

These matrices are *not* complex numbers. They're a different set of objects. But they add and multiply in exactly the same way. Most $2 \times 2$ matrices don't commute with each other, yet this particular two-dimensional slice does.

### A dictionary

| Complex numbers | Matrices |
|---|---|
| $\lvert z \rvert^2 = a^2 + b^2$ | $\det M(z)$ |
| $\lvert zw \rvert = \lvert z \rvert \lvert w \rvert$ | $\det(AB) = \det A \det B$ |
| conjugate $\bar{z}$ | transpose $M(z)^T$ |
| $e^{i\theta}$ | rotation matrix $\left(\begin{smallmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{smallmatrix}\right) = e^{\theta J}$ |
| $re^{i\theta}$ | $r \times$ (rotation by $\theta$) |

The last row *proves* the claim from Section 2 that multiplying by $w$ rotates and scales.

### Rotations versus rotations with scaling

A natural question is whether the rotation matrices are isomorphic to $\mathbb{C}$. Not quite.

**Rotation matrices alone** correspond to the **unit circle**, the complex numbers with $\lvert z\rvert = 1$. The product of two rotations is a rotation, and every rotation has an inverse, so they form a *group* under multiplication. (This group is called $SO(2)$, and it matches the unit circle $S^1$ in $\mathbb{C}$.) But they don't form a field. The sum of two rotations isn't a rotation: for example $I + I = 2I$ stretches lengths by 2. And there is no zero.

**Adding scaling (of rotation matrices) gives all of $\mathbb{C}$.** Every matrix $aI + bJ$ can be written as $r\,R_\theta$, a scalar $r = \lvert z\rvert \ge 0$ times a rotation. This is polar form in matrix language. Multiplying by the scalar $r$ is the same as multiplying by the matrix $rI$, which represents the real number $r$. It commutes with everything, so scaling and rotating don't interfere with each other. Negative scalings aren't needed, because $-R_\theta = R_{\theta + \pi}$.

What scaling adds is closure under **addition** (and a zero). Adding matrices is always possible; the question is whether the sum stays in the set. The sum of two scaled rotations is again a scaled rotation, because $(a_1 I + b_1 J) + (a_2 I + b_2 J) = (a_1 + a_2)I + (b_1 + b_2)J$.

**Why rotations alone aren't closed, geometrically.** A matrix $aI + bJ$ is completely determined by where it sends $(1, 0)$, namely its first column $(a, b)$. (The second column is that arrow turned $90°$.) So scaled rotations correspond to *arrows of any length*, and pure rotations to *arrows of length exactly 1*. Two arrows always add to an arrow. Two unit arrows usually don't add to a unit arrow. For example, $R_0 + R_{90°}$ sends $(1,0)$ to $(1,0) + (0,1) = (1,1)$:

$$I + J = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \sqrt{2}\, R_{45°}.$$

That's a scaled rotation, not a rotation. Opposite rotations cancel completely, $R_0 + R_{180°} = I - I = 0$, which produces the zero that rotations lacked. In general two unit arrows form a rhombus whose diagonal points at the average angle, so

$$R_\alpha + R_\beta = 2\cos\left(\frac{\alpha - \beta}{2}\right) R_{\frac{\alpha + \beta}{2}}.$$

(This is the sum-to-product formulas.) A neat way to say it: since $R_\theta = \cos\theta\, I + \sin\theta\, J$, **$\mathbb{C}$ is exactly the set of all linear combinations of rotation matrices.**

| Matrices | Structure | Complex numbers |
|---|---|---|
| rotations $R_\theta$ | group under $\times$ | unit circle, $\lvert z\rvert = 1$ |
| positive scalings $rI$ | group under $\times$ | positive reals |
| nonzero scaled rotations $rR_\theta$ | group under $\times$ ($\cong \mathbb{R}_{>0} \times SO(2)$) | nonzero complex numbers |
| all $aI + bJ$, including $0$ | field | $\mathbb{C}$ |

### Payoff 1: complex eigenvalues of real matrices

Let $A$ be a real $2 \times 2$ matrix with complex eigenvalues $a \pm bi$ ($b \neq 0$). Then $A$ is similar to $\left(\begin{smallmatrix} a & -b \\ b & a \end{smallmatrix}\right)$. In other words, in a suitable (possibly skewed) basis, $A$ *is* multiplication by the complex number $a + bi$, which is a rotation combined with a scaling. This is why complex eigenvalues of a system $\dot{\mathbf{x}} = A\mathbf{x}$ mean oscillation, and why the trajectories spiral. In higher dimensions it's the "real canonical form": complex eigenvalue pairs show up as rotation–scaling blocks acting on invariant planes.

### Payoff 2: Cauchy–Riemann without calculation

Write $f(x + iy) = u(x, y) + iv(x, y)$ and view $f$ as a map $\mathbb{R}^2 \to \mathbb{R}^2$. If $f$ is real-differentiable, near a point it is approximately linear, with the Jacobian matrix $\left(\begin{smallmatrix} u_x & u_y \\ v_x & v_y \end{smallmatrix}\right)$. Being *complex*-differentiable means more: the local linear map must be multiplication by one complex number, $f'(z)$. So the Jacobian must have the shape $\left(\begin{smallmatrix} a & -b \\ b & a \end{smallmatrix}\right)$, which means

$$u_x = v_y, \qquad u_y = -v_x.$$

These are the **Cauchy–Riemann equations**, read straight off the matrix shape. (This is a sketch. The precise theorem assumes $f$ is real-differentiable.) It also shows at once why holomorphic maps are **conformal** (angle-preserving) wherever $f'(z) \neq 0$: locally they just rotate and scale.

### History

Matrices themselves only became a systematic theory with Arthur Cayley in 1858. After that, this representation is a natural thing to write down. I don't know of a single clear originator.

---

## 6. Polynomials modulo $x^2 + 1$

### The idea

Take ordinary polynomials in $x$ with real coefficients and declare that $x^2 + 1$ counts as zero. Any polynomial can be divided by $x^2 + 1$, leaving a unique remainder of the form $a + bx$. So add and multiply polynomials as usual, then reduce:

$$(a + bx)(c + dx) = ac + (ad + bc)x + bd\,x^2 \equiv (ac - bd) + (ad + bc)x, \qquad \text{since } x^2 \equiv -1.$$

That's the complex multiplication rule with $x$ in place of $i$. It's the same move as clock arithmetic. "Integers mod 12" treats 12 as zero. Here we work with "polynomials mod $x^2 + 1$".

### Formal version

Write $(x^2 + 1)$ for the set of all polynomial multiples of $x^2 + 1$. (In ring theory this is called an *ideal*.) The **quotient ring** $\mathbb{R}[x]/(x^2 + 1)$ treats two polynomials as equal when their difference is a multiple of $x^2 + 1$. It's automatically a ring, because quotients of rings by ideals always are.

It's also a **field**. There's a general theorem: $F[x]/(p)$ is a field exactly when $p$ is irreducible over $F$, and $x^2 + 1$ has no real roots, so it's irreducible over $\mathbb{R}$. You can also see it directly: $(a + bx)(a - bx) = a^2 - b^2x^2 \equiv a^2 + b^2$, so $a + bx$ has inverse $\frac{a - bx}{a^2 + b^2}$.

**Theorem.** $\mathbb{R}[x]/(x^2 + 1) \cong \mathbb{C}$.

**Proof (full, given the First Isomorphism Theorem for rings).** Let $\varphi : \mathbb{R}[x] \to \mathbb{C}$ be "evaluate at $i$", $\varphi(p) = p(i)$. It respects $+$ and $\times$, and it's onto because $\varphi(a + bx) = a + bi$. Its kernel is the set of real polynomials with $i$ as a root. Such a polynomial also has $-i$ as a root (complex roots of real polynomials come in conjugate pairs), so it's divisible by $(x - i)(x + i) = x^2 + 1$. So the kernel is exactly $(x^2 + 1)$, and the First Isomorphism Theorem gives the result. $\blacksquare$

### History

In 1847 Augustin-Louis Cauchy proposed treating $i$ as a plain symbol and computing with "algebraic equivalences" modulo $i^2 + 1$. **The insight is that you never need to know what $i$ *is*, only the equation it satisfies.** In the 1880s Leopold Kronecker turned this into a general method. Given any field $F$ and any irreducible polynomial $p$, the quotient $F[x]/(p)$ is a new field in which $p$ has a root. You can *build* roots of equations out of nothing but the equations themselves. This fits Kronecker's well-known view that only the integers are given, and everything else should be constructed.

### Best for: generalizing

This is the representation that generalizes furthest:

- **It's a template for all field extensions.** $\mathbb{Q}[x]/(x^2 - 2)$ is $\mathbb{Q}(\sqrt{2})$, the rationals with $\sqrt{2}$ added.
- **Finite fields.** $\mathbb{F}_2[x]/(x^8 + x^4 + x^3 + x + 1)$ is the 256-element field $\mathrm{GF}(2^8)$ used inside AES encryption. Fields built the same way power Reed–Solomon error-correcting codes (QR codes, CDs, deep-space links). It's the same construction as $\mathbb{C}$, with a different base field and polynomial.
- **A preview of the DFT.** In $\mathbb{C}[x]/(x^N - 1)$, multiplying polynomials is **circular convolution**. Over $\mathbb{C}$, $x^N - 1$ factors as $\prod_k (x - \omega^k)$ with $\omega = e^{2\pi i/N}$, and the ring splits into $N$ independent copies of $\mathbb{C}$. The splitting map is "evaluate at every $\omega^k$", which is exactly the **discrete Fourier transform**. That is why the DFT turns convolution into pointwise multiplication. (This deserves its own note.)

---

## 7. Same thing, or isomorphic?

**Short answer to "is $i$ the same as $(0, 1)$?"** *Within a single construction, yes.* In the ordered-pairs construction, $i$ *is* $(0, 1)$, by definition. *Across constructions, no.* In the matrix construction $i$ is $J$, and in the quotient ring it is the class of $x$. These are different objects that correspond under an isomorphism.

In practice mathematicians build $\mathbb{C}$ once, by any method, and then forget how they did it. The uniqueness theorem below is what makes that safe: every construction yields the same structure, up to swapping $i$ and $-i$.

In more detail, "these are all the complex numbers" can mean three quite different things.

### Level 1: the same object in different notation

$a + bi$, the pair $(a, b)$ and the point $(a, b)$ in the plane are one thing. Once Section 4 makes the identifications $a = (a, 0)$ and $i = (0, 1)$, the expression $a + bi$ is *literally* the pair $(a, b)$.

One pedantic footnote. In a strict set-theoretic construction, the real number $3$ and the pair $(3, 0)$ are different objects. We *embed* $\mathbb{R}$ in $\mathbb{C}$ by $a \mapsto (a, 0)$ and then agree to write $a$. Every mathematician does this silently, and the same thing happens at each step of $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$.

Also note that the plane $\mathbb{R}^2$ by itself has addition but no multiplication. The plane picture only becomes $\mathbb{C}$ once you add the rotate-and-scale multiplication, which is Hamilton's rule.

### Level 2: the same numbers in different coordinates

Polar form names the same numbers by $(r, \theta)$ instead of $(a, b)$. It isn't a different structure. It's a different coordinate system on the same set, and not even a one-to-one one. Its algebraic content is the group isomorphism $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times S^1$ for *multiplication only*.

### Level 3: different objects with the same structure

The matrices $aI + bJ$ and the remainders $a + bx$ mod $x^2 + 1$ are genuinely different objects from pairs of reals. What they share is **structure**.

**Definition.** A *field isomorphism* is a bijection $\varphi$ with $\varphi(z + w) = \varphi(z) + \varphi(w)$ and $\varphi(zw) = \varphi(z)\varphi(w)$.

An isomorphism is a perfect renaming. Every true statement about $+$ and $\times$ in one structure translates into a true statement in the other. For anything you can say with arithmetic, there's no way to tell them apart.

**"Isomorphic" always means isomorphic *with respect to some structure*.** Which structure you keep matters:

| Keep only… | $\mathbb{C}$ is isomorphic to… | Comment |
|---|---|---|
| the set | $\mathbb{R}$, $\mathbb{R}^2$, … | same size of infinity; useless |
| $+$ and real scaling (vector space) | $\mathbb{R}^2$ | infinitely many isomorphisms, one per basis |
| $\times$ on nonzero elements (group) | $\mathbb{R}_{>0} \times S^1$ | this is what polar form captures |
| $+$ and $\times$ (field) | the matrices $aI + bJ$; $\mathbb{R}[x]/(x^2 + 1)$ | exactly two isomorphisms that fix $\mathbb{R}$ (see below) |

### The uniqueness theorem: there was never a choice

**Theorem.** Let $K$ be a field that contains $\mathbb{R}$, is two-dimensional as a real vector space, and contains an element $j$ with $j^2 = -1$. Then $\varphi(a + bi) = a + bj$ is a field isomorphism $\mathbb{C} \to K$.

**Proof (full).** $j$ isn't real, because no real number squares to $-1$. So $1$ and $j$ are linearly independent, and since $K$ is two-dimensional, they form a basis. So $\varphi$ is a bijection that respects addition. For multiplication, $\varphi\big((a + bi)(c + di)\big) = (ac - bd) + (ad + bc)j$, and

$$(a + bj)(c + dj) = ac + (ad + bc)j + bd\,j^2 = (ac - bd) + (ad + bc)j. \qquad \blacksquare$$

The proof is almost embarrassingly short, and that's the point. **Once you ask for a two-dimensional number system over $\mathbb{R}$ with a square root of $-1$, the distributive law dictates the multiplication rule.** There is nothing left to choose. That's why every construction, by every author, in every century, agrees.

Stronger results (stated without proof):

- Every field that is finite-dimensional over $\mathbb{R}$ is either $\mathbb{R}$ or isomorphic to $\mathbb{C}$. (This follows from the Fundamental Theorem of Algebra.)
- **Frobenius (1877):** the only finite-dimensional real *division algebras* that are associative are $\mathbb{R}$, $\mathbb{C}$ and the quaternions $\mathbb{H}$. Here a division algebra is like a field, except that multiplication need not commute. This is why Hamilton's search for "triples" was doomed.

### The one genuine ambiguity: $i$ versus $-i$

Any field $K$ like the one in the theorem contains *two* square roots of $-1$, namely $j$ and $-j$. So there are two isomorphisms $\mathbb{C} \to K$, not one. Equivalently, **complex conjugation $a + bi \mapsto a - bi$ preserves both $+$ and $\times$.** It's a *field automorphism*, an isomorphism from $\mathbb{C}$ to itself.

The consequence is striking. Any statement built from arithmetic that is true of $i$ is equally true of $-i$. Nothing in the algebra says which square root of $-1$ is "the" $i$. Putting $i$ at $(0, 1)$, "up", so that multiplying by $i$ turns counterclockwise, is a **convention**, like choosing right-handed coordinate axes. In Galois theory this two-element symmetry group $\lbrace \text{identity}, \text{conjugation} \rbrace$ is called $\mathrm{Gal}(\mathbb{C}/\mathbb{R})$. It is the simplest example of the idea that a field's symmetries reveal its structure.

You can see this in engineering. Electrical engineers write $j$ and use $e^{j\omega t}$. Physicists often write waves as $e^{-i\omega t}$, and Fourier transform sign conventions differ from book to book. Every one of these conventions works, and the conjugation automorphism is why. In the matrix picture, $J$ and $J^T = -J$ both square to $-I$, and either one could play the role of $i$.

(A technical footnote. If you drop the requirement that $\mathbb{R}$ stays fixed, the axiom of choice produces bizarre automorphisms of $\mathbb{C}$ that scramble the real numbers. They aren't continuous and never appear in practice.)

---

## 8. Discovery or invention?

This is philosophy, not a theorem, so treat it as my view.

**The representations are inventions.** Pairs, matrices and quotient rings are human choices, each with an author and a date, picked for convenience or rigor. Different cultures could have picked different ones.

**The structure is much closer to a discovery.** Three pieces of evidence:

1. **It was forced on people who didn't want it.** Bombelli wasn't looking for new numbers. He was trying to find a real root of a real equation, and the imaginaries got in the way. Mathematicians resisted them for 250 years and used them anyway, because they kept giving correct real answers.
2. **There's no freedom in it.** By the uniqueness theorem, once you want a square root of $-1$ alongside the reals, the whole structure is determined, up to swapping $i$ and $-i$.
3. **You get far more out than you put in.** You add one root of one equation and get the Fundamental Theorem of Algebra. Then come Euler's formula linking exponentials and trigonometry, the remarkable rigidity of complex analysis, and the fact that quantum mechanics is most naturally written with complex amplitudes. Nobody designed any of these properties. They were found.

A useful analogy: the rules of chess were invented, but the facts about chess endgames are discovered. With $\mathbb{C}$, even the "rules" were barely a choice. So the best short summary might be: **the question was invented ("what if $-1$ had a square root?"); the answer was discovered.**

---

## 9. Which representation for which job

| Problem | Best representation | Why |
|---|---|---|
| Solving polynomial equations, symbolic algebra | $a + bi$ | ordinary algebra with one extra rule |
| Adding, subtracting | $a + bi$ / plane | componentwise; vector addition |
| Multiplying, dividing, powers, roots | polar $re^{i\theta}$ | multiply lengths, add angles |
| Trig identities | $e^{i\theta}$ | angle addition becomes $e^{i(\alpha + \beta)} = e^{i\alpha}e^{i\beta}$ |
| Oscillations, AC circuits, linear ODEs, Fourier | $e^{i\omega t}$, phasors | differentiation becomes multiplication by $i\omega$ |
| 2D geometry and rotations | plane | multiplying by $e^{i\theta}$ rotates |
| Proving $\mathbb{C}$ exists and is consistent | ordered pairs | built from $\mathbb{R}$ alone |
| Storing and computing on a machine | ordered pairs | two floats, Hamilton's product |
| Complex eigenvalues, spiral dynamics | matrices | real canonical form: rotation–scaling blocks |
| Complex differentiability, conformal maps | matrices | Cauchy–Riemann is the matrix shape |
| Building other number systems (finite fields, $\mathbb{Q}(\sqrt{2})$) | $F[x]/(p)$ | the construction generalizes directly |

---

## 10. Checking it in Python

[representations.py](representations.py) multiplies $z = 1 + 2i$ by $w = 3 - i$ in each representation. By hand, $(1 + 2i)(3 - i) = 3 - i + 6i - 2i^2 = 5 + 5i$. It also computes $e^{\pi J}$, checks that conjugation is an automorphism, reruns Bombelli's calculation, and compares the Jacobian of $f(z) = z^2$ with the matrix $M(f'(z))$:

```
1. a + bi        : z*w = (5+5j)
3. polar         : r = 7.0711, theta = 0.7854 rad  ->  5.0000+5.0000i
4. ordered pairs : (5.0, 5.0)
5. matrices      : M(z) M(w) =
[[ 5. -5.]
 [ 5.  5.]]
   e^(pi J) =
[[-1.  0.]
 [ 0. -1.]]
6. R[x]/(x^2+1)  : (a+bx)(c+dx) = [ 3.  5. -2.] -> remainder [5. 5.]

All representations agree; conjugation preserves + and *.

Bombelli: cbrt(2+11i) = 2.0000+1.0000j, cbrt(2-11i) = 2.0000-1.0000j, sum = 4.0000+0.0000j

Jacobian of z^2 at 1+2i (finite differences):
[[ 2. -4.]
 [ 4.  2.]]
M(2z) at z = 1+2i:
[[ 2. -4.]
 [ 4.  2.]]
```

Points to notice:

- In the polar line, $r = \sqrt{5} \cdot \sqrt{10} = \sqrt{50}$ and $\theta = \pi/4$. The angles of $z$ and $w$ really do add.
- In the matrix line, the first column of $M(z)M(w)$ is $(5, 5)$, which is $zw$.
- $e^{\pi J} = -I$ is Euler's identity $e^{i\pi} = -1$ as a matrix: half a turn.
- In the polynomial line, $3 + 5x - 2x^2$ reduces to $5 + 5x$, because $-2x^2 \equiv +2$.
- The Jacobian of $z^2$ has exactly the rotation–scaling shape, which is Cauchy–Riemann in action.

---

## Where this leads

Complex numbers opened up much of 19th-century mathematics, from abstract algebra and vector analysis to topology and the study of primes. The companion note [What complex numbers led to](legacy.md) tells that story. Directions most relevant to engineering:

- **Quaternions** (Hamilton 1843): four dimensions, non-commutative, and the standard tool for 3D rotations.
- **Fourier analysis**: $e^{i\omega t}$ as a basis, and the DFT as evaluation at roots of unity.
- **Finite fields**: the quotient construction applied to $\mathbb{F}_2$, behind error-correcting codes and cryptography.
- **Complex analysis**: why the Cauchy–Riemann condition makes complex-differentiable functions so rigid.

## Further reading

- Paul J. Nahin, *An Imaginary Tale: The Story of $\sqrt{-1}$* (1998). Readable history with lots of engineering.
- Barry Mazur, *Imagining Numbers* (2003). An extended meditation on Bombelli's leap.
- Tristan Needham, *Visual Complex Analysis* (1997). The geometric viewpoint, done beautifully.
- John Stillwell, *Mathematics and Its History*. Chapters on the cubic, complex numbers and quaternions.

---

## Appendix: algebra as the science of pure time

Hamilton's 1837 paper on couples opens with a long essay titled "Algebra as the Science of Pure Time". It explains what Hamilton thought the real numbers, and so his couples, actually rest on. The answer seems odd today, but it makes sense once you see the problem he faced.

### The problem: algebra about nothing?

In the 1830s it wasn't only $\sqrt{-1}$ that was in doubt. Some British mathematicians still rejected *negative* numbers. How can you take 5 from 3? Others, led by George Peacock, answered the doubts by treating algebra as a formal game. You fix rules for manipulating symbols, and the symbols needn't mean anything. Hamilton disliked both positions. He wanted algebra to be a *science* with genuine subject matter, the way geometry is the science of space.

### The source: Kant

Hamilton took his answer from the philosopher Immanuel Kant. Kant argued that some knowledge comes neither from logic alone nor from experience. It rests on two built-in forms of intuition, **space** and **time**, which structure all experience:

- **Geometry** rests on our intuition of space. That's why we can be certain of geometric truths without measuring anything.
- **Arithmetic** rests on our intuition of time, because counting is succession: one, then the next, then the next.

Hamilton's conclusion: if geometry is the science of space, then algebra is the science of pure time.

### Building numbers from time

- A **moment** is a point in time.
- A **step** is the transition from one moment to another.
- **Numbers are ratios of steps.** "3" means a step three times as long as a given step.
- **Negative numbers** are steps backwards in time. Reversing a step is no more mysterious than reversing direction, so the old objection disappears.
- **Irrational numbers** come from the *continuity* of time. Any two steps have a ratio, even if no fraction expresses it exactly.

Couples, his complex numbers, were pairs of moments or pairs of steps. So in Hamilton's own mind $(a, b)$ was *not* a point in the plane. The geometric reading of his construction is ours, not his.

### Why this isn't rigorous

The property of the real numbers that matters most for analysis is that they have **no gaps** (*completeness*). Every bounded increasing sequence converges, and every cut through the number line falls at a number. Hamilton got this property by appealing to the felt continuity of time. That's an intuition, not a proof, and intuitions about continuity had already misled people. Before Weierstrass, for example, it was widely believed that a continuous function must be differentiable at most points.

In 1872 Richard Dedekind built the reals from the rationals alone. He defined each real number as a **cut**: a split of the rationals into a lower set and an upper set. ($\sqrt{2}$ is the cut whose lower set is every rational $q$ with $q < 0$ or $q^2 < 2$.) In the same year Georg Cantor gave an equivalent construction using Cauchy sequences. Either way, completeness becomes a theorem, and no appeal to time or space is needed. (Some historians see a partial anticipation of Dedekind's cuts in Hamilton's essay, but the details are debated.)

The full chain of justification became

$$\mathbb{C} \xrightarrow{\text{Hamilton 1833}} \mathbb{R} \xrightarrow{\text{Dedekind, Cantor 1872}} \mathbb{Q} \to \mathbb{Z} \to \mathbb{N} \to \text{set theory}.$$

Hamilton's step was rigorous. The next one, from $\mathbb{R}$ to $\mathbb{Q}$, took 35 more years.

### What became of Kant's view

The view that geometry rests on a built-in intuition of space was badly shaken in the same century. Non-Euclidean geometries (Lobachevsky 1829, Bolyai 1832, Riemann 1854) are perfectly consistent. Later, general relativity suggested that physical space isn't Euclidean at all. If intuition can't even settle which geometry is true, it is a shaky foundation for algebra. That's one reason mathematics moved towards the modern approach: build everything from sets and logic, and treat space and time as sources of intuition rather than of justification. That is exactly the split described in [Foundation versus intuition](#foundation-versus-intuition).

Hamilton's time-based foundation didn't survive. But it did what he needed in 1833. It gave him a reason to believe that pairs of reals were *about* something, and that belief carried him on to the quaternions.

### An aside: do the laws of algebra come from space?

A thought I keep coming back to: some algebraic laws look like facts about the space we live in. Rearranging the order of additions or multiplications doesn't change the result, because rearranging physical things doesn't change them.

Euclid would have agreed. Proposition 1 of Book II of the *Elements* is essentially the distributive law, stated about areas. A rectangle of height $a$ on a base of length $b + c$ splits into two rectangles, $ab$ and $ac$. Commutativity of multiplication is the same rectangle turned on its side. Commutativity of addition is laying two lengths end to end in either order.

The twist comes from Hamilton himself. Space also gives us operations that *don't* commute. Rotate a book $90°$ about one axis and then about another, then do the same two rotations in the opposite order: the book ends up in different positions. That is why quaternions, which describe 3D rotations, had to give up $ab = ba$. So space doesn't hand us "the" laws of algebra. Each operation has its own laws: lengths and areas commute, but 3D rotations don't.

Mathematicians prefer to strip a structure down to its essential axioms. I can see the power of that, because the bare axioms suggest extensions that a picture would hide; non-Euclidean geometry is the classic example. But the world we live in and its practical problems are a huge driver of mathematics too. Understanding the simple parts of the real world well (lengths, areas, rotations) is often what lets us understand the more complex parts. The two approaches complement each other. Intuition about the world suggests the laws, and abstraction tells us which laws we actually used and what happens if we change them.
