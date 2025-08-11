class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = last = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:   # first time we see target
                    first = i
                last = i          # keep updating last index
        
        return [first, last]



       




        