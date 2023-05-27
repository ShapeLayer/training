def compute(a: list[int], b: list[int]) -> str:
    result = 0
    for i in range(10):
        if a[i] > b[i]:
            result -= 1
        elif a[i] < b[i]:
            result += 1
    if result < 0:
        return 'A'
    elif result > 0:
        return 'B'
    else:
        return 'D'

if __name__ == '__main__':
    print(compute(list(map(int, input().split())), list(map(int, input().split()))))
