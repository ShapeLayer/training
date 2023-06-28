def compute(t: int, s: int) -> bool:
    return 12 <= t <= 16 and s == 0

if __name__ == '__main__':
    t, s = map(int, input().split())
    print(320 if compute(t, s) else 280)
