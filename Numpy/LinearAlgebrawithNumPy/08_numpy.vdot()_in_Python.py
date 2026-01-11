# numpy.vdot() returns the dot product of two vectors. If the first vector contains complex numbers, vdot() automatically takes its complex conjugate before performing the multiplication. For multi-dimensional arrays, it first flattens them and then computes the dot product.

# Example: This example shows how numpy.vdot() works on complex numbers by conjugating the first input.

import numpy as np
a = 2 + 3j
b = 4 + 5j
print(np.vdot(a, b))

# Output
# (23-2j)
# Explanation:

# np.vdot(a, b) -> uses conjugate(a) = 2 - 3j.
# Computes: (2 - 3j) * (4 + 5j) -> 23 - 2j.
# Syntax
# numpy.vdot(a, b)

# Parameters:

# a (array_like): First input vector. If complex, its conjugate is used.
# b (array_like): Second input vector.
# Examples
# Example 1: This example shows how vdot() conjugates the first complex value before multiplication.


a = 1 + 2j
b = 3 + 4j
print(np.vdot(a, b))

# Output
# (11-2j)
# Explanation:

# Conjugate of a -> 1 - 2j.
# Computation -> (1 - 2j) * (3 + 4j) = 11 + 2j.
# Example 2: Here both arrays are 2×2 matrice, vdot() flattens them and performs element-wise multiplication.

a = np.array([[1, 4],
              [5, 6]])
b = np.array([[2, 4],
              [5, 2]])
print(np.vdot(a, b))

# Output
# 55
# Explanation:

# Flattened arrays -> a = [1,4,5,6], b = [2,4,5,2].
# Dot product -> 1*2 + 4*4 + 5*5 + 6*2 = 55.
# Example 3: This example shows vdot() working like a normal dot product when inputs are real numbers.

a = np.array([3, 7, 1])
b = np.array([2, 1, 4])
print(np.vdot(a, b))

# Output
# 17
# Explanation: Computes -> 3*2 + 7*1 + 1*4 = 17.