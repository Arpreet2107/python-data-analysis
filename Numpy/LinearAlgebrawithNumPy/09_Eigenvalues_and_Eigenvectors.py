# # Eigenvalues and Eigenvectors

# Eigenvalues and eigenvectors are fundamental concepts in linear algebra, used in applications such as matrix diagonalization, stability analysis, and data analysis (for example, Principal Component Analysis – PCA). They are associated with a **square matrix** and provide important insights into the behavior and properties of linear transformations.

# ---

# ## Eigenvalues

# Eigenvalues are unique **scalar values** associated with a matrix or linear transformation. They represent how much an eigenvector is stretched or compressed during the transformation.

# * If the eigenvalue is **positive**, the direction of the eigenvector remains unchanged.
# * If the eigenvalue is **negative**, the direction of the eigenvector is reversed.
# * If the eigenvalue is **zero**, the vector collapses into a lower dimension.

# ### Eigenvalue Equation

# A v = λ v

# Where:

# * **A** is the given square matrix
# * **v** is the associated eigenvector
# * **λ** is the scalar eigenvalue

# ---

# ## Eigenvectors

# Eigenvectors are **non-zero vectors** that, when multiplied by a matrix, change only in magnitude (stretch or shrink) but not in direction. The eigenvalue must be found first in order to determine the corresponding eigenvector.

# For a square matrix **A** of order *n × n*, the eigenvector is a column matrix of size *n × 1*. This is called the **right eigenvector**, since matrix multiplication is not commutative.

# ### Left Eigenvector

# A left eigenvector is defined using the equation:

# v A = λ v

# Here, **v** is a row vector of size *1 × n*.

# ---

# ## Eigenvector Equation Derivation

# Starting from the eigenvalue equation:

# A v = λ v

# The right-hand side represents scalar multiplication. This can be rewritten using the identity matrix **I**:

# λ v = (λI) v

# Rearranging terms:

# A v − λI v = 0

# (A − λI) v = 0

# For a **non-zero vector v**, this equation has a solution only if the determinant of the matrix is zero. Hence:

# det(A − λI) = 0

# This equation is called the **characteristic equation**.

# ---

# ## How to Find an Eigenvector

# Follow these steps to find the eigenvectors of a square matrix:

# **Step 1:** Find the eigenvalues of matrix A using:

# det(A − λI) = 0

# **Step 2:** Denote the eigenvalues as:

# λ₁, λ₂, λ₃, ...

# **Step 3:** For each eigenvalue λᵢ, solve:

# (A − λᵢ I) X = 0

# **Step 4:** Repeat Step 3 for all remaining eigenvalues.

# ---

# ## Types of Eigenvectors

# ### Right Eigenvector

# A Vᴿ = λ Vᴿ

# Where:

# * **A** is the square matrix of order *n × n*
# * **λ** is an eigenvalue
# * **Vᴿ** is a column vector

# Vᴿ = [v₁, v₂, v₃, ..., vₙ]ᵀ

# ### Left Eigenvector

# Vᴸ A = λ Vᴸ

# Where:

# * **Vᴸ** is a row vector

# Vᴸ = [v₁, v₂, v₃, ..., vₙ]

# ---

# ## Eigenvectors of a 2 × 2 Matrix

# ### Example

# Find the eigenvalues and eigenvectors of:

# A = [[1, 2],
# [5, 4]]

# #### Step 1: Eigenvalues

# det(A − λI) = 0

# (1 − λ)(4 − λ) − (2 × 5) = 0

# λ² − 5λ − 6 = 0

# (λ − 6)(λ + 1) = 0

# Eigenvalues:

# λ = 6, −1

# #### Step 2: Eigenvectors

# For λ = 6:

# (A − 6I)v = 0 → 5a − 2b = 0

# Eigenvector:

# v = [2, 5]

# For λ = −1:

# (A + I)v = 0 → a = −b

# Eigenvector:

# v = [1, −1]

# *Note:* Any scalar multiple of an eigenvector is also an eigenvector.

# ---

# ## Eigenvectors of a 3 × 3 Matrix

# ### Example

# A = [[2, 2, 2],
# [2, 2, 2],
# [2, 2, 2]]

# #### Eigenvalues

# λ = 6, 0, 0

# #### Eigenvectors

# For λ = 0:

# Eigenvectors:

# [-1, 1, 0]
# [-1, 0, 1]

# For λ = 6:

# Eigenvector:

# [1, 1, 1]

# ---

# ## Eigenspace

# The **eigenspace** of a matrix is the set of all eigenvectors corresponding to all eigenvalues of the matrix.

# ### Steps to Find Eigenspace

# 1. Find all eigenvalues
# 2. Find eigenvectors corresponding to each eigenvalue
# 3. The set of all eigenvectors forms the eigenspace

# Example eigenspace:

# [-1, 1, 0]
# [-1, 0, 1]
# [ 1, 1, 1]

# ---

# ## Diagonalization of a Matrix

# A matrix can be diagonalized as:

# A = X D X⁻¹

# Where:

# * **A** is the original matrix
# * **X** is the matrix of eigenvectors
# * **D** is a diagonal matrix of eigenvalues
# * **X⁻¹** is the inverse of X

# ---

# ## Applications of Eigenvalues and Eigenvectors

# * **Google PageRank Algorithm** – ranks web pages using eigenvectors
# * **Markov Processes** – steady-state probability analysis
# * **Principal Component Analysis (PCA)** – dimensionality reduction
# * **Latent Semantic Analysis (LSA)** – text and document similarity
# * **Spectral Graph Theory** – community detection and network analysis
# * **Computer Vision (Eigenfaces)** – face recognition
# * **Control Systems** – system stability analysis
# * **Signal Processing** – noise filtering and feature extraction

# ---

# ## Solved Examples

# ### Example 1

# A = [[1, 0, 0],
# [1, 1, 0],
# [0, 1, 1]]

# Eigenvalues:

# λ = 1, 1, 1

# Eigenvector:

# k [1, 0, 0]

# ---

# ### Example 2

# A = [[5, 0],
# [0, 5]]

# Eigenvalues:

# λ = 5, 5

# Eigenvectors:

# [1, 0]
# [0, 1]
# ---