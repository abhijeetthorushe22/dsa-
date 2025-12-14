class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        temp1 = []
        temp2 = []
        for num in nums:
            if num > 0:
                temp1.append(num)
        for num in nums:
            if num < 0:
                temp2.append(num)
        
        result = []
        for i in range(len(temp1)):
            result.append(temp1[i])
            result.append(temp2[i])
        return result