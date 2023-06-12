from sys import stdin
input = stdin.readline

def compute(n: int, remains: list[int]) -> int:
    cnt = 0
    for remain in remains:
        if remain <= 90:
            cnt += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    remains: list[int] = [int(input()[2:]) for _i in range(n)]
    print(compute(n, remains))
