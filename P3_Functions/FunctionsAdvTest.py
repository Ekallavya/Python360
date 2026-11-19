x = 300  # Global

def myfunc():
    x = 200 #Local
    print(x) #200

myfunc()
print(x) #300

def myfunc1():
    global x
    x = 400
    print(x) # 400

myfunc1()
print(x) #400

## inner function
def myfunc3():
    x = 300
    def myinnerfunc():
        print(x)
        return x
    return 1000 + myinnerfunc()

y=myfunc3()
print(x) #400
print(y) #1300
# nonlocal
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1()) #hello