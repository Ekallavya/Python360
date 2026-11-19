
"""
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #[2 3 4 5]
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:]) #[5 6 7]
print(arr[:4]) #[1 2 3 4]
print(arr[2:5]) #[3 4 5]

#Negative slicing -Use the minus operator to refer to an index from the end
print(arr[-3:-1]) #[5 6]

# Step -Use the step value to determine the step of the slicing
print(arr[1:5:2]) #[2 4]
print(arr[0:6:2]) #[1 3 5]

# Return every other element from the entire array
print(arr[::2]) #[1 3 5 7]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 3:5]) #[9 10]
#From both elements, return index 2:
print(arr[0:2, 2]) #[3 8]
#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print("-------------------------------")
print(arr[0:2, 1:4]) #[[2 3 4][7,8,9]]