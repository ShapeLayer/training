from math import pi

def compute(d: float, r: float, t: float) -> tuple[float]:
    distance = d / 63360 * pi * r
    mph = distance / t * 3600
    return distance, mph

if __name__ == '__main__':
    loops = 0
    while True:
        loops += 1
        d, r, t = map(float, input().split())
        if r == 0:
            break
        distance, mph = compute(d, r, t)
        print(f'Trip #{loops}:', '%.2f' % distance, '%.2f' % mph)