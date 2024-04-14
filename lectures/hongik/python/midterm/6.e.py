# Euclidean algorithm

def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def lcd(a: int, b: int):
    return a * b // gcd(a, b)
a = int(input('범위의 시작 정수: '))
b = int(input('범위의 마지막 정수: '))
lcd_s = lcd(a, a+1)
for i in range(a+2, b+1):
    lcd_s = lcd(lcd_s, i)
print('{}에서 {}까지의 정수들의 최소공배수는: {}'.format(a, b, lcd_s))