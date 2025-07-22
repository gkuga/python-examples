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
