from sys import stdin
input = stdin.readline

def compute(n: int, gets: list[list[int]]):
    pos = 0
    prev_diff = sum([abs(each[0] - pos) * each[1] for each in gets])
    while True:
        l, r = 0, 0
        for x, a in gets:
            l += abs(x - (pos - 1)) * a
            r += abs(x - (pos + 1)) * a
        if prev_diff > l:
            pos -= 1
            prev_diff = l
        elif prev_diff > r:
            pos += 1
            prev_diff = r
        else:
            break
    return pos

if __name__ == '__main__':
    n = int(input())
    gets = [[*map(int, input().split())] for _i in range(n)]
    print(compute(n, gets))
