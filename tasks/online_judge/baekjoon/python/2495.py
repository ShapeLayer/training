def compute(n: int) -> int:
    prev, result, now = -1, 1, 1
    while True:
        ends: int = n % 10
        n //= 10
        if prev == ends:
            now += 1
        else:
            if result < now:
                result = now
            now = 1
            prev = ends
        if n == 0:
            break
    if result < now:
        result = now
    return result

if __name__ == '__main__':
    for t in range(3):
        print(compute(int(input())))
