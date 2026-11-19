"""
The Insertion Sort algorithm uses one part of the array to hold the sorted values,
and the other part of the array to hold values that are not sorted yet.
How it works:

Take the first value from the unsorted part of the array.
Move the value into the correct place in the sorted part of the array.
Go through the unsorted part of the array again as many times as there are values.
"""

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
    insert_index = i
    current_value = mylist.pop(i)
    for j in range(i-1, -1, -1):
        if mylist[j] > current_value:
            insert_index = j
    mylist.insert(insert_index, current_value)

print(mylist) #[5, 11, 12, 22, 25, 34, 64, 90]