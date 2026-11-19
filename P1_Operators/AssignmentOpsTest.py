x=10
print(x)
x=10
x += 3
print(x)
x=10
x-=2
print(x)
x=10
x*=3
print(x)
x=10
x//=3
print(x)
x=10
x%=3
print(x)
x=10
x**=3
print(x)
x=10
x/=2
print(x)
x=10
x&=3
print(x)
x=10
x|=3
print(x)
x=10
x>>=3
print(x)
x=10
x<<=1
print(x)
#assignment expression operator or warlus operator
print(x := 3)

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Ternary Operator
num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)