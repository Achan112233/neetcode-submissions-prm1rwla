class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        string array -> reutn longest common prefix.

        iterate through every string and do it like that
        '''

        first = strs[0]
        pref = ""

        for string in strs:
            #iterate thrpugh every char in string
            for i, char in enumerate(string):
                if i < len(first) and char == first[i]:
                    pref += char
                else:
                    break
            first = pref
            pref = ""

        return first