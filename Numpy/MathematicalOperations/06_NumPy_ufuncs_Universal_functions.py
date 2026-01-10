# # NumPy ufuncs (universal functions) are fast, vectorized functions that perform element-wise operations on NumPy arrays. They are highly optimized and support features like broadcasting and automatic type handling. NumPy includes many ufuncs for arithmetic, trigonometry, statistics, etc, and they execute operations very fast because they are implemented in optimized C code.

# # Why use ufuncs?
# # Fast vectorized operations: Ufuncs apply calculations to entire arrays at once, making them much faster than Python loops.
# # Automatic broadcasting and type handling: They adjust array shapes automatically and handle datatype conversion internally, reducing errors.
# # Cleaner and more efficient code: They simplify complex numerical tasks into short, readable code that scales well on large datasets.
# # Basic Universal Functions (ufunc) in NumPy
# # 1. Trigonometric functions
# # NumPy provides several trigonometric functions that operate element-wise on arrays. Angles should be in radians, so degree values must be converted using np.deg2rad(). These functions include standard, inverse, and hyperbolic trigonometric operations.
# ===============================
# Common Trigonometric ufuncs in NumPy
# ===============================

# 1. np.sin(), np.cos(), np.tan()
# --------------------------------
# Description:
# Compute the sine, cosine, and tangent of angles.
# Note:
# • Input angles must be in radians
# • Works element-wise on NumPy arrays

# --------------------------------

# 2. np.arcsin(), np.arccos(), np.arctan()
# --------------------------------
# Description:
# Calculate the inverse (arc) sine, cosine, and tangent.
# Note:
# • Returns angles in radians
# • Useful for recovering angles from trigonometric values

# --------------------------------

# 3. np.sinh(), np.cosh(), np.tanh()
# --------------------------------
# Description:
# Compute hyperbolic sine, cosine, and tangent.
# Note:
# • Commonly used in scientific computing and neural networks

# --------------------------------

# 4. np.deg2rad()
# --------------------------------
# Description:
# Converts angles from degrees to radians.
# Note:
# • Helps when working with degree-based input values

# --------------------------------

# 5. np.rad2deg()
# --------------------------------
# Description:
# Converts angles from radians to degrees.
# Note:
# • Useful for displaying results in a human-readable format

# --------------------------------

# 6. np.hypot()
# --------------------------------
# Description:
# Calculates the hypotenuse of a right-angled triangle.
# Formula:
# • sqrt(x² + y²)
# Use Case:
# • Distance calculation
# • Geometry and physics problems

# ===============================
# End of Trigonometric ufuncs Notes
# ===============================

# Example: This example demonstrates sine, inverse sine, hyperbolic sine, and hypotenuse calculation using NumPy arrays.


import numpy as np

angles = np.array([0, 30, 45, 60, 90]) 
rad = np.deg2rad(angles)  # convert degrees to radians

# Sine of angles
sin_vals = np.sin(rad)
print("Sine values:", sin_vals)

# Inverse sine in degrees
inv_sin = np.rad2deg(np.arcsin(sin_vals))
print("Inverse sine (degrees):", inv_sin)

# Hyperbolic sine
sinh_vals = np.sinh(rad)
print("Hyperbolic sine:", sinh_vals)

# Hypotenuse of a right triangle
hyp = np.hypot(3, 4)
print("Hypotenuse:", hyp)
# Explanation:

# np.deg2rad() converts degrees to radians.
# np.sin() computes sine for each element.
# np.arcsin() calculates inverse sine; np.rad2deg() converts it back to degrees.
# np.sinh() applies the hyperbolic sine function element-wise.
# np.hypot(a, b) computes the hypotenuse of a right triangle with sides a and b.
# 2. Statistical functions
# NumPy provides several statistical functions to calculate properties like mean, median, variance, and range. These functions operate element-wise and along specified axes, making analysis of arrays fast and efficient.
# ===============================
# Common Statistical ufuncs in NumPy
# ===============================

# 1. np.amin(), np.amax()
# --------------------------------
# Description:
# Compute the minimum or maximum value of an array.
# Features:
# • Can operate on the entire array
# • Can compute along a specific axis

# --------------------------------

# 2. np.ptp()
# --------------------------------
# Description:
# Calculates the range of values in an array.
# Formula:
# • ptp = max − min
# Use Case:
# • Measuring data spread

# --------------------------------

# 3. np.percentile(a, p)
# --------------------------------
# Description:
# Computes the p-th percentile of array values.
# Example:
# • p = 50 gives the median
# Use Case:
# • Data distribution analysis
# • Outlier detection

# --------------------------------

# 4. np.mean()
# --------------------------------
# Description:
# Computes the arithmetic mean (average) of data.
# Use Case:
# • Central tendency measurement

# --------------------------------

# 5. np.median()
# --------------------------------
# Description:
# Computes the median (middle value) of sorted data.
# Use Case:
# • Robust measure of central tendency

# --------------------------------

# 6. np.std()
# --------------------------------
# Description:
# Computes the standard deviation.
# Meaning:
# • Measures how much data deviates from the mean
# Use Case:
# • Variability and risk analysis

# --------------------------------

# 7. np.var()
# --------------------------------
# Description:
# Computes the variance of data.
# Meaning:
# • Square of standard deviation
# Use Case:
# • Spread measurement in statistics and ML

# --------------------------------

# 8. np.average()
# --------------------------------
# Description:
# Computes the weighted or unweighted average.
# Features:
# • Supports weights for weighted mean calculations
# Use Case:
# • Weighted scoring systems

# ===============================
# End of Statistical ufuncs Notes
# ===============================
# Example: This example demonstrates common statistical calculations on an array of student weights.


# import numpy as np

weights = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45])

# Min and Max
print("Min and Max:", np.amin(weights), np.amax(weights))

# Range
print("Range:", np.ptp(weights))

# 70th Percentile
print("70th Percentile:", np.percentile(weights, 70))

# Mean
print("Mean:", np.mean(weights))

# Median
print("Median:", np.median(weights))

# Standard Deviation
print("Std Dev:", np.std(weights))

# Variance
print("Variance:", np.var(weights))

# Average
print("Average:", np.average(weights))
# Explanation:

# np.amin() and np.amax() find the smallest and largest values.
# np.ptp() calculates the range (max − min).
# np.percentile(weights, 70) finds the value below which 70% of weights fall.
# np.mean() and np.average() compute the average of the array.
# np.median() returns the middle value.
# np.std() and np.var() measure dispersion via standard deviation and variance.
# 3. Bitwise Functions
# NumPy provides bitwise functions to perform operations on the binary representation of integers. These allow element-wise manipulation of arrays at the bit level.
# ===============================
# Common Bitwise ufuncs in NumPy
# ===============================

# 1. np.bitwise_and()
# --------------------------------
# Description:
# Performs element-wise bitwise AND operation.
# Rule:
# • Result bit is 1 only if both input bits are 1
# Use Case:
# • Masking operations
# • Low-level data manipulation

# --------------------------------

# 2. np.bitwise_or()
# --------------------------------
# Description:
# Performs element-wise bitwise OR operation.
# Rule:
# • Result bit is 1 if at least one input bit is 1
# Use Case:
# • Combining bit masks

# --------------------------------

# 3. np.bitwise_xor()
# --------------------------------
# Description:
# Performs element-wise bitwise XOR operation.
# Rule:
# • Result bit is 1 if input bits are different
# Use Case:
# • Toggling bits
# • Encryption logic

# --------------------------------

# 4. np.invert()
# --------------------------------
# Description:
# Performs bitwise NOT operation (bit inversion).
# Rule:
# • Flips all bits (0 → 1, 1 → 0)
# Note:
# • Equivalent to `~x`
# Use Case:
# • Bit flipping and complements

# --------------------------------

# 5. np.left_shift()
# --------------------------------
# Description:
# Shifts bits of elements to the left.
# Effect:
# • Each left shift multiplies the number by 2
# Use Case:
# • Fast multiplication
# • Binary arithmetic

# --------------------------------

# 6. np.right_shift()
# --------------------------------
# Description:
# Shifts bits of elements to the right.
# Effect:
# • Each right shift divides the number by 2
# Use Case:
# • Fast division
# • Bit-level optimization

# ===============================
# End of Bitwise ufuncs Notes
# ===============================
# Example: This example demonstrates basic bitwise operations on arrays of integers.

even = np.array([0, 2, 4, 6, 8, 16, 32])
odd  = np.array([1, 3, 5, 7, 9, 17, 33])
# Bitwise AND, OR, XOR
print("AND:", np.bitwise_and(even, odd))
print("OR :", np.bitwise_or(even, odd))
print("XOR:", np.bitwise_xor(even, odd))
# Bitwise NOT
print("Invert:", np.invert(even))
# Bit shifts
print("Left shift :", np.left_shift(even, 1))
print("Right shift:", np.right_shift(even, 1))
# Explanation:

# np.bitwise_and(), np.bitwise_or(), np.bitwise_xor() perform element-wise logical operations at the bit level.
# np.invert() flips all bits of each element.
# np.left_shift() and np.right_shift() move the bits of each element left or right, effectively multiplying or dividing by powers of 2.
