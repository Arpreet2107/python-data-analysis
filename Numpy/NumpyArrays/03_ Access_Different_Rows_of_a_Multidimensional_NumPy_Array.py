# When we need to access different rows of a multidimensional NumPy array such as first row, last two rows or middle rows it can be done using slicing. NumPy provides simple ways to select specific rows according to given conditions.

# In 2D Array
# Example 1: Accessing the First and Last row of a 2D NumPy array
import numpy as np

arr = np.array([[10, 20, 30], [40, 5, 66], [70, 88, 94]])
print("Array:")
print(arr)
res = arr[[0,2]]
print("Accessed Rows :")
print(res)

# Example 2: Accessing the Middle row of 2D NumPy array
arr = np.array([[101, 20, 3, 10], [40, 5, 66, 7], [70, 88, 9, 141]])
print("Array:")
print(arr)
res = arr[1]
print("Accessed Row :")
print(res)

# Example 3: Accessing Specific Rows and Columns of a 2D NumPy array
arr = np.array([[12, 15, 18], 
                [25, 30, 35], 
                [40, 45, 50]])
print("Array:")
print(arr)
res = arr[:2, :2]   # first 2 rows, first 2 columns
print("Accessed Elements:")
print(res)

# In 3D Arrays
# Example 1: Accessing the Middle rows of 3D NumPy array

arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]], [[50, 65, 8], [70, 85, 10], [11, 22, 33]]])
print("Array:")
print(arr)
res = arr[:,[1]]
print("Accessed Rows:")
print(res)

# Example 2: Accessing the First and Last rows of 3D NumPy array

arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]], 
                 [[50, 65, 8], [70, 85, 10], [11, 22, 33]],
                 [[19, 69, 36], [1, 5, 24], [4, 20, 96]]])
print("Array:")
print(arr)
res =arr[:,[0, 2]]
print("Accessed Rows:")
print(res)

# Example 3: Accessing Specific Rows and Columns in a 3D NumPy array

arr = np.array([
    [[5, 10, 15], [20, 25, 30], [35, 40, 45]],
    [[2,  4,  6], [ 8, 10, 12], [14, 16, 18]],
    [[7, 14, 21], [28, 35, 42], [49, 56, 63]]
])
print("Array:")
print(arr)
res = arr[:, :2, :2]   # first 2 rows and first 2 columns from each 2D slice
print("Accessed Elements:")
print(res)
