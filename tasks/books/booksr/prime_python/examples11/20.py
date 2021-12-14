import numpy as np

a = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
b = np.array([16, 9, 3])
x, y, z = np.linalg.solve(a, b)
print('x = {}, y = {}, z = {}'.format(x, y, z))
