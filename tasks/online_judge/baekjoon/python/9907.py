def compute(gets: str) -> str:
    chars = 'JABCDEFGHIZ'
    result = int(gets[0]) * 2
    for i in range(1, 7):
        result += int(gets[i]) * (8 - i)
    return chars[result % 11]

if __name__ == '__main__':
    gets = input()
    print(compute(gets))
