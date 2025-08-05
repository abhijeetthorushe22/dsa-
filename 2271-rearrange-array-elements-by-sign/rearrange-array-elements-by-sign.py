class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        output = []
        for i in range(len(positive)):
            output.append(positive[i])
            output.append(negative[i])
        
        return output

                
        