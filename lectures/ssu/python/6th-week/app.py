print('세자리 정수 5개를 순차적으로 키보드로 입력하세요:')
arr = []
for _ in range(5):
    arr += [int(input())]
print('입력받은 값 = {}'.format(arr))
arr.sort()
print('정렬된 값 = {}'.format(arr))
filtered = []
for n in arr:
    print(n)
    if n // 100 == 5:
        filtered += [n]
print('500단위의 정수 개수 = {}개'.format(len(filtered)))
print('500단위의 정수 합 = {}'.format(sum(filtered)))
print('500단위의 정수 = {}'.format(filtered))