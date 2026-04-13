class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        
        i = 0
        while s[i] == " ":
            i += 1
        j = i
        while j < len(s):
            if s[j] == " ":
                break
            j += 1
        return j - i