#An iterator is an object that contains a countable number of values.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) #apple
print(next(myit)) #banana
print(next(myit)) #cherry
#print(next(myit)) will throw error

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit)) #b
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a

#The for loop actually creates an iterator object and executes the next() method for each loop.
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

mystr = "banana"

for x in mystr:
    print(x)
