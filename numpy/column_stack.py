import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.column_stack([a, b, np.zeros(a.size)])

print(result)
