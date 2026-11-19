import pandas as pd

df = pd.read_json('data.json')

#print(df.to_string())

for index, row in df.iterrows():
    print(index, row)

print(df.head())

print(df.loc[0])

print(df.loc[20:40])

print("df.size:", df.size) #df.size: 676
print(df.head())
print(df.head(10))

print(df.tail())
print(df.head(20))

print("==================df.info()=======================================")
print(df.info())