def compute(n: int) -> str:
    result = []
    for i in range(1, n + 1):
        row = []
        if i == 1 or i == n:
            for _j in range(n - i):
                row.append(' ')
            for _j in range(2 * i - 1):
                row.append('*')
        else:
            for _j in range(n - i):
                row.append(' ')
            row.append('*')
            for _j in range(2 * (i - 1) - 1):
                row.append(' ')
            row.append('*')
        result.append(''.join(row))
    return '\n'.join(result)

if __name__ == '__main__':
    print(compute(int(input())))
