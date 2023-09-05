def compute(gets: str):
    a, b, c, d, p = map(gets.count, 'ABCD+')
    return (4 * a + 3 * b + 2 * c + 1 * d + .5 * p) / (len(gets) - p)

if __name__ == '__main__':
    print(compute(input()))
