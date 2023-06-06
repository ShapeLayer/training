from sys import stdin
input = stdin.readline

def compute(n: int, arr: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(n):
        result.append(arr[i] * (n - i))
    return result

if __name__ == '__main__':
    for t in range(int(input())):
        gets: list[int] = list(map(int, input().split()))
        n, arr = gets[0], gets[1:]
        print(f'Case {t + 1}: {n - 1}', *compute(n, arr))
