class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sums = n*(n+1)//2
        array_sum=sum(nums)

        return sums-array_sum
        
        