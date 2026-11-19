# We can evaluate any expression in Python, and get one of two answers, True or False.
print(10 > 9) #True
print(10 == 9) # False
print(10 < 9) # False

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

"""
Some Values are False
In fact, there are not many values that evaluate to False, 
except empty values, such as (), [], {}, "", 
the number 0, and the value None. 
And of course the value False evaluates to False.
"""
print('------------------')
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))