# numpy.dot() is used to compute the dot product of two arrays.

# For 1D arrays, it returns the scalar dot product.
# For 2D arrays, it performs matrix multiplication.
# For arrays with N dimensions, it performs a sum-product over the last axis of the first array and the second-to-last axis of the second array.
# Example: This example shows how numpy.dot() calculates the dot product of two 1D arrays.


import numpy as np
a = np.array([2, 3])
b = np.array([4, 5])
print(np.dot(a, b))

# Output
# 23
# Explanation: np.dot(a, b) -> 2*4 + 3*5 = 8 + 15 = 23.

# Syntax
# numpy.dot(a, b, out=None)

# Parameters:

# a: First input array.
# b: Second input array.
# out (Optional): array to store the result.
# Examples
# Example 1: This example demonstrates the dot product of two complex numbers using numpy.dot().

a = 2 + 3j
b = 4 + 5j
print(np.dot(a, b))

# Output
# (-7+22j)
# Explanation: np.dot(a, b) multiplies using complex arithmetic -> 2*(4+5j) + 3j*(4+5j) -> -7 + 22j.

# Example 2: This example shows matrix multiplication using numpy.dot() on two 2D arrays.

a = np.array([[1, 4],
              [5, 6]])
b = np.array([[2, 4],
              [5, 2]])
print(np.dot(a, b))

# Output
# [[22 12]
#  [40 32]]
# Explanation: np.dot(a, b) performs matrix multiplication

# For output [0,0] -> (1×2) + (4×5) = 2 + 20 = 22
# For output [0,1] -> (1×4) + (4×2) = 4 + 8 = 12
# For output [1,0] -> (5×2) + (6×5) = 10 + 30 = 40
# For output [1,1] -> (5×4) + (6×2) = 20 + 12 = 32
# Example 3: This example uses numpy.dot() with a 2D array and a 1D array to produce a vector.

a = np.array([[3, 5],
              [1, 2],
              [4, 1]])
b = np.array([2, 3])
print(np.dot(a, b))

# Output
# [21  8 11]
# Explanation: Each row of a is dotted with vector b

# Row 1 -> 3×2 + 5×3 = 6 + 15 = 21
# Row 2 -> 1×2 + 2×3 = 2 + 6 = 8
# Row 3 -> 4×2 + 1×3 = 8 + 3 = 11