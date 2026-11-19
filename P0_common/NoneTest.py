"""
None is a special constant in Python that represents the absence of a value.
Its data type is NoneType, and None is the only instance of a NoneType object.
Variables can be assigned None to indicate "no value" or "not set".
"""

x = None
print(x) #None
print(type(x)) #<class 'NoneType'>

result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

result = 10

if result is not None:
    print("Result is ready")
else:
    print("No result yet")