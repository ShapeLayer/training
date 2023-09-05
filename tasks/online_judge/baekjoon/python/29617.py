def compute(a: int, b: int, k: int) -> int:
    if a + b == 1 and k < 0:
        return 2
    elif a == 1 and b == 1 and k < 0:
        return 1
    elif a == b and k == -1:
        return 1
    elif a == b:
        return 2
    else:
        return 1

if __name__ == '__main__':
    a, b, k = map(int, input().split())
    print(['', 'First', 'Second'][compute(a, b, k)])
