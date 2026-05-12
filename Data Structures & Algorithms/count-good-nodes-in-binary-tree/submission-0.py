# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maximum):

            if not root:
                return

            if root.val >= maximum:
                self.res += 1
            
            dfs(root.left, max(root.val, maximum))
            dfs(root.right, max(root.val, maximum))
        
        dfs(root, -float('inf'))
        return self.res