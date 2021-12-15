import numpy as np

n = int(input('n을 입력하시오: '))
a = np.ones((n, n), dtype=np.int32)
b = a
b[1:-1, 1:-1] = 0

if __name__ == '__main__':
    print('a 행렬')
    print(a)
    print(b)