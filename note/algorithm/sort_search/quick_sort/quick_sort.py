def quick_sort(arr):
    if len(arr) <= 1: # 만약 처리할 정렬이 아니면
        return arr # 그냥 반환 (처리할 정렬이면 처리 후 재귀 호출 => 이 조건에 걸릴때까지)
    pivot = arr[len(arr)//2] # 피벗 인덱스
    lesser_arr, equal_arr, greater_arr = [], [], []
    for n in arr:
        if pivot > n:
            lesser_arr += [n] # 피벗보다 작은 값을 lesser_arr에 추가
        elif pivot < n:
            greater_arr += [n] # 피벗보다 큰 값을 greater_arr에 추가
        else:
            equal_arr += [n] # 피벗과 같은 값은 equal_arr에 추가
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr) # equal_arr을 제외한 값들을 전부 재귀호출함

if __name__ == '__main__':
    print(quick_sort([3, 99, 6, 8, 9, 3, 5, 11, 16, 17]))