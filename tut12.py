# Search , Sort , Search Shorted, Filter Functions in numpy arrays

import numpy as np

# Search in an array

var=np.array([3,4,2,5,1,6])
ans1=np.where(var == 5)     
ans2=np.where(var%2 == 0)
print(ans1)
print()
print(ans2)
print()

# Search in a sorted array

l=np.array([1,2,3,4,5,6,7,8])
ans=np.searchsorted(l,5)
print(ans)
print()

# Sort anything such as number as well as character

li=np.array([3,2,4,1,5,7,6])
res=np.sort(li)
print(res)
print()

# Filter Array 

lis=np.array(['a','b','c','d'])
f=[True,False,True,False]
result=lis[f]
print(result)


