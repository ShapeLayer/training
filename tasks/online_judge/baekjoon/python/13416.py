from sys import stdin
input = stdin.readline

def compute(t: int, costs: list[list[int]]) -> int:
    result = 0
    for cost in costs:
        if max(cost) >= 0:
            result += max(cost)
    return result

if __name__ == '__main__':
    c = int(input())
    for _i in range(c):
        t = int(input())
        costs = [list(map(int, input().split())) for _j in range(t)]
        print(compute(t, costs))
