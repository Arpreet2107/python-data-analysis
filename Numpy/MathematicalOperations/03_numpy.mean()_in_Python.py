# numpy.mean() is a NumPy function used to calculate the average (arithmetic mean) of numeric values.
#  It can compute the mean of a 1D list/array or compute mean row-wise and column-wise for multi-dimensional arrays.
# Example:
# Input: [1, 2, 3]
# Output: 2.0
# Syntax
# We use the following syntax to calculate the mean in NumPy:
# numpy.mean(arr, axis=None, dtype=None, out=None)
# Parameters:
# arr: Input array of numbers
# axis: None - mean of all elements, 0 - column-wise mean and 1 - row-wise mean
# dtype(Optional): type used while computing mean
# out(Optional): array to store the result
# Examples
# Example 1: This example finds the average value of a 1D list using np.mean().
import numpy as np
arr = [20, 2, 7, 1, 34]
res = np.mean(arr)
print(res)
# Explanation: (20 + 2 + 7 + 1 + 34)/5 = 12.8

# Example 2: This example shows how to compute the mean of all elements, each column, and each row using axis.

arr = [[14, 17, 12],
       [15,  6, 27],
       [23,  2, 54]]
print(np.mean(arr))           # entire array
print(np.mean(arr, axis=0))   # column-wise mean
print(np.mean(arr, axis=1))   # row-wise mean
# Example 3: This example stores the result of row-wise mean into another array using out.

arr = [[5, 10, 15],
       [3,  6,  9],
       [8, 16, 24]]
res = np.zeros(3)
np.mean(arr, axis=1, out=res)
print(res)