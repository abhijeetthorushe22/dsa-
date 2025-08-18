class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        string_1 = s+s
        if len(s)!=len(goal):
            return False

        
        if goal in string_1:
            return True
        
        else:
            return False
        