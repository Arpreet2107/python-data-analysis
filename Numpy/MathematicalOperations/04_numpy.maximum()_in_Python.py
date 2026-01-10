# numpy.maximum() is a NumPy function that compares two arrays (or scalars) element-wise and returns a new array containing the maximum value at each position. If any compared element is NaN, the NaN is returned. If both elements are NaN, the first NaN is returned.

# Example: This example shows how numpy.maximum() compares two numbers and returns the larger one.
import numpy as np
a = 10
b = 21
print(np.maximum(a, b))
# Syntax
# numpy.maximum(arr1, arr2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None)

# Parameters:

# arr1: First input array (or scalar).
# arr2: Second input array (or scalar).
# out (optional): Array to store the result.
# where: Boolean mask; True positions are computed.
# dtype (optional): Data type of the output.
# casting / order: Controls data casting and memory layout (rarely used).
# Note: / -> Parameters before / are positional-only (must be passed without argument names).
#            * -> Parameters after * are keyword-only (must be passed using their names).

# Examples of numpy.maximum()
# Example 1: This example compares two 1D arrays and returns the element-wise maximum values.

a = np.array([2, 8, 125])
b = np.array([3, 3, 15])
print(np.maximum(a, b))
# Explanation: np.maximum(a, b) compares each index, max(2, 3) -> 3, max(8, 3) -> 8 and max(125, 15) -> 125.

# Example 2: This example shows how numpy.maximum() behaves when the arrays contain NaN values.

a = np.array([np.nan, 0, np.nan])
b = np.array([np.nan, np.nan, 0])
print(np.maximum(a, b))

# Explanation:

# When one element is np.nan, the result is np.nan.
# When both elements are np.nan, the first np.nan is returned.
# Example 3: This example compares two arrays of different shapes using broadcasting and returns element-wise maxima.

a = np.array([[1, 4, 7], [2, 5, 8]])
b = np.array([3, 3, 3])
print(np.maximum(a, b))

# Explanation:

# b is broadcast across rows.
# np.maximum(a, b) compares each column with [3, 3, 3].