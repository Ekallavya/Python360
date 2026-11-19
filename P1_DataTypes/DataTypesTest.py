"""
#Built-in Data Types
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# We can get the data type of any object by using the type() function:
x = 5
print(type(x)) #<class 'int'>
#Examples
x = "Hello World"	#str
x = 20	#int
x = 20.5	#float
x = 1j	#complex
x = ["apple", "banana", "cherry"]	#list
x = ("apple", "banana", "cherry")	#tuple
x = range(6)	#range
x = {"name" : "John", "age" : 36}	#dict
x = {"apple", "banana", "cherry"}	#set
x = frozenset({"apple", "banana", "cherry"})	#frozenset
x = True	#bool
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryview
x = None	#NoneType

# If we  want to specify the data type, you can use the following constructor functions:
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(["apple", "banana", "cherry"])
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict({"name" : "John", "age" : 36})
x = set({"apple", "banana", "cherry"})
x = frozenset({"apple", "banana", "cherry"})
x = bool(True)
x = bytes(b"Hello")	
x = bytearray(5)
x = memoryview(bytes(5))
x = None
