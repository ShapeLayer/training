def compute(n: int) -> str:
    _sum = sum([i if n % i == 0 else 0 for i in range(1, n)])
    if _sum == n:
        return f'{n} is a perfect number.'
    elif _sum < n:
        return f'{n} is a deficient number.'
    else:
        return f'{n} is an abundant number.'

if __name__ == '__main__':
    for i in range(int(input())):
        if i != 0:
            print()
        n = int(input())
        print(compute(n))
