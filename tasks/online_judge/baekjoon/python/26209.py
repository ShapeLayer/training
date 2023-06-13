def compute(arr: list[int]) -> bool:
    for each in arr:
        if not (each == 0 or each == 1):
            return False
    return True

if __name__ == '__main__':
    print('S' if compute(list(map(int, input().split()))) else 'F')
