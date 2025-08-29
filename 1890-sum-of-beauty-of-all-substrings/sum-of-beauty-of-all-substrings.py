class Solution:

    def beautySum(self, s: str) -> int:
        n = len(s)
        beauty = 0
        
        for i in range(n):
            c = Counter()
            for j in range(i,n):
                c[s[j]]+=1
                vals = c.values()
                beauty += max(vals)-min(vals)
            
        return beauty

               
       