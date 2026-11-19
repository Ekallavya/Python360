#Short Hand If
a = 5
b = 10
if a > b: print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#nestedif
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

#pass stmt
age = 20

if age < 18:
    pass # TODO: Add underage logic later
else:
    print("Access granted")

#while

i = 1
while i < 6:
    print(i)
    i += 1
#for

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
"""
b
a
n
a
n
a
"""
for x in "banana":
    print(x)