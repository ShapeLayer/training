def leap_1(start: int, end: int) -> list[int]:
    return list(filter(lambda year: year if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else None, [i for i in range(start, end+1)]))

def leap_2(start: int, end: int) -> list[int]:
    return [year for year in range(start, end+1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

if __name__ == '__main__':
    print('2001년부터 2030년 사이의 윤년:', leap_1(2001, 2030))
    print('2001년부터 2030년 사이의 윤년:', leap_2(2001, 2030))