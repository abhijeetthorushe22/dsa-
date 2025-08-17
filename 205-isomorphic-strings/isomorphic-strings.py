class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for char_s, char_t in zip(s, t):
            # If mapping exists in s_map, it must match
            if char_s in s_map:
                if s_map[char_s] != char_t:
                    return False
            # If mapping exists in t_map, it must match
            elif char_t in t_map:
                if t_map[char_t] != char_s:
                    return False
            else:
                # Assign new mapping
                s_map[char_s] = char_t
                t_map[char_t] = char_s

        return True




        