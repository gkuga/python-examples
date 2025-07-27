import numpy as np

# --- 1次元の重み付き平均サンプル ---
positions_1d = np.array([0, 10, 20])
weights_1d = np.array([1, 2, 3])
weighted_avg_1d = np.average(positions_1d, weights=weights_1d)
print("1次元の重み付き平均:", weighted_avg_1d)

print("-------------------")

# --- 2次元の重み付き平均サンプル（位置推定） ---
transmitter_positions = np.array([
    [0, 0],
    [10, 0],
    [0, 10],
    [10, 10]
])
rssi = np.array([-60, -70, -80, -65])
top_n = 3
indices = np.argsort(rssi)[::-1][:top_n]
top_rssi = rssi[indices]
top_positions = transmitter_positions[indices]
weights = 10 ** (top_rssi / 5)
x = np.average(top_positions[:, 0], weights=weights)
y = np.average(top_positions[:, 1], weights=weights)
estimated_position = (x, y)
print("2次元の重み付き平均による推定位置:", estimated_position)
