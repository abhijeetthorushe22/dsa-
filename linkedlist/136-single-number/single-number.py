class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            count = nums.count(num)
            if count == 1:
                return num
        