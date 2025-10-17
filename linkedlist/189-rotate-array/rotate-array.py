class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        arr = []
        for i in range(n-k,n):
            arr.append(nums[i])
        
        for i in range(0,n-k):
            arr.append(nums[i])
        
        for i in range(n):
            nums[i]= arr[i]
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        