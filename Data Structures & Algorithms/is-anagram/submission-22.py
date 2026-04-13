class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hash[s[i]] += 1
        
        for j in range(len(t)):
            hash[t[j]] -= 1
            if hash[t[j]] == 0:
                del hash[t[j]]            

        return hash == {}