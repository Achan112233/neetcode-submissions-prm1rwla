class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        m x n matrix
        sr, sc
        color -> to change
        we have store the original color in memory
        keep repreating until ther eare no more adjacent pixels of the original to update
        return the modified..
        
        color = gird[sr][sc] 
        recursive(sr, sc, color, newcolor):
            
            if oob or if color is not equal:
                return
            
            if image[sr][sc] = color:
                image[sr][sc] = newcolor

            

            recursive(sr + 1, sc, color, newcolor)
            recursive(sr, sc + 1, color, newcolor)
            recursive(sr, sc - 1, color, newcolor)
            recursive(sr - 1, sc, color, newcolor)
        ''' 
        ogcolor = image[sr][sc]
        row, col = len(image), len(image[0])
        def dfs(x, y):
            nonlocal image
            if x < 0 or y < 0 or x >= row or y >= col:
                return

            if image[x][y] != ogcolor or image[x][y] == color:
                return 
            image[x][y] = color

            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
            return
            
        dfs(sr, sc)
        return image
