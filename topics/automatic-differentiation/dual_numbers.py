"""Dual numbers a + b*eps with eps^2 = 0, and forward-mode automatic differentiation.

Companion to dual-numbers.md. Run with: uv run python topics/automatic-differentiation/dual_numbers.py
"""
import math

import numpy as np


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
        # (a + b eps)(c + d eps) = ac + (ad + bc) eps + bd eps^2, and eps^2 = 0
        return Dual(self.a * other.a, self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __repr__(self):
        return f"{self.a} + {self.b}ε"


def sin(x):
    return Dual(math.sin(x.a), math.cos(x.a) * x.b) if isinstance(x, Dual) else math.sin(x)


def exp(x):
    return Dual(math.exp(x.a), math.exp(x.a) * x.b) if isinstance(x, Dual) else math.exp(x)


def derivative(f, x):
    """f'(x), exactly (up to rounding), by evaluating f at x + 1*eps."""
    return f(Dual(x, 1.0)).b


# 1. eps^2 = 0, and the derivative of x^2 at 3 appears as the eps part.
eps = Dual(0.0, 1.0)
print("1. eps*eps =", eps * eps, "  (3 + eps)^2 =", (3 + eps) * (3 + eps))


# 2. A function written as ordinary code, differentiated without touching its source.
def f(x):
    return x * sin(x * x) + exp(x)


def f_prime_by_hand(x):
    return math.sin(x * x) + 2 * x * x * math.cos(x * x) + math.exp(x)


x0 = 1.3
print(f"2. dual numbers: {derivative(f, x0):.15f}")
print(f"   by hand:      {f_prime_by_hand(x0):.15f}")

# 3. Finite differences: error first falls (truncation) then rises (rounding).
print("3. forward difference (f(x+h) - f(x)) / h, error vs h:")
exact = f_prime_by_hand(x0)
for h in [1e-2, 1e-5, 1e-8, 1e-11, 1e-14]:
    approx = (f(x0 + h) - f(x0)) / h
    print(f"   h = {h:.0e}   error = {abs(approx - exact):.1e}")

# 4. Complex-step derivative: i*h with tiny h behaves almost like eps, since (ih)^2 = -h^2.
def f_numpy(x):
    return x * np.sin(x * x) + np.exp(x)   # same f, written with NumPy so it accepts complex input


h = 1e-20
complex_step = f_numpy(x0 + 1j * h).imag / h
print(f"4. complex step, h = 1e-20: error = {abs(complex_step - exact):.1e}")

# 5. Dual numbers as 2x2 matrices: a*I + b*N with N = [[0, 1], [0, 0]], N^2 = 0.
N = np.array([[0.0, 1.0], [0.0, 0.0]])
print("5. N @ N =\n", N @ N)
A = 3 * np.eye(2) + 1 * N
print("   (3 + eps)^2 as a matrix =\n", A @ A)


# 6. AD differentiates the program, not the function. This g is the identity
#    function, but the branch at 0 hides that from the dual number.
def g(x):
    a = x.a if isinstance(x, Dual) else x
    return 0.0 if a == 0 else x


result = g(Dual(0.0, 1.0))
slope = result.b if isinstance(result, Dual) else 0.0   # a plain constant has derivative 0
print("6. g(x) = x, true g'(0) = 1, dual-number answer:", slope)
