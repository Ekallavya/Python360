import numpy as np
#Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
#create 3D Array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
#check number of dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# create n dimension array

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr) #[[[[[1 2 3 4]]]]]
print('number of dimensions :', arr.ndim)