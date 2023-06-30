def compute(gets: list[int]) -> int:
    return sum(sorted(gets)[1:])

if __name__ == '__main__':
    print(compute(list(map(int, input().split()))))
