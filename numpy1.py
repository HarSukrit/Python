import numpy as np
arr=np.array([1,2,3,4,5])
arr2D=np.array([[1,2],[3,4],[5,6]])
print("Accessing 1st element from 1st row in 2D array:",arr2D[0,0])
#Iterating in 2D array:

print("Iterating in 2D array.")
for x in np.nditer(arr2D):
    print(x)
print("Iterating with index using ndenumerate():")
for idx,x in np.ndenumerate(arr2D):
    print(idx,x)
