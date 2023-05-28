def compute(n: int) -> int:
    result = 0
    for i in range(1, n + 1):
        k = sum([int(c) for c in str(i)])
        if i % k == 0:
            result += 1
    return result

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
