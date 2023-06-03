def compute(r: int, c: int) -> str:
    buf = ['*' * c for _i in range(r)]
    return '\n'.join(buf)

if __name__ == '__main__':
    r, c = int(input()), int(input())
    print(compute(r, c))
