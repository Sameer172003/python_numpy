# Matrix Function in numpy 

import numpy as np

# Transpose function

var1=np.matrix([[1,2,3],[4,5,6]])
print(np.transpose(var1))
print()

# Swapaxes function

print(np.swapaxes(var1,0,1))
print()

# Inverse function

var2=np.array([[1,2],[3,4]])
print(np.linalg.inv(var2))
print()

# Power function

var3=np.array([[1,2],[3,4]])
print(np.linalg.matrix_power(var3,2))   # n>0
print()
print(np.linalg.matrix_power(var3,0))   # n=0
print()
print(np.linalg.matrix_power(var3,-2))  # n<0
print()

# Determinate function

var5=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.linalg.det(var5))
print()