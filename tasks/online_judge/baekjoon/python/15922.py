from sys import stdin
input = stdin.readline

def compute(n: int, lines: list[tuple[int]]) -> int:
    total = 0
    prev_start, prev_end = -2_000_000_000, -2_000_000_000
    lines.sort()
    for line in lines:
        start, end = line
        if prev_end < start:
            total += end - start
            prev_start, prev_end = start, end
        else:
            if prev_end < end:
                total += end - prev_end
                prev_start, prev_end = start, end
    return total

if __name__ == '__main__':
    n = int(input())
    lines: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(n, lines))
