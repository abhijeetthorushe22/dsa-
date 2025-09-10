class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i]>nums[(i+1)%len(nums)]:
                count+=1
        
        return count<=1
        
      
        