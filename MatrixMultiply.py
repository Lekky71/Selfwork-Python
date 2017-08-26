import numpy as np

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
n = a.__len__()
c = np.empty((n, n))
for i in range(0, n):
    for j in range(0, n):
        c[i][j] = 0
        for k in range(0, n):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]
print c


