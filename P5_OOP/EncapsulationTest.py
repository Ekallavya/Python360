"""
Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
This prevents accidental changes to your data and hides the internal details of how your class works.

"""

#In Python, you can make properties private by using a double underscore __ prefix

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
try:
    print(p1.__age) # This will cause an error
except AttributeError:
    print("Age is a private property and cannot be accessed directly")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())