from sys import stdin
input = stdin.readline

class Checker:
    def __init__(self, n: int):
        self.n = n
    
    def is_multiple(self, n: int):
        return n % self.n == 0

if __name__ == '__main__':
    checker: Checker = Checker(int(input()))
    while True:
        n = int(input())
        if n == 0:
            break
        print('{} is {}a multiple of {}.'.format(n, 'NOT ' if not checker.is_multiple(n) else '', checker.n))
