import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
"""
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
"""

print(pd.__version__) #3.0.6
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
"""
   calories  duration
0       420        50
1       380        40
2       390        45
"""

print(df.loc[0])
# calories    420
# duration     50
# Name: 0, dtype: int64

print(df.loc[[0, 1]])
"""
   calories  duration
0       420        50
1       380        40
"""

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
"""
   calories  duration
day1       420        50
day2       380        40
day3       390        45
"""

print(df.loc["day2"])

"""
calories    380
duration     40
Name: day2, dtype: int64
"""