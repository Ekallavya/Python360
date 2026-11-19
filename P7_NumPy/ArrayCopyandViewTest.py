"""
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
"""
import numpy as np

# Array Copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) #[42  2  3  4  5]
print(x) #[1  2  3  4  5]

# Array View

x = arr.view()
arr[0] = 42

print(arr) #[42  2  3  4  5]
print(x) #[42  2  3  4  5]
# make changes to view
x[0] = 31

print(arr) #[31  2  3  4  5]
print(x) #[31  2  3  4  5]