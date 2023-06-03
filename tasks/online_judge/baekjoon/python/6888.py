def compute(x: int, y: int) -> list[int]:
    buf: list[int] = []
    while x <= y:
        buf.append(x)
        x += 60
    return buf

if __name__ == '__main__':
    x, y = int(input()), int(input())
    for year in compute(x, y):
        print(f'All positions change in year {year}')
