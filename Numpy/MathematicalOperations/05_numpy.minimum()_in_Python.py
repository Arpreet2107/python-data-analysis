# numpy.minimum() is a NumPy function that compares two arrays (or scalars) element-wise and returns a new array containing the minimum value at each position. If either element is NaN, that NaN is returned. If both are NaN, the first one is returned.

# Example: This example shows how numpy.minimum() compares two numbers and returns the smaller one.
import numpy as np
a = 10
b = 21
print(np.minimum(a, b))
# Syntax
# numpy.minimum(arr1, arr2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None)

# Parameters:

# arr1: First input array (or scalar).
# arr2: Second input array (or scalar).
# out: Optional array to store output.
# where: Boolean mask; only True positions are computed.
# dtype (optional): Data type of output.
# casting / order: Controls casting and memory layout (advanced use).
# Note on / and *
# / -> parameters before it are positional-only.
# * -> parameters after it are keyword-only.

# Examples of numpy.minimun()
# Example 1: This example compares two 1D arrays element-wise and returns the minimum of each pair.


a = np.array([2, 8, 125])
b = np.array([3, 3, 15])
print(np.minimum(a, b))

# Explanation: np.minimum(a1, a2), min(2, 3) -> 2, min(8, 3) -> 3 and min(125, 15) -> 15

# Example 2: This example shows how numpy.minimum() behaves when NaN values are present in the arrays.

a = np.array([np.nan, 0, np.nan])
b = np.array([np.nan, np.nan, 0])
print(np.minimum(a, b))

# Explanation:

# When one side is np.nan, the result becomes np.nan.
# When both are np.nan, the first np.nan is returned.
# Example 3: This example compares arrays of different shapes using broadcasting and finds element-wise minimum values.

a = np.array([[4, 7, 9], [1, 5, 8]])
b = np.array([3, 6, 10])
print(np.minimum(a, b))

# Explanation:

# a2 is broadcast across each row.
# np.minimum(a1, a2) compares each column pair.