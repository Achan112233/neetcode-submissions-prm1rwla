class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        1 = land 
        0 = water 
        returns a 1

        # base case return 1
        <= if next is water or none means that we have 1
        we may have to keep track of visited

        '''
        
        row, col = len(grid), len(grid[0])
        vis = [[False for _ in range(col)] for _ in range(row)]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == 0:
                return 1
            if vis[x][y]: 
                return 0
            vis[x][y] = True
            return dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    val = dfs(r, c)    
                    return val

        
            