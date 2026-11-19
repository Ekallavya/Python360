"""
Data cleaning means fixing bad data in your data set.
Bad data could be:
        Empty cells
        Data in wrong format
        Wrong data
        Duplicates
"""
import pandas as pd

df = pd.read_csv('dataset.csv')

new_df = df.dropna()

print(new_df.to_string())

print("new_df.size:", new_df.size)

#print(new_df.duplicated())
#Remove all rows with NULL values:
new_df.dropna(inplace = True)
#Replace NULL values with the number 130:
new_df.fillna(130, inplace = True)
#Replace NULL values in the "Calories" columns with the number 130:
df.fillna({"Calories": 130}, inplace=True)

#Calculate the MEAN, and replace any empty values with it:
df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)
#Calculate the MEDIAN, and replace any empty values with it
x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)
#Calculate the MODE, and replace any empty values with it
x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

#Remove rows with a NULL value in the "Date" column:
#df.dropna(subset=["Date"], inplace=True)

#Set "Duration" = 45 in row 7:
df.loc[7, "Duration"] = 45

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# drop rows
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)

#To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace=True)

print("df.size:", df.size)