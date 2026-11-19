import os
os.remove("D:/save_text/python_demo1.txt")

print("File deleted successfully")
if os.path.exists("D:/save_text/python_demo1.txt"):
    os.remove("D:/save_text/python_demo1.txt")
else:
    print("The file does not exist")