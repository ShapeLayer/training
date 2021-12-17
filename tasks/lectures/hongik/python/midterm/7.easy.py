def binary_sum(a, b):
    if len(a) != len(b):
        return 0
    leng = len(a)
    for val in list(a)+list(b):
        if ord(val) != 48 and ord(val) != 49:
            return 1
    arr = list(reversed(list(map(int, a))))
    for i in range(leng):
        arr[i] += int(b[leng-i-1])
        while arr[i] > 1:
            arr[i] -= 2
            if i == leng-1:
                arr += [1]
            else:
                arr[i+1] += 1
    result = ''
    for i in range(len(arr)-1, -1, -1):
        result += str(arr[i])
    return result

a, b = input('2진수를 2개 입력하세요 : ').split()
res = binary_sum(a, b)
if res == 0:
    print('두 수의 자릿수가 다릅니다.')
elif res == 1:
    print('입력값이 2진수가 아닙니다.')
else:
    print('두 이진수의 합은: {}'.format(res))