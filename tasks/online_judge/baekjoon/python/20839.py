def compute(x: int, y: int, z: int, a: int, b: int, c: int) -> int:
    if x <= a and y <= b and z <= c:
        return 0
    if x / 2 <= a and y <= b and z <= c:
        return 1
    if y <= b and z <= c:
        return 2
    if y / 2 <= b and z <= c:
        return 3
    return 4

if __name__ == '__main__':
    print('ABCDE'[compute(*map(int, input().split()), *map(int, input().split()))])
