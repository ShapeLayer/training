def compute(n: int, k: int, a: int) -> int:
    sums = 0
    for each in a:
        if each % 2 == 0:
            sums += each // 2
        else:
            sums += each // 2 + 1
    return sums - n

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    result = compute(n, k, a)
    if result >= 0:
        print('YES')
    else:
        print('NO')
