# A sparse matrix is a matrix in which most elements are zeros. Sparse matrices are widely used in machine learning, natural language processing (NLP), and large-scale data processing, where storing all zero values is inefficient.

# Example of a sparse matrix:

# 0 0 3 0 4
# 0 0 5 7 0
# 0 0 0 0 0
# 0 2 6 0 0

# Storing such a matrix as a normal 2D array wastes memory, as most elements are zeros. Instead, we store only non-zero elements along with their row and column indices (triplets format).

# Benefits of using sparse matrices:

# Reduced Memory Usage: Only non-zero elements are stored, saving memory.
# Faster Computations: Operations can be performed only on non-zero elements, improving speed.
# Sparse Matrix Formats in SciPy
# The scipy.sparse module provides several formats for storing sparse matrices, each optimized for different operations:

# Format            Best For                          Description
# ---------------------------------------------------------------------------
# csr_matrix        Fast row slicing, math operations
#                   Compressed Sparse Row; good for arithmetic and row access.

# csc_matrix        Fast column slicing
#                   Compressed Sparse Column; efficient for column-based operations.

# coo_matrix        Easy matrix building
#                   Coordinate format using (row, col, value) triples.

# lil_matrix        Incremental row-wise construction
#                   List of Lists format; rows can be modified easily before converting.

# dia_matrix        Diagonal-dominant matrices
#                   Stores only diagonals; saves memory for diagonal-heavy matrices.

# dok_matrix        Fast item assignment
#                   Dictionary-based format; ideal for random updates.


# Example 1: csr_matrix (Compressed Sparse Row)
# CSR format stores non-zero values row-wise, enabling fast row slicing and efficient matrix operations.

import numpy as np
from scipy.sparse import csr_matrix
d = np.array([3, 4, 5, 7, 2, 6])     # data
r = np.array([0, 0, 1, 1, 3, 3])     # rows
c = np.array([2, 4, 2, 3, 1, 2])     # cols
csr = csr_matrix((d, (r, c)), shape=(4, 5))
print(csr.toarray())
# Output

# [[0 0 3 0 4]
#  [0 0 5 7 0]
#  [0 0 0 0 0]
#  [0 2 6 0 0]]

# Explanation: csr_matrix stores only non-zero values with their coordinates and reconstructs full matrix using toarray().

# Example 2: csc_matrix (Compressed Sparse Column)
# CSC format stores data column-wise, making column-based operations faster.

# import numpy as np
from scipy.sparse import csc_matrix
d = np.array([3, 4, 5, 7, 2, 6])     
r = np.array([0, 0, 1, 1, 3, 3])     
c = np.array([2, 4, 2, 3, 1, 2])     
csc = csc_matrix((d, (r, c)), shape=(4, 5)) 
print(csc.toarray())
# Output

# [[0 0 3 0 4]
#  [0 0 5 7 0]
#  [0 0 0 0 0]
#  [0 2 6 0 0]]

# Explanation: Stores non-zero values in column-compressed format, efficient for column operations.

# Example 3: coo_matrix (Coordinate Format)
# COO format represents the matrix using (row, col, value) triplets. Useful when constructing matrices dynamically before converting to CSR/CSC.

import numpy as np
from scipy.sparse import coo_matrix
d = np.array([3, 4, 5, 7, 2, 6]) 
r = np.array([0, 0, 1, 1, 3, 3]) 
c = np.array([2, 4, 2, 3, 1, 2]) 
coo = coo_matrix((d, (r, c)), shape=(4, 5))
print(coo.toarray())
# Output

# [[0 0 3 0 4]
#  [0 0 5 7 0]
#  [0 0 0 0 0]
#  [0 2 6 0 0]]

# Explanation: Stores elements as (row, col, value) tuples.

# Example 4: lil_matrix (List of Lists)
# LIL (List of Lists) format allows efficient row-wise construction. You can easily insert or modify values before converting the matrix to CSR or CSC for faster computation.

import numpy as np
from scipy.sparse import lil_matrix
lil = lil_matrix((4, 5))
lil[0, 2] = 3
lil[0, 4] = 4
lil[1, 2] = 5
lil[1, 3] = 7
lil[3, 1] = 2
lil[3, 2] = 6
print(lil.toarray())
# Output

# [[0. 0. 3. 0. 4.]
#  [0. 0. 5. 7. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 2. 6. 0. 0.]]

# Explanation: Creates a List of Lists (LIL) matrix and assigns values directly by row and column.

# Example 5: dok_matrix (Dictionary of Keys)
# DOK (Dictionary of Keys) format is ideal for random assignments. You can assign elements at any position efficiently, making it perfect for incremental matrix construction.

import numpy as np
from scipy.sparse import dok_matrix
dok = dok_matrix((4, 5))
dok[0, 2] = 3
dok[0, 4] = 4
dok[1, 2] = 5
dok[1, 3] = 7
dok[3, 1] = 2
dok[3, 2] = 6
print(dok.toarray())
# Output

# [[0. 0. 3. 0. 4.]
#  [0. 0. 5. 7. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 2. 6. 0. 0.]]

# Explanation: Internally stored as dictionary {(row, col): value}.

# Example 6: dia_matrix (Diagonal Matrix)
# DIA (Diagonal) format stores only the diagonals of the matrix. It is very memory-efficient for diagonal-dominant matrices, where most non-zero elements lie along certain diagonals.

import numpy as np
from scipy.sparse import dia_matrix
data = np.array([[3, 5, 6, 7]])  
offsets = np.array([0])         
dia = dia_matrix((data, offsets), shape=(4, 5))
print(dia.toarray())
# Output

# [[3 0 0 0 0]
# [0 5 0 0 0]
# [0 0 6 0 0]
# [0 0 0 7 0]]

# Explanation: Creates a Diagonal (DIA) matrix storing only specified diagonals.