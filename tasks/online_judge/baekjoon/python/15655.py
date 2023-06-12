def compute(n: int, m: int, gets: list[int]) -> list[list[int]]:
    buf: list[list[int]] = []
    def step(start: int, elapsed: int, values: list[int]):
        if elapsed == m:
            buf.append(values)
            return
        for i in range(start, n):
            step(i + 1, elapsed + 1, values + [i])
    step(0, 0, [])
    gets.sort()
    result: list[list[int]] = []
    for case in buf:
        each = [gets[i] for i in case]
        result.append(each)
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    gets = list(map(int, input().split()))
    for each in compute(n, m, gets):
        print(*each)
