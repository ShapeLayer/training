def compute(n: int, events: list[str], submits: list[str]) -> tuple[int]:
    total = n * (n - 1) // 2
    now = 0
    real = {}
    for i in range(n):
        real[events[i]] = i
    for i in range(n):
        for j in range(i):
            before, after = submits[j], submits[i]
            if real[before] < real[after]:
                now += 1
    return (now, total)

if __name__ == '__main__':
    n = int(input())
    events = input().split()
    submits = input().split()
    print('{}/{}'.format(*compute(n, events, submits)))
