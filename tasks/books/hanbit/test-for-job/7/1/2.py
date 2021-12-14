# Binary Search
def process(arr: list, target: int, start: int, end: int):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    else:
        if arr[mid] > target:
            return process(arr, target, start, mid-1)
        elif arr[mid] < target:
            return process(arr, target, mid+1, end)
    
if __name__ == '__main__':
    n, target = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    res = process(arr, target, 0, n-1)
    print('{}'.format(res+1) if res else '원소가 존재하지 않습니다.')