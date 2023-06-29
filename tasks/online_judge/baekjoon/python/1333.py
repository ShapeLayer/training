from sys import stdin
input = stdin.readline

def compute(n: int, l: int, d: int):
    total = n * l + (n - 1) * 5
    is_sound = [False for _i in range(total)]
    for i in range(0, total, l + 5):
        is_sound[i:i + l] = [True for _i in range(l)]

    for i in range(0, total, d):
        if not is_sound[i]:
            return i
    return i + d

if __name__ == '__main__':
    n, l, d = map(int, input().split())
    print(compute(n, l, d))
