class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        wordList = set(words)
        ans = []
        for word in wordList:
            for word2 in wordList:
                if word == word2:
                    continue
                else:
                    if self.substr(word, word2):
                        ans.append(word)
        return list(set(ans))
    
    def substr(self, word1, word2) -> bool:
        return word1 in word2