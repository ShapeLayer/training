def compute(a: int, b: int, c: int, d: int) -> str:
    if c < 0 and d >= 10:
        return 'A storm warning for tomorrow! Be careful and stay home if possible!'
    elif c < a:
        return 'MCHS warns! Low temperature is expected tomorrow.'
    elif d > b:
        return 'MCHS warns! Strong wind is expected tomorrow.'
    else:
        return 'No message'

if __name__ == '__main__':
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(compute(a, b, c, d))
