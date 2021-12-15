import numpy as np
n = int(input('n을 입력하시오: '))
a = np.eye(n, dtype=np.int32)
a *= [i for i in range(1, 1+n)]
print(a)