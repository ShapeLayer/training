def compute(gets: list[list[str]]):
    gets.sort(key=lambda each: int(each[1]))
    return gets[0][0]

if __name__ == '__main__':
    gets = [input().split() for _i in range(int(input()))]
    print(compute(gets))
