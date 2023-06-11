def compute(a: int, b: int):
    return (b - a + 1) * (a + b) // 2

if __name__ == '__main__':
    for i in range(int(input())):
        print(f'Scenario #{i + 1}:')
        print(compute(*map(int, input().split())))
        print()
