import pandas as pd

df = pd.read_csv("./data.csv")

print("df")
print(df)
print(df.info())
print(df.describe())

print('df.loc[:, ["ID", "Birth_year"]]')
print(df.loc[:, ["ID", "Birth_year"]])

print('df["City"] == "Tokyo"')
print(df["City"] == "Tokyo")

print('df[df["City"] == "Tokyo"]')
print(df[df["City"] == "Tokyo"])

print('df.sort_values("ID", ascending=False)')
print(df.sort_values("ID", ascending=False))
