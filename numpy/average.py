import numpy as np

# 仮のRSSI値（3つの送信機）
rssi = np.array([-70, -80, -75])

# 送信機の座標（x, y）
p_DRx = np.array([
    [0, 0],   # 送信機1
    [10, 0],  # 送信機2
    [5, 10]   # 送信機3
])

ref_DRx = 2  # 上位2つの受信機を使う

# 1. RSSI値が大きい順にインデックスを取得
print("np.argsort(rssi):", np.argsort(rssi))
srtIndex = np.argsort(rssi)[::-1]
print("srtIndex:", srtIndex)  # [0, 2, 1]

# 2. 上位ref_DRx個のRSSI値を取得
srtRSSI = rssi[srtIndex[0:ref_DRx]]
print("srtRSSI:", srtRSSI)  # [-70, -75]

# 3. 重みを計算
w = 10 ** (srtRSSI / 5)
print("weights:", w)  # [0.01, 0.000316...]

# 4. 上位受信機の座標を重み付き平均
x = np.average(p_DRx[srtIndex[0:ref_DRx], 0], weights=w)
y = np.average(p_DRx[srtIndex[0:ref_DRx], 1], weights=w)
print("推定位置: x =", x, ", y =", y)
