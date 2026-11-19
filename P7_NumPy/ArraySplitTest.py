"""
Splitting is reverse operation of Joining.
Joining merges multiple arrays into one and Splitting breaks one array into multiple.
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) #[array([1, 2]), array([3, 4]), array([5, 6])]

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr) #[array([1, 2]), array([3, 4]), array([5]), array([6])]
print(newarr[0]) #[1 2]
print(newarr[1]) #[3 4]
print(newarr[2]) #[5]
print(newarr[3]) #[6]
#Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)
"""
[array([[1, 2],[3, 4]]),
 array([[5, 6],[7, 8]]),
 array([[ 9, 10],[11, 12]])]
"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)
"""
[array([[1, 2, 3],
       [4, 5, 6]]), array([[ 7,  8,  9],
       [10, 11, 12]]), array([[13, 14, 15],
       [16, 17, 18]])]
"""