dictionary1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = dictionary1["model"]
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])
## Add new item
dictionary1["color"] = "white"
dictionary1["owner"] = "Vijay"
dictionary1["Country"] = "Germany"

dictionary1.popitem()
dictionary1.pop("owner")
print(dictionary1)

print(dictionary1) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}
print(dictionary1.keys()) #dict_keys(['brand', 'model', 'year', 'color'])
print(dictionary1.values()) #dict_values(['Ford', 'Mustang', 1964, 'white'])
print(dictionary1.items()) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])

"""
brand Ford
model Mustang
year 1964
color white
"""
for key, value in dictionary1.items():
    print(key, value)

for key in dictionary1:
    print(key, dictionary1[key])

dictionary2 = {
    "brand": "Suzuki",
    "model": "Swift",
    "year": 3014
}
dictionary3 = {
    "brand": "RollsRoyce",
    "model": "Bond",
    "year": 1975
}

main_dictionary = {"car1": dictionary1, "car2": dictionary2, "car3": dictionary3}
print(main_dictionary)
print(main_dictionary["car1"]["brand"])
print(main_dictionary["car2"]["brand"])

for key,value in main_dictionary.items():
    print(key, main_dictionary[key])
    for key1 in value:
       print(key1, value[key1])


backup_dictionary =  main_dictionary.copy()
print(backup_dictionary)

card4 = {
    "brand": "TaTa",
    "model": "Indica",
    "year": 1974
}

x = card4.setdefault("color", "white")
print(x)
x = card4.setdefault("color", "Yellow")
print(x)
