class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0
        i = 0
        while j < len(word) and i < len(abbr):
            if word[j] != abbr[i]:
                if not abbr[i].isdigit():
                    return False
                num = ""
                while i < len(abbr) and abbr[i].isdigit():
                    num += abbr[i]
                    i += 1
                if num != "":
                    if num[0] == '0':
                        return False
                    num = int(num)
                else: 
                    num = 0
                j += num
                if j > len(word):
                    return False
            else:
                i += 1
                j += 1
        return len(word) == j and i == len(abbr)
