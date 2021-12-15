import numpy as np

n = int(input('n을 입력하시오: '))
a = np.array([[i%2 for i in range(j%2, j%2+n)] for j in range(1, 1+n)], dtype=np.int32)
print(a)