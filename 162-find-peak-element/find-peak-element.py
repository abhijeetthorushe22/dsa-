class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        if n == 1:
            return 0
        if n == 2:
            if nums[i + 1] > nums[i]:
                return i + 1
            else:
                return 0
        if n == 3:
            if nums[i + 2] > nums[i + 1]:
                return i + 2
            elif nums[i] < nums[i + 1] and nums[i + 1] > nums[i + 2]:
                return i + 1
            else:
                return 0
        
        else:
            for i in range(1, n - 1):
                if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                    return i
            
            # Check last element
            if nums[n - 1] > nums[n - 2]:
                return n - 1
            
            # If no other peak found, return first
            return 0
