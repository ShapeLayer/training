from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    arr = sorted([*map(int, input().split()), *map(int, input().split()), *map(int, input().split())], reverse=True)
    diff = 0
    for i in range(9):
        if i % 2 == 0:
            diff += arr[i]
        else:
            diff -= arr[i]
    print('Takahashi' if diff > 0 else 'Aoki')
