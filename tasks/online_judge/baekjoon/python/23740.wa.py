from sys import stdin
input = stdin.readline

def compute(n: int, lines: list[tuple[int]]) -> list[tuple[int]]:
    result: list[tuple[int]] = []
    lines.sort(key=lambda x: (x[1], x[2]))
    min_cost, prev_start, prev_end = lines[0]
    for line in lines[1:]:
        cost, start, end = line
        if start > prev_end:
            result.append((min_cost, prev_start, prev_end))
            min_cost, prev_start, prev_end = cost, start, end
        else:
            prev_end = max(prev_end, end)
            min_cost = min(min_cost, cost)
    result.append((min_cost, prev_start, prev_end))
    return result

if __name__ == '__main__':
    n = int(input())
    lines: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    result = sorted(compute(n, lines))
    print(len(result))
    for each in result:
        print(*each)
