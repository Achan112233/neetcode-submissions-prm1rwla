class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(0, len(s) - 1):
            fst, snd = ord(s[i]), ord(s[i + 1])
            score += abs(snd - fst)
        return score