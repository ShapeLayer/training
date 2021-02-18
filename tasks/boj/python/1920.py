from sys import stdin

def binary_search(arr, target):
    if len(arr) == 0:
        return 0
    bench = len(arr)//2
    smaller_arr = []
    if arr[bench] > target:
        smaller_arr = arr[0:bench-1]
    elif arr[bench] < target:
        smaller_arr = arr[bench+1:len(arr)]
    else:
        return 1
    return binary_search(smaller_arr, target)

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))
a.sort()

for i in b:
    print(binary_search(a, i))