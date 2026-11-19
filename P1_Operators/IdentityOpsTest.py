x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("x is z:", x is z) #True
print("x is y:", x is y) #False
print("x == y:", x == y) #True
print("x is not y:", x is not y) #True

#Membership Operators
print("apple in x:", "apple" in x) #True
print("cherry in x:", "cherry" in x) #False
print("apple not in x:", "apple" not in x) #False

text = "Hello World"
print("text:", text)
print("/"H/" in text:","H" in text) #True
print("/"hello/" in text:","hello" in text) #False
print("/"z/" not in text:","z" not in text) #True