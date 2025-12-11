class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ans = []
        for i in range(len(nums)):
            if nums[i] == 0 :
                ans.append(nums[i])
                i+=1
        for i in range(len(nums)):
            if nums[i] == 1:
                ans.append(nums[i])
                i+=1
        for i in range(len(nums)):
            if nums[i] == 2 :
                ans.append(nums[i])
                i+=1
        
        for i in range(len(ans)):
            nums[i]=ans[i]
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        