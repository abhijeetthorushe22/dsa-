class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in a:
                return [a[x], i]
            a[num] = i