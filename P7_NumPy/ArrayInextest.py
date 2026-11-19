import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
#print(arr[4]) index error
print(arr[-1]) # prints last element
print(arr[-2]) # prints second last element
print(arr[-3]) # prints third last element
print(arr[-4])
print(arr[2]+arr[3])
# 2D Array indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(' 1st row , 2nd element  : ', arr[0, 1])
print(' 2nd row , 5th element  : ', arr[1, 4])
print('Last element from 2nd dim: ', arr[1, -1])
#3D Array indexing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#Access the third element of the second array of the first array:
print("third element of the second array of the first array: ", arr[0, 1, 2])

