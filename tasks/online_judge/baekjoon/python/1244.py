from sys import stdin
from math import ceil
inpupt = stdin.readline

class Switches:
    def __init__(self, n: int, sw: list[bool]):
        self.n = n
        self.sw = [False] + sw
        self.pal_dp = [[True if i == j else None for i in range(n + 1)] for j in range(n + 1)]

    def oper(self, sex: int, idx: int):
        if sex == 1:
            self.male_oper(idx)
        else:
            self.female_oper(idx)
    
    def male_oper(self, idx: int):
        for i in range(idx, self.n + 1, idx):
            self.sw[i] = not self.sw[i]

    def female_oper(self, idx: int):
        i = 0
        while idx - i > 0 and idx + i <= self.n:
            if self.sw[idx - i] != self.sw[idx + i]:
                break
            i += 1
        i -= 1
        for j in range(idx - i, idx + i + 1):
            self.sw[j] = not self.sw[j]

if __name__ == '__main__':
    n = int(input())
    sw = Switches(n, list(map(bool, map(int, input().split()))))
    for q in range(int(input())):
        s, i = map(int, input().split())
        sw.oper(s, i)
    for l in range(ceil(n / 20)):
        print(' '.join(list(map(str, map(int, sw.sw)))[l * 20 + 1:(l + 1) * 20 + 1]))
