def compute(a: int, b: int, c: int) -> bool:
    return a == b or \
        b == c or \
        a + b == c

if __name__ == '__main__':
    print('S' if compute(*sorted(map(int, input().split()))) else 'N')
