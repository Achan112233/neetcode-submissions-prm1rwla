class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxContain = 0
        fst, snd = 0, len(heights) - 1
        while fst < snd:
            currContain = (snd - fst) * min(heights[fst], heights[snd])
            maxContain = max(currContain, maxContain)
            if heights[fst] <= heights[snd]:
                fst += 1
            else: 
                snd -= 1
        return maxContain
