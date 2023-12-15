from sys import stdin
input = stdin.readline
MAX = int(1e10)
MIN = -1
MOD = 1999

def compute(n: int, a: int, b: int):
    min_a, min_b = [[MAX for _j in range(2)] for _i in range(30)], [[MAX for _j in range(2)] for _i in range(30)]
    max_a, max_b = [[MIN for _j in range(2)] for _i in range(30)], [[MIN for _j in range(2)] for _i in range(30)]
    cnt_a, cnt_b = [0 for _i in range(30)], [0 for _i in range(30)]
    for i in range(n):
        for j in range(30):
            if(a[i] & (1 << j)):
                cnt_a[j] += 1
                min_a[j][1] = min(a[i] & ((1 << (j + 1)) - 1), min_a[j][1])
                max_a[j][1] = max(a[i] & ((1 << (j + 1)) - 1), max_a[j][1])
            else:
                min_a[j][0] = min(a[i] & ((1 << (j + 1)) - 1), min_a[j][0])
                max_a[j][0] = max(a[i] & ((1 << (j + 1)) - 1), max_a[j][0])
            if b[i] & 1 << j:
                cnt_b[j] += 1
                min_b[j][1] = min(b[i] & ((1 << (j + 1)) - 1), min_b[j][1])
                max_b[j][1] = max(b[i] & ((1 << (j + 1)) - 1), max_b[j][1])
            else:
                min_b[j][0] = min(b[i] & ((1 << (j + 1)) - 1), min_b[j][0])
                max_b[j][0] = max(b[i] & ((1 << (j + 1)) - 1), max_b[j][0])

    res_1 = 0
    for i in range(30):
        res_1 = (res_1 + 1 * cnt_a[i] % MOD * cnt_b[i] % MOD * (1 << i)) % MOD
    
    arr = [1 for _i in range(30)]
    p = 1
    for i in range(30):
        if min_a[i][0] != MAX and min_b[i][0] != MAX and ((min_a[i][0] + min_b[i][0]) & p) == 0:
            arr[i] = 0
        if min_a[i][1] != MAX and min_b[i][1] != MAX and ((min_a[i][1] + min_b[i][1]) & p) == 0:
            arr[i] = 0
        if max_a[i][1] != MIN and max_b[i][0] != MIN and ((max_a[i][1] + max_b[i][0]) & p) == 0:
            arr[i] = 0
        if max_a[i][0] != MIN and max_b[i][1] != MIN and ((max_a[i][0] + max_b[i][1]) & p) == 0:
            arr[i] = 0
        
        p <<= 1
    
    res_2 = 0
    cache = 1
    for i in range(30):
        if arr[i] != 0:
            res_2 += cache
        cache <<= 1
    
    return res_1, res_2

if __name__ == '__main__':
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    print(*compute(n, a, b))
