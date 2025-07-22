import numpy as np

# 0から5まで1刻み
a = np.arange(0, 5, 1)
print(a)  # [0 1 2 3 4]

# 0から10まで2刻み
b = np.arange(0, 10, 2)
print(b)  # [0 2 4 6 8]

# 1.5から5.5まで0.5刻み
c = np.arange(1.5, 5.5, 0.5)
print(c)  # [1.5 2.  2.5 3.  3.5 4.  4.5 5. ]

# 終了値を含めたい場合は stop+step まで指定
d = np.arange(0, 5 + 1, 1)
print(d)  # [0 1 2 3 4 5]
