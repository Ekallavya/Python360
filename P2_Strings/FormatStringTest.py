#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars" #59.00 dollars
print(txt)

price = 59.8978
txt = f"The price is {price:.2f} dollars" #59.90 dollars
print(txt)

#Perform a math operation in the placeholder, and return the result
txt = f"The price is {20 * 59} dollars" #1180 dollars
print(txt)