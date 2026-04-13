class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        max amount a container can store

        min of side bars gives us the height
        and we mult by the distance between thge two
        we get the container with all the elements first
        if l is larger we increment r
        if r is larger we increment l
        '''

        l, r = 0, len(heights) - 1

        ans = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)

            ans = max(curr, ans)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return ans