# 1번 문제
num = int(input('정수 : '))
if num < 100:
    print(num)

# 2번 문제
num = int(input('정수 : '))
if num % 2 == 0:
    print('짝수')

# 3번 문제
num = int(input('정수 : '))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 4번 문제
num = int(input('정수 : '))
if num < 100:
    print(num * 0.9)
else:
    print(num * 1.1)

# 5번 문제
a = int(input('a : '))
b = int(input('b : '))
tmp = a + b - b**2
if tmp >= 0:
    print(tmp)
else:
    print('음수')

# 6번 문제
num = int(input('정수 : '))
if num % 2 == 0 and num % 3 == 0:
    print('나누어짐')
else:
    print('나누어지지 않음')

# 7번 문제
a, b = 5, 3
oper = input('연산자 : ')
if oper == '+':
    res = a + b
elif oper == '-':
    res = a - b
elif oper == '*':
    res = a * b
elif oper == '/':
    res = a / b
else:
    res = -1
print('{} {} {} = {}'.format(a, oper, b, res))

# 8번 문제
ph = int(input('ph : '))
if ph >= 0 and ph <= 4:
    print('강산성')
elif ph >= 5 and ph <= 6:
    print('약산성')
elif ph == 7:
    print('중성')
elif ph >= 8 and ph <= 9:
    print('약염기성')
elif ph >= 10 and ph <= 14:
    print('강염기성')

# 9번 문제
year = int(input('년도 : '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('윤년')
else:
    print('평년')