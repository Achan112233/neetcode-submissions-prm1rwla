class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given an array of strings, return a 2d array of all strings grouped
        # dict, 
        group = defaultdict(list)
        for stre in strs:
            key_ls = sorted(stre)
            key = "".join(key_ls)
            group[key].append(stre)
        return list(group.values())

