# Splitting arrays means dividing a single NumPy array into multiple smaller sub-arrays. NumPy provides several functions that make this easy by allowing you to split arrays along different directions (rows, columns, depth).

# Below are some important terms to understand when splitting arrays:

# Axis: The direction along which the array is split (0 for rows, 1 for columns).
# Sub-arrays: Smaller arrays created after splitting the original array.
# Splitting Methods: Functions like np.split(), np.hsplit(), np.vsplit() and np.array_split().
# Equal vs. Unequal Splits: Splits can divide data evenly, or slightly unevenly if needed (using array_split()).

# Example: This example splits a 1D array into three smaller parts using np.array_split().
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
res = np.array_split(arr, 3)
print(res)
# Explanation: np.array_split(arr, 3) divides the array into 3 sub-arrays, splitting elements as evenly as possible.

# Splitting Methods
# NumPy provides several built-in functions to split arrays into smaller parts. These methods help divide 1D, 2D, and even 3D arrays along different axes. Let's go through each method one by one with simple examples, outputs, and clear explanations.
# 1. numpy.split()
# numpy.split() is used to divide an array into equal-sized subarrays. The number of splits must perfectly divide the size of the array along the chosen axis. If equal division is not possible, NumPy will raise an error.
arr = np.arange(6)
res = np.split(arr, 2)
print(res)
# Explanation: np.arange(6) creates [0 1 2 3 4 5], np.split(array, 2) splits the array into 
# 2 equal parts and result in two subarrays, each containing 3 elements

# 2. numpy.array_split()
# numpy.array_split() works like split(), but it allows uneven splitting. This is useful when the array size does not divide evenly by the number of splits. NumPy will distribute the extra elements automatically.

arr = np.arange(13)
res = np.array_split(arr, 4)
print(res)
# Explanation: np.arange(13) creates array of 13 elements, np.array_split(array, 4) splits into 4 unequal parts and extra elements are distributed among the first subarrays

# 3. numpy.vsplit()
# numpy.vsplit() performs vertical splitting, meaning it divides a matrix row-wise (along axis=0). It works only on arrays with 2 or more dimensions.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
res = np.vsplit(arr, 2)
print(res)
# Explanation: vsplit(matrix, 2) splits into 2 vertical (row-wise) partsand each part contains 2 rows

# 4. numpy.hsplit()
# numpy.hsplit() performs horizontal splitting, which divides the array column-wise (axis=1). This is helpful when separating feature columns in datasets.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
res = np.hsplit(arr, 2)
print(res)
# Explanation: hsplit(array, 2) splits into 2 equal column groups and each output contains 2 columns

# 5. numpy.dsplit()
# numpy.dsplit() is used for 3D arrays. It splits the array along the third axis (axis=2). This is useful when working with stacked matrices, images, or multi-channel data.

arr = np.arange(24).reshape((2, 3, 4))
res = np.dsplit(arr, 2)
print(res)
# Explanation: Array shape is (2, 3, 4) and dsplit(..., 2) splits last axis into 2 equal parts. Each result contains half of the last dimension
