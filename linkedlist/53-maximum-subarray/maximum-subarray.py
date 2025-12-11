class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = cursum = nums[0]
        for num in nums[1:]:
            cursum = max(num,cursum+num)
            maxsum = max(cursum,maxsum)
    
        return maxsum
        