import numpy as np

# 例: RSSI履歴が4時刻・3台分ある場合
rssi_array = [
    [-70, -80, -75],  # 1st time
    [-72, -81, -76],  # 2nd time
    [-71, -79, -74],  # 3rd time
    [-71, -79, -74]   # 4rd time
]

# そのまま配列化
a = np.array(rssi_array)
print("a.shape:", a.shape)
print("a:", a)

# 2重にリストで囲んで2つ余分な次元を作る
b = np.array([[a]])
print("b.shape:", b.shape)
print("b:", b)

# squeezeで2つのサイズ1の次元を落とす
c = np.squeeze(b)
print("c.shape:", c.shape)
print("c:", c)

# flattenで全要素を1次元に並べる
c_flat = c.flatten()
print("c_flat.shape:", c_flat.shape)
print("c_flat:", c_flat)
