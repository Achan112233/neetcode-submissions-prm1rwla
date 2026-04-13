class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 , dic2 = {}, {}
        for char in s:
            dic1[char] = dic1.get(char, 0) + 1

        for char2 in t:
            dic2[char2] = dic2.get(char2, 0) + 1

        return dic1 == dic2