def compute(n: int):
    row, col = 0, 0
    while row * col < n:
        if row == col:
            row += 1
        else:
            col += 1
    return row, col

if __name__ == '__main__':
    n = int(input())
    print(*compute(n))
