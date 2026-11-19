#unpacking tuple
fruits = ("apple", "banana", "cherry")
print(fruits[1])
## fruits[1]="mango" #TypeError: 'tuple' object does not support item assignment
(f1,f2,f3) = fruits
print(f1) # apple
print(f2) # banana
print(f3) # cherry

#If the number of variables is less than the number of values,
# we can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(f1,f2,*f3) = fruits

print(f1) # apple
print(f2) # banana
print(f3) # ['cherry', 'strawberry', 'raspberry']

(f1,*f2,f3) = fruits
print(f1) # apple
print(f2) #['banana', 'cherry', 'strawberry']
print(f3) #raspberry

(*f1,f2,f3) = fruits
print(f1) #['apple', 'banana', 'cherry']
print(f2) #strawberry
print(f3) #raspberry

#Loop tuple

for x in fruits:
    print(x)

fruits = fruits * 2
#('apple', 'banana', 'cherry', 'strawberry', 'raspberry', 'apple', 'banana', 'cherry', 'strawberry', 'raspberry')
print(fruits)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
#('a', 'b', 'c', 1, 2, 3)
print(tuple3)