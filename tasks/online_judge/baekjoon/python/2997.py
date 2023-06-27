def compute(gets: list[int]) -> int:
    gets.sort()
    d = min(gets[1] - gets[0], gets[2] - gets[1])
    for each in gets:
        if each + d not in gets:
            if each + d <= 100:
                return each + d
    return gets[0] - d if gets[0] - d >= -100 else gets[2] + d

if __name__ == '__main__':
    gets: list[int] = list(map(int, input().split()))
    print(compute(gets))
