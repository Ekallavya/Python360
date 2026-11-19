import numpy as np

arr = np.array([41, 42, 43, 44])
arr1= [True, False, True, False]

newarr = arr[arr1]
"""
The example above will return [41, 43], why?
Because the new array contains only the values 
where the filter array had the value True, in this case, index 0 and 2.
"""
print(newarr) #[41 43]

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)