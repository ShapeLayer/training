from sys import stdin, setrecursionlimit
setrecursionlimit(int(2e5))
input = stdin.readline

class Solution:
  def __call__(self, n: int) -> int:
    if n == 0:
      return 0
    if n == 1:
      return 1

    return self(n - 1) + self(n - 2)

def compute(N: int) -> int:
  sol = Solution()
  return sol(N)

if __name__ == "__main__":
    N = int(input())
    print(compute(N))
