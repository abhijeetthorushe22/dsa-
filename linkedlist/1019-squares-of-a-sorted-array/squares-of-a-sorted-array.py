class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 2
        for j in range(len(nums)):
            nums[j]=nums[j]**2
            
        nums.sort()
        return nums
        