# # # The inverse of a matrix is like the reciprocal of a number. When a matrix is multiplied by its inverse, the result is an identity matrix. It is used to solve equations and find unknown values.

# # # The inverse of a matrix exists only if the matrix is non-singular i.e., the determinant should not be 0. Using determinant and adjoint, we can easily find the inverse of a square matrix using the below formula:

# # # if det(A) != 0:
# # #     A_inv = adj(A) / det(A)
# # # else:
# # #     print("Inverse doesn't exist")
# # Matrix Equation:
# # Ax = B
# # A^-1Ax = A^-1B
# # x = A^-1B
# # A^-1 : is the inverse of matrix A
# # x : the unknown variable column
# # B: the solution matrix
# Inverse Matrix using NumPy
# numpy.linalg.inv() in the NumPy module is used to compute the inverse matrix in Python.

# Syntax:

# numpy.linalg.inv(a)

# Parameters: a - Matrix to be inverted

# Returns:  Inverse of the matrix a.

# Example 1:
# This example creates a 3×3 NumPy matrix and finds its inverse using np.linalg.inv()
import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
print(np.linalg.inv(A))
# Example 2:
# This example creates a 4×4 NumPy matrix and computes its inverse using np.linalg.inv()
import numpy as np
A = np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])
print(np.linalg.inv(A))
# Example 3:
# This example computes the inverses of multiple NumPy matrices using np.linalg.inv()

A = np.array([[[1., 2.], [3., 4.]],
              [[1, 3], [3, 5]]])
print(np.linalg.inv(A))
