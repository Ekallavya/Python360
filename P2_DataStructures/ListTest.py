#List items are indexed
# we can access them by referring to the index number:

#Print the second item of the list:
fruitList= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruitList[1]) #banana
#Negative Indexing ,Negative indexing means start from the end
print(fruitList[-1]) #mango
#Range of Indexes
print(fruitList[2:5]) #['cherry', 'orange', 'kiwi']


#By leaving out the start value, the range will start at the first item:
print(fruitList[:4]) #['apple', 'banana', 'cherry', 'orange']
print(fruitList[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
print(fruitList[-4:-1]) #['orange', 'kiwi', 'melon']