import numpy as np
n = int(input('n을 입력하시오: '))
a = np.ones((n, n), dtype=np.int32)
b = np.array(a)
b[1:-1, 1:-1] = 0
b = a - b

if __name__ == '__main__':
    print('a 행렬')
    print(a)
    print('b 행렬')
    print(b)