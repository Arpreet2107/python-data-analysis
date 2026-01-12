# The numpy.random.randint() function is used to generate random integers within a specified range. It allows you to create arrays of any shape filled with random integer values, making it useful in simulations, testing, and numerical experiments.

# Example:

# Input: Generate integers between 0 and 5
# Output: [3 1 4 0 2]

# Explanation: Each value is a random integer from the interval [0, 5).

# Syntax
# numpy.random.randint(low, high=None, size=None, dtype=int)
# Parameters:

# low: lowest integer that can appear in the output.
# high(Optional): Upper limit (exclusive). If omitted, range becomes [0, low).
# size(Optional): Shape of the output array (e.g., 5, (2,3), (2,3,4)).
# dtype(Optional): Data type of the returned numbers. Default is integer.
# Examples
# Example 1: This example generates five random integers between 0 and 4, stored in a one-dimensional array.
import numpy as np
arr = np.random.randint(0, 5, size=5)
print(arr)

# Example 2: This example creates a 2×3 matrix of random integers ranging from 0 to 9.


arr = np.random.randint(0, 10, size=(2, 3))
print(arr)

# Explanation:

# size=(2, 3): creates 2 rows and 3 columns.
# 0 to 10: upper limit 10 is excluded.
# Example 3: This example produces a 3D array (2×2×4) with values between 5 and 15.

arr = np.random.randint(5, 15, size=(2, 2, 4))
print(arr)
