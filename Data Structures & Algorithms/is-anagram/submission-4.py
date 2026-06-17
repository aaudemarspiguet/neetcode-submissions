from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_sig = [0] * 26
        t_sig = [0] * 26
        for i in range(len(s)):
            s_sig[ord(s[i]) - ord("a")] += 1
            t_sig[ord(t[i]) - ord("a")] += 1
        
        return s_sig == t_sig


