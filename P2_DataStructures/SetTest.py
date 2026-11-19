mySet = {"apple", "banana", "cherry"}
print(mySet)

fSet = {"apple", "banana", "cherry", "apple"}

print(fSet) #{'banana', 'cherry', 'apple'}

#True and 1 is considered the same value:

fSet = {"apple", "banana", "cherry", True, 1, 2}

print(fSet) #{True, 2, 'banana', 'cherry', 'apple'}

#False and 0 is considered the same value:

fSet = {"apple", "banana", "cherry", False, True, 0}

print(fSet) #{False, 0, 'banana', 'cherry', 'apple'}

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = set1.union(set2).union(set3)
print(set4)

s1 = {"apple", "banana", "cherry"}
s1.add("Grape")
s2 = {"pineapple", "mango", "papaya"}
s1.update(s2)

print(s1) #{'papaya', 'cherry', 'apple', 'banana', 'pineapple', 'mango', 'Grape'}

l1 =["xxx","yyy","zzz"]
t1 =("aaa","bbb","ccc")
# update any iterable
s1.update(l1)
#{'mango', 'papaya', 'apple', 'yyy', 'xxx', 'pineapple', 'Grape', 'banana', 'cherry', 'zzz'}
print(s1)
#{'zzz', 'mango', 'cherry', 'banana', 'aaa', 'pineapple', 'xxx', 'yyy', 'papaya', 'bbb', 'Grape', 'apple', 'ccc'}
s1.update(t1)
print(s1)

s1.remove("xxx")
s1.discard("zzz")
s1.discard("kkk")
#s1.remove("kkk") # will throw exception
print(s1)

for x in s1:
    print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
print('-------------------------')
set4 = set1 | set2 | set3 |set4
print(set4)
set5 = set1.union(set2,set3,set4)
print(set5)