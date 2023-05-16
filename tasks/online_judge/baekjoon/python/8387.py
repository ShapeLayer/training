def compute(n: int, t1: str, t2: str) -> int:
    count = 0
    for i in range(n):
        if t1[i] != t2[i]:
            count += 1
    return n - count

if __name__ == '__main__':
    n = int(input())
    t1, t2 = input(), input()
    print(compute(n, t1, t2))
