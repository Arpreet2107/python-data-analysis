# Reshaping in NumPy refers to modifying the dimensions of an existing array without changing its data. The reshape() function is used for this purpose. It reorganizes the elements into a new shape, which is useful in machine learning, matrix operations and data preparation.
import numpy as np
# Example 1: This example converts a 1-D array into a 2-D array by specifying rows and columns that match the total number of elements.
a = np.array([1, 2, 3, 4, 5, 6])
r = a.reshape(2, 3)
print(r)
# Explanation: a.reshape(2, 3) arranges the 6 elements into 2 rows and 3 columns, forming a 2-D matrix.
# array.reshape(shape)

# Parameter: shape - Tuple, defining the new dimensions. One dimension can be -1, letting NumPy auto-calculate it based on the total elements.
# Returns: A new reshaped ndarray.
# Example 2: This example creates a 3-D array by grouping the original elements into blocks, each containing equal-sized 2-D sections.

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
r = a.reshape(2, 2, 2)
print(r)
a.reshape(2, 2, 2) 
# transforms the array into 2 blocks, each containing a 2×2 matrix, forming a 3-D structure.

# Example 3: This example demonstrates the use of -1 when one dimension is unknown. NumPy calculates that missing dimension automatically.

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
r = a.reshape(3, -1)
print(r)
# Explanation: a.reshape(3, -1) tells NumPy to create 3 rows, and it computes the remaining dimension as 4 columns, since 12 ÷ 3 = 4.