def compute(nx: int, ny: int, w: float, xi: list[float], yi: list[float]) -> bool:
    xi.sort(reverse=True)
    yi.sort(reverse=True)

    pivot: float = 75
    for x in xi:
        if pivot - x > w / 2:
            break
        pivot = x - w / 2
    if pivot > 0:
        return False
    
    pivot: float = 100
    for y in yi:
        if pivot - y > w / 2:
            break
        pivot = y - w / 2
    if pivot > 0:
        return False

    return True

if __name__ == '__main__':
    while True:
        nx, ny, w = map(float, input().split())
        if nx == ny == w == 0:
            break
        nx, ny = int(nx), int(ny)
        xi: list[float] = list(map(float, input().split()))
        yi: list[float] = list(map(float, input().split()))
        if compute(nx, ny, w, xi, yi):
            print('YES')
        else:
            print('NO')
