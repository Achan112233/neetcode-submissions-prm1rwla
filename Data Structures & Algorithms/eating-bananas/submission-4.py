class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return the minimum amouunt of hours needed to eat all bananas in the pile within h hours
        l, r = 1, max(piles) # this makes us have the max amount rate where we could finish bananas
        
        while l <= r:
            m = (l + r) // 2
            # lets say we start at the middle between 1 and max
            count = 0
            for bananas in piles:
                count += math.ceil(float(bananas) / m)
            
            if count <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res