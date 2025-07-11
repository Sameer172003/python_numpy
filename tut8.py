# Indexing & Slicing in numpy arrays

import numpy as np

# 1D array (Indexing)

var=np.array([1,2,3,4,5])
print(var[2])
print()
print(var[-3])
print()

# 2D array (Indexing)

var1=np.array([[1,2,3],[4,5,6]])
print(var1[0,1])
print()

# 3D array (Indexing)

var2=np.array([[[1,2],[6,7]]])
print(var2[0,1,1])
print()

# 1D array (Slicing)

res=np.array([1,2,3,4,5,6,7,8])
print("2 to 6 : ",res[1:6])
print("2 to End : ",res[1:])
print("Start to 6 : ",res[:6])
print(var[1:6:2]) # Skiping 1 value
print()

# 2D array (Slicing)

ans=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(ans[1,0:3])
