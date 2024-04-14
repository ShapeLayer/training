arr = list(map(int, input('수열을 입력하시오 : ').split()))
n = int(input('검색할 숫자를 입력하시오 : '))
arr.sort()

def bin_search(arr:list, target: int):
    index = len(arr)//2
    if arr[index] == target:
        return index
    if arr[index] > target:
        return bin_search(arr[0:index], target)
    elif arr[index] < target:
        return index + bin_search(arr[index:len(arr)], target) 
    else:
        return index
print('숫자 {}은 입력 수열 중 인덱스 {}에 위치함'.format(n, bin_search(arr, n)))