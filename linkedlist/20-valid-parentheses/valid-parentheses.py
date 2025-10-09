class Solution:
    def isValid(self, s: str) -> bool:
       
        n = len(s)
        if n % 2 == 1:
            return False
        st = []

        for ch in s:
            if ch == '(' or ch == '{' or  ch == '[':
                st.append (ch)
            else:
                if len(st)==0:
                    return False
                top = st.pop()

                if ch == ')' and top != '(':
                    return False
                elif ch == '}' and top != '{':
                    return False
                elif ch == ']' and top != '[':
                    return False
        if len(st) == 0:
                return True
        else:
            return False
