class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        i = 1
        while i != len(nums):
            if nums[i-1] != nums[i]:
                cnt = 1
            else:
                cnt += 1
            if cnt > 2:
                nums.pop(i)
            else:
                i += 1
        return len(nums)