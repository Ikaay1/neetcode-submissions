# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    found = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root):

            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)

            if not self.found:
                condition1 = left and right
                condition2 = (root.val == p.val or root.val == q.val) and (left or right)
                if condition1 or condition2:
                    self.found = root
                    return True
                return left or right or root.val == p.val or root.val == q.val
            
            return True
        
        dfs(root)
        return self.found