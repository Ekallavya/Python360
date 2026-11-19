"""
frozenset is an immutable version of a set.
Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset.
"""

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b)) #frozenset({1, 2})
print(a - b) #frozenset({1, 2})

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b)) #frozenset({3, 4})
print(a & b) #frozenset({3, 4})
# check commonality
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b)) # True
print(a.isdisjoint(c)) # False

a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b)) # True
print(a <= b) # True
print(a < b) # True

a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b)) # True
print(a >= b) # True
print(a > b) # True
#Returns a new frozenset with the symmetric differences
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b)) # frozenset({1, 2, 4, 5})
print(a ^ b) # frozenset({1, 2, 4, 5})

#Returns a new frozenset containing the union
a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b)) # frozenset({1, 2, 3})
print(a | b) # frozenset({1, 2, 3})
