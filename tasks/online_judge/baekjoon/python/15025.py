def compute(a: int, b: int) -> str:
    if a == b == 0:
        return 'Not a moose'
    elif a != b:
        return f'Odd {max(a, b) * 2}'
    elif a == b:
        return f'Even {b * 2}'

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
