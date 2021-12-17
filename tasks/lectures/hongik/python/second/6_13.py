arr = [5, 6, 3, 9, 2, 12, 3, 8, 7]
flag = [0, 0]
print('주어진 리스트는 = ', arr)
for j in range(len(arr), 0, -1):
    if (j - len(arr)) % 2 == 0:
        for i in range(1 + flag[0], j, 1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        flag[0] += 1
    else:
        for i in range(j, flag[1], -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        flag[1] += 1
print('정렬된 결과는 = ', arr)
