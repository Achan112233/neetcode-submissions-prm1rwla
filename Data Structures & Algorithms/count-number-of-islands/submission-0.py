class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        # to find an island we must look at all adjacent nodes

        row, col = len(grid), len(grid[0])

        def removeAdj(x, y):
            if x < 0 or y < 0 or x >= row or y >= col:
                return
                 
            if grid[x][y] == "1":
                grid[x][y] = "0"
                removeAdj(x + 1, y)
                removeAdj(x - 1, y)
                removeAdj(x, y + 1)
                removeAdj(x, y - 1)
            else:
                return
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    removeAdj(i, j)
                    count += 1
        
        
        return count

