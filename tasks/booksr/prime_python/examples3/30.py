print('1)덧셈    2)뺄셈    3)곱셈    4)나눗셈')
task = int(input('어떤 연산을 원하는지 번호를 입력하세요:'))
print('연산을 원하는 숫자 두개를 입력하세요')
a, b = [int(input()) for i in range(2)]
if task == 1:
    print('{} + {} = {}'.format(a, b, a+b))
elif task == 2:
    print('{} - {} = {}'.format(a, b, a-b))
elif task == 3:
    print('{} * {} = {}'.format(a, b, a*b))
elif task == 4:
    print('{} / {} = {}'.format(a, b, a/b))