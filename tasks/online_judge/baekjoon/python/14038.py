def compute(gets: list[str]) -> int:
    counts = 0
    for get in gets:
        if get == 'W':
            counts += 1
    if counts >= 5:
        return 1
    if counts >= 3:
        return 2
    if counts >= 1:
        return 3
    return -1

if __name__ == '__main__':
    print(compute([input() for _i in range(6)]))
