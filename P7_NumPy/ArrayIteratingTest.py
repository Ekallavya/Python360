# 1D Array  iterating

import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# 2D Array  iterating

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
"""
[1 2 3]
[4 5 6]
 """

for x in arr:
    for y in x:
        print(y, end=" ") # 1 2 3 4 5 6

#Iterating 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)
""" 
[[1 2 3]
 [4 5 6]]
[[ 7  8  9]
 [10 11 12]]
 """
for x in arr:
    for y in x:
        print(y)
"""
[1 2 3]
[4 5 6]
[7 8 9]
[10 11 12]
"""

for x in arr:
    for y in x:
        for z in y:
            print(z,end=" ") #1 2 3 4 5 6 7 8 9 10 11 12

#Iterating Arrays Using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x, end=" ") #1 2 3 4 5 6 7 8

#Iterate through every scalar element of the 2D array skipping 1 element
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(" ")

for x in np.nditer(arr[:, ::2]):
    print(x , end=" ")  #1 3 5 7