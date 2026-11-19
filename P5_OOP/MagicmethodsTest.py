# __init__() and __str__() are both magic methods

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

p1 = Person("Emil")
print(p1)

"""
Method	Called By	Description
__init__()	Person(...)	Runs when a new object is created
__str__()	print(obj), str(obj)	Controls the readable text shown for an object
__repr__()	repr(obj)	Controls the developer-facing representation
__eq__()	obj1 == obj2	Controls what "equal" means for the class
__add__()	obj1 + obj2	Controls what the + operator does
__len__()	len(obj)	Returns the "length" of an object
__lt__()	obj1 < obj2	Controls how objects are ordered when compared or sorted
__contains__()	item in obj	Controls what the in operator checks
__call__()	obj(...)	Lets an object be called like a function
"""