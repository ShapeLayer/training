def compute(n: int, t: int, c: int, p: int):
    return (n - 1) // t * c * p

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
