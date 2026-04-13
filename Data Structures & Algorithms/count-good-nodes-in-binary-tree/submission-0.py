# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        - good node has no elements larger than itself from root to itself
        - root is always going to be a good node
        arr = [2, 1, 5] max = arr
        count = 0

        count = 3  
        m = -inf
        '''
        arr = []
        count = 0

        def dfs(r):
            nonlocal count 
            if r is None:
                return
            
            m = max(arr) if len(arr) > 0 else float('-inf')

            if r.val >= m:
                count += 1

            arr.append(r.val)
            dfs(r.left)
            dfs(r.right)
            arr.pop()
        
        dfs(root)
        return count

        

