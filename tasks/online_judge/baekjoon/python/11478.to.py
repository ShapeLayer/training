from sys import setrecursionlimit
setrecursionlimit(1500)

class Solution:
    def __init__(self, s: str):
        self.s = s
        self.strs = {}
        self.result = 0
        self.compute(s)

    def compute(self, s: str) -> int:
        self.compute_range(0, len(s))
    
    def compute_range(self, i: int, e: int):
        if i == e: return
        if s[i:e] not in self.strs:
            self.strs[s[i:e]] = True
            self.result += 1
        self.compute_range(i, e - 1)
        self.compute_range(i + 1, e)

if __name__ == '__main__':
    s = input()
    solution = Solution(s)
    print(solution.result)
