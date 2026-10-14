# Positional notation and zero: the concrete before the abstract

We write numbers with ten digits whose meaning depends on where they sit. In 203 the 2 means two hundreds, and the 0 says "no tens here". This feels too obvious to have a history. Yet most civilizations that had serious arithmetic, including Egypt, Greece and Rome, never wrote numbers this way. The full system, with a true zero, appears to have come together only once, in India around the 6th–7th century CE.

This note covers why it took so long, using a line from Tobias Dantzig's *Number: The Language of Science* (Chapter 2, "The Empty Column"): **"The concrete has ever preceded the abstract."** Then it states the theorem that makes place value work and what it pays off in computing. Finally it asks how well Dantzig's principle holds up, and where he went further than the evidence.

**Prerequisites:** none beyond arithmetic. The last section links to the [complex numbers notes](../complex-numbers/representations.md).

---

## 1. The puzzle

Roman numerals are *additive*: MMXXVI means $1000 + 1000 + 10 + 10 + 5 + 1$. The meaning of a symbol doesn't depend on where it sits (apart from the small subtraction rule, as in IV). Written calculation in such a system is miserable. Try multiplying CCCXLVII by XXIX on paper.

The Romans didn't try. They **calculated on a counting board** (an abacus) and used numerals only to **record** results. Our word *calculate* comes from Latin *calculus*, a small pebble, the counter moved on the board.

The counting board is already positional. Each column stands for a power of ten, and the number of pebbles in a column is the digit. A column with no pebbles is zero, in physical form. So the Romans did place-value arithmetic every day, with their hands. What they never did was write it down.

## 2. Dantzig's point: the concrete came first, and got in the way

Dantzig's reading of this history has two halves.

1. **The concrete came first.** Counting on fingers, with pebbles and on boards is far older than any abstract idea of number. Place value existed as a *physical device* (columns on a board) long before it existed as *notation*. The empty column existed long before the symbol 0.
2. **The concrete also held things back.** The board worked well enough that there was little pressure to replace it. The leap to notation needed a symbol for *nothing*: something that isn't a quantity of anything, yet has to be written down and calculated with. That is a much more abstract step than moving pebbles, and it took more than a thousand years.

So the device both contained the idea and hid it. Dantzig suggests that the inventor of zero was probably an anonymous calculator who wanted to record the state of the board on paper, with a mark for the empty column.

## 3. How it actually happened

Place value and zero arrived separately, and several cultures got part of the way.

| Culture | Base | Place value? | Zero? |
|---|---|---|---|
| Babylon (from c. 1800 BCE) | 60 | yes | no zero at first, so the meaning had to come from context. A placeholder sign appears by c. 300 BCE, used between digits but not at the end |
| Egypt, Greece, Rome | 10 | no (additive) | no |
| China (counting rods) | 10 | yes, on the counting board | a blank space at first. A round written zero appears in the 13th century |
| Maya (early centuries CE) | 20 (modified) | yes | yes, a shell glyph, used in calendar counts |
| India (by c. 600 CE) | 10 | yes | yes, as a placeholder **and** as a number |

The Babylonian case shows why the zero matters. Without it, the sexagesimal digits "3 23" could mean $3 \cdot 60 + 23 = 203$, or $3 \cdot 60^2 + 23$, or $3 \cdot 60^2 + 0 \cdot 60 + 23$. A scribe had to work it out from context. Our "23" versus "203" versus "230" has the same problem if you leave out the 0.

**India took the final step.** By around 600 CE Indian mathematicians wrote numbers with nine digits plus a zero, in base ten with place value. The decisive move came in Brahmagupta's *Brāhmasphuṭasiddhānta* (628 CE). It gives rules for calculating *with* zero as a number: $a + 0 = a$, $a - a = 0$, $a \cdot 0 = 0$. Negative numbers ("debts") get rules too. Zero was no longer just a mark for an empty column. It was a number you could operate on. Brahmagupta also tried to define division by zero, and got it wrong ($0/0 = 0$), which is a sign of how new the idea was.

**The spread west** took centuries, and it was resisted:

- **c. 825:** al-Khwārizmī in Baghdad writes a book on Indian reckoning. Its Latin translation begins *"Algoritmi dicit…"* ("al-Khwārizmī says…"). That is where the word **algorithm** comes from.
- **The word "zero":** Sanskrit *śūnya* ("empty") was translated into Arabic as *ṣifr*, which became Latin *zephirum* and then Italian *zero*. The same Arabic word gave English **cipher**.
- **1202:** Fibonacci's *Liber Abaci* introduces the system to European merchants.
- **1299:** a statute of Florence's bankers' guild bans the new numerals in account books. One reason was that a 0 is easily changed into a 6 or 9, while Roman numerals are harder to forge.
- **15th–16th centuries:** "abacists" (board calculators) and "algorists" (pen-and-paper calculators) compete. The algorists win once paper becomes cheap, because written calculation leaves a record that can be checked.

## 4. The theorem behind place value

Here is the precise statement that makes positional notation work.

**Theorem (base-$b$ representation).** Fix an integer base $b \ge 2$. Every integer $n \ge 1$ can be written in exactly one way as

$$n = d_k b^k + d_{k-1} b^{k-1} + \cdots + d_1 b + d_0, \qquad 0 \le d_i < b, \quad d_k \ne 0.$$

The digit string $d_k d_{k-1} \ldots d_0$ is the base-$b$ numeral for $n$.

**Proof (complete).** *Existence:* by the division algorithm, $n = q b + d_0$ with $0 \le d_0 < b$ and $q < n$. If $q = 0$ we're done. Otherwise apply the same step to $q$ (by induction, $q$ has a representation), then multiply by $b$ and add $d_0$. *Uniqueness:* any representation gives $n \equiv d_0 \pmod b$ with $0 \le d_0 < b$. So $d_0$ is forced to be the remainder of $n$ divided by $b$. Subtract it, divide by $b$, and repeat. Every digit is forced. $\blacksquare$

Two things to notice:

- **Zero is built into the statement.** The digits run over $0, 1, \ldots, b-1$. Without a digit for 0, a number like $2 \cdot 10^2 + 0 \cdot 10 + 3$ has no numeral, and uniqueness fails in practice, as the Babylonians found.
- **The proof is the algorithm.** Repeated division with remainder gives the digits. In Python:

```python
def digits(n, b):
    """Digits of n in base b, most significant first (n >= 0)."""
    if n == 0:
        return [0]
    ds = []
    while n > 0:
        n, d = divmod(n, b)
        ds.append(d)
    return ds[::-1]

def value(ds, b):
    """Evaluate a digit string with Horner's rule: ((d0*b + d1)*b + d2)..."""
    n = 0
    for d in ds:
        n = n * b + d
    return n

print(digits(203, 10), digits(203, 2), digits(203, 60))
# [2, 0, 3] [1, 1, 0, 0, 1, 0, 1, 1] [3, 23]
print(value([3, 23], 60))
# 203
```

The last line is the Babylonian scribe's problem. The digit list `[3, 23]` is the base-60 numeral for 203. Without a zero, `[3, 0, 23]` would be written the same way.

## 5. The payoff

**A numeral is a polynomial evaluated at the base.** The numeral 203 is $p(x) = 2x^2 + 0x + 3$ evaluated at $x = 10$. That is why the school algorithms work. Adding and multiplying numerals is adding and multiplying polynomials, followed by **carrying**: whenever a coefficient reaches $b$, trade it for 1 in the next position up. Carrying is exactly what an abacus user does by hand when a column fills up. The same idea of "polynomials, then reduce" defines the complex numbers in [representations.md, Section 6](../complex-numbers/representations.md).

**Computers are electronic counting boards.** Binary is base-2 place value. Each bit is a column that is either empty or holds one pebble. Floating point is positional notation plus an exponent that says where the point goes, just like scientific notation $6.02 \times 10^{23}$. Horner's rule (the `value` function above) is still the standard way to evaluate polynomials numerically, because it uses the fewest multiplications.

**Notation is a tool for thinking.** Positional notation turned arithmetic from a skill done with a device into a procedure written on paper, one that anyone can learn and check. Al-Khwārizmī's name became the word *algorithm* for good reason.

## 6. Invention or discovery?

Both, at different levels.

- **The notation is an invention.** The choice of base is arbitrary: 10 for our fingers, 60 for Babylon, 20 for the Maya, 2 for electronics. The shapes of the digits are a cultural accident.
- **The theorem is a discovery.** That every integer has exactly one base-$b$ representation is true whatever symbols you use, and the counting board was obeying it long before anyone proved it.
- **Zero is somewhere in between.** As a placeholder it is a piece of notation. As a *number* with its own arithmetic (Brahmagupta's rules) it is a new mathematical object. Once you have it, its properties aren't up to you: $a \cdot 0 = 0$ follows from the distributive law whether you like it or not.

This is the same pattern as complex numbers, as told in [What complex numbers led to](../complex-numbers/legacy.md). People used them in practice for centuries before anyone could say what they *were*, and the concrete meaning came later. Dantzig's principle runs through the whole history of number.

## 7. How well does Dantzig's principle hold up?

### Where it holds: practice usually comes first

As a general pattern, "concrete before abstract" is well supported. Historians of mathematics broadly agree that practical needs came first: trade, taxes, land measurement, calendars and astronomy. Theory grew out of the techniques those needs produced. The examples in this note and its neighbours all fit:

| Concrete practice | Later abstraction |
|---|---|
| the empty column on a counting board | the symbol 0, then zero as a number (Brahmagupta, 628) |
| arranging pebbles into triangles and squares | early Greek theory of odd, even and figurate numbers |
| calculating with $\sqrt{-1}$ to solve cubics (Cardano, Bombelli, 16th century) | complex numbers as points or pairs (Wessel, Argand, Hamilton, 1797–1837) |
| steam engines (Newcomen 1712, Watt 1770s) | thermodynamics (Carnot 1824, then entropy) |
| telegraph and telephone engineering | information theory (Shannon 1948) |

The pattern is common, not universal. Sometimes theory comes first: Maxwell's equations predicted radio waves before Hertz produced them, and Turing's abstract machine (1936) came before working computers. So "usually" is accurate. Dantzig's "ever" (in the older sense of "always") isn't.

### Where Dantzig went too far

Dantzig draws a specific historical conclusion from the principle: "That is why the theory of numbers preceded arithmetic."

His terms are older than ours. By the **theory of numbers** he means the properties of particular numbers: whether a number is prime, perfect ($6 = 1 + 2 + 3$) or triangular. By **arithmetic** he means the art of reckoning, the general methods for calculating with any numbers. The Greeks drew the same line, between *arithmētikē* (the study of numbers themselves) and *logistikē* (practical calculation). His argument is that a particular number, like six pebbles, is concrete, while a general method of calculation is abstract, so the first must have come first.

**As a claim about history, this is wrong.** Calculation came first, by more than a thousand years:

- **Babylon, c. 1800 BCE**, had a highly developed computing culture: sexagesimal place value, tables of multiplication and reciprocals, and division done by multiplying by a reciprocal. The tablet YBC 7289 gives $\sqrt{2}$ as 1;24,51,10 in base 60, about 1.414213, which is accurate to roughly six decimal places.
- **Egypt, c. 1650 BCE:** the Rhind papyrus is essentially a textbook of worked calculations.
- **Greek number theory** came much later: the Pythagoreans around 500 BCE, Euclid's *Elements* around 300 BCE. Even in Greece, practical reckoning on the abacus went on before and alongside it.

**A narrower version is right.** *Written, general* algorithms of the kind taught in school today needed place value with a zero. They came from India around 600 CE and reached Europe after 1200, long after Euclid had proved that there are infinitely many primes. And the earliest Greek number theory really was concrete "pebble arithmetic". So the theory of numbers did come before *paper* arithmetic, but not before calculation.

### Why he went too far

Three reasons, from most to least forgivable:

1. **Incomplete evidence.** *Number* was first published in 1930. Most of the Babylonian mathematical tablets were deciphered after that, mainly by Otto Neugebauer and his colleagues in the 1930s and 1940s. In 1930 the depth of Mesopotamian computation simply wasn't widely known.
2. **A Greek-centred view.** Like most writers of his time, Dantzig treated mathematics as beginning with the Greeks. From that starting point, Greek number theory does come before the Indian numerals that made written calculation easy. The earlier calculating cultures of Babylon and Egypt drop out of the picture.
3. **Overextending a good principle.** Once you have a striking pattern, it's tempting to read every episode as an instance of it. Dantzig used "concrete before abstract" to *derive* a historical order instead of checking it against the record.

None of this undermines the book's main insight. The principle is a good guide to how ideas usually develop. It is a heuristic, though, not a law, and a historical claim based on it still has to be checked against the evidence.

**Further reading:** Eleanor Robson, *Mathematics in Ancient Iraq: A Social History* (2008), for Babylonian computation as historians now understand it. Otto Neugebauer, *The Exact Sciences in Antiquity* (1952), for the decipherments that changed the picture.
