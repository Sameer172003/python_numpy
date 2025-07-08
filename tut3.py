# Creating Random Valued Arrays

# 1) rand() 2) randn() 3) ranf() 4) randint()

import numpy as np

var=np.random.rand(4) # 1D array
print(var)
print()

var1=np.random.rand(3,4) #2D array
print(var1)
print()

var2=np.random.randn(5)
print(var2)
print()

var3=np.random.ranf(4)
print(var3)
print()

var4=np.random.randint(1,10,5)
print(var4)  