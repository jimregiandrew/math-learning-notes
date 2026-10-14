# The last number: infinity and reasoning by recurrence

Why do we trust mathematics more than any other kind of knowledge? A physicist accepts a law after enough experiments, and knows a new experiment could overturn it. A mathematician claims that $a + b = b + a$ for **every** pair of whole numbers, and nobody expects a counterexample to turn up. Yet nobody has checked every pair, because there are infinitely many.

This note follows Chapter 4 of Tobias Dantzig's *Number: The Language of Science*, "The Last Number". Dantzig traces the certainty of mathematics back to one small word, **all**, and to the one tool that lets a finite argument cover infinitely many cases. He calls it **reasoning by recurrence**; today it is usually called **mathematical induction**. He then asks where the tool gets its authority, and his answer is surprising: not from logic and not from experience, but from an *assumption* that counting never ends.

The engineering payoff is unusually direct. Dantzig describes, as a thought experiment, an arithmetic that stops at a largest number. Every computer does exactly that, and the laws of arithmetic that induction proves start to fail in it.

**Prerequisites:** none beyond arithmetic. It helps to have read the Chapter 2 note, [Positional notation and zero](../numeration/positional-notation-and-zero.md), which this one refers back to.

---

## 1. The puzzle: everything hangs on "all"

Dantzig starts in the classroom. We memorized $1 + 1 = 2$, $1 + 2 = 3$, ... and then were shown that $5 + 3 = 3 + 5$ "is not an accident, but a general rule". Later the rules got names:

$$a + b = b + a \quad \text{(commutative)}, \qquad (a + b) + c = a + (b + c) \quad \text{(associative)}, \qquad a(b + c) = ab + ac \quad \text{(distributive)}.$$

These look like trivia, but every written calculation depends on them. Long multiplication is the distributive law used over and over:

$$25 \times 43 = (20 + 5)(40 + 3) = 20 \cdot 40 + 5 \cdot 40 + 20 \cdot 3 + 5 \cdot 3 = 1075.$$

This is the payoff of [place value](../numeration/positional-notation-and-zero.md#5-the-payoff) from Chapter 2: a numeral is a sum of digits times powers of ten, and the school algorithms rearrange those sums. So the place-value algorithms are only as reliable as the laws they rest on.

Dantzig's observation is that we learn these laws at age six, when we ask *how*, and by the time we're old enough to ask *why*, they feel too obvious to question. The same happened historically: "the 'how' always preceded the 'why'". The rules of reckoning were settled by the end of the Renaissance. Nobody seriously asked why they were true until the late 19th century.

So why are they true? The laws are claims about **all** numbers. For a finite collection, "all" is unproblematic: you could in principle check every member. Whole numbers are different:

> All numbers! Everything hangs on this short but so tremendously important word *all*.

There is no last number, so the checking can never finish. How, then, can anyone prove anything about all of them?

## 2. Where does infinity come from?

Every number has a successor, so the counting never ends. Dantzig asks where we get this belief, and he rules out the obvious sources:

- **Not from experience.** Everything we experience is finite. "Any attempt on our part to exhaust number by counting would only end in our own exhaustion."
- **Not from a proof.** That counting never ends is not a theorem. It is "the basic assumption of arithmetic, on which all mathematics rests".

He suggests that early peoples didn't think of infinity as *uncountable*, but as *not yet counted*. There was a last number, but it belonged to the gods. The stars, the grains of sand and the drops of the ocean were the standard examples of a number too big for people.

### Archimedes and the grains of sand

The most famous attack on this idea is Archimedes' *The Sand Reckoner* (c. 250 BCE), written to King Gelon of Syracuse. Some people, he says, think the number of grains of sand is infinite. Others think it is finite but bigger than any number that can be *named*. He sets out to show both are wrong.

The second group had a point, and it was a point about **notation**, just like Chapter 2. Greek numerals ran out at the myriad, 10,000. The largest number with a standard name was a myriad myriads, $10^8$. Archimedes built a new naming scheme on top of that:

- Numbers up to $10^8$ are the **first order**.
- $10^8$ is the unit of the **second order**, which runs up to $10^{16}$. The third order runs up to $10^{24}$, and so on.
- He continued to the $10^8$-th order, and then built "periods" of orders on top of that. His largest named number is $(10^8)^{10^{16}} = 10^{8 \times 10^{16}}$, a 1 followed by eighty quadrillion zeros.

In effect this is **place value in base $10^8$**, used for naming numbers rather than calculating. Along the way Archimedes proves that multiplying numbers in his scheme means *adding their positions*, which in modern terms is $10^a \cdot 10^b = 10^{a+b}$. That is the core idea of logarithms, eighteen centuries before Napier.

Then he estimates the sand. He assumes that 10,000 grains fill a poppy seed, and uses generous bounds for the sizes of the earth and the cosmos. A universe reaching out to the sun would hold fewer than $10^{51}$ grains. That number has 52 digits, the figure Dantzig quotes. Even the much larger universe of Aristarchus, who put the sun at the centre, would hold fewer than $10^{63}$. (This passage is our main source for Aristarchus' heliocentric model.)

The point isn't the estimate. Archimedes showed that "a very large number" and "infinity" are different things, and that the difference is one of notation and patience, not of kind. Any finite collection, however huge, can be named and exceeded.

**Two corrections to Dantzig's account.** He says the new unit "corresponded to our 100,000". It was $10^8$, a myriad myriads. He also attaches the 52-digit count to the sphere of the fixed stars. In Archimedes the $10^{51}$ bound is for the smaller universe, and $10^{63}$ is for the sphere of the fixed stars.

### Infinity as "not yet reached"

Dantzig's second example is squaring the circle. You can construct a square equal in area to a regular polygon. If you double the number of sides of a polygon inside a circle, 8, 16, 32, ..., its area gets closer and closer to the circle's. Some Greek geometers seem to have thought that continuing long enough would actually *reach* the circle: a final polygon equal to it. This is infinity treated as a very large finite number, the same mistake Archimedes was correcting with sand. It is also the first appearance of limits, which Dantzig returns to in later chapters.

## 3. Two meanings of "induction"

Dantzig carefully separates two kinds of reasoning.

**Physical induction** goes from particular cases to a general rule. You melt many samples of lead, every one melts at the same temperature, and you conclude that this is the melting point of lead. Behind it is a belief that nature is uniform. All experimental science works this way, and it is never certain.

**In mathematics this is banned**, and Dantzig gives an example of why. The expression

$$n^2 - n + 41$$

gives a prime for $n = 1, 2, \ldots, 40$, forty times in a row. At $n = 41$ it gives $41^2 - 41 + 41 = 41^2$, which isn't prime. "Many a physical law has been held valid on less evidence."

In mathematics, no number of examples proves a general statement, and a single counterexample disproves it. So the laws of arithmetic must be proved by deduction. But ordinary deduction handles only finitely many steps. What principle bridges the gap?

## 4. Reasoning by recurrence

Dantzig's illustration is a line of soldiers. Each soldier has orders to pass any news to the neighbour on their right. An officer wants to know whether every soldier has heard about some event. Asking each soldier isn't necessary. It is enough to know two things:

1. **The first soldier has heard.**
2. **Whatever any soldier knows, the next one also knows.**

Then the news reaches the second soldier, then the third, and so on down the line.

That is the whole principle. Stated for whole numbers:

> **Principle of induction.** Suppose a statement $P(n)$ about whole numbers satisfies
> 1. $P(1)$ is true (the **base case**), and
> 2. for every $n$, if $P(n)$ is true then $P(n+1)$ is true (the **inductive step**).
>
> Then $P(n)$ is true for every whole number $n$.

Bertrand Russell called a property that passes from each number to its successor **hereditary**, so step 2 says that $P$ is hereditary.

**A warning about terms.** Dantzig calls the base case "the induction step" and the inductive step "the hereditary feature". Modern usage is the reverse: the *inductive step* is the hereditary part. This note uses the modern terms. Dantzig also disliked the name "mathematical induction" for this method. He preferred "reasoning by recurrence", because the method has nothing to do with collecting examples. The name "induction" stuck anyway. Augustus De Morgan popularized "mathematical induction" in 1838.

### Both steps are needed

Fermat supplies examples where only one step is available.

- **Fermat numbers.** Fermat checked that $2^{2^n} + 1$ is prime for $n = 0, 1, 2, 3, 4$. That's a base case, five times over. But he had no inductive step, and in 1732 Euler showed that $n = 5$ fails: $2^{32} + 1 = 641 \times 6700417$.
- **Fermat's Last Theorem.** Dantzig presents this as a base case ($x^3 + y^3 = z^3$ has no solutions, which Euler proved) that was still waiting for an inductive step from $n$ to $n + 1$. That isn't quite how the problem works, though. Knowing the result for $n$ says almost nothing about $n + 1$. What actually helps is that a solution for $n = pq$ gives one for $n = p$, since $x^{pq} = (x^q)^p$. So it is enough to handle $n = 4$ and every odd prime. Wiles' proof in 1994 didn't use induction on $n$ at all. Dantzig was writing when the problem was still open.

The base case alone is the trap of physical induction. The inductive step alone is just as useless. The step "if $n^2 - n + 41$ is prime then so is the next value" is false, but even a true hereditary property proves nothing until something starts it off.

### History

Dantzig credits the first explicit statement of the principle to **Blaise Pascal**, in his *Treatise on the Arithmetical Triangle* (written in 1654). Pascal proves a property of his triangle by showing that it holds in the first row, and that if it holds in one row it holds in the next.

Dantzig points out an irony. The treatise grew out of Pascal's letters with Fermat about a gambling question: how to split the stakes fairly when a game is stopped early. Those letters are also the starting point of probability theory. So recurrence, the basis of certainty in pure mathematics, and probability, the basis of reasoning in the uncertain experimental sciences, were both born from the same gambling problem.

Historians have since found earlier, less explicit uses of the method. Al-Karajī (Baghdad, c. 1000) proved the formula for the sum of cubes with an argument that steps from one case to the next. Levi ben Gershon (France, 1321) and Francesco Maurolico (Sicily, 1575) used it more clearly. Maurolico used it to prove that the sum of the first $n$ odd numbers is $n^2$. Pascal's version is the first to state the principle cleanly as a method.

## 5. The theorem: proving a law of arithmetic

Here is how induction proves a law that school takes on faith. This is Dantzig's own example, tidied up.

**Start with less than you'd think.** Assume only that we have whole numbers $1, 2, 3, \ldots$ and the operation "add one", written $n \mapsto n + 1$. Then **define** addition in general by recurrence:

$$a + 1 \text{ is the successor of } a, \qquad a + (b + 1) = (a + b) + 1. \tag{D}$$

In words: to add $b + 1$, add $b$, then add one more. This defines $a + b$ for every $b$, by recurrence on $b$.

**Theorem (associativity of addition).** For all whole numbers $a, b, c$: $\;a + (b + c) = (a + b) + c$.

**Proof (complete).** Fix $a$ and $b$ and use induction on $c$.

*Base case, $c = 1$:* $a + (b + 1) = (a + b) + 1$. This is exactly definition (D).

*Inductive step:* assume $a + (b + n) = (a + b) + n$ for some $n$. Then

$$
\begin{aligned}
a + \big(b + (n + 1)\big) &= a + \big((b + n) + 1\big) && \text{by (D)} \\
&= \big(a + (b + n)\big) + 1 && \text{by (D)} \\
&= \big((a + b) + n\big) + 1 && \text{by the assumption} \\
&= (a + b) + (n + 1) && \text{by (D)}.
\end{aligned}
$$

That is the statement for $c = n + 1$. By induction it holds for every $c$. $\blacksquare$

A few things to notice:

- **Nothing was checked by example.** Every line follows from the definition and the assumption. One finite argument covers infinitely many cases.
- **Commutativity is harder.** Proving $a + b = b + a$ the same way takes two inductions: first prove $1 + b = b + 1$ by induction on $b$, then use that to prove the general case. Multiplication is defined by recurrence in the same way ($a \cdot 1 = a$, $a \cdot (b + 1) = a \cdot b + a$), and its laws, including the distributive law, are proved by further inductions. All of school arithmetic can be rebuilt this way. Giuseppe Peano did exactly that in 1889.
- **The definition is a program.** Definition (D) is a recursive function. Recursion and induction are the same idea seen from two sides: a recursion builds a value step by step, and an induction proves something about it step by step.

```python
def add(a, b):
    """a + b for whole numbers, using only 'add 1' (a + 1 is the successor of a)."""
    if b == 1:
        return a + 1              # a + 1 is the successor of a
    return add(a, b - 1) + 1      # a + (b' + 1) = (a + b') + 1, with b' = b - 1

print(add(25, 34))
# 59
print(all(add(a, add(b, c)) == add(add(a, b), c)
          for a in range(1, 20) for b in range(1, 20) for c in range(1, 20)))
# True
```

The second check is physical induction: 6,859 cases, all of them passing, and still not a proof. The proof above is what makes it certain.

## 6. Poincaré's dilemma

Dantzig gives much of the chapter to Henri Poincaré's essay *On the Nature of Mathematical Reasoning* (1894), later the first chapter of *Science and Hypothesis* (1902). Dantzig had studied under Poincaré in Paris, and the essay shaped his thinking.

Poincaré starts from a dilemma. If mathematics is pure logic, deducing everything from the principle of contradiction, then it can never tell us anything new. Logic only unpacks what the premises already contain. Then all those volumes of theorems would be "devious ways of saying that A is A". But mathematics obviously does produce new knowledge. So where does the new knowledge come from?

His answer is reasoning by recurrence:

- **It isn't logic.** Logic can chain together as many steps as you like, but always a finite number. Induction packs *infinitely many* steps into one formula: $P(1)$, so $P(2)$, so $P(3)$, ... "It is only before the infinite that this principle of logic fails."
- **It isn't experience.** Experience could confirm the rule for the first hundred numbers, never for all of them.
- **It is a fact about the mind.** The principle forces itself on us because it is "the affirmation of the power of the mind which knows itself capable of conceiving the indefinite repetition of the same act when this act is possible at all". It is certain, unlike physical induction, because it depends on what we can do, not on any order in nature.

He ends with a nice remark. Induction works only when the same operation can be repeated indefinitely, and that "is why the theory of chess can never become a science: the different moves of the game do not resemble one another."

## 7. Dantzig's answer: what induction really assumes

Dantzig then adds his own analysis, which is the sharpest part of the chapter. He splits induction in two.

**The restricted principle is just logic.** Applied to a *finite* sequence, like the soldiers, induction is a finite chain of ordinary deductions. Nothing beyond classical logic is needed.

**A bounded arithmetic is perfectly consistent.** Imagine an arithmetic that stops at a last number, say 1,000,000. In it, addition and multiplication are associative and commutative *when they are defined*. But many sums and products don't exist: $500{,}000 + 500{,}001$ and $1000 \times 1001$ are meaningless. Decimals could have at most six places, so $1/3$ would have no decimal form. Dividing anything into a million parts would reach the indivisible. Dantzig says this arithmetic is "logically impregnable" and even closer to what our senses tell us than the infinite version.

**So what does the general principle add?** When induction is used on all whole numbers, it *tacitly assumes that every number has a successor*. That assumption is:

- not required by logic, since bounded arithmetic is equally consistent;
- not given by experience, which "proclaims its falsity";
- not supported by physics, which (in Dantzig's day) suggested a finite universe and atoms that can't be divided forever.

"And yet the concept of infinity, though not imposed upon us either by logic or by experience, is a mathematical necessity." Without it you get the crippled arithmetic above. Dantzig leaves the question of where this power comes from open, and says he will return to it throughout the book.

## 8. The payoff: computers do bounded arithmetic

Dantzig offered bounded arithmetic as a thought experiment. Every processor runs one, with a last number fixed by its word size. His predictions come true, and engineers have to deal with them every day. Computers handle the missing successor in three main ways.

### Fixed-width integers: the last number wraps around

A 32-bit signed integer has a last number, $2^{31} - 1 = 2{,}147{,}483{,}647$. Its "successor" wraps around to the most negative number:

```python
import numpy as np

x = np.array([2_147_483_647], dtype=np.int32)
print(x + 1)
# [-2147483648]
```

Real failures have come from exactly this:

- In 2014 the view counter for the video "Gangnam Style" passed $2^{31} - 1$, and YouTube had to switch to 64-bit counters.
- In 1996 the Ariane 5 rocket was destroyed 37 seconds after launch, after a 64-bit floating-point value was converted to a 16-bit integer that couldn't hold it.
- Unix systems that store time as signed 32-bit seconds since 1970 run out on 19 January 2038, the "Year 2038 problem".

Wraparound is an interesting choice, though. For unsigned integers, arithmetic mod $2^{32}$ is a **ring**: addition and multiplication are still associative, commutative and distributive, *with no exceptions*. Instead of Dantzig's "meaningless" sums, the line of numbers is bent into a circle. What breaks is order: in this arithmetic $x + 1 > x$ is no longer always true. In Peano's terms, every number now has a successor, but the successor of the last one is 0. (Modular arithmetic is the [same construction](../complex-numbers/representations.md) that built the complex numbers: do the arithmetic, then reduce.)

### Floating point: the laws themselves fail

Floating-point numbers have a largest value, and also a smallest step, which is Dantzig's "indivisible". Near 1.0, the gap between neighbouring double-precision numbers is about $2.2 \times 10^{-16}$ (machine epsilon), and anything smaller just disappears. As he predicted, $1/3$ has no exact form:

```python
print(np.finfo(np.float64).eps, 1.0 + 1e-17 == 1.0)
# 2.220446049250313e-16 True
print(1 / 3)
# 0.3333333333333333
```

The bigger casualty is the law proved in Section 5. **Floating-point addition is not associative:**

```python
print((0.1 + 0.2) + 0.3, 0.1 + (0.2 + 0.3))
# 0.6000000000000001 0.6
print((1.0 + 1e16) - 1e16, 1.0 + (1e16 - 1e16))
# 0.0 1.0
```

The proof breaks because rounding destroys definition (D): in floating point, $(a + b) + 1$ isn't always one step past $a + b$. In practice this means:

- **Order changes the answer.** Summing the same array in a different order gives a slightly different result. GPU and multi-threaded code sums in an unpredictable order, so the same computation can give different results on different runs.
- **Compilers can't reorder.** A compiler isn't allowed to rewrite `(a + b) + c` as `a + (b + c)` unless you tell it to ignore floating-point rules (flags like `-ffast-math`).
- **Careful summation is a real technique.** Kahan summation, or adding small terms before large ones, exists because associativity fails.

### Arbitrary precision: Archimedes' solution

Python's own integers take the other path: they have no last number, apart from available memory.

```python
print(2**100)
# 1267650600228229401496703205376
```

Internally, CPython stores a big integer as a list of "digits" in base $2^{30}$ (see `sys.int_info`). This is the [base-$b$ representation](../numeration/positional-notation-and-zero.md#4-the-theorem-behind-place-value) from Chapter 2 with a very large base, and the same move Archimedes made with base $10^8$: when the numbers outgrow your notation, use a bigger base and go on counting.

### Proving programs correct

Induction is also the main tool for proving that code is correct. A **loop invariant** is a statement that is true before the loop starts (base case) and stays true after each pass (inductive step), so it is true when the loop ends. This method is due to Robert Floyd (1967) and Tony Hoare (1969). Take Horner's rule from the Chapter 2 note:

```python
def value(ds, b):
    """Evaluate the digit list ds in base b with Horner's rule."""
    n = 0
    for d in ds:
        n = n * b + d    # invariant: n is the value of the digits read so far
    return n
```

Base case: before any digits are read, $n = 0$, the value of the empty digit string. Inductive step: if $n$ is the value of the first $k$ digits, then $n b + d_{k+1}$ is the value of the first $k + 1$, because appending a digit shifts everything up one place. So when the loop finishes, $n$ is the value of the whole numeral. Any recursive function is proved correct in the same way.

## 9. Invention or discovery?

Dantzig's analysis gives an unusually clear answer here.

- **That counting never ends is an assumption, not a discovery.** Dantzig shows that logic doesn't force it and experience doesn't support it. Modern mathematics agrees and makes the choice explicit: Peano's axioms include induction as an axiom, and set theory includes an **Axiom of Infinity**, which states outright that an infinite set exists.
- **The choice isn't arbitrary.** The alternative, bounded arithmetic, is consistent but much weaker. We choose infinity because it makes arithmetic *closed* (every sum and product exists) and its laws *exceptionless*. Computers show the cost of choosing the other way.
- **Once the choice is made, the consequences are discoveries.** Given definition (D) and the induction axiom, associativity isn't up to anyone. It has to be proved, and once proved it holds.

This is the same pattern as [zero in Chapter 2](../numeration/positional-notation-and-zero.md#6-invention-or-discovery). A concept is introduced for human reasons, and then has properties that nobody chose.

## 10. Infinity as a construction

The chapter can leave the impression that infinity is something mysterious. A more useful way to see it, and the one most mathematicians hold today, is that infinity is **another construction** in the same line as zero, negative numbers and fractions. It is a very powerful one. But it has one feature the earlier ones didn't: it needs a genuinely new assumption, and it behaves less nicely.

### Potential and actual infinity

Aristotle separated two ideas that the word "infinity" runs together:

- **Potential infinity:** a process with no upper bound. However far you've counted, you can count one more. No infinite *object* is involved.
- **Actual infinity:** the completed whole. All the natural numbers taken together as one finished object, $\mathbb{N}$.

Aristotle accepted only the first, and mathematics mostly followed him for over two thousand years. Gauss, in an 1831 letter:

> I protest against the use of infinite magnitude as something completed, which is never permissible in mathematics. Infinity is merely a way of speaking, the true meaning being a limit which certain ratios approach indefinitely close, while others are permitted to increase without restriction.

Induction needs only potential infinity. A proof by induction is a recipe: give me any $n$, and the argument produces $P(n)$ in $n$ steps. Even Brouwer's intuitionists, the strictest critics of the infinite in Dantzig's time, accepted it.

### "Reachable from 0" is induction

It is tempting to justify induction by saying that every whole number can be reached from 0 by adding 1 enough times. But that isn't a separate fact that supports induction. It *is* induction, in other words.

Try to define "whole number" using only 0 and the successor $n \mapsto n + 1$. The successor gives you $0, 1, 2, \ldots$, so these are *at least* in the collection. You still need to say that **nothing else** is. Dedekind (1888) said it this way: $\mathbb{N}$ is the **smallest** collection that contains 0 and contains the successor of everything it contains. "Smallest" is the induction axiom. If a property holds for 0 and is hereditary, then the numbers with that property form such a collection, and since $\mathbb{N}$ is the smallest, they include all of $\mathbb{N}$.

You can't escape this by defining a whole number as "something reached in finitely many steps", because "finitely many" already uses the whole numbers. And the "nothing else" part has real content. In 1934 Thoralf Skolem showed that the usual first-order axioms for arithmetic also hold in "nonstandard" number systems, which contain extra numbers beyond every $0, 1, 2, \ldots$ that can never be reached from 0 (see Section 11).

### Limits need only potential infinity; their existence needs more

Calculus used to be built on infinitely small quantities. Cauchy, Bolzano and Weierstrass replaced them with the $\varepsilon$–$N$ definition:

$$a_n \to L \quad \text{means} \quad \text{for every } \varepsilon > 0 \text{ there is an } N \text{ such that } |a_n - L| < \varepsilon \text{ for all } n > N.$$

Every quantity here is finite. This is Gauss's "limit which certain ratios approach", made precise.

But the definition assumes the number $L$ already exists, and with only rational numbers it may not. The rationals

$$1,\ 1.4,\ 1.41,\ 1.414,\ 1.4142,\ \ldots$$

get as close to each other as you like, but there is no rational number for them to approach, since $\sqrt{2}$ is irrational. In the same way, $x^2 - 2$ is negative at 1 and positive at 2 but has no rational root.

In 1872 Cantor and Dedekind independently filled the gaps by turning the problem around. Cantor defined a real number to *be* the whole sequence: $\sqrt{2}$ is the entire infinite sequence $1, 1.4, 1.41, \ldots$ (strictly, the class of all rational sequences that get arbitrarily close to it). Dedekind defined a real number as a "cut", an infinite set of rationals. Either way, once the construction is made, every such sequence has a limit by construction. That is the property called **completeness**.

### The one new assumption

Line up the constructions of the number systems:

| Number system | Construction | Built from |
|---|---|---|
| Integers | pairs $(a, b)$ of naturals, meaning $a - b$ | finite objects |
| Rationals | pairs $(p, q)$ of integers, meaning $p / q$ | finite objects |
| Reals | sequences of rationals (Cantor) or cuts (Dedekind) | **infinite objects** |
| Complex numbers | pairs of reals ([Hamilton](../complex-numbers/representations.md#4-ordered-pairs-of-reals-hamilton)) | reals |

Up to the rationals, each step uses pairs of things you already have, and nothing new has to be assumed. The reals are different. A sequence of rationals is a function from $\mathbb{N}$ to $\mathbb{Q}$, so before you can build reals you need $\mathbb{N}$ available as a completed collection. Potential infinity isn't enough.

That is the one genuinely new assumption in the whole chain, and modern set theory states it as an axiom. The **Axiom of Infinity** (Zermelo, 1908) says that there exists a set containing 0 and the successor of each of its members. It is Dantzig's "every number has a successor", promoted from a property of a process to the existence of a completed object. Everything after it is construction.

### What the infinite costs

Zero and negative numbers behave very nicely: they extend arithmetic without disturbing anything. The infinite is more powerful and less tame.

- **Paradoxes.** Unrestricted reasoning about infinite collections leads to contradictions. Russell's paradox (1901) concerns "the set of all sets that don't contain themselves". Mathematics had to lay down careful rules for which collections can be built: Zermelo's axioms (1908), later extended to the standard system, ZF.
- **Questions with no answer.** Is there a size of infinity strictly between the whole numbers and the reals? This is Cantor's continuum hypothesis. Gödel (1940) and Cohen (1963) showed that the standard axioms can't decide it either way. No construction of negative numbers ever left a question like that open.
- **Existence without construction.** Classical analysis proves that things exist, such as roots, minima and solutions of equations, without giving a way to compute them. Errett Bishop's *Foundations of Constructive Analysis* (1967) rebuilt much of analysis using only potential infinity, treating a real number as a *rule* for computing approximations. Some classical theorems then need extra conditions. For example, the intermediate value theorem ("a continuous function that changes sign has a root") no longer holds in its classical form.

A computer lives on the potential side. Floats are finite rationals, so bisection on floats stops at two neighbouring floats with the root somewhere between them. The guarantee that a root *exists* comes from the complete reals, which no computer can hold. The existence theorems behind Fourier series in $L^2$, solutions of differential equations and minima in optimization all rest on completeness in the same way.

### Several infinities

There isn't one "infinity". There are several constructions, each built for a job, each with its own rules:

| Infinity | What it is | Rules |
|---|---|---|
| No upper bound | potential infinity, as in $n \to \infty$ in a limit | not an object at all, only a way of speaking |
| Point at infinity | one extra point added to the complex plane (the Riemann sphere) | $1/0 = \infty$; poles of transfer functions can sit "at infinity" |
| IEEE `inf` | a value in floating-point arithmetic | in NumPy, `np.float64(1.0) / 0.0` is `inf`; `inf - inf` is `nan` |
| Cardinals (Cantor) | sizes of sets, compared by one-to-one matching | $\aleph_0 + 1 = \aleph_0$; there are more reals than naturals |
| Ordinals (Cantor) | positions after "counting forever": $\omega, \omega + 1, \ldots$ | $1 + \omega = \omega$ but $\omega + 1 \ne \omega$, so addition isn't commutative |
| Infinitesimals | infinitely small numbers (Robinson's nonstandard analysis, 1960s) | Leibniz's calculus made rigorous, 300 years later |

Each one is introduced the same way zero and Hamilton's pairs were: decide what you want the new object to do, build it, and then find out what laws it obeys. Dantzig takes up the infinite again in Chapters 9–11.

## 11. How well does the chapter hold up?

The chapter appeared in 1930, with the final revision in 1954. The core argument holds up well, and later developments mostly sharpened it.

**The logicists conceded Dantzig's point.** Gottlob Frege and Bertrand Russell tried to show that arithmetic is pure logic, against Poincaré. They *defined* the natural numbers as everything you can reach from 1 by repeatedly taking successors, so that induction holds by definition. But to guarantee that there are infinitely many numbers, Russell and Whitehead had to add an **Axiom of Infinity** to *Principia Mathematica* (1910–13). They admitted that it isn't a truth of logic. That is exactly Dantzig's conclusion: logic gives you the restricted principle, and infinity has to be assumed.

**"All" turned out to be even more slippery.** In 1931 Kurt Gödel showed that any consistent set of axioms for arithmetic that a computer could check leaves some true statements about whole numbers unprovable. In 1934 Thoralf Skolem showed that the usual first-order version of the induction axiom can't even pin down which collection it is talking about: there are "nonstandard" number systems containing infinitely large elements that satisfy all the same first-order axioms. Induction captures "all whole numbers" only in a stronger (second-order) logic, which has its own problems. Dantzig's dragon at the gate of mathematics is still there.

**Some details have dated or need correcting:**

- His physics is from the 1920s. Current cosmology finds the *observable* universe finite, but the universe as a whole may well be infinite.
- The Archimedes figures need the corrections in Section 2.
- His terms for the two steps of induction are the reverse of modern usage (Section 4).
- His framing of Fermat's Last Theorem as an induction on $n$ is misleading (Section 4).

**Further reading:** Poincaré, *Science and Hypothesis*, chapter 1, the essay Dantzig quotes, short and readable. Archimedes, *The Sand Reckoner*, in T. L. Heath's translation (*The Works of Archimedes*, 1897, freely available online). John Stillwell, *Roads to Infinity* (2010), on where infinity leads next, including Gödel. David Goldberg, "What Every Computer Scientist Should Know About Floating-Point Arithmetic" (1991), for the bounded arithmetic of real machines.
