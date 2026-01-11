# Inner product (or dot product) of two 1D arrays is the sum of the products of their corresponding elements. NumPy provides the inner() function to calculate this efficiently.

# Example: In this example, we compute the inner product of two small arrays with values.

import numpy as np
x = np.array([1, 2])
y = np.array([3, 4])
res = np.inner(x, y)
print(res)
# Explanation: np.inner(x, y) multiplies corresponding elements (1*3 + 2*4) and sums them to get 11.

# Syntax
# numpy.inner(array1, array2)

# Parameters: array1, array2 -> 1D arrays whose inner product is to be calculated.
# Returns: A single scalar value representing the inner product.
# Examples
# Example 1: Calculating the inner product of two small arrays.

a = np.array([6, 2])
b = np.array([2, 5])
res = np.inner(a, b)
print(res)
# Explanation: np.inner(a, b) multiplies corresponding elements (6*2 + 2*5) and sums them to get 22.

# Example 2: In this example, the inner product of two arrays with more elements is calculated.

a = np.array([1, 3, 5])
b = np.array([0, 1, 5])
res = np.inner(a, b)
print(res)
# Explanation: np.inner(a, b) calculates (1*0 + 3*1 + 5*5) which equals 28.

# Example 3: In this example, we compute the inner product of arrays containing varied values. # pyright: ignore[reportInvalidTypeForm]

a = np.array([1, 2, 2, 8])
b = np.array([2, 1, 0, 6])
res = np.inner(a, b)
print(res)