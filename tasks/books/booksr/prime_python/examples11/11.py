import numpy as np

a = np.array([0, 10, 20, 40, 60, 80], dtype=np.int32)
b = np.array([0, 20], dtype=np.int32)
c = np.array([True if i in b else False for i in a], dtype=np.bool)

print('a 배열:', a)
print('b 배열:', b)
print(c)