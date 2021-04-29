from sys import stdin

def c(n):
    return (n%10)*100 + ((n%100)//10)*10 + (n//100)

a, b = list(map(int, stdin.readline().rstrip().split()))
a = c(a)
b = c(b)

if a > b:
    print(a)
else:
    print(b)