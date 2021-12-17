# Euclidean algorithm

def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def lcd(a: int, b: int):
    return a * b // gcd(a, b)

a, b = map(int, input('두 수를 입력하세요: ').split())
print('두 수의 최대공약수는 {}, 최소공배수는 {}'.format(gcd(a, b), lcd(a, b)))