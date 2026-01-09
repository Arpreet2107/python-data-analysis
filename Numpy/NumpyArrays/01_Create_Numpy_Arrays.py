# Creating NumPy arrays is a fundamental aspect of working with numerical data in Python. NumPy provides various methods to create arrays efficiently, catering to different needs and scenarios. In this article, we will see how we can create NumPy arrays using different ways and methods.

# Ways to Create Numpy Arrays
# Below are some of the ways by which we can create NumPy Arrays in Python:

# Create Numpy Arrays Using Lists or Tuples
# The simplest way to create a NumPy array is by passing a Python list or tuple to the numpy.array() function. This method creates a one-dimensional array.
import numpy as np

my_list = [1, 2, 3, 4, 5]
numpy_array = np.array(my_list)
print("Simple NumPy Array:",numpy_array)
# Initialize a Python NumPy Array Using Special Functions
# NumPy provides several built-in functions to generate arrays with specific properties.

# np.zeros(): Creates an array filled with zeros.
# np.ones(): Creates an array filled with ones.
# np.full(): Creates an array filled with a specified value.
# np.arange(): Creates an array with values that are evenly spaced within a given range.
# np.linspace(): Creates an array with values that are evenly spaced over a specified interval.
zeros_array = np.zeros((2, 3))
ones_array = np.ones((3, 3))
constant_array = np.full((2, 2), 7)
range_array = np.arange(0, 10, 2)  # start, stop, step
linspace_array = np.linspace(0, 1, 5)  # start, stop, num

print("Zero Array:","\n",zeros_array)
print("Ones Array:","\n",ones_array)
print("Constant Array:","\n",constant_array)
print("Range Array:","\n",range_array)
print("Linspace Array:","\n",linspace_array)

# Create Python Numpy Arrays Using Random Number Generation
# NumPy provides functions to create arrays filled with random numbers.

# np.random.rand(): Creates an array of specified shape and fills it with random values sampled from a uniform distribution over [0, 1).
# np.random.randn(): Creates an array of specified shape and fills it with random values sampled from a standard normal distribution.
# np.random.randint(): Creates an array of specified shape and fills it with random integers within a given range.

random_array = np.random.rand(2, 3)
normal_array = np.random.randn(2, 2)
randint_array = np.random.randint(1, 10, size=(2, 3))  
print(random_array)
print(normal_array)
print(randint_array)

# Create Python Numpy Arrays Using Matrix Creation Routines
# NumPy provides functions to create specific types of matrices.

# np.eye(): Creates an identity matrix of specified size.
# np.diag(): Constructs a diagonal array.
# np.zeros_like(): Creates an array of zeros with the same shape and type as a given array.
# np.ones_like(): Creates an array of ones with the same shape and type as a given array.

identity_matrix = np.eye(3)
diagonal_array = np.diag([1, 2, 3])
zeros_like_array = np.zeros_like(diagonal_array)
ones_like_array = np.ones_like(diagonal_array)
print(identity_matrix)
print(diagonal_array)
print(zeros_like_array)
print(ones_like_array)
