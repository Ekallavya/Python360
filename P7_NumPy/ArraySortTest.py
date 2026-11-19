"""
Sorting means putting elements in an ordered sequence.
Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
The NumPy ndarray object has a function called sort(), that will sort a specified array.
"""

import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) #[0 1 2 3]

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr)) #['apple' 'banana' 'cherry']

arr = np.array([True, False, True])

print(np.sort(arr)) #[False True True]

# 2D Arrays sorting
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
"""
[[2 3 4]
 [0 1 5]]
"""