def compute(n: int) -> str:
    buf: list[str] = []
    for i in range(1, n + 1):
        buf.append(str(i))
        if i % 6 == 0 or i == n:
            buf.append('Go!')
    return ' '.join(buf)

if __name__ == '__main__':
    print(compute(int(input())))
