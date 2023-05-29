def compute(n: int) -> int:
    cnt = 0
    for i in range(1, n + 1):
        if '50' in str(i - 1):
            cnt += 1
        cnt += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
