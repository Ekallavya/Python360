"""
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
"""

def my_function():
    print("Hello from a function")

my_function()

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77)) #25.0
print(fahrenheit_to_celsius(95)) #35.0
print(fahrenheit_to_celsius(50)) #10.0

"""
Arbitrary Arguments - *args
If we do not know how many arguments will be passed into a function ,then we use arbitrary arguments
"""

def my_function(*args):
    print("The youngest child is " + args[2]) #The youngest child is Linus
    #print("The youngest child is " + args[5]) # IndexError: tuple index out of range

my_function("Emil", "Tobias", "Linus")

"""
The **kwargs parameter allows a function to accept any number of keyword arguments.
Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
"""

def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")