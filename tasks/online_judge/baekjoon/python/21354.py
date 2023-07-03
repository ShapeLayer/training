def compute(a: int, b: int) -> str:
    y, z = a * 7, b * 13
    if y > z:
        return 'Axel'
    if y < z:
        return 'Petra'
    return 'lika'

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
