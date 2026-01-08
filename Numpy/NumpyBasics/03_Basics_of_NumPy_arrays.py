# Types of Array
# Various types of arrays are as follows:

# 1. One Dimensional Array
# A one-dimensional array is a type of linear array.
import numpy as np

a = [1, 2, 3, 4]

arr = np.array(a)

print("List in python : ", a)

print("Numpy Array in python :",arr)
# 2. Multi-Dimensional Array
# A Multi-Dimensional Array is an array that can store data in more than one dimension such as rows and columns.
# In simple terms it is a array of arrays.For example a 2D array is like a table with rows and columns where each element is accessed by two 
# indices: one for the row and one for the column. Higher dimensions like 3D arrays involve adding additional layers.


list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

sample_array = np.array([list_1, 
                         list_2,
                         list_3])
print("Numpy multi dimensional array in python\n",sample_array)

# Note: use [ ] operators inside numpy.array() for multi-dimensional.

# Parameters of a Numpy Array
# 1. Axis: Axis of an array describes the order of the indexing into the array.

# Axis 0 = one dimensional
# Axis 1 = Two dimensional
# Axis 2 = Three dimensional 

# 2. Shape: Number of elements along with each axis and is returned as a tuple.

# Example:
sample_array = np.array([[0, 4, 2],
                       [3, 4, 5],
                       [23, 4, 5],
                       [2, 34, 5],
                       [5, 6, 7]])

print("shape of the array :",sample_array.shape)
# 3. Rank: Rank of an array is simply the number of axes or dimensions it has.
# One-dimensional array has rank 1.
# Two-dimensional array has rank 2.

# 4. Data type objects (dtype): Data type objects (dtype) is an example of numpy.dtype class.
# It describes how the bytes in the fixed-size block of memory corresponding to an array item should be interpreted.
# Example:
sample_array_1 = np.array([[0, 4, 2]])
sample_array_2 = np.array([0.2, 0.4, 2.4])
print("Data type of the array 1 :",sample_array_1.dtype)
print("Data type of array 2 :",sample_array_2.dtype)
# Different Ways of Creating Numpy Array
# 1. numpy.array(): Numpy array object in Numpy is called ndarray. We can create ndarray using this function.

# Syntax: numpy.array(parameter)

# Example: 
arr = np.array([3,4,5,5])
print("Array :",arr)
# 2. numpy.fromiter(): The fromiter() function create a new one-dimensional array from an iterable object.
# Syntax: numpy.fromiter(iterable, dtype, count=-1)
var = "Geekforgeeks"
arr = np.fromiter(var, dtype = 'U2')
print("fromiter() array :",arr)

#  3. numpy.arange(): This is an inbuilt NumPy function that returns evenly spaced values within a given interval.
# Syntax:  numpy.arange( start , stop, step , dtype=None )
# Example:

np.arange(1, 20 , 2,
          dtype = np.float32)

# 4. numpy.linspace(): This function returns evenly spaced numbers over a specified between two limits. 
# Syntax: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# Example:
np.linspace(3.5, 10, 3,
            dtype = np.int32)

# 5. numpy.empty(): This function create a new array of given shape and type without initializing value.
# Syntax: numpy.empty(shape, dtype=float, order='C')
# Example:
np.empty([4, 3],
         dtype = np.int32,order = 'f')
# 6. numpy.ones(): This function is used to get a new array of given shape and type filled with ones (1).
# Syntax: numpy.ones(shape, dtype=None, order='C')
# Example:
np.ones([4, 3],
            dtype = np.int32,order = 'f')
# 7. numpy.zeros(): This function is used to get a new array of given shape and type filled with zeros (0). 
# Syntax: numpy.ones(shape, dtype=None)
# Example:
np.zeros([4, 3],
         dtype = np.int32,order = 'f')
# As we move forward NumPy will remain an important tool for 
# efficient data manipulation and mastering its core concepts will helps us to solve more complex computational
# challenges in the future.