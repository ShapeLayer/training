def binary_search(arr, target):
    # 리스트는 오름차순으로 정리되어있어야함
    if len(arr) == 0: # 리스트 길이가 0이면 False 반환 후 종료
        return False
    bench = len(arr)//2
    smaller_arr = []
    if arr[bench] > target:
        smaller_arr = arr[0:bench-1]
    elif arr[bench] < target:
        smaller_arr = arr[bench+1:len(arr)]
    else:
        return True # arr[bench] == target 이면 True 반환 후 종료
    return binary_search(smaller_arr, target)

if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))