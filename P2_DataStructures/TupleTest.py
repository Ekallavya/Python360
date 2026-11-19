#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Allows duplicates
fTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(fTuple)
print(len(fTuple))  # 5
#To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
fTuple = ("apple",)
print(type(fTuple)) # tuple

#NOT a tuple
cTuple = ("Red")
print(type(cTuple)) #str

empTyTuple = ()
print(type(empTyTuple))
#Tupe Data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# update tuple - indirectly

tuple1 = ("apple", "banana", "cherry")
y = list(tuple1)
y[1] = "kiwi"
tuple1 = tuple(y)

print(tuple1) #('apple', 'kiwi', 'cherry')


