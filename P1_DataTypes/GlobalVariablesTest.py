"""
Variables that are created outside a function  are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

x = "awesome"

def myfunc2():
    print("Python is " + x)

myfunc2()

def myfunc2():
    x = "fantastic"
    print("Python is " + x)

myfunc2()

print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)