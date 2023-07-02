def compute(n: int, a: int, b: int) -> str:
    bus = a
    subway = b
    if bus > subway:
        return 'Subway'
    if bus < subway:
        return 'Bus'
    return 'Anything'

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
