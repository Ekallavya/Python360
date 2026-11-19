#The NumPy array object has a property called dtype that returns the data type of the array
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int64
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) #<U7

arr = np.array([1, 2, 3, 4], dtype='S1')

print(arr) #[b'1' b'2' b'3' b'4']
print(arr.dtype) #|S1

arr = np.array([True,False], dtype='b')

print(arr) #[1 0]
print(arr.dtype) #|int8

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype) #int32
#A non integer string like 'a' can not be converted to integer (will raise an error):
try:
    arr = np.array(['a', '2', '3'], dtype='i4')
    print(arr)
    print(arr.dtype) #int32
except ValueError as e:
    print(f"Error: {e}") #Error: invalid literal for int() with base 10: 'a'


#converting data type for existing arrays
arr = np.array([1.1, 2.1, 3.1])
print(arr) #[1.1 2.1 3.1]
print(arr.dtype) #float64
newarr = arr.astype('i')

print(newarr) #[1 2 3]
print(newarr.dtype) #int32
