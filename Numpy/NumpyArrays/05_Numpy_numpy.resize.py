# The numpy.resize() function is used to change the size of an existing NumPy array. It modifies the array permanently and adjusts its shape to the new dimensions. If the new shape requires more elements than available, NumPy repeats the array elements. If less space is required, elements are truncated.

# Example 1: This example resizes a 1D array of 6 elements into a 2×3 array. No values need repetition or truncation.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
arr.resize((2, 3))
# Syntax
# numpy.resize(a, new_shape)
# Parameters:
# a: Input array to be resized.
# new_shape: Target shape (int or tuple).
# refcheck(optional): If True, checks whether the array is referenced elsewhere before resizing.

# Example 2: This example resizes a 6-element array into a 3×4 shape (12 elements needed). NumPy repeats the array elements to fill the new size.
arr = np.array([1, 2, 3, 4, 5, 6])
arr.resize((3, 4))
print(arr)

# Example 3: This example resizes an array into a 2×2 shape. Since fewer elements are required, the extra values are removed.
arr = np.array([10, 20, 30, 40, 50])
arr.resize((2, 2))
print(arr)