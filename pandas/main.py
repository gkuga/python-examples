import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ID': ['100', '101'],
    'City': ['Tokyo', 'Osaka'],
    'Birth_year': [1990, 1989],
    'Name': ['Hiroshi', 'Akiko'],
})

print("---df---")
print(df)
print("---df.values---")
print(df.values)
print("---df.index---")
print(df.index)
print("---df.columns---")
print(df.columns)
print(df["Birth_year"])
print(df.Birth_year)
print(df[["ID", "Birth_year"]])

print("---df.isnull()---")
print(df.isnull())

df2 = pd.DataFrame({
    'ID': ['200', '101'],
    'City': ['Tokyo', 'Osaka'],
    'Birth_year': [1990, 1989],
    'Name': ['Hiroshi', 'Akiko'],
    'XXX': ['AAA', 'BBB'],
})

print("---pd.merge(df, df2)---")
print(pd.merge(df, df2))

print("---pd.concat([df, df2])---")
print(pd.concat([df, df2], ignore_index=True))

print("---pd.concat([df, df2], axis=1)---")
print(pd.concat([df, df2], ignore_index=True, axis=1))


print('---df.drop([0])---')
print(df.drop([0]))

print('---df.drop(["Birth_year"], axis=1)---')
print(df.drop(["Birth_year"], axis=1))

df3 = pd.DataFrame([[1, 2.12], [3.356, 4.567]])
print('---df3---')
print(df3)

print('---df3.map(lambda x: len(str(x)))---')
print(df3.map(lambda x: len(str(x))))

print('---df.map(lambda x: len(str(x)))---')
df3["index 2 len"] = df3[1].map(lambda x: len(str(x)))
print(df3)

print('---pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)---')
print(pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3))
