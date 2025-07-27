import numpy as np

# exp関数の基本例
# eはネイピア数（自然対数の底、約2.718）
x = 1
print(f"np.exp({x}) =", np.exp(x))  # e^1

# 配列に対してexpを使う
arr = np.array([0, 1, 2])
print("np.exp([0, 1, 2]) =", np.exp(arr))  # [e^0, e^1, e^2]

# 実用例：指数的増加
base = 2
powers = np.arange(5)
print(f"{base}のべき乗:", base ** powers)
print("np.exp(powers * np.log(base)) =", np.exp(powers * np.log(base)))  # 2^nと同じ