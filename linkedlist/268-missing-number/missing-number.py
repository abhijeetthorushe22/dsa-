class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sum(nums)
        y = len(nums)
        x = y * (y+1)//2
        return x-n
        