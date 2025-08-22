class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = list(set(nums))
        if len(nums)==len(x):
            return False
        else:
            return True
        