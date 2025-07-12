# Insert and Delete Function in numpy arrays

import numpy as np

# Insert in 1d array

var=np.array([1,2,4,5])
ans=np.insert(var,2,3)
print(ans)
print()

# Insert in 2D array

var1=np.array([[1,2,3],[4,5,6]])
res1=np.insert(var1,2,7,axis=0)
res2=np.insert(var1,2,7,axis=1)
print(res1)
print()
print(res2)
print()


# Delete in 1D array

var2=np.array([1,2,3,4,5])
d=np.delete(var,1)
print(d)