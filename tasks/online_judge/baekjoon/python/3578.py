def compute(n: int):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n % 2 == 0:
        return int('8' * (n // 2))
    return int('4' + '8' * (n // 2))

if __name__ == '__main__':
    print(compute(int(input())))
