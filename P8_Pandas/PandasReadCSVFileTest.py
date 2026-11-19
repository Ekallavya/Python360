import pandas as pd

df = pd.read_csv("data.csv")
#pd.options.display.max_rows = 50
#print(pd.options.display.max_rows)
print(df.to_string()) # entire data

print(df.loc[10: 20])