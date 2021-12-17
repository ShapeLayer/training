# 1번 문제
li = [1, 3, 5, 7, 9]
n = 0
for i in li:
    n += i
    print(i, n)

# 2번 문제
li = ['국어', '영어', '수학', '과학', '한국사']
for i in li:
    print(i, end=' ')

## 2번 제시한 방법 외 방법
from sys import stdout
for i in li:
    stdout.write(i + ' ')

# 3번 문제
name = ['홍길동', '임꺽정']
subject = ['국어', '영어', '수학']

for name_obj in name:
    for sub_obj in subject:
        print(name_obj, sub_obj)

# 4번 문제
n = 0
for i in range(1, 101):
    n += i
print(n)

# 5번 문제
o = 0
e = 0
for i in range(1, 101):
    if i % 2 == 1:
        o += i
    else:
        e += i
print('홀수 합 : {}'.format(o))
print('짝수 합 : {}'.format(e))

# 6번 문제
for i in range(3, -4, -1):
    print(i, end=' ')
print('')

# 7번 문제
for i in range(1, 6):
    for i in range(1, 5):
        print('*', end='')
    print('')

# 8번 문제
for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')
    print('')

# 9번 문제
n = 0
while True:
    i = int(input('정수 : '))
    n += i
    if i == 0:
        break
print('합 : {}'.format(n))

# 10번 문제
n = 0
while True:
    i = int(input('정수 : '))
    if i == 0:
        break
    elif i < 0:
        continue
    else:
        n += i
print('합 : {}'.format(n))