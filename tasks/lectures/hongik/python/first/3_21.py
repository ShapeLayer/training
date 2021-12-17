n = int(input('숫자를 입력하세요 : '))
m = 2
for m in range(2, n+1):
    if n%m == 0:
        if n == m:
            print('{}는 소수입니다'.format(n))
        else:
            print('{}는 소수가 아닙니다'.format(n))
            break