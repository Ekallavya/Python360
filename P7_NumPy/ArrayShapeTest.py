# NumPy arrays have an attribute called shape
# that returns a tuple with each index having the number of corresponding elements.
# i.e (number rows ,now of columns each row)

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) #(2, 4)

arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])

print(arr.shape) #(2, 2, 4)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape) #shape of array : (1, 1, 1, 1, 4)

# Array Reshaping
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15])

newarr = arr.reshape(5, 3)

print(newarr)
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]
 [13 14 15]]
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
"""
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 2, 2)
print(newarr)

"""
[[[ 1  2]
  [ 3  4]]

 [[ 5  6]
  [ 7  8]]

 [[ 9 10]
  [11 12]]]
"""