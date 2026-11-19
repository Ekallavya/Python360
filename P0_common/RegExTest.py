#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
import re

#Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #
print(x) #<re.Match object; span=(0, 17), match='The rain in Spain'>
print(x.__getitem__(0)) #The rain in Spain