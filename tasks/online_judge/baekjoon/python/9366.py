from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for i in range(int(input())):
        a, b, c = sorted(map(int, input().split()))
        result = ''
        if a + b <= c:
            result = 'invalid!'
        elif a == b == c:
            result = 'equilateral'
        elif a == b or b == c or c == a:
            result = 'isosceles'
        else:
            result = 'scalene'
        print(f'Case #{i + 1}: {result}')
