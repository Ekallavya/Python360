#ou can search an array for a certain value, and return the indexes that get a match.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) #(array([3, 5, 6]),)

arr = np.array([10, 14, 93, 41, 8, 7])

x = np.where(arr%2 == 1)

print(x) #(array([2, 3, 5]),)

arr = np.array([10, 14, 93, 41, 8, 7])

x = np.where(arr%2 == 0)

print(x) #(array([0, 1, 4]),)

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
#Find the indexes where the value 7 should be inserted, starting from the right:
print(x) #1
arr = np.array([6, 7, 8, 9,10])
x = np.searchsorted(arr, 7, side='right')

print(x) #2
#Find the indexes where the values 2, 4, and 6 should be inserted:
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6]) #[1 2 3]

print(x)
