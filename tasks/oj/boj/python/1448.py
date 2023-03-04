from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _i in range(n):
        arr += [int(input())]
    arr.sort()
    for i in range(n - 3, -1, -1):
        if arr[i + 2] < arr[i + 1] + arr[i]:
            print(sum(arr[i:i + 3]))
            break
        elif i == 0:
            print(-1)
