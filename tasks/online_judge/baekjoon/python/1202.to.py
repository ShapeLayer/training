from sys import stdin
input = stdin.readline

def compute(n: int, k: int, jewels: list[tuple[int]], bags: list[int]) -> int:
    result: int = 0
    jewels_offset: int = 0
    targets: list[tuple[int]] = []
    for i in range(k):
        for _j in range(n - jewels_offset):
            if jewels[0][0] <= bags[i]:
                targets.append(jewels.pop(0)[1])
                jewels_offset += 1
            else:
                break
        targets.sort()
        if targets:
            result += targets.pop()
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    jewels: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    bags: list[int] = [int(input()) for _i in range(k)]
    jewels.sort()
    bags.sort()
    print(compute(n, k, jewels, bags))
