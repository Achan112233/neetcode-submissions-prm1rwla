class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashs = {}
        for word in strs:
            hashs["".join(sorted(word))] = hashs.get("".join(sorted(word)), []) + [word]
        return list(hashs.values())