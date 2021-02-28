from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split()) # list() 함수로 싸지 않아도 됨
    res = [(a ** i) % 10 for i in range(1, 5)][(b % 4) - 1]
    print(res if res != 0 else 10)