# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs on both trees


        def dfs(root, root2):

            if root is None and root2 is None:
                return True
            elif root is None or root2 is None or root2.val != root.val:
                return False
            else:    
                left = dfs(root.left, root2.left)
                right = dfs(root.right, root2.right)
                return left and right            
            
        if not subRoot:
            return True
        if not root:
            return False
        if dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)