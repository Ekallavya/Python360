thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
#Change the second and third value by replacing it with one value:
thislist[1:3] = ["Pineapple"]
print(thislist) # ['apple', 'Pineapple', 'orange', 'kiwi', 'mango']
thislist.insert(2, "Grapes")
print(thislist) # ['apple', 'Pineapple', 'Grapes', 'orange', 'kiwi', 'mango']
thislist.append("WoodApple")
print(thislist) #['apple', 'Pineapple', 'Grapes', 'orange', 'kiwi', 'mango', 'WoodApple']
#To append elements from another list to the current list, use the extend() method.
tropical = ["xxx", "yyy", "zzz"]
thislist.extend(tropical)
print(thislist)  #['apple', 'Pineapple', 'Grapes', 'orange', 'kiwi', 'mango', 'WoodApple', 'xxx', 'yyy', 'zzz']
#Add Any Iterable
thistuple = ("aaa", "bbb")
thislist.extend(thistuple)
print(thislist) #['apple', 'Pineapple', 'Grapes', 'orange', 'kiwi', 'mango', 'WoodApple', 'xxx', 'yyy', 'zzz', 'aaa', 'bbb']

print(thislist.index("kiwi")) # 4