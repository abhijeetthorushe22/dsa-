class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        

        prefix = strs[0]

        for i in range(len(prefix)):
            for words in strs[1:]:
                if (i==len(words)) or prefix[i]!=words[i]:
                    return prefix[0:i]

        return prefix
            
       


        
        

        