import pandas as pd

# サンプルデータの作成
data = {
    '名前': ['田中', '佐藤', '鈴木', '高橋', '伊藤'],
    '年齢': [23, 35, 29, 41, 18],
    '得点': [88, 92, 75, 60, 95]
}
df = pd.DataFrame(data)

print('元のデータフレーム:')
print(df)

print('info:')
df.info()

# 年齢が30歳以上の行だけ抽出（ブールインデックス）
age_filter = df['年齢'] >= 30
print('age_filter:')
print(age_filter)
print('\n年齢が30歳以上の人:')
print(df[age_filter])

# 得点が90点以上の人だけ抽出
score_filter = df['得点'] >= 90
print('\n得点が90点以上の人:')
print(df[score_filter])

# 複数条件（年齢が30歳以上かつ得点が80点以上）
complex_filter = (df['年齢'] >= 30) & (df['得点'] >= 80)
print('\n年齢が30歳以上かつ得点が80点以上の人:')
print(df[complex_filter])
