# NumPy - Arithmetic Operations

import numpy as np

# 1D array

v1=np.array([1,2,3])
v2=np.array([4,5,6])

ans1=np.add(v1,v2)
ans2=np.subtract(v1,v2)
ans3=np.multiply(v1,v2)
ans4=np.divide(v1,v2)

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print()

v3=np.array([1,2,3])
res=np.pow(v3,2)
print(res)
print()

v3=np.array([2,4,6])
res2=np.mod(v3,2)
print(res2)
print()

# 2D array

v11=np.array([[1,2,3],[4,5,6]])
v12=np.array([[6,5,4],[3,2,1]])

final1=np.add(v11,v12)
final2=np.subtract(v11,v12)
final3=np.multiply(v11,v12)
final4=np.divide(v11,v12)
print(final1)
print(final2)
print(final3)
print(final4)
