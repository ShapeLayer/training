from sys import stdin
input = stdin.readline

class Solution:
    def __init__(self, n: int):
        self.n = n
    
    def calc(self, oper: str, n: int):
        if oper == '+':
            self.n += n
        elif oper == '-':
            self.n -= n
        elif oper == '*':
            self.n *= n
        elif oper == '/':
            self.n //= n

if __name__ == '__main__':
    solve: Solution = Solution(int(input()))
    while True:
        oper = input().strip()
        if oper == '=':
            break
        solve.calc(oper, int(input()))
    print(solve.n)
