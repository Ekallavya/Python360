# We can return a range of characters by using the slice syntax.
# We need to Specify the start index and the end index, separated by a colon, to return a part of the string.

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[6:12])

# Slice From the Start
print(b[:5])

# Slice from the end
print(b[5:])
#Use negative indexes to start the slice from the end of the string
b = "Hello, World!"
print(b[-6:-2]) #Worl