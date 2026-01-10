# Working with vector and matrix operations is a fundamental part of scientific computing and data analysis. NumPy is a Python library that computes various types of vector and matrix products. Let's discuss how to find the inner, outer and cross products of matrices and vectors using NumPy in Python.

# Inner Product
# The inner product (or dot product) is obtained by multiplying corresponding elements of two arrays and summing them. For matrices, NumPy computes it row-wise.

# Syntax:
# numpy.inner(arr1, arr2)

# Example: Below we compute the inner product of two vectors and two matrices using np.inner().
import numpy as np

# Define vectors
a = np.array([2, 6])
b = np.array([3, 10])

print("Inner product of vectors a and b =")
print(np.inner(a, b))

# Define matrices
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])

print("Inner product of matrices x and y =")
print(np.inner(x, y))
# Outer Product
# The outer product of two vectors creates a matrix where each element is the product of elements from both vectors. For matrices, they are flattened to 1D before applying the operation.

# Syntax:
# numpy.outer(arr1, arr2, out = None)

# Example: Here we calculate the outer product of vectors and matrices using np.outer().
import numpy as np

# Define vectors
a = np.array([2, 6])
b = np.array([3, 10])

print("Outer product of vectors a and b =")
print(np.outer(a, b))

# Define matrices
x = np.array([[3, 6, 4], [9, 4, 6]])
y = np.array([[1, 15, 7], [3, 10, 8]])

print("Outer product of matrices x and y =")
print(np.outer(x, y))
# Cross Product
# The cross product is defined for 3D vectors and produces a new vector that is perpendicular to both input vectors. For 2D vectors, NumPy previously returned a scalar, but in NumPy ≥ 2.0 this behavior is deprecated. To avoid warnings and stay consistent, we explicitly represent 2D vectors as 3D by adding a zero in the z-axis (e.g., [x, y, 0]).

# For matrices, the cross product is applied row by row, treating each row as a 3D vector.

# Syntax:
# numpy.cross(arr1 , arr2)

# Example: Here we compute the cross product for vectors (converted to 3D) and for matrices row-wise.
import numpy as np

# Define vectors as 3D (z=0 for 2D compatibility)
a = np.array([3, 6, 0])
b = np.array([9, 10, 0])

print("Cross product of vectors a and b =")
print(np.cross(a, b))

# Define matrices (already 3D rows)
x = np.array([[2, 6, 9], [2, 7, 3]])
y = np.array([[7, 5, 6], [3, 12, 3]])

print("Cross product of matrices x and y =")
print(np.cross(x, y))
# Explanation:

# For vectors a and b: We added 0 in the z-axis, so the result is [0, 0, -24] instead of just a scalar.
# For matrices: Each row in x is crossed with the corresponding row in y.
# Example: [2,6,9] × [7,5,6] = [-39, 45, -32].