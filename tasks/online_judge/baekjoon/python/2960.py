def compute(n: int, k: int) -> int:
    cnt = 0
    is_prime = [True for _i in range(n + 1)]
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i, n + 1, i):
                if is_prime[j]:
                    is_prime[j] = False
                    cnt += 1
                    if cnt == k:
                        return j

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(compute(n, k))
