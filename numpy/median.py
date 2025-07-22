import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# axis=0で各列の中央値を計算
median_col = np.median(arr, axis=0)
median_row = np.median(arr, axis=1)

print("元の配列:")
print(arr)
print("各列の中央値:")
print(median_col)
print("各行の中央値:")
print(median_row)