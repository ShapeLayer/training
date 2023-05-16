from sys import stdin
input = stdin.readline

def compute(n: int, vals: list[tuple[int]]) -> int:
    prev, result = 0, 0
    for val in vals:
        speed, time = val
        result += speed * (time - prev)
        prev = time
    return result

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == -1:
            break
        vals = [tuple(map(int, input().split())) for _i in range(n)]
        print(f'{compute(n, vals)} miles')
