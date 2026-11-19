# file exist   in same location
f = open("demofile.txt")
print(f.read())
#using with statement
with open("demofile.txt") as f:
    print(f.read())
f.close()
# file exist   in different location
f = open("D:/save_text/PythonIntroduction.txt")
print(f.read())
f.close()