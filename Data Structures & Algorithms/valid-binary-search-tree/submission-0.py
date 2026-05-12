# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root, greater, less):

            if not root:
                return True

            if root.val <= greater or root.val >= less:
                return False

            return dfs(root.left, greater, root.val) and dfs(root.right, root.val, less)
        
        return dfs(root, -float('inf'), float('inf'))