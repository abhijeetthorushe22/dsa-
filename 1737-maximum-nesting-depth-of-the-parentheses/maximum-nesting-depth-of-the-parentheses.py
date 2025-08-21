class Solution:
    def maxDepth(self, s: str) -> int:
        count1 = 0
        max_count = 0
        for i in s:
            if i == "(" :
                count1+=1
                max_count = max(max_count,count1)
            elif i ==")":
                count1-=1
       

        return max_count
        

        
        