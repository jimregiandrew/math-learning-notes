"""Check that the representations of the complex numbers agree.

Companion to representations.md. Each section multiplies the same two
numbers z = 1 + 2i and w = 3 - i in a different representation.
By hand: (1 + 2i)(3 - i) = 3 - i + 6i - 2i^2 = 5 + 5i.
"""
import numpy as np
from numpy.polynomial import polynomial as P
from scipy.linalg import expm

a, b = 1.0, 2.0    # z = a + bi
c, d = 3.0, -1.0   # w = c + di
z, w = complex(a, b), complex(c, d)

# 1. Formal symbol a + bi: Python's built-in complex type.
print(f"1. a + bi        : z*w = {z * w}")

# 3. Polar form: multiply the lengths, add the angles.
r = abs(z) * abs(w)
theta = np.angle(z) + np.angle(w)
print(f"3. polar         : r = {r:.4f}, theta = {theta:.4f} rad"
      f"  ->  {r * np.cos(theta):.4f}{r * np.sin(theta):+.4f}i")


# 4. Ordered pairs (Hamilton): only real arithmetic, no i anywhere.
def pair_mul(p, q):
    (a, b), (c, d) = p, q
    return (a * c - b * d, a * d + b * c)


print(f"4. ordered pairs : {pair_mul((a, b), (c, d))}")


# 5. 2x2 real matrices: M(z) is the matrix of "multiply by z" on R^2.
def M(z):
    return np.array([[z.real, -z.imag],
                     [z.imag, z.real]])


print(f"5. matrices      : M(z) M(w) =\n{M(z) @ M(w)}")
assert np.allclose(M(z) @ M(w), M(z * w))             # respects *
assert np.allclose(M(z) + M(w), M(z + w))             # respects +
assert np.isclose(np.linalg.det(M(z)), abs(z) ** 2)   # det = |z|^2

# Euler's identity in matrix form: e^{pi J} = -I (half a turn).
J = M(1j)
print(f"   e^(pi J) =\n{expm(np.pi * J).round(12) + 0.0}")

# 6. Polynomials a + bx modulo x^2 + 1 (coefficients listed low to high).
product = P.polymul([a, b], [c, d])              # 3 + 5x - 2x^2
_, remainder = P.polydiv(product, [1, 0, 1])     # divide by 1 + x^2
print(f"6. R[x]/(x^2+1)  : (a+bx)(c+dx) = {product} -> remainder {remainder}")

# Conjugation is a field automorphism: algebra can't tell i from -i.
assert np.isclose((z * w).conjugate(), z.conjugate() * w.conjugate())
assert np.isclose((z + w).conjugate(), z.conjugate() + w.conjugate())
print("\nAll representations agree; conjugation preserves + and *.")

# Bombelli (1572): x^3 = 15x + 4 has the real root 4, but Cardano's
# formula reaches it through the cube roots of 2 + 11i and 2 - 11i.
u = (2 + 11j) ** (1 / 3)   # principal cube root
v = (2 - 11j) ** (1 / 3)
print(f"\nBombelli: cbrt(2+11i) = {u:.4f}, cbrt(2-11i) = {v:.4f},"
      f" sum = {u + v:.4f}")


# Cauchy-Riemann: the Jacobian of f(z) = z^2, seen as a map R^2 -> R^2,
# has the rotation-scaling shape of M(f'(z)) = M(2z).
def f_real(x, y):
    fz = complex(x, y) ** 2
    return np.array([fz.real, fz.imag])


x0, y0, h = 1.0, 2.0, 1e-6
jacobian = np.column_stack([
    (f_real(x0 + h, y0) - f_real(x0, y0)) / h,
    (f_real(x0, y0 + h) - f_real(x0, y0)) / h,
])
print(f"\nJacobian of z^2 at 1+2i (finite differences):\n{jacobian.round(4)}")
print(f"M(2z) at z = 1+2i:\n{M(2 * z)}")
