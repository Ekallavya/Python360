"""
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""

f = open("D:/save_text/PythonIntroduction.txt","rt")
print(f.read())
f.close()

f = open("D:/save_text/python_demo1.txt","w")
f.write("Hello, Python!")
f.close()

f = open("D:/save_text/python_demo1.txt","rt")
print(f.read())
f.close()

f = open("D:/save_text/python_demo1.txt","a")
f.write("Hello, Programmer ,how are you doing?!")
f.close()

f = open("D:/save_text/python_demo1.txt","rt")
print(f.read())
f.close()