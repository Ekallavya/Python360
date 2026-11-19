"""A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.
"""
import camelcase
import random

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

print(random.randint(1, 10))