import numpy as np

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
