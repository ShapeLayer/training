# WIP
import numpy as np

a = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 2, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
], dtype=np.int32)

b = a[1:-1][1:-1]
c = a[0:3][0:3]

if __name__ == '__main__':
    print('배열 a:')
    print(a)
    # Result 1
    print('배열 b')
    print(b)
    # Result 2
    print('배열 c')
    print(c)