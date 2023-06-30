def compute(n: int, gets: list[tuple[int]]) -> list[tuple[int]]:
    return [(get[0] + get[1], get[0] * get[1]) for get in gets]

if __name__ == '__main__':
    for _t in range(int(input())):
        n = int(input())
        gets: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
        for each in compute(n, gets):
            print(*each)
