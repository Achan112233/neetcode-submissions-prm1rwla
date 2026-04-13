class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        ptr = 0
        for i in range(len(t)):
            if ptr >= len(s):
                break
            if s[ptr] == t[i]:
                ptr += 1
        
        return ptr == len(s)