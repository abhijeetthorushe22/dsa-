class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = "".join(map(str,digits))
        x = str(int(x)+1)
        x = [int(ch) for ch in x]
        return x

        