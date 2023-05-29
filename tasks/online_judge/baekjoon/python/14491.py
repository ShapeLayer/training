def compute(n: int, p: int) -> int:
    buf = []
    if n:
        buf += compute(n // p, p)
        buf.append(n % p)
    return buf

if __name__ == '__main__':
    n = int(input())
    print(''.join(map(str, compute(n, 9))))
