# In this example, a 2D NumPy array named arr is created, and its characteristics are demonstrated:
#  the array type, number of dimensions (2), shape (2 rows, 3 columns), size (6 elements), 
# and the data type of its elements (int64).
# 
# 
# # Python program to demonstrate
# basic array characteristics
import numpy as np

# Creating array object
arr = np.array( [[ 1, 2, 3],
                [ 4, 2, 5]] )

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)