#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
print(a.lower())

#Replace String
print(a.replace("H", "J"))

#Split String
print(a.split(","))
# Remove white spaces
a = "  Hello, World!       "
print(a.strip()) # returns "Hello, World!"

a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)