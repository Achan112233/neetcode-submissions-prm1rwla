class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countAZ = defaultdict(list) 
        for s in strs:
            count = [0] * 26 # array with 26 spaces of memory allocated

            for c in s:
                count[ord(c) - ord("a")] += 1

            countAZ[tuple(count)].append(s)

        return list(countAZ.values()) #returning the values
                         