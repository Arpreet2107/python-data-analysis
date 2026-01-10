# Arithmetic operations are used for numerical computation and we can perform them on arrays using NumPy. With NumPy we can quickly add, subtract, multiply, divide and get power of elements in an array. NumPy performs these operations even with large amounts of data.

# In this article, we’ll see at the basic arithmetic functions in NumPy and show how to use them for simple calculations.

# Addition of Arrays
# Addition is an arithmetic operation where the corresponding elements of two arrays are added together. In NumPy the addition of two arrays is done using the np.add() function.

import numpy as np
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.add(a, b)
print(res)
# Subtraction of Arrays
# We can subtract two arrays element-wise using the np.subtract() function. This function subtracts each element of the second array from the corresponding element in the first array.

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.subtract(a, b)
print(res)

# Multiplication of Arrays
# Multiplication in NumPy can be done element-wise using the np.multiply() function. This multiplies corresponding elements of two arrays.

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.multiply(a, b)
print(res)
# Division of Arrays
# Division is another important operation that is performed element-wise using the np.divide() function. This divides each element of the first array by the corresponding element in the second array.

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.divide(a, b)
print(res)
# Exponentiation (Power)
# It allows us to raise each element in an array to a specified power. In NumPy, this can be done using the np.power() function.

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.power(a, b)
print(res)
# Modulus Operation
# It finds the remainder when one number is divided by another. In NumPy, you can use the np.mod() function to calculate the modulus element-wise between two arrays.

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.mod(a, b)
print(res)