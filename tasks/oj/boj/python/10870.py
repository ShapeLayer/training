from sys import stdin

n = int(stdin.readline())

def fibo(s, n1, n2):
    if n != s:
        s += 1
        fibo(s, n2, n1 + n2)
    else:
        print(n1)

fibo(0, 0, 1)