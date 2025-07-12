# Shuffle, Unique, Resize, Flatten, Ravel Functions in numpy arrays

import numpy as np

# Shuffle Function

var1=np.array([1,2,3,4,5])
np.random.shuffle(var1)
print(var1)
print()

# Unique Function

var2=np.array([1,2,2,1,3,4,4,5])
x=np.unique(var2)
print(x)
print()

# Resize function

var3=np.array([1,2,3,4,5,6])
y=np.resize(var3,(2,3))
print(y)
print()

# Flatten function

var4=np.array([[1,2],[3,4],[5,6]])
print(var4.flatten(order='F'))
print(var4.flatten(order='C'))
