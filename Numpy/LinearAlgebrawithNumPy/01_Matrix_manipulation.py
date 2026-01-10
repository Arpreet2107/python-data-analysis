# In Python, matrices can be represented as 2D lists or 2D arrays. Using NumPy arrays for matrices provides additional functionalities for performing various operations efficiently. NumPy is a Python library that offers fast, optimized array operations.

# Why Use NumPy for Matrix Operations?
# Efficient Computation: Uses optimized C-level implementations.
# Cleaner Code: Eliminates explicit loops in many operations.
# Wide Functionality: Supports element-wise operations, matrix multiplication, aggregation, and more.
# Matrix Operations in NumPy
# 1. Element-wise Addition, Subtraction, and Division
# Performing element-wise operations allows you to directly apply arithmetic operations between matrices of the same shape.
import numpy as np

x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

print("Addition:\n", np.add(x, y))
print("Subtraction:\n", np.subtract(x, y))
print("Division:\n", np.divide(x, y))
# 2. Element-wise Multiplication vs. Matrix Multiplication
# Use np.multiply() for element-wise multiplication and np.dot() or @ for standard matrix multiplication.

x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])
print("Element-wise multiplication:\n", np.multiply(x, y))
print("Matrix multiplication:\n", np.dot(x, y))
# 3. Other Useful NumPy Matrix Functions
# NumPy provides utility functions to perform common matrix operations like square root, sum, or transpose.

x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])
print("Square root:\n", np.sqrt(x))
print("Sum of all elements:", np.sum(y)
print("Column-wise sum:", np.sum(y, axis=0))
print("Row-wise sum:", np.sum(y, axis=1))
print("Transpose:\n", x.T))
# Matrix Operations Using Nested Loops
# If you are not using NumPy, you can perform matrix operations using nested loops:
A = [[1,2],[4,5]]
B = [[7,8],[9,10]]
rows = len(A)
cols = len(A[0])

C = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        C[i][j] = A[i][j] + B[i][j]
print("Addition:\n", C)

D = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        D[i][j] = A[i][j] - B[i][j]
print("Subtraction:\n", D)

E = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        E[i][j] = A[i][j] / B[i][j]
print("Division:\n", E)
