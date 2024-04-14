arr = [5, 6, 3, 9, 2, 12, 3, 8, 7]
print('주어진 리스트는 = ', arr)
for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
print('가장 큰 수를 마지막으로 옮긴 결과 : ', arr)
