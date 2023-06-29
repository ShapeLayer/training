def compute(n: int) -> int:
    result = 0
    for i in range(n):
        result += (n - i) ** 2
    return result

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        print(compute(n))
