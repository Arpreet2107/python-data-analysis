# Array indexing in NumPy refers to the method of accessing specific elements or subsets of data within an array. This feature allows us to retrieve, modify and manipulate data at specific positions or ranges helps in making it easier to work with large datasets. In this article, we’ll see the different ways to index and slice NumPy arrays which helps us to work with our data more effectively.

# 1. Accessing Elements in 1D Arrays
# A 1D NumPy array is a sequence of values with positions called indices which starts at 0. We access elements by using these indices in square brackets like arr[0] for the first element. Negative indices count from the end so arr[-1] gives the last element.

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])

# 2. Accessing Elements in Multidimensional Arrays
# In this we will see how to access elements in both 2D and 3D arrays using specific indices.
# 2D Arrays: We can access elements by specifying both row and column indices like matrix[row, column].

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])

# Here matrix[1, 2] accesses the element in the second row (index 1) and third column (index 2) which is 6.
# 3D Arrays: It can be visualized as a stack of 2D arrays, we need three indices-
# Depth: Specifies the 2D slice.
# Row: Specifies the row within the slice.
# Column: Specifies the column within the row.
# We can access elements by specifying row, column and depth indices like matrix[depth, row, column].
cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 
                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])
print(cube[1, 2, 0])

# 3. Slicing Arrays
# It allows us to extract a range of elements using the format start:stop:step. This can be done for both 1D and multidimensional arrays which allows us to select ranges of elements or submatrices easily.
# Slicing 1D Arrays: For a 1D array, slicing returns a subset of elements between the start and stop indices.

arr = np.array([0, 1, 2, 3, 4, 5])
print(arr[1:4])

# Here arr[1:4] slices the array starting at index 1 up to (but not including) index 4 so it returns the elements [1, 2, 3].
# Slicing Multidimensional Arrays: In this slicing can be applied to each dimension separately which allows us to extract submatrices or smaller blocks of data.

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0:2, 1:3])

# Slicing for multidimensional arrays
# 4. Boolean Indexing
# It allows us to filter elements from an array based on a condition and returns only those that meet it. We create a boolean array from a condition and use it to select elements and can combine conditions with logical operators.

arr = np.array([10, 15, 20, 25, 30])
print(arr[arr > 20])

# The condition arr > 20 returns True for elements greater than 20 so only 25 and 30 are selected and printed.
# We can also use logical operators like & (AND), | (OR) and ~ (NOT) to combine conditions.

arr = np.array([10, 15, 20, 25, 30])
print(arr[(arr > 10) & (arr < 30)])

# The combined condition selects elements greater than 10 and less than 30 resulting in [15, 20, 25].
# 5. Fancy Indexing
# It is also known as Advanced Indexing which allows us access elements of an array by using another array or list of indices. This allows selecting multiple elements at once even if they are not next to each other which makes it easy to pick specific values from different positions in the array.

arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])

# It uses the list [0, 2, 4] to pick elements at those specific positions which returns [10, 30, 50].

# 6. Integer Array Indexing
# It is similar to fancy indexing and uses an array of integers to select multiple elements from another array. This method allows us to access elements at specific, non-adjacent positions which makes it useful for extracting scattered data points.

arr = np.array([1, 2, 3, 4, 5])
print(arr[[0, 2, 4]])

# Using an integer array [0, 2, 4] which selects the elements at those indices and returns [1, 3, 5].
# 7. Ellipsis (...) in Indexing
# The ellipsis (...) can be used to select all dimensions which are not explicitly mentioned. This is helpful in multidimensional arrays when we don’t want to specify every dimension.

cube = np.random.rand(4, 4, 4)
print(cube[..., 0])

# Ellipsis in Indexing
# Here it selects all elements in the first two dimensions and 0 selects the first element along the last dimension for each.

# Note: It will generate random number as it uses random function.

# 8. Using np.newaxis to Add New Dimensions
# The np.newaxis keyword adds a new axis to the array which helps in converting a 1D array into a row or column vector.


arr = np.array([1, 2, 3])
print(arr[:, np.newaxis])

# Using np.newaxis
# Here it adds a new axis helps in converting the 1D array into a 2D column vector with shape (3,1).

# 9. Modifying Array Elements
# We can modify array elements directly by using indexing or slicing. This makes it easy to update specific elements or ranges of elements in an array.


arr = np.array([1, 2, 3, 4])
arr[1:3] = 99
print(arr)

# The slice arr[1:3] selects elements at indices 1 and 2 and replaces them with 99. By mastering these techniques, we'll be able to manipulate and analyze data more efficiently with NumPy.