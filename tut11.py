# Join & Split Function in numpy arrays

import numpy as np

# 1D array (Join)

var=np.array([1,2,3,4])
var1=np.array([6,7,8,9])
ans=np.concatenate((var,var1))
print(ans)
print()

# 2D array (Join)

vr=np.array([[1,2],[3,4]])
vr1=np.array([[6,7],[8,9]])
res=np.concatenate((vr,vr1),axis=1)
print(res)
print()

var_1=np.array([1,2,3,4])
var_2=np.array([6,7,8,9])
ans1=np.hstack((var_1,var_2))
ans2=np.vstack((var_1,var_2))
ans3=np.dstack((var_1,var_2))
print(ans1)
print()
print(ans2)
print()
print(ans3)
print()


l=np.array([1,2,3,4,5,6])
result=np.array_split(l,3)
print(result)
print(result[0])  # Getting elements from each array

