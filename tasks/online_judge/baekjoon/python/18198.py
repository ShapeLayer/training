def compute(gets: str) -> int:
    a, b = 0, 0
    for i in range(0, len(gets), 2):
        if gets[i] == 'A':
            a += int(gets[i + 1])
        elif gets[i] == 'B':
            b += int(gets[i + 1])
    return a, b

if __name__ == '__main__':
    a, b = compute(input())
    print('A' if a > b else 'B')
