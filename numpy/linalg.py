import numpy as np

"""
ベクトルの「長さ」（ノルム）は、いくつかの定義があります。
代表的なものは次の3つです：

ユークリッドノルム（2-ノルム）：通常の距離（√(x²+y²+...)）
1-ノルム：各要素の絶対値の合計
無限大ノルム：要素の絶対値の最大値
1-ノルムと無限大ノルムは、特定の状況で便利です。
"""

# ベクトルのノルム（長さ）を計算
vec = np.array([3, 4])
norm_vec = np.linalg.norm(vec)
print("ベクトル:", vec)
print("ベクトルのノルム（長さ）:", norm_vec)

# 行列のノルム（デフォルトはFrobeniusノルム）
mat = np.array([[1, 2], [3, 4]])
norm_mat = np.linalg.norm(mat)
print("行列:\n", mat)
print("行列のノルム（Frobeniusノルム）:", norm_mat)

# 他のノルム（例: 1-ノルム, 無限大ノルム）
norm_1 = np.linalg.norm(vec, ord=1)
norm_inf = np.linalg.norm(vec, ord=np.inf)
print("1-ノルム:", norm_1)
print("無限大ノルム:", norm_inf)

print("ベクトルの差のノルム:", np.linalg.norm(np.array([1, 2]) - np.array([4, 6])))

print('-' * 20)

############################################
# グリッド点と基準点の距離を計算する例
############################################


# 1次元空間のグリッド点（例：4点）
grid_points_1d = np.array([
    [0],
    [1],
    [2],
    [3]
])

# 基準点（送信機の座標）
ptx_x = np.array([1.5])

# 各グリッド点と基準点の距離（絶対値）を一括計算
distances = np.linalg.norm(grid_points_1d - ptx_x, axis=1)

print(distances)
# 出力例: [1.5 0.5 0.5 1.5]

print('-' * 20)

# 2次元空間のグリッド点（例：4点）
grid_points_2d = np.array([
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
])

# 基準点（送信機の座標）
ptx_xy = np.array([1, 1])

# 各グリッド点と基準点のユークリッド距離を一括計算
distances = np.linalg.norm(grid_points_2d - ptx_xy, axis=1)

print(distances)
# 出力例: [1.41421356 1.         1.         0.        ]

print('-' * 20)

# 3次元空間のグリッド点（例：4点）
grid_points_3d = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# 基準点
ptx_xyz = np.array([1, 1, 1])

# 各グリッド点と基準点のユークリッド距離を一括計算
distances = np.linalg.norm(grid_points_3d - ptx_xyz, axis=1)

print(distances)
