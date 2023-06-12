def compute(n: int, m: int) -> list[list[int]]:
    buf: list[list[int]] = []
    def step(elapsed: int, values: list[int]):
        if elapsed == m:
            buf.append(values)
            return
        for i in range(1, n + 1):
            if i not in values:
                step(elapsed + 1, values + [i])
    step(0, [])
    return buf

if __name__ == '__main__':
    n, m = map(int, input().split())
    for each in compute(n, m):
        print(*each)
