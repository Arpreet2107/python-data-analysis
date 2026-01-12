# A Uniform Distribution is used when every value in a given range has an equal probability of occurring.
# NmPy provides the numpy.random.uniform() method to generate such values for simulations, sampling, and numerical experiments.
# Exampe: Here’s the example demonstrating how to generate one random value from a Uniform Distribution.

import numpy as np
num = np.random.uniform()
print(num)

# Output
# 0.6869717010984568
# Explanation: This generates a random floating-point number between 0 and 1, the default uniform range.

# Syntax
# numpy.random.uniform(low=0.0, high=1.0, size=None)

# Parameters:

# low: Lower bound of the range (inclusive).
# high: Upper bound of the range (exclusive).
# size: Shape of the output array.
# Examples
# Example 1: This example shows how to generate five random numbers between 0 and 1 multiple uniform distribution values.

arr = np.random.uniform(size=5)
print(arr)

# Output
# [0.11403523 0.69111039 0.92330809 0.65533514 0.6227924 ]
# Explanation: np.random.uniform(size=5) creates an array of 5 random numbers in the range [0, 1).

# Example 2: In this example, we generate five random numbers in the range 10 to 20 using the numpy.random.uniform() method.

import numpy as np
vals = np.random.uniform(10, 20, size=5)
print(vals)

# Output
# [15.33364215 15.62793284 19.66237254 18.56727821 11.27919983]
# Explanation: This creates an array vals with 5 values sampled uniformly from the interval 10 ≤ x < 20 using np.random.uniform(10, 20, size=5).

# Using NumPy Generator
# NumPy now recommends using the Generator class for random number generation instead of the legacy numpy.random functions. The Generator provides better randomness, reproducibility, and performance. You can create a Generator instance using np.random.default_rng() and then use its .uniform() method to generate uniform random numbers.

# Example: Here, we generate a 2×3 matrix where each value comes from the Uniform Distribution between 1 and 5 using Generator.

rng = np.random.default_rng()  # Create a Generator instance
m = rng.uniform(1, 5, size=(2, 3))
print(m)

# Output
# [[4.42554691 4.11402029 2.90202497]
#  [4.74049492 3.26084455 2.00333856]]
# Explanation: The rng.uniform(1, 5, size=(2, 3)) call generates a 2×3 array where each value is drawn uniformly from 1 ≤ x < 5.

# Visualizing the Uniform Distribution
# Visualizing the generated numbers helps in understanding their behavior. Let's see a example to plot a histogram of random numbers using numpy.random.uniform function.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
low = 10
high = 20
size = 1000
data = np.random.uniform(low, high, size)
sns.histplot(data, bins=30, kde=False, color='skyblue', edgecolor='black')
plt.title(f"Uniform Distribution (Range: {low} to {high})")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Explanation:

# The histogram shows values scattered uniformly between low (10) and high (20).
# Every number in this interval appears with similar frequency, which is the core property of a uniform distribution.
# The flat pattern of bars confirms equal probability for all values in the range.