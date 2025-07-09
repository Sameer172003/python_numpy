# Shape and Reshape in NumPy

import numpy as np
 
var=np.array([[1,2],[3,4]])
print(var)
print()
print(var.shape)  # It gives the matrix size
print()


var2=np.array([1,2,3,4,5,6,7,8,9])
x=var2.reshape(3,3)  # It makes 1D array into multidimensional array (rows,columns)
print(x)