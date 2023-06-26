from sys import stdin
input = stdin.readline

def compute(n: int, lines: list[tuple[int]]) -> int:
    lines.sort()
    start, end = lines[0]
    total = end - start
    for line in lines[1:]:
        new_start, new_end = line
        if end <= new_start:
            start, end = new_start, new_end
            total += end - start
        else:
            if end < new_end:
                total += new_end - end
                end = new_end
    return total

if __name__ == '__main__':
    n = int(input())
    lines: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(n, lines))
