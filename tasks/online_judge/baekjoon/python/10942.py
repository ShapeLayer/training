from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(5000)

class Proc:
    def __init__(self, n: int, nums: list[int]):
        self.n = n
        self.nums = nums
        self.dp = [[None for _i in range(n)] for _j in range(n)]
    
    def is_pal(self, init: int, fin: int) -> bool:
        if self.dp[init][fin] != None:
            return self.dp[init][fin]
        if fin - init > 1:
            pal = self.is_pal(init + 1, fin - 1)
            if not pal:
                self.dp[init][fin] = False
            else:
                if nums[init] == nums[fin]:
                    self.dp[init][fin] = True
                else:
                    self.dp[init][fin] = False
        else:
            if nums[init] == nums[fin]:
                self.dp[init][fin] = True
            else:
                self.dp[init][fin] = False
        return self.dp[init][fin]

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    proc = Proc(n, nums)
    m = int(input())
    for _i in range(m):
        rs, re = map(int, input().split())
        print(int(proc.is_pal(rs - 1, re - 1)))
