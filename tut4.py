# Data types in numpy arrays

import numpy as np

var=np.array([2,3,4,5])
var1=np.array([1.2,4.5,5.6,3.4])
var2=np.array(["A","B","C","D"])
var3=np.array(["A","B","C",4,1,3])

print("Data type: ",var3.dtype)

# How to change data type

# 1) Method - 1 

x=np.array([1,2,3,4],dtype=np.int8)
print("Data type: ",x.dtype)
print()

# 2) Method - 2

x1=np.array([1,2,3,4,5],dtype="f")
print("Data type: ",x1.dtype)
print(x1)
print()

# 3) Method - 3

x2=np.array([1,2,3,4,5])
new=np.float32(x2)
print("Data type: ",new.dtype)
print(new)
print()

# 4) Method - 4

x3=np.array([1,2,3,4])
ans=x3.astype(float)
print("Data type: ",ans.dtype)
print(ans)





