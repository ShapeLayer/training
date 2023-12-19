def compute(n: int) -> bool:
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while True:
        if i * i > n:
            break
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    n = int(input())
    input()
    print('Yes' if compute(n) else 'No')
