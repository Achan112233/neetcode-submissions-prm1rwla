class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        q = []
        fresh = 0
        minute = 0

        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        while fresh and len(q) > 0:
            for i in range(len(q)):
                i, j = q.pop(0)

                for adjx, adjy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r, c = i + adjx, j + adjy

                    if r in range(row) and c in range(col) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            minute += 1
        return minute if fresh == 0 else -1 