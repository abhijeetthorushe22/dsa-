from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indices = []

        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)

        if not indices:  # if list is empty
            return [-1, -1]
        else:
            return [indices[0], indices[-1]]



       




        