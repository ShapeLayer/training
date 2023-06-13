def compute(n: int, m: int, gets: list[int]) -> list[list[int]]:
    buf: list[tuple[int]] = []
    gets.sort()
    def step(start: int, elapsed: int, values: list[int]):
        if elapsed == m:
            buf.append(tuple([gets[i] for i in values]))
            return
        for i in range(start, n):
            step(i + 1, elapsed + 1, values + [i])
    step(0, 0, [])

    result: list[tuple[int]] = []
    prev = [-1]
    for each in sorted(buf):
        if prev != each:
            result.append(each)
            prev = each
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    gets = list(map(int, input().split()))
    for each in compute(n, m, gets):
        print(*each)
