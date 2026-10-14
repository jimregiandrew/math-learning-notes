# Number lore: from number mysticism to number theory

Perfect numbers, amicable numbers and triangular numbers sound like puzzle-book material. Yet they are among the oldest questions in mathematics, and some of them are still unsolved after 2,500 years. They were first asked by people who believed numbers had **moral and cosmic meaning**: odd numbers were male, even numbers female, 6 was perfect and 220 and 284 were friends.

This note follows Chapter 3 of Tobias Dantzig's *Number: The Language of Science*, "Number Lore". The chapter's thread is that **number theory grew out of number mysticism**. The mysticism was wrong, but it asked good questions and kept people interested in them for centuries. The answers turned out to be real mathematics, and some of it now runs the internet's security.

The note covers the main pieces of number lore in turn: figurate numbers, letters as numbers, perfect numbers, amicable numbers and primes. For each it gives the history, the precise statement and, where it's short, the proof. It ends with what Dantzig's account gets right and what has changed since 1930.

**Prerequisites:** arithmetic, and modular arithmetic ("$a \equiv b \pmod m$" means $m$ divides $a - b$) for Section 7. The previous chapter's note, [Positional notation and zero](../numeration/positional-notation-and-zero.md), gives the background and discusses Dantzig's claim that "the theory of numbers preceded arithmetic".

---

## 1. The puzzle

Why would serious mathematics come out of numerology?

Part of the answer is that the Pythagoreans (Pythagoras lived c. 570–495 BCE, in southern Italy) had real evidence. They found that pleasing musical intervals come from simple whole-number ratios of string lengths. Halve a string and you get the octave (2:1). Two thirds gives the fifth (3:2), three quarters the fourth (4:3). Sound, which seems to have nothing to do with counting, was ruled by small whole numbers. It wasn't a crazy jump to guess that **everything** was: "all is number".

From there the Pythagoreans gave numbers characters:

- **1** was the source of number, not a number itself. The Greeks generally counted from 2.
- **Odd numbers** were male and **even numbers** female, so 5 = 2 + 3 was "marriage".
- **10** was sacred, because $10 = 1 + 2 + 3 + 4$, the *tetractys*, a triangle of ten dots.

A caution about sources: Pythagoras wrote nothing, and most of what we "know" comes from writers six to eight centuries later, who turned him into a legend. Historians now treat specific attributions to Pythagoras himself as doubtful. "The Pythagoreans" is a safer label.

Mystical or not, these people were looking hard at particular numbers and asking what properties they had. That is exactly what number theory does.

## 2. Figurate numbers: proofs with pebbles

If you count with pebbles (see the [counting board](../numeration/positional-notation-and-zero.md#1-the-puzzle)), numbers have **shapes**. Some numbers of pebbles make a triangle, some a square:

```
triangular: 1, 3, 6, 10, ...          square: 1, 4, 9, 16, ...

  o          o           o            o     o o    o o o
            o o         o o                 o o    o o o
                       o o o                       o o o
```

The $n$-th triangular number is $T_n = 1 + 2 + \cdots + n$, and the $n$-th square is $n^2$.

Arranging pebbles gives theorems almost for free. To grow an $n \times n$ square into an $(n+1) \times (n+1)$ square, you add an L-shaped border of $2n + 1$ pebbles. The Greeks called the L-shape a **gnomon**, after the carpenter's square:

```
  o o o | x
  o o o | x        3 x 3 square plus a gnomon of 2*3 + 1 = 7
  o o o | x        gives a 4 x 4 square
  - - - +
  x x x   x
```

Starting from one pebble and adding gnomons of 3, 5, 7, ... gives:

**Theorem.** The sum of the first $n$ odd numbers is a square: $1 + 3 + 5 + \cdots + (2n - 1) = n^2$.

Two more come from cutting and joining shapes:

- **Two consecutive triangles make a square:** $T_{n-1} + T_n = n^2$. Cut a square along a diagonal just above the main diagonal.
- **Two copies of a triangle make a rectangle:** $2T_n = n(n+1)$, so $T_n = n(n+1)/2$. Put one triangle upside down against the other.

**How rigorous is this?** Each picture is a complete proof for the size drawn, and the pattern for growing it to the next size is clear. Written out, each one is a proof by induction. For example, if $1 + 3 + \cdots + (2n-1) = n^2$, then adding $2n + 1$ gives $n^2 + 2n + 1 = (n+1)^2$, which is the gnomon in algebra. So the pebble proofs are real proofs once you notice they are inductions. What the Greeks lacked was not rigor but notation: there was no way to write "$n$" for a general number of pebbles, so the argument lived in the picture.

## 3. Letters as numbers

Greek and Hebrew wrote numbers with letters of the alphabet: alpha = 1, beta = 2, ..., iota = 10, kappa = 20, and so on. This is an *additive* system like Roman numerals, with no place value (see the [table in the previous note](../numeration/positional-notation-and-zero.md#3-how-it-actually-happened)).

A side effect is that **every word is also a number**: add up the values of its letters. The Greeks called this *isopsephy*, and Hebrew tradition calls it *gematria*. Two words with the same total were thought to be linked. The best-known example is the "number of the beast", 666, in the Book of Revelation (13:18). A common scholarly reading is that it encodes the emperor Nero: "Nero Caesar" written in Hebrew letters adds up to $50 + 200 + 6 + 50 + 100 + 60 + 200 = 666$.

There is no mathematics in this, but it shows how the *notation* shapes the lore. Once Indian place-value numerals replaced alphabetic ones, words and numbers came apart and this game lost its hold.

## 4. Perfect numbers

### What they are

The **proper divisors** of $n$ are its divisors other than $n$ itself. A number is **perfect** if it equals the sum of its proper divisors:

$$6 = 1 + 2 + 3, \qquad 28 = 1 + 2 + 4 + 7 + 14.$$

Most numbers aren't perfect. For 12 the sum is $1 + 2 + 3 + 4 + 6 = 16$, too much ("abundant"); for 8 it is $1 + 2 + 4 = 7$, too little ("deficient"). The Greeks knew four perfect numbers: 6, 28, 496 and 8128. The fifth, 33,550,336, wasn't recorded until the 15th century.

The meanings attached to them lasted a long time. St Augustine (c. 400 CE) wrote that God created the world in six days *because* 6 is perfect, and that "six is a number perfect in itself, and not because God created all things in six days; rather the converse is true." The number's property came first, and creation followed it.

### The theorem

It's convenient to include $n$ itself. Write $\sigma(n)$ for the sum of **all** the divisors of $n$. Then $n$ is perfect exactly when $\sigma(n) = 2n$.

**Theorem (Euclid, *Elements* IX.36, c. 300 BCE; converse by Euler, 18th century).** An even number is perfect if and only if it has the form

$$n = 2^{p-1}(2^p - 1) \qquad \text{where } 2^p - 1 \text{ is prime.}$$

For $p = 2, 3, 5, 7$ this gives $2^p - 1 = 3, 7, 31, 127$, all prime, and $n = 6, 28, 496, 8128$.

**Proof of Euclid's half (complete).** Let $q = 2^p - 1$ be prime and $n = 2^{p-1} q$. The divisors of $n$ are $2^i$ and $2^i q$ for $i = 0, 1, \ldots, p-1$. So

$$\sigma(n) = (1 + 2 + \cdots + 2^{p-1})(1 + q) = (2^p - 1) \cdot 2^p = 2n. \qquad \blacksquare$$

**Proof of Euler's half (complete, given one fact).** The fact: $\sigma$ is *multiplicative*, meaning $\sigma(ab) = \sigma(a)\sigma(b)$ when $a$ and $b$ have no common factor. (This holds because each divisor of $ab$ splits uniquely into a divisor of $a$ times a divisor of $b$.)

Let $n$ be even and perfect, and write $n = 2^k m$ with $m$ odd and $k \ge 1$. Then

$$\sigma(n) = \sigma(2^k)\,\sigma(m) = (2^{k+1} - 1)\,\sigma(m), \quad \text{and this must equal } 2n = 2^{k+1} m.$$

Since $2^{k+1} - 1$ is odd, it must divide $m$. Write $m = (2^{k+1} - 1)c$. Substituting gives $\sigma(m) = 2^{k+1} c = m + c$. But $m$ and $c$ are both divisors of $m$, and if $c > 1$ then 1 is a third one, so $\sigma(m) > m + c$. Hence $c = 1$, the only divisors of $m$ are $1$ and $m$, and $m = 2^{k+1} - 1$ is prime. Set $p = k + 1$. $\blacksquare$

### Mersenne primes

So even perfect numbers correspond one-to-one with primes of the form $2^p - 1$. These are **Mersenne primes**, after the French friar Marin Mersenne, who published a list of them in 1644.

Two easy facts:

- **$p$ itself must be prime.** If $p = ab$, then with $x = 2^a$, $2^p - 1 = x^b - 1 = (x - 1)(x^{b-1} + \cdots + x + 1)$, and $x - 1 = 2^a - 1$ is a factor.
- **$p$ prime is not enough.** $2^{11} - 1 = 2047 = 23 \times 89$.

### What's still open

- **Are there infinitely many** Mersenne primes, and so infinitely many even perfect numbers? Nobody knows.
- **Is there an odd perfect number?** Nobody knows. None exists below $10^{1500}$, and any that exists must satisfy a long list of conditions. This may be the oldest open problem in mathematics.

A question first asked out of number mysticism, in a book from 300 BCE, is still unanswered.

## 5. Amicable numbers

Two numbers are **amicable** ("friendly") if each is the sum of the other's proper divisors. The smallest pair is 220 and 284:

- Proper divisors of 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110. Their sum is 284.
- Proper divisors of 284: 1, 2, 4, 71, 142. Their sum is 220.

Iamblichus (c. 300 CE) says Pythagoras, asked what a friend is, answered "another I, like 220 and 284". Amicable numbers were used in medieval love charms for the same reason.

The history of finding more pairs is a good lesson in what rules can and can't do:

| Date | Who | Pair | How |
|---|---|---|---|
| Antiquity | Pythagoreans | 220, 284 | known |
| 9th century | Thābit ibn Qurra | (a rule) | proves a formula that generates pairs |
| c. 1300 / 1636 | Ibn al-Bannā' or al-Fārisī; rediscovered by Fermat | 17296, 18416 | Thābit's rule |
| 1638 | Descartes | 9363584, 9437056 | Thābit's rule |
| 1747–50 | Euler | about 60 new pairs | new methods |
| 1866 | Nicolò Paganini, aged 16 | **1184, 1210** | by hand |

**Thābit's rule.** If $p = 3 \cdot 2^{n-1} - 1$, $q = 3 \cdot 2^n - 1$ and $r = 9 \cdot 2^{2n-1} - 1$ are all prime, then $2^n p q$ and $2^n r$ are amicable. With $n = 2$: $p = 5$, $q = 11$, $r = 71$, giving 220 and 284. With $n = 4$ and $n = 7$ you get Fermat's and Descartes' pairs.

The last row is the punchline. After two thousand years of interest, and after Euler, a teenager found that the **second-smallest** pair had been missed. Everyone after Thābit had been using rules, and 1184 and 1210 aren't produced by the rules they used. A computer search finds it at once:

```python
def s(n):
    """Sum of the proper divisors of n."""
    total = 1 if n > 1 else 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            if d != n // d:
                total += n // d
        d += 1
    return total

print([n for n in range(2, 10_000) if s(n) == n])
# [6, 28, 496, 8128]
print([(m, s(m)) for m in range(2, 20_000) if m < s(m) and s(s(m)) == m])
# [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368),
#  (10744, 10856), (12285, 14595), (17296, 18416)]
```

Note (12285, 14595): an **odd** amicable pair. Whether there is a pair with one odd and one even member is, again, unknown.

## 6. Primes

### Infinitely many

Every whole number above 1 is a product of primes, in only one way up to order. (This is the Fundamental Theorem of Arithmetic. Euclid had the key step, and Gauss gave the first full proof in 1801.) So primes are the atoms of multiplication. The first question about them is whether they run out.

**Theorem (Euclid, *Elements* IX.20).** There are infinitely many primes.

**Proof (complete).** Take any finite list of primes $p_1, \ldots, p_k$, and let $N = p_1 p_2 \cdots p_k + 1$. Dividing $N$ by any $p_i$ leaves remainder 1, so no $p_i$ divides $N$. But $N > 1$ has at least one prime factor, so that factor is a prime not on the list. No finite list contains every prime. $\blacksquare$

The proof doesn't say $N$ is prime, only that it has a new prime factor. For example $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$.

### When patterns lie: Fermat's numbers

Pierre de Fermat (1601–1665), a lawyer in Toulouse, did mathematics in letters to friends. He is the person who turned number lore into modern number theory: he stopped asking what numbers *meant* and started asking what could be *proved* about them. He was also wrong at least once, instructively.

The **Fermat numbers** are $F_n = 2^{2^n} + 1$:

$$F_0 = 3, \quad F_1 = 5, \quad F_2 = 17, \quad F_3 = 257, \quad F_4 = 65537.$$

All five are prime. In 1640 Fermat said he believed all $F_n$ were prime, though he admitted he had no proof. In 1732 Euler showed

$$F_5 = 2^{32} + 1 = 4294967297 = 641 \times 6700417.$$

Since then, every Fermat number that has been checked has turned out to be composite. Five examples were a misleading sample.

Another famous example, from Euler: $n^2 + n + 41$ is prime for $n = 0, 1, \ldots, 39$, forty times in a row. At $n = 40$ it gives $40^2 + 40 + 41 = 41^2$.

These examples are the main reason number theorists insist on proof. In physics, forty confirmations would be strong evidence. In number theory they can mean nothing, because the first counterexample can be very large. Dantzig's point is that number theory is unusual here: it is the most *experimental* branch of mathematics, since anyone can compute examples and spot patterns, and it is also the one where patterns most often lie.

### Fermat's "last theorem"

Around 1637, in the margin of his copy of Diophantus, Fermat wrote that $x^n + y^n = z^n$ has no solutions in positive whole numbers when $n \ge 3$, and that he had a "truly marvellous proof" too large for the margin. For $n = 2$ there are infinitely many solutions (Pythagorean triples like $3^2 + 4^2 = 5^2$), so the claim is that squares are special.

When Dantzig wrote, this was open, and a 100,000-mark prize (the Wolfskehl Prize, 1908) waited for a proof. Andrew Wiles proved it in 1994, with a gap repaired together with Richard Taylor, using some of the deepest mathematics of the 20th century. Almost nobody believes Fermat really had a proof.

## 7. The payoff: from useless to essential

In 1940 G. H. Hardy, in *A Mathematician's Apology*, praised number theory for being useless: no one had found a warlike purpose for it, and he expected no one would. Within forty years that had reversed.

**Fermat's little theorem** (1640, the one he got right): if $p$ is prime and $a$ is any whole number, then $a^p \equiv a \pmod p$.

**RSA encryption** (Rivest, Shamir and Adleman, 1977; found earlier in secret by Clifford Cocks at GCHQ) is built on a generalization of it due to Euler. Multiplying two large primes is easy, and factoring the product appears to be very hard. Every HTTPS connection you make depends on that gap, and on fast tests that a 300-digit number is prime. Those tests are refinements of Fermat's little theorem.

The old lore keeps turning up in this machinery:

- **$F_4 = 65537$**, the largest known Fermat prime, is the standard RSA public exponent. In binary it is $10000000000000001$, so raising to that power takes only 17 multiplications.
- **The Mersenne Twister**, the random number generator behind Python's `random` module and NumPy's older `RandomState`, has period $2^{19937} - 1$, a Mersenne prime. Its design uses the fact that this number is prime.
- **The search for Mersenne primes** is a long-running test of computer hardware. The Great Internet Mersenne Prime Search (GIMPS, since 1996) uses the Lucas–Lehmer test, which works only for numbers of the form $2^p - 1$. As of late 2024 the largest known prime was $2^{136279841} - 1$, which has about 41 million digits. It gives the 52nd known perfect number.

And one result from pure geometry: Gauss proved at 19 (1796) that a regular polygon with $n$ sides can be constructed with ruler and compass exactly when $n$ is a power of 2 times a product of **distinct Fermat primes**. So the 17-gon can be constructed and the 7-gon can't. Fermat's numbers, which Fermat studied as a curiosity, turned out to answer a problem the Greeks had left open.

## 8. Invention or discovery?

The chapter separates these cleanly.

- **The meanings are inventions.** That 6 is perfect in a moral sense, that odd numbers are male, that 220 and 284 are friends: these are stories people told. Nothing in mathematics supports or refutes them.
- **The definitions are choices.** Why care about the sum of proper divisors instead of some other function of a number? There's no deep reason; the mystics happened to care about it.
- **The facts are discoveries.** Once you define perfect numbers, it is not up to you that every even one has Euclid's form, or that whether an odd one exists is very hard to decide. Euler didn't decide that 641 divides $F_5$. He found it.

This is the same pattern as zero in the [previous note](../numeration/positional-notation-and-zero.md#6-invention-or-discovery): the concept is introduced for human reasons, and then it has properties of its own that nobody chose.

## 9. How well does the chapter hold up?

*Number* was first published in 1930, with a last revised edition in 1954. The main thread, that number theory grew out of number lore, is still the standard account. Some details have changed:

- **Fermat's Last Theorem** is now proven (Wiles, 1994).
- **Computers changed the subject.** In 1930 finding a new perfect number was a heroic hand calculation. Since 1952, every new Mersenne prime has been found by computer, and searches like the one in Section 5 take seconds. "Experimental mathematics" is now a field with its own journals.
- **Number theory is now applied.** In 1930 it was the purest of pure mathematics. Since 1977 it has been the mathematical foundation of public-key cryptography.
- **The Pythagoreans are murkier.** Later scholarship, especially Walter Burkert's, argues that much of what was attributed to Pythagoras, perhaps including the mathematics, was added by later admirers. The ideas are ancient, but who had them first is uncertain.

What hasn't changed is the open problems. Odd perfect numbers, infinitely many Mersenne primes, and whether there are more Fermat primes are all exactly as open as they were for Dantzig. The lesson he drew from this, that number theory questions are easy to state and very hard to answer, still holds.

**Further reading:** Øystein Ore, *Number Theory and Its History* (1948, Dover reprint), the natural next book: real number theory taught through its history. André Weil, *Number Theory: An Approach Through History from Hammurapi to Legendre* (1984), at a higher level. Walter Burkert, *Lore and Science in Ancient Pythagoreanism* (1972), for what we actually know about the Pythagoreans.
