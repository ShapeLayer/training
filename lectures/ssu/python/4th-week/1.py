n = int(input())
for i in [2, 3, 5]:
    if n % i == 0:
        print('{}은 {}의 배수입니다.'.format(n, i))
    else:
        print('{}은 {}의 배수가 아닙니다.'.format(n, i))