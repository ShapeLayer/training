from sys import stdin
input = stdin.readline

def compute(n: int, arr: list[int]) -> list[list[int]]:
    buf = []
    arr.sort()
    def step(elapsed: int, start: int, values: list[int]):
        if elapsed == 6:
            buf.append(values)
            return
        for i in range(start, n):
            step(elapsed + 1, i + 1, values + [i])
    step(0, 0, [])
    result = []
    for case in buf:
        result.append([arr[i] for i in case])
    return result

if __name__ == '__main__':
    while True:
        gets = list(map(int, input().split()))
        if gets[0] == 0:
            break
        for each in compute(gets[0], gets[1:]):
            print(*each)
        print()
