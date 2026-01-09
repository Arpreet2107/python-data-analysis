# The numpy.stack() function is used to join multiple arrays by creating a new axis in the output array. This means the resulting array always has one extra dimension compared to the input arrays. To stack arrays,
# they must have the same shape, and NumPy places them along the axis you specify
# Example: This example stacks two 1D arrays along a new axis to form a 2D array.
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
res = np.stack((a, b), axis=0)
print(res)

# Explanation: np.stack((a, b), axis=0) creates a new 0th axis and places arrays one below another.

# Syntax
# numpy.stack(arrays, axis=0, out=None)

# Parameters:

# arrays: Sequence of input arrays with the same shape.
# axis: Position of the new axis where arrays will be stacked (default: 0).
# out(Optional): output array to store the result.
# Examples
# Example 1: This example shows how stacking the same 1D arrays along axis 0, 1, and -1 changes the output shape.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=1))
print(np.stack((a, b), axis=-1))
# Explanation:

# axis=0: a and b become rows.
# axis=1: a and b become columns.
# axis=-1: same as axis 1 because it refers to the last dimension.
# Example 2: This example stacks two 2D arrays along axis 0, 1, and 2 to show how the new 3D structure changes.

x = np.array([[1, 2, 3],
              [4, 5, 6]])
y = np.array([[7, 8, 9],
              [10, 11, 12]])
print(np.stack((x, y), axis=0))
print(np.stack((x, y), axis=1))
print(np.stack((x, y), axis=2))

# Explanation:

# axis=0: stacks arrays as two “layers” of a 3D array.
# axis=1: stacks row-wise.
# axis=2: stacks column-wise forming 3D structure.

# Example 3: This example stacks two 3D arrays along axis 0, 1, 2, and 3 to demonstrate how stacking works with higher-dimension data.
m = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
n = np.array([[[10, 20], [30, 40]],
              [[50, 60], [70, 80]]])
print(np.stack((m, n), axis=0))
print(np.stack((m, n), axis=1))
print(np.stack((m, n), axis=2))
print(np.stack((m, n), axis=3))

# Explanation:
# axis=0: stacks arrays as two 3D layers.
# axis=1: stacks "planes" together.
# axis=2: stacks each corresponding row.
# axis=3: stacks each corresponding element as a new last-axis pair.