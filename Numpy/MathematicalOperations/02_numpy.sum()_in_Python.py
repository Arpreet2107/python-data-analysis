# numpy.sum() is a NumPy function used to calculate the sum of array elements. It can sum values across the entire array or along a specific axis. It also allows controlling the output data type, initial value, and shape of the result.

# Example: This example shows the use of numpy.sum() to find the total of a 1D numeric array.
import numpy as np
arr = np.array([5, 10, 15])
print(np.sum(arr))
# Explanation: np.sum(arr) adds all elements (5 + 10 + 15) and returns the total.

# Syntax
# numpy.sum(arr, axis=None, dtype=None, out=None, initial=0, keepdims=False)

# Parameters:

# arr: Input array whose elements are to be summed.
# axis: Axis along which the sum is computed. 0 -> column-wise, 1 -> row-wise and None -> entire array
# dtype: Data type of the returned sum.
# out: Output array to store the result.
# initial: Starting value of the sum.
# keepdims: Keeps the reduced axis as dimension in result.
# Examples
# Example 1: This example shows how numpy.sum() works on a 1D array and how changing the dtype affects the result.
arr = np.array([20, 2, 0.2, 10, 4])
print(np.sum(arr))
print(np.sum(arr, dtype=np.uint8))
print(np.sum(arr, dtype=np.float32))
# Explanation:

# np.sum(arr) sums all values normally.
# np.sum(arr, dtype=np.uint8) result is converted into uint8, causing decimal removal.
# np.sum(arr, dtype=np.float32) keeps decimal since it's a float type.
# Example 2: This example calculates the sum of a 2D array and shows how using different data types changes the output

arr = np.array([ [14, 17, 12, 33, 44],
               [15,  6, 27,  8, 19],
               [23,  2, 54,  1,  4] ])
print(np.sum(arr))
print(np.sum(arr, dtype=np.uint8))
print(np.sum(arr, dtype=np.float32))
# Example 3: This example demonstrates summing a 2D array along rows, columns, and using keepdims=True.

arr = np.array([ [14, 17, 12, 33, 44],
               [15,  6, 27,  8, 19],
               [23,  2, 54,  1,  4] ])
print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(np.sum(arr, axis=1, keepdims=True))
# Explanation:

# np.sum(arr, axis=0) column-wise sum.
# np.sum(arr, axis=1) row-wise sum.
# np.sum(arr, axis=1, keepdims=True) keeps each row's sum in a column format.