from sys import stdin, setrecursionlimit

setrecursionlimit(10000)

n = int(stdin.readline())
arr = []
for i in range(n):
    arr += [int(stdin.readline())]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for n in arr:
        if pivot > n:
            lesser_arr += [n]
        elif pivot < n:
            greater_arr += [n]
        else:
            equal_arr += [n]
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

arr = quick_sort(arr)
for i in arr:
    print(i)