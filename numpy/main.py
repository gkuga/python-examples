import numpy as np


"""
ndarray sample
"""

arr = np.array([5, 6, 7])
print(arr)
print(np.array([2, 4]) + np.array([2, 4]))
print(np.array([2, 4]) == np.array([2, 4]))

matrix = np.array([[75, 60, 82, 80], [90, 73, 75, 85], [82, 92, 80, 63]])
print(np.max(matrix, axis=0, keepdims=True))  # axis=0 は 縦軸, 1 は 横軸

# indexing
print(matrix[:, 1])
print(matrix[:2, 1:])
print(matrix[[0, 2], [1, 3]])
print(matrix[[[0], [2]], [[1], [3]]])

print(list(range(3, 10)))
print(np.arange(3, 10))

# 1次元のndarrayを作成
a = np.array([1, 2, 3])
print("1次元配列 a:")
print(a)
print("形状:", a.shape)
print("次元数:", a.ndim)

# 2次元のndarrayを作成
b = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2次元配列 b:")
print(b)
print("形状:", b.shape)
print("次元数:", b.ndim)

# 要素のアクセス
print("\nb[1, 2] の値（2行目3列目）:", b[1, 2])

# 配列の演算
print("\na + 10:")
print(a + 10)

print("\nb の転置:")
print(b.T)
