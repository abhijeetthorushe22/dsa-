class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        temp = []

        
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
                
        zero = n - len(temp)
        temp.extend([0]*zero)
        for i in range(n):
            nums[i]=temp[i]
        
    

        """
        Do not return anything, modify nums in-place instead.
        """
        