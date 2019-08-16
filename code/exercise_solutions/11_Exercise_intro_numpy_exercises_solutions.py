##########################################################################
# File: Python Numpy Exercises Solution
# Author: Evan Carey
# Date Created: 2016-07-21
# Purpose: This is the solution to the Python Numpy Exercises
##########################################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1
mat1 = [(4, 6, 7),
        (3, 5, 7),
        (2, 5, 4)]

mt1_np = np.array(mat1)

# a
mt1_np[0, 0]

# b
mt1_np[1, 1] + mt1_np[2, 2]

# c - row means
mt1_np.mean(1)

# d - column means
mt1_np.mean(0)

# 2
# a
np.random.seed(42)
mat2 = np.random.normal(loc=10, scale=5, size=(100, 10))
mat2.mean()
mat2.std()
mat2.var()

# b
colmeans = mat2.mean(0, keepdims=True)
colmeans.shape
mat2 - colmeans

# c
colsd = mat2.std(0, keepdims=True)
colsd.shape
mat2/colsd

# d
mat2_scaled = (mat2 - colmeans)/colsd
mat2_scaled.mean(0)  # notice the floating point error here!
mat2_scaled.std(0)

# 3
mat3 = np.array([np.random.poisson(i, 15) for i in range(1, 21)])
plt.plot(mat3.mean(1), mat3.var(1))

mat3 = np.array([np.random.poisson(i, 100) for i in range(1, 21)])
plt.plot(mat3.mean(1), mat3.var(1))

mat3 = np.array([np.random.poisson(i, 1000) for i in range(1, 21)])
plt.plot(mat3.mean(1), mat3.var(1))
# The mean is equal to the variance (asymptotically, as N increases to infinity)
