#Joining means putting contents of two or more arrays in a single array.
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultArr = np.concatenate((arr1, arr2))

print(resultArr) #[1 2 3 4 5 6]
#Join two 2-D arrays along rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
resultArr = np.concatenate((arr1, arr2), axis=1)
print(resultArr)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""
#stacking
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultArr = np.stack((arr1, arr2), axis=1)

print(resultArr)
"""
[[1 4]
 [2 5]
 [3 6]]"""