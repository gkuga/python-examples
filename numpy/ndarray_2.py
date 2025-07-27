import numpy as np

# 例: 5時刻分×3送信機のRSSI履歴
rssi_table = np.array([
    [-70, -80, -75],  # 1st time
    [-72, -81, -76],  # 2nd time
    [-71, -79, -74],  # 3rd time
    [-69, -78, -73],  # 4th time
    [-68, -77, -72],  # 5th time 最新値
])
print("rssi_table:\n", rssi_table)

t = 3  # 直近3時刻分で最大値を取りたい

# 直近t個分の履歴を抜き出す
# -t: は「後ろからt行分」
# :   は「全ての列」
# つまり「最後のt行・全列」を抜き出す（1次元配列の[-t:]と同じ感覚）
window = rssi_table[-t:, :]
print("window:\n", window)

# 各送信機ごとに最大値を計算
max_rssi = np.max(window, axis=0)
print("max_rssi:", max_rssi)
