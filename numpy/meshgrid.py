import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5])

X, Y = np.meshgrid(x, y)

print("X:")
print(X)
print("Y:")
print(Y)