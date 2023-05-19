from sys import stdin
input = stdin.readline

def compute(n: int, c: int, cycles: list[int]) -> int:
    count: int = 0
    for i in range(1, c + 1):
        for cycle in cycles:
            if i % cycle == 0:
                count += 1
                break
    return count

if __name__ == '__main__':
    n, c = map(int, input().split())
    cycles: list[int] = [int(input()) for _i in range(n)]
    print(compute(n, c, cycles))
