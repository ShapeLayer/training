import numpy as np

# 1
a = np.arange(1, 11)
print('a =', a)

# 2
a = np.arange(10, 0, -1)
print('a =', a)

# 3
a = np.arange(1, 11).reshape(2, 5)
print(a)

# 4
a = a.reshape(5, 2)
print(a)