# The outer product of two vectors is a matrix where each element [i, j] is the product of the ith element of the first vector and the jth element of the second vector. NumPy provides the outer() function to calculate this efficiently.

# Example: In this example, we calculate the outer product of two small 1D arrays.
import numpy as np

x = np.array([1, 2])
y = np.array([3, 4])
res = np.outer(x, y)
print(res)

# Explanation: np.outer(x, y) multiplies each element of x with each element of y to form a 2x2 matrix.

# Syntax
# numpy.outer(a, b, out=None)

# Parameters:

# a: First input vector (1D array or flattened).
# b: Second input vector (1D array or flattened).
# out (Optional): array to store the result.
# Returns: A 2D array where each element is a[i] * b[j].

# Examples
# Example 1: In this example, the outer product of two small arrays is calculated.

a = np.array([6, 2])
b = np.array([2, 5])
res = np.outer(a, b)
print(res)


# Explanation: np.outer(a, b) multiplies each element of a with each element of b to form a 2x2 matrix.

# Example 2: Here, two 2x2 matrices are flattened automatically and the outer product is computed.

# a = np.array([[1, 3], [2, 6]])
b = np.array([[0, 1], [1, 9]])
res = np.outer(a, b)
print(res)

# Explanation: np.outer(a, b) first flattens both matrices and then computes the outer product, producing a 4x4 matrix.

# Example 3: In this example, two 3x3 matrices are flattened and their outer product is calculated.

a = np.array([[2, 8, 2], [3, 4, 8], [0, 2, 1]])
b = np.array([[2, 1, 1], [0, 1, 0], [2, 3, 0]])
res = np.outer(a, b)
print(res)

# Explanation: np.outer(a, b) flattens both 3x3 matrices into 1D arrays and calculates the outer product, resulting in a 9x9 matrix.