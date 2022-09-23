import numpy as np

ar = np.array([
    [1, 2, 3],
    [3, 2 ,5],
    [3, 4, 5]
])

rows, columns = np.where((ar == (1, 2, 3)).all(axis=1))
print(rows)