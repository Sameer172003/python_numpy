# NumPy Array Creation

import numpy as np
y=[1,2,3,4]
x=np.array(y) # Creating array from list

print(x)
print()
print(y)

# How to create an array by taking user input
l=[]
for i in range(0,5):
    ele=int(input("Enter an element: "))
    l.append(ele)
ans=np.array(l)
# print(ans.dim)  # To find the dimension of an array
print(ans) 

ar2=np.array([[1,2,3,4],[5,6,7,8]]) # 2D array
print(ar2)

ar3=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]]) # 3D array
print(ar3)

# How to create n dimensional array
arn=np.array([1,2,3,4],ndmin=10)
print(arn)