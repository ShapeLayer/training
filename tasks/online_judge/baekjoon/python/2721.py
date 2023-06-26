def compute(n: int):
    buf = 0
    for k in range(1, n + 1):
        buf += k * sum(range(k + 2))
    return buf

if __name__ == '__main__':
    for _t in range(int(input())):
        n = int(input())
        print(compute(n))
