# NumPy Array Iterating

import numpy as np

# 1D array (Iteration)

var=np.array([1,2,3,4,5,6,7])
print(var)
print()
for i in var:
    print(i)
print()

# 2D array (Iteration)

res=np.array([[1,2,3,4],[5,6,7,8]])
print(res)
print()
for i in res:
    print(i)

print()

for j in res:
    for k in j:
        print(k)
print()

# 3D array (Iteration)

ans=np.array([[[1,2,3,4],[5,6,7,8]]])

for i in ans:
    for j in i:
        for k in j:
            print(k)

print()


# Iterate using function

for i in np.nditer(ans):
    print(i)
print()

# Getting indexing as well as data

for i,d in np.ndenumerate(ans):
    print(i,d)