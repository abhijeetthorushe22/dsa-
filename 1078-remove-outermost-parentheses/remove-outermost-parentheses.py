class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        result = []

        for char in s:
            if char == '(':
                balance +=1
                if balance > 1:
                    result.append ('(')
            elif char == ')':
                balance -=1
                if balance > 0:
                    result.append (')')
        

        return "".join(result)


        