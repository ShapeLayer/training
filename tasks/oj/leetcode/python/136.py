from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = dict(Counter(nums))
        for n in counter:
            if counter[n] == 1:
                return n

if __name__ == '__main__':
    print(Solution().singleNumber([2, 2, 1]))
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
    print(Solution().singleNumber([1]))