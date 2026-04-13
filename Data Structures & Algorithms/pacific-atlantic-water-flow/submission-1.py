class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])

        pacific = False
        atlantic = False

        def dfs(r, c, prevVal):
            nonlocal pacific, atlantic
            if r < 0 or c < 0:
                pacific = True
                return 
            if r >= row or c >= col:
                atlantic = True
                return
            if heights[r][c] > prevVal:
                return
            tmp = heights[r][c]
            heights[r][c] = float('inf')
            
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ax, ay = r + i, c + j

                dfs(ax, ay, tmp)
                if pacific and atlantic:
                    break
            heights[r][c] = tmp
        res = []
        for r in range(row):
            for c in range(col):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])
        return res