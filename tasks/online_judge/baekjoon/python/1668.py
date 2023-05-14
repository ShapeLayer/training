from sys import stdin
input = stdin.readline

def compute(n: int, trophies: list[int]) -> tuple[int]:
    l, r, l_max, r_max = 0, 0, -1, -1
    for i in range(n):
        if trophies[i] > l_max:
            l_max = trophies[i]
            l += 1
    for i in range(n - 1, -1, -1):
        if trophies[i] > r_max:
            r_max = trophies[i]
            r += 1
    return (l, r)

if __name__ == '__main__':
    n = int(input())
    trophies: list[int] = []
    for _i in range(n):
        trophies.append(int(input()))
    l, r = compute(n, trophies)
    print(l)
    print(r)
