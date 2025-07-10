# Arithmatic Functions in numpy 

import numpy as np

var=np.array([4,3,2,5,1,6,8])
ans1=np.max(var)
ans2=np.argmax(var)

ans3=np.min(var)
ans4=np.argmin(var)

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print()

var2=np.array([4,9,16,25])
ans=np.sqrt(var2)
print(ans)
print()

var3=np.array([3,4,5,6])
res1=np.sin(var3)
res2=np.cos(var3)
print(res1)
print(res2)
print()

var4=np.array([34,23,27,54,21,39])
res=np.cumsum(var4)
print(res)