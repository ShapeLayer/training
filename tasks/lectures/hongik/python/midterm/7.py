def binary_sum(a, b):
    if len(a) != len(b):
        raise ValueError('두 수의 자릿수가 다릅니다.')
    leng = len(a)
    for val in list(a)+list(b):
        if ord(val) != 48 and ord(val) != 49:
            raise ValueError('입력값이 2진수가 아닙니다.')
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
try:
    print('두 이진수의 합은: {}'.format(binary_sum(a, b)))
except ValueError as e:
    print(e)