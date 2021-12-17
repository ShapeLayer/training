n = int(input('피보나치 수열의 입력값 n을 입력하세요: '))
def F(n):
    f = [1, 1]
    for i in range(n-1):
        nf = f[0] + f[1]
        f = [f[1], nf]
    return f[1]
print('F({}) = {}'.format(n, F(n)))