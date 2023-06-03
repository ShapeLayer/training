def compute(a: int, b: int, c: int) -> str:
    if a == b and a == c:
        return '*'
    elif a != b and a != c and b == c:
        return 'A'
    elif a != b and b != c and a == c:
        return 'B'
    else:
        return 'C'

if __name__ == '__main__':
    print(compute(*(map(int, input().split()))))
