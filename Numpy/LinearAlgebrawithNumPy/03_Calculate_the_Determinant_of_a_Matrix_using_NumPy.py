# The determinant of a square matrix is a special number that helps determine whether the matrix is invertible and how it transforms space. NumPy provides built-in functions to easily compute the determinant of a matrix, let's explore some of these methods:

# Using numpy.linalg.slogdet()
# For large matrices, numpy.linalg.slogdet() is a numerically stable method. It computes the sign and the logarithm of the determinant separately, which helps prevent numerical overflow or underflow when dealing with very large or very small values.

import numpy as np
A = np.array([[50, 29], [30, 44]])
sign, logdet = np.linalg.slogdet(A)
res = sign * np.exp(logdet)
print(res)
# Using numpy.linalg.det()
# This method provides a straightforward way to compute the determinant. It is suitable for small to medium-sized matrices and is a direct approach based on linear algebra techniques.

A = np.array([[1, 2], [3, 4]])
res = np.linalg.det(A)
print(res)
# Using scipy.linalg.lu
# LU decomposition can also be used to calculate the determinant by decomposing the matrix into lower (L) and upper (U) triangular matrices. The determinant is the product of the diagonal elements of the U matrix.

import scipy.linalg
A = np.array([[1, 2], [3, 4]])
P, L, U = scipy.linalg.lu(A)
res = np.prod(np.diag(U))
print(res)