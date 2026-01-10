# NumPy contains a large number of various mathematical operations. NumPy provides standard trigonometric functions, functions for arithmetic operations, handling complex numbers, etc.

# Trigonometric Functions –
# NumPy has standard trigonometric functions which return trigonometric ratios for a given angle in radians.

# numpy.sin(x[, out]) = ufunc ‘sin’) : This mathematical function helps user to calculate trignmetric sine for all x(being the array elements).




# Python program explaining
# sin() function
 
import numpy as np
import math
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
Sin_Values = np.sin(in_array)
print ("\nSine values : \n", Sin_Values)
# Output :

# Input array : 
#  [0, 1.5707963267948966, 1.0471975511965976, 3.141592653589793]

# Sine values : 
#  [  0.00000000e+00   1.00000000e+00   8.66025404e-01   1.22464680e-16]
# numpy.cos(x[, out]) = ufunc ‘cos’) : This mathematical function helps user to calculate trignmetric cosine for all x(being the array elements).




# Python program explaining
# cos() function

 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
cos_Values = np.cos(in_array)
print ("\nCosine values : \n", cos_Values)
# Output :

# Input array : 
#  [0, 1.5707963267948966, 1.0471975511965976, 3.141592653589793]

# Cosine values : 
#  [  1.00000000e+00   6.12323400e-17   5.00000000e-01  -1.00000000e+00]
# ===============================
# Additional Trigonometric Functions in NumPy
# ===============================

# FUNCTION        DESCRIPTION
# ------------------------------------------------------------
# tan()           Compute tangent element-wise.

# arcsin()        Compute inverse sine element-wise.
#                 Returns values in radians.

# arccos()        Compute inverse cosine element-wise.
#                 Returns values in radians.

# arctan()        Compute inverse tangent element-wise.
#                 Returns values in radians.

# arctan2()       Compute element-wise arctangent of x1/x2
#                 while correctly determining the quadrant.

# degrees()       Convert angles from radians to degrees.
#                 Alias of rad2deg().

# rad2deg()       Convert angles from radians to degrees.

# deg2rad()       Convert angles from degrees to radians.

# radians()       Convert angles from degrees to radians.
#                 Alias of deg2rad().

# hypot()         Given the two legs of a right triangle,
#                 return the hypotenuse using:
#                 sqrt(x² + y²)

# unwrap()        Unwrap phase angles by changing deltas
#                 between values to 2π complements.
#                 Commonly used in signal processing.

# ===============================
# End of Trigonometric Functions
# ===============================
# Hyperbolic Functions –
# numpy.sinh(x[, out]) = ufunc ‘sin’) : This mathematical function helps user to calculate hyperbolic sine for all x(being the array elements).

# Equivalent to 1/2 * (np.exp(x) - np.exp(-x)) or -1j * np.sin(1j*x).

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
Sinh_Values = np.sinh(in_array)
print ("\nSine Hyperbolic values : \n", Sinh_Values)
# Python3 program explaining
# cosh() function
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
cosh_Values = np.cosh(in_array)
print ("\ncosine Hyperbolic values : \n", cosh_Values)
# ===============================
# Hyperbolic Trigonometric Functions in NumPy
# ===============================

# FUNCTION        DESCRIPTION
# ------------------------------------------------------------
# tanh()          Compute hyperbolic tangent element-wise.

# arcsinh()       Compute inverse hyperbolic sine element-wise.

# arccosh()       Compute inverse hyperbolic cosine element-wise.
#                 Input values must be ≥ 1.

# arctanh()       Compute inverse hyperbolic tangent element-wise.
#                 Input values must be in the range (-1, 1).

# ===============================
# End of Hyperbolic Trigonometric Functions
# ===============================

# Functions for Rounding –
# numpy.around(arr, decimals = 0, out = None) : This mathematical function helps user to evenly round array elements to the given number of decimals.


# Python program explaining
# around() function

in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : \n", in_array)
 
round_off_values = np.around(in_array)
print ("\nRounded values : \n", round_off_values)
 
 
in_array = [.53, 1.54, .71]
print ("\nInput array : \n", in_array)
 
round_off_values = np.around(in_array)
print ("\nRounded values : \n", round_off_values)
 
in_array = [.5538, 1.33354, .71445]
print ("\nInput array : \n", in_array)
 
round_off_values = np.around(in_array, decimals = 3)
print ("\nRounded values : \n", round_off_values)
# numpy.round_(arr, decimals = 0, out = None) : This mathematical function round an array to the given number of decimals.
# # Python program explaining
# round_() function

in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : \n", in_array)
 
round_off_values = np.round_(in_array)
print ("\nRounded values : \n", round_off_values)
 
 
in_array = [.53, 1.54, .71]
print ("\nInput array : \n", in_array)
 
round_off_values = np.round_(in_array)
print ("\nRounded values : \n", round_off_values)
 
in_array = [.5538, 1.33354, .71445]
print ("\nInput array : \n", in_array)
 
round_off_values = np.round_(in_array, decimals = 3)
print ("\nRounded values : \n", round_off_values)
# ===============================
# Rounding & Truncation Functions in NumPy
# ===============================

# FUNCTION        DESCRIPTION
# ------------------------------------------------------------
# rint()          Round elements to the nearest integer.
#                 Halfway values are rounded to the nearest even integer.

# fix()           Round elements toward zero.
#                 Equivalent to truncation for positive and negative values.

# floor()         Return the floor of the input, element-wise.
#                 Rounds down to the nearest integer.

# ceil()          Return the ceiling of the input, element-wise.
#                 Rounds up to the nearest integer.

# trunc()         Return the truncated value of the input, element-wise.
#                 Removes the decimal part without rounding.

# ===============================
# End of Rounding & Truncation Functions
# ===============================


# Exponents and logarithms Functions –
# numpy.exp(array, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None) : This mathematical function helps user to calculate exponential of all the elements in the input array.

# Python program explaining
# exp() function

in_array = [1, 3, 5]
print ("Input array : ", in_array)
 
out_array = np.exp(in_array)
print ("Output array : ", out_array)
# numpy.log(x[, out] = ufunc ‘log1p’) : This mathematical function helps user to calculate Natural logarithm of x where x belongs to all the input array elements.
# Natural logarithm log is the inverse of the exp(), so that log(exp(x)) = x. The natural logarithm is log in base e.

# Python program explaining
# log() function 
in_array = [1, 3, 5, 2**8]
print ("Input array : ", in_array)
 
out_array = np.log(in_array)
print ("Output array : ", out_array)
 
 
print("\nnp.log(4**4) : ", np.log(4**4))
print("np.log(2**8) : ", np.log(2**8))

# ===============================
# Exponential & Logarithmic Functions in NumPy
# ===============================

# FUNCTION            DESCRIPTION
# ------------------------------------------------------------
# expm1()             Calculate exp(x) − 1 for all elements.
#                     More accurate than exp(x) − 1 for small values of x.

# exp2()              Calculate 2**p for all elements in the input array.
#                     Computes exponential base 2.

# log10()             Return the base-10 logarithm of the input array,
#                     element-wise.

# log2()              Return the base-2 logarithm of the input array,
#                     element-wise.

# log1p()             Return the natural logarithm of (1 + x),
#                     element-wise.
#                     More accurate for small values of x.

# logaddexp()         Compute log(exp(x1) + exp(x2)) element-wise.
#                     Used for numerical stability in probability calculations.

# logaddexp2()        Compute log2(2**x1 + 2**x2) element-wise.
#                     Base-2 version of logaddexp().

# ===============================
# End of Exponential & Logarithmic Functions
# ===============================

# Arithmetic Functions –
# numpy.reciprocal(x, /, out=None, *, where=True) : This mathematical function is used to calculate reciprocal of all the elements in the input array.
# Note: For integer arguments with absolute value larger than 1, the result is always zero because of the way Python handles integer division. For integer zero the result is an overflow.
# Python3 code demonstrate reciprocal() function
 
# importing numpy

in_num = 2.0
print ("Input  number : ", in_num)
 
out_num = np.reciprocal(in_num)
print ("Output number : ", out_num)
# numpy.divide(arr1, arr2, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None) : Array element from first array is divided by elements from second element (all happens element-wise). Both arr1 and arr2 must have same shape and element in arr2 must not be zero; otherwise it will raise an error.
# Python program explaining
# divide() function
 
# input_array
arr1 = [2, 27, 2, 21, 23]
arr2 = [2, 3, 4, 5, 6]
print ("arr1         : ", arr1)
print ("arr2         : ", arr2)
 
# output_array
out = np.divide(arr1, arr2)
print ("\nOutput array : \n", out)

# ===============================
# Arithmetic Functions in NumPy
# ===============================

# FUNCTION           DESCRIPTION
# ------------------------------------------------------------
# add()              Add arguments element-wise.
# positive()         Return numerical positive of elements, element-wise.
# negative()         Return numerical negative of elements, element-wise.
# multiply()         Multiply arguments element-wise.
# power()            Raise first array elements to powers from second array, element-wise.
# subtract()         Subtract arguments element-wise.
# true_divide()      Return true division of inputs, element-wise.
# floor_divide()     Return largest integer ≤ division of inputs.
# float_power()      Raise first array elements to powers from second array, element-wise.
# mod()              Return element-wise remainder of division.
# remainder()        Return element-wise remainder of division.
# divmod()           Return element-wise quotient and remainder simultaneously.

# ===============================
# End of Arithmetic Functions Notes
# ===============================


# Complex number Function –
# numpy.isreal(array) : Test element-wise whether it is a real number or not(not infinity or not Not a Number) and return the result as a boolean array.

# Python Program illustrating
# numpy.isreal() method
import numpy as geek
print("Is Real : ", geek.isreal([1+1j, 0j]), "\n")
 
print("Is Real : ", geek.isreal([1, 0]), "\n")

# numpy.conj(x[, out] = ufunc ‘conjugate’) : This function helps the user to conjugate any complex number.
# The conjugate of a complex number is obtained by changing the sign of its imaginary part. If the complex number is 2+5j then its conjugate is 2-5j.
# Python3 code demonstrate conj() function
 
#importing numpy

in_complx1 = 2+4j
out_complx1 = np.conj(in_complx1)
print ("Output conjugated complex number of  2+4j : ", out_complx1)
 
in_complx2 =5-8j
out_complx2 = np.conj(in_complx2)
print ("Output conjugated complex number of 5-8j: ", out_complx2)

# Special functions –
# numpy.cbrt(arr, out = None, ufunc ‘cbrt’) : This mathematical function helps user to calculate cube root of x for all x being the array elements.

# Python program explaining
# cbrt () function

arr1 = [1, 27000, 64, -1000]
print ("cbrt Value of arr1 : \n", np.cbrt(arr1))
  
arr2 = [1024 ,-128]
print ("\ncbrt Value of arr2 : ", np.cbrt(arr2))
  
# numpy.clip() : This function is used to Clip (limit) the values in an array.
# Given an interval, values outside the interval are clipped to the interval edges. For example, if an interval of [0, 1] is specified, values smaller than 0 become 0, and values larger than 1 become 1.

# Python3 code demonstrate clip() function
 
# importing the numpy

 
in_array = [1, 2, 3, 4, 5, 6, 7, 8 ]
print ("Input array : ", in_array)
 
out_array = np.clip(in_array, a_min = 2, a_max = 6)
print ("Output array : ", out_array)
# ===============================
# Miscellaneous Functions in NumPy
# ===============================

# FUNCTION              DESCRIPTION
# ------------------------------------------------------------
# convolve()            Returns the discrete, linear convolution of two 1D sequences.
# sqrt()                Return the non-negative square root of an array, element-wise.
# square()              Return the element-wise square of the input.
# absolute()            Calculate the absolute value element-wise.
# fabs()                Compute the absolute values element-wise.
# sign()                Return an element-wise indication of the sign of a number.
# interp()              One-dimensional linear interpolation.
# maximum()             Element-wise maximum of array elements.
# minimum()             Element-wise minimum of array elements.
# real_if_close()       If input is complex, return real array if imaginary parts are close to zero.
# nan_to_num()          Replace NaN with zero and infinity with large finite numbers.
# heaviside()           Compute the Heaviside step function.

# ===============================
# End of Miscellaneous Functions Notes
# ===============================
