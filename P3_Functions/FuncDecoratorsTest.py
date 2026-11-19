def changecase(func):
    def myinner():
        return func().upper()
    return myinner



@changecase
def myfunction1():
    return "Hello Sally"

@changecase
def myfunction2():
    return "I am speed!"
print(myfunction1()) # HELLO SALLY
print(myfunction2()) # I AM SPEED!

def changecase1(func):
    print("I am changing case1")
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase1
def myfunction3(nam):
    return "Hello "+nam
print(myfunction3("BOb")) # HELLO BOB


def changecase2(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase2
def myfunction4(nam):
    return "Hello " + nam

print(myfunction4("John" )) # HELLO JOHN


