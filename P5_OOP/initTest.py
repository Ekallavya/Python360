class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
print(p1.name)
print(p1.age)
p1.greet()
# modify property
p1.age = 26
print(p1.age)


class Calculator:
    def func1(self, a, b):
        return a + b

    def func2(self, a, b):
        return a * b

calc = Calculator()
print(calc.func1(5, 3))
print(calc.func2(4, 7))