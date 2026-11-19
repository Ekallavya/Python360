# Empty list
x = []
# List with initial values
y = [1, 2, 3, 4, 5]
# List with mixed types
z = [1, "hello", 3.14, True]
x = [9, 12, 7, 4, 11, 8]

# Add element:
x.append(10)
print("x:",x) #[9, 12, 7, 4, 11, 8, 10]
# Sort list ascending:
x.sort()
print("sorted x:",x) #sorted x: [4, 7, 8, 9, 10, 11, 12]

#Create an algorithm to find the lowest value in a list
my_array = [7, 12, 9, 4, 11, 8]
print("my_array:",my_array)
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value:', minVal)