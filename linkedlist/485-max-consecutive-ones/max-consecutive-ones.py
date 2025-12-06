class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1 = 0
        count2 = 0

        for num in nums:
            if num == 1:
                count1+=1
                count2 = max(count1,count2)
            else:
                count1 = 0
        return count2
        
        