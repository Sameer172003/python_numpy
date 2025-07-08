# Special Types of Arrays ( filled with specific value)

import numpy as np

# Arrays filled with zeroes

ar_1=np.zeros(4) # 1D array
ar_2=np.zeros((3,4)) # 2D array


print(ar_1)
print()
print(ar_2)
print()

# Arrays filled with ones

ar1=np.ones(4)
print(ar1)
print()

# An array with range of elements

ar2=np.arange(5)
print(ar2)
print()

# Array diagonal element filled with 1's

ar3=np.eye(3)
print(ar3)
print()

#  Create an array with values that are spaced linearly in a specified interval

ar4=np.linspace(0,10,num=5)
print(ar4)


