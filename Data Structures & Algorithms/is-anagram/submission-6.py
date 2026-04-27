class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = sorted(s)
        t_c = sorted(t)
        if s_c == t_c:
            return True
        else:
            return False
        

        