# Dual numbers: Leibniz's infinitesimals made exact

Leibniz did calculus with infinitely small quantities $dx$. To differentiate $x^2$, he expanded

$$(x + dx)^2 = x^2 + 2x\,dx + dx^2,$$

then **dropped $dx^2$** because it was "infinitely smaller" than everything else, and read off $2x$ as the derivative. It worked every time, and nobody could justify it. Bishop Berkeley's 1734 objection was fair: $dx$ is treated as nonzero in one step and as zero in the next.

This note gives the clean fix. Invent a symbol $\varepsilon$ and declare one rule:

$$\varepsilon^2 = 0, \qquad \varepsilon \ne 0.$$

The resulting numbers $a + b\varepsilon$ are the **dual numbers**. In them, Leibniz's calculation is exact algebra, with no limits and no fudge. They are also a practical tool: running ordinary code on dual numbers gives exact derivatives. This is **forward-mode automatic differentiation**, built into PyTorch, JAX and Julia, and its reverse-mode sibling is the backpropagation that trains neural networks.

The construction is the same one that builds the complex numbers, with $\varepsilon^2 = 0$ in place of $i^2 = -1$. Section 3 explains that construction, "polynomials modulo $x^2$", from the ground up. Dual numbers are the easiest case to understand it with, and it then carries straight over to "polynomials modulo $x^2 + 1$", which is the complex numbers.

**Prerequisites:** basic calculus and algebra. The companion notes are [Complex numbers: six definitions of one thing](../complex-numbers/representations.md) (Sections 4–6) and the [section on infinity as a construction](../foundations/infinity-and-induction.md#10-infinity-as-a-construction), which places infinitesimals among the other constructions. Code: [dual_numbers.py](dual_numbers.py).

---

## 1. The problem: derivatives in code

Engineering software needs derivatives constantly: Newton's method, optimization, sensitivity analysis, Jacobians for circuit and ODE solvers, gradients for training models. There are three ways to get them.

**By hand, or by computer algebra.** Exact, but slow to do and easy to get wrong for big expressions. Symbolic differentiation of a long program also tends to blow up in size.

**Finite differences.** Approximate $f'(x) \approx \big(f(x + h) - f(x)\big)/h$. It's simple, but it has to balance two errors. Large $h$ gives *truncation* error from the curvature of $f$. Small $h$ gives *rounding* error, because $f(x + h)$ and $f(x)$ agree in most of their digits and subtracting them throws those digits away. For $f(x) = x \sin(x^2) + e^x$ at $x = 1.3$:

| $h$ | $10^{-2}$ | $10^{-5}$ | $10^{-8}$ | $10^{-11}$ | $10^{-14}$ |
|---|---|---|---|---|---|
| error | $3 \times 10^{-2}$ | $3 \times 10^{-5}$ | $1 \times 10^{-7}$ | $9 \times 10^{-6}$ | $3 \times 10^{-3}$ |

The best you can do is about $h \approx 10^{-8}$, the square root of machine epsilon, which gives roughly 8 correct digits out of 16. There is no way to do better with this formula.

**Automatic differentiation.** Exact to machine precision, at a small constant multiple of the cost of evaluating $f$, and without touching the source of $f$. Dual numbers are the simplest way to do it.

## 2. The construction

A **dual number** is $a + b\varepsilon$ with $a, b$ real. You calculate with dual numbers exactly as with polynomials in $\varepsilon$, using the single extra rule $\varepsilon^2 = 0$:

$$(a + b\varepsilon) + (c + d\varepsilon) = (a + c) + (b + d)\varepsilon,$$

$$(a + b\varepsilon)(c + d\varepsilon) = ac + (ad + bc)\varepsilon + bd\,\varepsilon^2 = ac + (ad + bc)\varepsilon.$$

Now repeat Leibniz's calculation with $\varepsilon$ in place of $dx$:

$$(3 + \varepsilon)^2 = 9 + 6\varepsilon + \varepsilon^2 = 9 + 6\varepsilon.$$

The **real part**, 9, is $f(3)$ for $f(x) = x^2$. The **$\varepsilon$ part**, 6, is $f'(3)$. Nothing was dropped by hand-waving. $\varepsilon^2$ is zero by the rule of the system.

Compare the complex numbers: $a + bi$ with the rule $i^2 = -1$ and otherwise ordinary algebra. It's the same kind of definition, with a different rule for the square.

## 3. What "polynomials modulo $x^2$" means

You can just accept the rule $\varepsilon^2 = 0$ and start calculating, and that's how most people use dual numbers. But it leaves two questions open. What *is* $\varepsilon$? And how do we know that declaring $\varepsilon^2 = 0$ (or $i^2 = -1$) can't lead to a contradiction somewhere? The polynomial construction answers both. Here it is in steps.

### Step 1: clock arithmetic

On a 12-hour clock, 14 o'clock is 2 o'clock. We say $14 \equiv 2 \pmod{12}$, "14 is congruent to 2 modulo 12", meaning that $14 - 2$ is a multiple of 12. Calculating "mod 12" means:

1. Do ordinary integer arithmetic.
2. Then **reduce**: replace the answer by its remainder after dividing by 12.

For example, $7 \times 5 = 35 \equiv 11$. In effect we have declared that **12 counts as zero**, and so does every multiple of 12.

### Step 2: the same with polynomials

Replace integers with polynomials in a variable $x$, and replace 12 with a fixed polynomial $m(x)$. Two polynomials are **congruent modulo $m$** if their difference is a multiple of $m$, that is, $m(x)$ times some polynomial. Calculating mod $m$ means:

1. Do ordinary polynomial arithmetic.
2. Then **reduce**: replace the answer by its remainder after dividing by $m(x)$.

In effect, **$m(x)$ counts as zero**.

### Step 3: modulo $x^2$ is truncation

Take $m(x) = x^2$. Dividing any polynomial by $x^2$ leaves as remainder its constant and linear terms:

$$c_0 + c_1 x + c_2 x^2 + c_3 x^3 + \cdots \;\equiv\; c_0 + c_1 x \pmod{x^2},$$

because everything from $c_2 x^2$ onward is $x^2$ times a polynomial. **Reducing mod $x^2$ just throws away $x^2$ and every higher power.** That's first-order Taylor truncation, something every engineer has done.

So every polynomial reduces to the form $a + bx$, and multiplying two of them gives

$$(a + bx)(c + dx) = ac + (ad + bc)x + bd\,x^2 \;\equiv\; ac + (ad + bc)x \pmod{x^2}.$$

That's exactly the dual number rule from Section 2. **The dual numbers are polynomials in $x$ with real coefficients, computed modulo $x^2$, and $\varepsilon$ is just $x$.** It isn't a mysterious number. It's an ordinary polynomial variable, and "$\varepsilon^2 = 0$" means "$x^2$ is a multiple of $x^2$", which is plainly true. In algebra this system is written $\mathbb{R}[x]/(x^2)$.

### Step 4: why this can't go wrong

Reducing in the middle of a calculation, or only at the end, has to give the same answer. Otherwise "the" result of a calculation wouldn't be well defined. This always works:

**Lemma.** If $p \equiv p'$ and $q \equiv q' \pmod m$, then $p + q \equiv p' + q'$ and $pq \equiv p'q' \pmod m$.

**Proof (complete).** The sum is clear: $(p + q) - (p' + q') = (p - p') + (q - q')$, which is a sum of multiples of $m$. For the product,

$$pq - p'q' = p(q - q') + (p - p')q',$$

and both terms are multiples of $m$. $\blacksquare$

This one line is the whole reason the construction is trustworthy. Polynomial arithmetic is already known to obey all the usual laws (associative, commutative, distributive). The lemma says that reducing mod $m$ respects addition and multiplication, so the reduced arithmetic inherits all those laws automatically. Declaring "$m$ counts as zero" can't create a contradiction. The same lemma, with integers in place of polynomials, is why clock arithmetic works.

### Step 5: modulo $x^2 + 1$ is the complex numbers

Now take $m(x) = x^2 + 1$. "$x^2 + 1$ counts as zero" means **$x^2$ counts as $-1$**. When you "replace $i^2$ by $-1$", you are already reducing mod $x^2 + 1$. The formal construction only names what you were doing.

Every polynomial again reduces to a remainder $a + bx$, because the remainder after dividing by a degree-2 polynomial has degree at most 1. Here's an example with the same numbers as in the complex numbers note:

$$(1 + 2x)(3 - x) = 3 + 5x - 2x^2.$$

To reduce, write $-2x^2 = -2(x^2 + 1) + 2$. The term $-2(x^2 + 1)$ is a multiple of $m$, so it counts as zero:

$$3 + 5x - 2x^2 \;\equiv\; 3 + 5x + 2 = 5 + 5x \pmod{x^2 + 1}.$$

Writing $i$ for $x$, that's $(1 + 2i)(3 - i) = 5 + 5i$, the ordinary complex product.

So the "glimpsed link" is this: **$i$ is just $x$, and $i^2 = -1$ is the reduction rule.** The construction answers "what is $i$?" with "a polynomial variable, which nobody doubts exists", and the lemma guarantees that $i^2 = -1$ is safe. That is why Cauchy (1847) and Kronecker (1880s) liked it: it builds a root of $x^2 + 1 = 0$ out of nothing but the equation itself. The [complex numbers note, Section 6](../complex-numbers/representations.md#6-polynomials-modulo-x2--1) goes on from here to finite fields and the DFT.

The only difference between the two systems is the polynomial you reduce by:

| System | Reduce modulo | Rule | Reduction in practice |
|---|---|---|---|
| Dual numbers | $x^2$ | $\varepsilon^2 = 0$ | drop $x^2$ and higher |
| Complex numbers | $x^2 + 1$ | $i^2 = -1$ | replace $x^2$ by $-1$ |
| Split-complex numbers | $x^2 - 1$ | $j^2 = +1$ | replace $x^2$ by $+1$ |

The third row is in Section 5.

## 4. Not a field, and why that answers Berkeley

Complex numbers form a **field**: every nonzero element has an inverse, so you can always divide. Dual numbers don't. The element $\varepsilon$ is nonzero, but

$$\varepsilon \cdot \varepsilon = 0,$$

so $\varepsilon$ has no inverse. If $\varepsilon \cdot y = 1$, multiplying both sides by $\varepsilon$ gives $0 = \varepsilon$, a contradiction. Two nonzero elements whose product is zero are called **zero divisors**. A system where you can add, subtract and multiply with all the usual laws, but not always divide, is a **ring**. (The integers are the familiar example.)

What you *can* divide by is anything with nonzero real part:

$$\frac{1}{a + b\varepsilon} = \frac{1}{a} - \frac{b}{a^2}\varepsilon \qquad (a \ne 0).$$

Check: $(a + b\varepsilon)\left(\frac{1}{a} - \frac{b}{a^2}\varepsilon\right) = 1 - \frac{b}{a}\varepsilon + \frac{b}{a}\varepsilon = 1$. And the $\varepsilon$ part, $-b/a^2$, is the derivative of $1/x$ times $b$, as Section 6 predicts.

This settles Berkeley's objection. Leibniz's $dx$ was incoherent because he **divided** by it (to form $dy/dx$) and then **dropped** it. In the dual numbers you never divide by $\varepsilon$, which is forbidden, so $\varepsilon$ can be nonzero and still square to zero. The derivative isn't a ratio of infinitesimals. It is a coefficient: the number in front of $\varepsilon$.

The general version of Section 3's construction explains the difference. $F[x]/(m)$ is a field exactly when $m$ can't be factored. $x^2 + 1$ has no real roots, so it can't be factored over $\mathbb{R}$, and $\mathbb{C}$ is a field. $x^2 = x \cdot x$ factors, and the factor $x$, which is $\varepsilon$, becomes a zero divisor.

## 5. Three siblings: the only two-dimensional number systems

Complex and dual numbers aren't two arbitrary inventions. They are two of exactly three possibilities.

**Theorem.** Let $A$ be a two-dimensional number system over $\mathbb{R}$: a real vector space of dimension 2 with a multiplication that is associative, distributes over addition, and has a unit 1. Then $A$ is isomorphic to exactly one of

$$\mathbb{R}[x]/(x^2 + 1) = \mathbb{C}, \qquad \mathbb{R}[x]/(x^2), \qquad \mathbb{R}[x]/(x^2 - 1).$$

**Proof (complete).** Pick any element $x$ not a multiple of 1, so $\{1, x\}$ is a basis. Then $x^2$ is in $A$, so $x^2 = p + qx$ for some reals $p$ and $q$. Complete the square: with $y = x - q/2$,

$$y^2 = x^2 - qx + \tfrac{q^2}{4} = p + \tfrac{q^2}{4} =: D.$$

If $D < 0$, then $y / \sqrt{-D}$ squares to $-1$. If $D = 0$, $y$ squares to 0. If $D > 0$, $y / \sqrt{D}$ squares to $+1$. In each case $\{1, \text{that element}\}$ is a basis whose multiplication is completely determined, which gives the three systems. They aren't isomorphic to one another: $\mathbb{C}$ has no zero divisors, the dual numbers have a nonzero element whose square is 0, and the split-complex numbers have neither property. (In them, $(1 + j)(1 - j) = 1 - j^2 = 0$, but no nonzero element squares to 0.) $\blacksquare$

Each sibling has a geometry, which shows up when you multiply by elements of "size 1":

| System | Quantity preserved | Multiplying by a unit is a | Physics |
|---|---|---|---|
| Complex, $i^2 = -1$ | $a^2 + b^2$ (circles) | rotation | rotations, phasors |
| Dual, $\varepsilon^2 = 0$ | $a^2$ (vertical lines) | shear: $(a + b\varepsilon)(1 + v\varepsilon) = a + (b + av)\varepsilon$ | Galilean boost: $t' = t$, $x' = x + vt$ |
| Split-complex, $j^2 = +1$ | $a^2 - b^2$ (hyperbolas) | hyperbolic rotation | Lorentz boost in special relativity |

Like complex numbers (see the [matrix view](../complex-numbers/representations.md#5-2-times-2-real-matrices)), dual numbers can be written as $2 \times 2$ matrices:

$$a + b\varepsilon \;\longleftrightarrow\; \begin{pmatrix} a & b \\ 0 & a \end{pmatrix} = aI + bN, \qquad N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad N^2 = 0.$$

$\varepsilon$ is a **nilpotent** matrix, one whose square is zero. Section 5 of the script checks that $(3I + N)^2 = 9I + 6N$.

## 6. The theorem: dual numbers compute derivatives

**Theorem.** For any polynomial $f$, and more generally any function given by a convergent power series,

$$f(a + b\varepsilon) = f(a) + f'(a)\,b\,\varepsilon.$$

In particular, $f(a + \varepsilon) = f(a) + f'(a)\,\varepsilon$: evaluate $f$ at $a + \varepsilon$ and read the derivative off the $\varepsilon$ part.

**Proof for polynomials (complete).** By the binomial theorem, which holds because dual numbers commute,

$$(a + b\varepsilon)^n = a^n + n a^{n-1} b\varepsilon + \binom{n}{2} a^{n-2} b^2 \varepsilon^2 + \cdots = a^n + n a^{n-1} b\,\varepsilon,$$

since every term with $\varepsilon^2$ or a higher power is zero. So the theorem holds for $f(x) = x^n$, whose derivative is $n x^{n-1}$. Both sides of the theorem are linear in $f$, so it holds for every polynomial. $\blacksquare$

**Extension to power series (complete, given convergence).** If $f(x) = \sum_n c_n (x - a)^n$ near $a$, then substituting $x = a + b\varepsilon$ gives $(b\varepsilon)^n = 0$ for $n \ge 2$, so the series **stops** after the linear term: $f(a + b\varepsilon) = c_0 + c_1 b \varepsilon = f(a) + f'(a) b\varepsilon$. This is Taylor's theorem with the remainder made *exactly* zero, not small. That covers $\sin$, $\exp$, $\log$ and the other standard functions. In fact this formula is how $f$ is *defined* on dual numbers when $f$ isn't a polynomial.

**The calculus rules fall out of the algebra.** You don't have to program the product and chain rules. They are already in the multiplication:

- **Product rule:** $(u + u'\varepsilon)(v + v'\varepsilon) = uv + (uv' + u'v)\varepsilon$. The $\varepsilon$ part is $(uv)' = uv' + u'v$.
- **Chain rule:** $f\big(g(a + \varepsilon)\big) = f\big(g(a) + g'(a)\varepsilon\big) = f(g(a)) + f'(g(a))\,g'(a)\,\varepsilon$, using the theorem twice.

So an implementation only needs to know the derivative of each *primitive* operation ($+$, $\times$, $\sin$, $\exp$, ...). The algebra of dual numbers then combines them correctly through any program, however long. This is the "easy to get right with familiar tools" part: the bookkeeping that is error-prone by hand is done by ring arithmetic, which can't make mistakes.

## 7. In Python

A complete forward-mode AD system fits in a few lines. This is condensed from [dual_numbers.py](dual_numbers.py):

```python
import math

class Dual:
    """a + b*eps, where eps^2 = 0. a is the value, b the derivative part."""
    def __init__(self, a, b=0.0):
        self.a, self.b = a, b
    def __add__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __mul__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.a * other.a, self.a * other.b + self.b * other.a)
    __rmul__ = __mul__

def sin(x):  # each primitive knows its own derivative
    return Dual(math.sin(x.a), math.cos(x.a) * x.b) if isinstance(x, Dual) else math.sin(x)

def exp(x):
    return Dual(math.exp(x.a), math.exp(x.a) * x.b) if isinstance(x, Dual) else math.exp(x)

def derivative(f, x):
    return f(Dual(x, 1.0)).b      # evaluate at x + eps, read off the eps part

def f(x):
    return x * sin(x * x) + exp(x)

print(derivative(f, 1.3))
# 4.260245414490813
```

The answer agrees with the hand-computed $f'(x) = \sin(x^2) + 2x^2 \cos(x^2) + e^x$ to all 16 digits. The finite-difference table in Section 1 managed 8. Note that `f` is ordinary code. It was written without derivatives in mind and is differentiated without being changed.

### A cousin: the complex-step derivative

Complex numbers can *almost* do the same job. If $h$ is tiny, then $(ih)^2 = -h^2$ is negligible, so $ih$ behaves almost like $\varepsilon$:

$$f'(x) \approx \frac{\operatorname{Im} f(x + ih)}{h}.$$

Unlike a finite difference, there is no subtraction, so nothing cancels, and $h$ can be absurdly small. With $h = 10^{-20}$ the script gets the derivative to full precision. This trick (Lyness and Moler 1967, popularized by Squire and Trapp 1998) is used in aerospace codes because any code that already handles complex numbers gets derivatives for free. Dual numbers are the exact version: instead of "$i h$ with $h$ tiny so that its square is negligible", they use an $\varepsilon$ whose square is exactly zero.

## 8. Engineering payoff, and limits

**Where it's used.**

- **Libraries.** Julia's `ForwardDiff.jl` uses dual numbers directly. PyTorch's forward-mode API is built on them (`torch.autograd.forward_ad.make_dual`). JAX's `jvp` (Jacobian–vector product) computes the same thing.
- **Higher derivatives.** Reduce modulo $x^3$ instead of $x^2$ and the $x^2$ coefficient carries $f''/2$. In general, computing mod $x^{k+1}$ gives a degree-$k$ Taylor polynomial. This is "Taylor-mode" AD, built by the same construction with a different modulus.
- **Rigid-body motion.** Clifford and Study combined dual numbers with quaternions to get **dual quaternions**, which represent a rotation and a translation together. They are used in robot kinematics and in computer graphics, for example to deform a character's skin smoothly around its skeleton.

**Forward vs. reverse mode.** One evaluation with dual numbers gives the derivative along **one** input direction. For $f : \mathbb{R}^n \to \mathbb{R}$, a full gradient takes $n$ evaluations. That's fine for a few inputs, but hopeless for a neural network with $10^9$ weights. **Reverse mode** applies the chain rule in the opposite order. It records the computation, then sweeps backwards once, and gets the whole gradient in a single pass at a few times the cost of evaluating $f$. Applied to neural networks, reverse mode is **backpropagation**. It is a different organization of the same chain rule, and deserves its own note.

**AD differentiates the program, not the function.** This function is mathematically the identity, $g(x) = x$, whose derivative is 1 everywhere:

```python
def g(x):
    return 0.0 if x.a == 0 else x      # equals x for every x, including 0
```

At $x = 0$ the branch returns a plain constant, which carries no $\varepsilon$ part, so AD reports $g'(0) = 0$. Branches, comparisons, and functions like $|x|$ or $\sqrt{x}$ at 0 are where AD can mislead. It differentiates the path the code actually took.

## 9. History

| Date | Who | What |
|---|---|---|
| 1670s–80s | Leibniz | calculus with infinitesimals $dx$, dropping $dx^2$ |
| 1734 | Berkeley | *The Analyst*: infinitesimals are "the ghosts of departed quantities" |
| 1820s–70s | Cauchy, Weierstrass | calculus rebuilt on ε–N limits, without infinitesimals |
| 1873 | W. K. Clifford | introduces dual numbers, for mechanics of screw motions |
| 1891 | Eduard Study | "dual angles" for the relative position of two lines in space; dual numbers become standard in kinematics |
| 1964 | R. E. Wengert | first forward-mode automatic differentiation program |
| 1970 | Seppo Linnainmaa | reverse-mode AD, in a master's thesis |
| 1986 | Rumelhart, Hinton, Williams | backpropagation popularized for training neural networks |

Clifford was after geometry, not derivatives. Using dual numbers to differentiate came later, and early AD programs didn't use the language of dual numbers at all. The connection was recognized afterwards. As happened with complex numbers, the construction found uses far from where it started.

Section 3's construction and Robinson's nonstandard analysis give two different ways to make infinitesimals rigorous. Robinson's infinitesimals live in a field: you can divide by them, and $dx^2$ is a tiny nonzero number. Dual numbers give up division to get $\varepsilon^2 = 0$ exactly. Which one to use depends on the job: Robinson's for proving theorems in analysis, dual numbers for computing derivatives.

## 10. Invention or discovery?

- **The symbol is an invention.** Nothing forces anyone to write $a + b\varepsilon$, just as nothing forced anyone to write $i$.
- **The options are a discovery.** Section 5 shows that two-dimensional number systems over $\mathbb{R}$ come in exactly three kinds. Once you ask for one in which some nonzero element squares to zero, the dual numbers are the only answer.
- **That they compute derivatives is a discovery.** Nobody designed $\varepsilon^2 = 0$ to produce the product rule. It falls out of the multiplication.

It's the pattern from the [complex numbers](../complex-numbers/representations.md#8-discovery-or-invention) and from [zero](../numeration/positional-notation-and-zero.md#6-invention-or-discovery): a new construction is introduced for practical reasons, and then turns out to have properties of its own that nobody chose.

**Further reading:** Atılım Güneş Baydin et al., "Automatic Differentiation in Machine Learning: a Survey" (*JMLR*, 2018), readable and free online. Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (2nd ed., 2008), the standard reference. J. R. R. A. Martins, P. Sturdza and J. J. Alonso, "The Complex-Step Derivative Approximation" (*ACM TOMS*, 2003), for the complex-step method in engineering.
