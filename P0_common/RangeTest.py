#The built-in range() function returns an immutable sequence of numbers,
# commonly used for looping a specific number of times
#range(start, stop, step)
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(range(1, 6))) #[1, 2, 3, 4, 5]
print(list(range(5, 20, 3))) #[5, 8, 11, 14, 17]

for i in range(10):
    print(i,end=" ") #0 1 2 3 4 5 6 7 8 9


list =["Apple","Pineapple","Banana","Grape","Kiwi","WoodApple","Orange","Papaya"]

for i in range(len(list)):
    print(list[i],end="-") #Apple-Pineapple-Banana-Grape-Kiwi-WoodApple-Orange-Papaya-
