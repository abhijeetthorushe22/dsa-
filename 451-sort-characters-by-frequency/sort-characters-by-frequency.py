class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        freq = Counter(s)

        sorted_freq = sorted(freq.items(),key = lambda x : x[1],reverse = True)

        for f in sorted_freq:
            result += f[0]*f[1]
        
        return result
        
        
        