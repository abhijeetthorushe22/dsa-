class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        string_1 = s+s
        if len(s)!=len(goal):
            return False

        
        return goal in string_1
           
        