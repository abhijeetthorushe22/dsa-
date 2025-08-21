class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i<n and s[i]==" ":
            i+=1
        
        sign = 1
        if i<n and s[i]=="-":
            sign = -1
            i+=1
        elif i<n and s[i]== "+":
            i+=1

        result = 0
        while i<n and s[i].isdigit():
            result = result*10+int(s[i])
            i+=1
        
        result = result * sign
        if result < - 2**31 :
            return -2**31
        elif result > 2**31 -1:
            return 2**31 - 1
        else:
            return result
        

        